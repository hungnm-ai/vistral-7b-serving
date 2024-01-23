import logging


# Create a logger
logger = logging.getLogger("Nocode")

# Set the logging level (optional)
logger.setLevel(logging.DEBUG)

# Create a console handler and set its level (optional)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a file handler and set its level (optional)
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

# Create a formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


