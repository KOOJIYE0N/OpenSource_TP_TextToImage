import logging
import os

class Logger:
    def __init__(self, log_file="project.log"):
        """
        Logger Initialization.
        :param log_file: 로그 저장할 파일 경로.
        """
        self.logger = logging.getLogger("ProjectLogger")
        self.logger.setLevel(logging.DEBUG)

        # Console Output Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # File Output Handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Format Settings
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add Handlers
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def info(self, message):
        """Info level message logging."""
        self.logger.info(message)

    def debug(self, message):
        """Debug level message logging."""
        self.logger.debug(message)

    def warning(self, message):
        """Warning level message logging."""
        self.logger.warning(message)

    def error(self, message):
        """Error level message logging."""
        self.logger.error(message)

    def critical(self, message):
        """Critical level message logging."""
        self.logger.critical(message)