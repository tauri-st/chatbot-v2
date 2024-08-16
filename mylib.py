import logging

#create a module level logger to do the logging
logger = logging.getLogger(__name__)

def do_something():
    logger.info('Doing something')