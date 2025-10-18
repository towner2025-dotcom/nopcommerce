import logging
import os

class Log_Maker:
    @staticmethod
    def log_gen():
        # Create log directory if not exists
        os.makedirs(".\\logs", exist_ok=True)

        # Set up the logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Create file handler
        file_handler = logging.FileHandler(".\\logs\\nopcommerce.log", mode='a')
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        ))

        # Avoid duplicate logs
        if not logger.handlers:
            logger.addHandler(file_handler)

        return logger
