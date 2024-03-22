import logging

Logger = logging.getLogger(__name__)
Logger.setLevel(logging.DEBUG)
Logger.addHandler(logging.StreamHandler())
Logger.propagate = False
Logger.debug('Logger initialized')

# Path: deck.py
