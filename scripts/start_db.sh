#!/usr/bin/env bash
# Start a local MySQL 8 database in Docker for this app, with no MySQL install needed.
# First run: creates a random password, writes it to .env (never committed),
# starts the container and loads db_schema/schema.sql.
# Later runs: just start the existing container (your data is kept).
# Stop it with: docker stop expense-mysql
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
NAME=expense-mysql
PORT=3306

# 1. Password: reuse the one in .env, or create a new random one
if [[ -f "$ROOT/.env" ]] && grep -q '^DB_PASSWORD=.\+' "$ROOT/.env"; then
  PW="$(grep '^DB_PASSWORD=' "$ROOT/.env" | cut -d= -f2-)"
else
  PW="$(openssl rand -hex 16)"
  printf 'DB_HOST=127.0.0.1\nDB_USER=root\nDB_PASSWORD=%s\nDB_NAME=expense_manager\n' "$PW" > "$ROOT/.env"
  echo "Wrote new credentials to $ROOT/.env"
fi

# 2. Container: start the existing one, or create it
if docker ps -a --format '{{.Names}}' | grep -qx "$NAME"; then
  docker start "$NAME" >/dev/null
  echo "Started existing container $NAME"
  exit 0
fi
docker run -d --name "$NAME" -e MYSQL_ROOT_PASSWORD="$PW" -p "$PORT:3306" \
  -v expense-mysql-data:/var/lib/mysql mysql:8.0 >/dev/null

# 3. Wait for MySQL to be ready, then load the schema and sample rows
echo -n "Waiting for MySQL"
# (TCP check: the first-run setup server inside the container has networking off)
until docker exec "$NAME" mysql -h127.0.0.1 -uroot -p"$PW" -e 'SELECT 1' >/dev/null 2>&1; do
  echo -n "."; sleep 2
done
echo
docker exec -i "$NAME" mysql -uroot -p"$PW" < "$ROOT/db_schema/schema.sql" 2>/dev/null
echo "Database ready on port $PORT (expense_manager, sample rows loaded)"
