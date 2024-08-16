import logging

#create a module level logger to do the logging
logger = logging.getLogger("chatbot_token_count")

def do_something():
    logger.info('Doing something')