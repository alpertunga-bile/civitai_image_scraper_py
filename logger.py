import logging
import sys

logger = logging.getLogger()


# For coloring log outputs
class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;21m"
    blue = "\x1b[38;5;39m"
    yellow = "\x1b[38;5;226m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.fmt,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset,
        }

    def format(self, record):
        logFormat = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(logFormat)
        return formatter.format(record)


def set_logger(logger_level=logging.INFO) -> None:
    logger = logging.getLogger()
    logger.setLevel(logger_level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    log_format = "[%(asctime)s] /_\ %(levelname)-8s /_\ %(message)s"
    formatter = CustomFormatter(log_format)

    handler.setFormatter(formatter)
    logger.addHandler(handler)
