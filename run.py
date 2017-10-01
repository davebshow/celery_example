import datetime
import logging

import tasks

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def run():
    """Iterate over the dataset. Create a Celery task for each item."""

    for snapid in range(1000):

        timestamp = datetime.datetime.now()

        # Call a celery task to process the dataset!
        tasks.process_data.delay(snapid, timestamp)  # calls to delay are completely async - doesn't block!


run()