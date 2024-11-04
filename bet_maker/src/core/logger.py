LOG_FORMAT = (
    "%(name)s\t[%(funcName)s:%(lineno)s]\t%(asctime)s\t[%(levelname)s]\t%(message)s"
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": LOG_FORMAT},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "consumer": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "executor": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
