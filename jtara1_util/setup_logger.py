import logging
from os.path import basename


def setup_logger(logger_path, write_mode='w'):
    """Setup logging to log output to both a file and stderr

    :param logger_path: the name of the logger & the name of the \n
        logger file with ".log" appended
    "param write_mode: 'a' for append 'w' for (over)write
    :return: the logger with the handlers added
    """
    logger_path = logger_path + ('.log' if not logger_path.endswith('.log') else '')
    logger_name = basename(logger_path)

    logger = logging.getLogger(logger_path)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(name)s] - %(levelname)s - %(asctime)s -\n\t%(message)s")

    # stream handler
    sh = logging.StreamHandler()  # std.err
    sh.setLevel(logging.WARNING)
    sh.setFormatter(formatter)

    # file handler
    fh = logging.FileHandler(logger_name)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(fh)
    return logger