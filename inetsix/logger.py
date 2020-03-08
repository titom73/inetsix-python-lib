import logging
import os

# Get Logging level from Environment variable / Default INFO

# Define standard logging verbosity
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

# Set loglevel for arista.cvp modules
LOGGING_LEVEL = os.getenv('INETSIX_LIB_LOG_LEVEL', 'debug')
LOGLEVEL = LEVELS.get(LOGGING_LEVEL, logging.NOTSET)

# Set loglevel for urllib3
# LOGGING_LEVEL_URLLIB3 = os.getenv('INETSIX_LIB_LOG_APICALL', 'warning')
# LOGLEVEL_URLLIB3 = LEVELS.get(LOGGING_LEVEL_URLLIB3, logging.WARNING)

# Get filename to write logs / default /temp/arista.cvp.debug.log
LOGGING_FILENAME = os.getenv(
    'INETSIX_LIB_LOG_FILE', '/tmp/inetsix-debug.log')

# set a format which is simpler for console use
formatter = logging.Formatter(
    '%(name)-12s: %(levelname)-s - func: %(funcName)-12s (L:%(lineno)-3d) - %(message)s')

# set up ROOT handler to use logging with file rotation.
handler = logging.handlers.RotatingFileHandler(
    LOGGING_FILENAME, maxBytes=1000000, backupCount=5)
handler.setFormatter(formatter)
handler.setLevel(LOGLEVEL)
# Unset default logging level for root handler
logging.getLogger('').setLevel(logging.NOTSET)
logging.getLogger('').addHandler(handler)

# Configure URLLIB3 logging (default Warning to avoid too much verbosity)
# logging.getLogger("urllib3").setLevel(LOGLEVEL_URLLIB3)
