# logger_config.py
import logging

def get_logger(
    name: str,
    log_level: int = logging.INFO,
) -> logging.Logger:
    """
    Returns a logger configured with console output only.

    Args:
        name (str): Usually pass __name__ from the calling module.
        log_level (int): Logging level (default INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Prevent duplicate handlers if called multiple times
    if not logger.handlers:
        # Console handler only
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)

        # Add handler
        logger.addHandler(console_handler)

    return logger
