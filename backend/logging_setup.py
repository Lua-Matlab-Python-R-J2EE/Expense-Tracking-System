# Import the built-in logging module for application-wide logging
import logging


def setup_logger(logger_name, log_file='server.log', level=logging.INFO):
    """
    Creates and configures a logger instance for the application.
    
    Args:
        logger_name (str): The name to assign to the logger instance.
        log_file (str): Path to the file where logs will be written.
                        Defaults to 'server.log'.
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
                     Defaults to logging.INFO.
    
    Returns:
        logging.Logger: A configured logger object ready for use.
    
    Notes:
        - This function sets up file-based logging.
        - The logs will be formatted with timestamp, logger name,
          severity level, and message.
        - To watch logs in real-time, use: `tail -f server.log` in the terminal.
    """
    # Create (or get, if already existing) a named logger instance
    logger = logging.getLogger(logger_name)

    # --- DEBUGGING PRINTS (for introspection) ---
    # These print statements help verify the types of logging components during runtime
    print(f"logging type: {type(logging)}")
    print(f"basicConfig type: {type(logging.basicConfig)}")

    # Configure the global logging system’s default behavior
    # Here, we set the default logging level for root logger
    logging.basicConfig(level=level)

    # Create a file handler — this writes all log messages to a file
    file_handler = logging.FileHandler(log_file)  # Log file destination (e.g., 'server.log')

    # Define the log message format:
    # Example: "2025-10-18 15:42:10,123 - db_helper - INFO - Database connection established"
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Apply the formatter to the file handler
    file_handler.setFormatter(formatter)

    # Attach the file handler to the logger so it knows where to send output
    logger.addHandler(file_handler)

    # Return the fully configured logger object
    return logger


# ---------------------------------------------------------------------
# NOTE:
# Logging can also be implemented using a decorator function to
# automatically log function calls, arguments, and results.
#
# To view logs live as they are written to 'server.log', run:
#     tail -f server.log
# ---------------------------------------------------------------------
