import logging
logging.basicConfig(filename= 'Test.log',format =" %(asctime)s  %(levelname)s : %(message)s",level = logging.DEBUG)
logging.info("what does this software does")
logging.debug("this is the problem")
logging.error("issue in the database")
logging.warning("might shutdown the app")
logging.critical("potential harming the system")
