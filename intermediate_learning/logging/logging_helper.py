import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

import helper_module
logging.debug("Debug message.")
logging.info("Info message.")
logging.warning("Warning message!")
logging.error("Error message!")
logging.critical("Critical message!")