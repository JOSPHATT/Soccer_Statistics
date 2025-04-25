import logging

def setup_logger(name, log_file, level=logging.INFO):
    """Setup a logger with the given name and log file."""
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    return logger

# Example usage:
# logger = setup_logger('data_processing', 'data_processing.log')
# logger.info('This is an info message.')