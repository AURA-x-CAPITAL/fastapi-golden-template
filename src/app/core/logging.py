import logging
import sys
from pythonjsonlogger import jsonlogger
from app.core.config import settings


class KubernetesJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            log_record['timestamp'] = record.created
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname

        # Kubernetes-specific fields
        log_record['service'] = settings.PROJECT_NAME
        log_record['module'] = record.module
        log_record['function'] = record.funcName
        log_record['line'] = record.lineno


def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO if not settings.DEBUG else logging.DEBUG)

    # Remove existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Create JSON formatter
    json_formatter = KubernetesJsonFormatter(
        '%(timestamp)s %(level)s %(name)s %(module)s %(funcName)s %(lineno)s %(message)s'
    )

    # Stream handler (stdout)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(json_formatter)
    logger.addHandler(stream_handler)

    return logger


logger = setup_logging()
