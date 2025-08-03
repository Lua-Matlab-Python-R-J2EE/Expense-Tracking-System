import logging

def setup_logger(logger_name, log_file='server.log', level=logging.INFO):
    logger = logging.getLogger(logger_name)

    # DEBUG
    print(f"logging type: {type(logging)}")
    print(f"basicConfig type: {type(logging.basicConfig)}")

    logging.basicConfig(level=level)
    file_handler = logging.FileHandler(log_file) # where the logs are dumped
    formatter    = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# logging can also be implemented as a Decorator also

# Use 'tail -f server.log' on terminal to watch the logging live on terminal