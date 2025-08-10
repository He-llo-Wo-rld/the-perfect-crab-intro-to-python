import logging
from logging.handlers import RotatingFileHandler

FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

file_handler = RotatingFileHandler("app.log", maxBytes=1_000_000, backupCount=5)
file_handler.setFormatter(logging.Formatter(FORMAT))

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(FORMAT))

logging.basicConfig(
    level=logging.INFO,
    handlers=[file_handler, console_handler]
)