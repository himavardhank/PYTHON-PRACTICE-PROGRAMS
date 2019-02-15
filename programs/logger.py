import logging
import test
logging.basicConfig(filename='mylog.txt',level=50)
logging.WARNING('message from warning ')
logging.error('message from error ')
logging.critical('message from critical ')
