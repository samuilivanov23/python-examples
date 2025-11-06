import logging
import logging.config
import traceback
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)

#create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logging/file.log')

# set level and format
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning("Warning message!")
logger.error("New Error message!")


logging.config.fileConfig('logging/logging.conf')

# create logger with the name from the config file. 
# This logger now has StreamHandler with DEBUG Level and the specified format
logger2 = logging.getLogger('simpleExample')

logger2.debug('debug message')
logger2.info('info message')

try:
  a = [1, 2, 3]
  value = a[3]
except IndexError as e:
  logger.error(e, exc_info=True)
  logger2.error(e, exc_info=True)
  logger2.error("The error is %s", traceback.format_exc())


logger3 = logging.getLogger(__name__)
logger3.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
handler = RotatingFileHandler('logging/app.log', maxBytes=2000, backupCount=5)
logger3.addHandler(handler)

for _ in range(10000):
    logger3.info('Hello, world!')