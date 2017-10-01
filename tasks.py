import logging
from celery import Celery


logger = logging.getLogger(__name__)


app = Celery('tasks',  broker='pyamqp://guest@localhost//')


@app.task
def process_data(snapid, timestamp):
    # All data processing occurs here for
    logger.info('{} - {}'.format(snapid, timestamp))

