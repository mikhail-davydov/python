import logging.config

config = {
    "version": 1,
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "sample.log",
            "encoding": "utf-8",
            "formatter": "default",
        },
    },
    "formatters": {
        "default": {
            "format": "[%(levelname)s] - %(message)s",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["file"],
    },
}

logging.config.dictConfig(config)
