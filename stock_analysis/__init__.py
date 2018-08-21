import os

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

# Manually set logging
log = True
if log:
    import logging
    # Create new empty file
    if os.path.isfile('python_logging.log'):
        with open('python_logging.log', 'w'):
            pass

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger_handler = logging.FileHandler('python_logging.log')
    logger_handler.setLevel(logging.DEBUG)
    # Create a Formatter for formatting the log messages
    logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    logger_handler.setFormatter(logger_formatter)
    logger.addHandler(logger_handler)

__version__ = 0.0  # Pre-release

