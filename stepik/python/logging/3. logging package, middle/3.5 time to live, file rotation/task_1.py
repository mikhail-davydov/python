logger = logging.getLogger(__name__)

handler = TimedRotatingFileHandler("errors.log",
                                   when="D",
                                   interval=1,
                                   backupCount=3,
                                   atTime=datetime.time(5, 0, 0)
                                   )

formatter = logging.Formatter("%(asctime)s - [%(levelname)-8s] - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
