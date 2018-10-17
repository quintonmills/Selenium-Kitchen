import logging

class LoggerDemoConsole():

    def testLogger(self):
        # create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        # create console handler and set level to info
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

        # add formatter to console handler
        consoleHandler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(consoleHandler)

        # logging messages
        logger.debug('debug boi')
        logger.info('info boi')
        logger.warn('warn boi')
        logger.error('error boi')
        logger.critical('critical boi')

demo = LoggerDemoConsole()
demo.testLogger()