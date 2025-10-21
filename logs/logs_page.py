import logging
import os
import datetime


class Log_Maker:
    _logger = None

    @staticmethod
    def log_gen():
        """Generate logger instance"""
        if Log_Maker._logger is not None:
            return Log_Maker._logger

        # Create log directory if not exists
        os.makedirs("logs", exist_ok=True)

        # Create log filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d")
        log_filename = f"logs/towner_test_{timestamp}.log"

        # Set up the logger
        logger = logging.getLogger("TownerLogger")
        logger.setLevel(logging.INFO)

        # Create file handler
        file_handler = logging.FileHandler(log_filename, mode='a', encoding='utf-8')
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        ))

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        ))

        # Avoid duplicate logs
        if not logger.handlers:
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        Log_Maker._logger = logger
        return logger

    @staticmethod
    def info(message):
        """Log info message"""
        logger = Log_Maker.log_gen()
        logger.info(message)

    @staticmethod
    def error(message):
        """Log error message"""
        logger = Log_Maker.log_gen()
        logger.error(message)

    @staticmethod
    def warning(message):
        """Log warning message"""
        logger = Log_Maker.log_gen()
        logger.warning(message)

    @staticmethod
    def debug(message):
        """Log debug message"""
        logger = Log_Maker.log_gen()
        logger.debug(message)