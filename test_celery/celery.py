from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery')

default_config = 'test_celery.celeryconfig'
app.config_from_object(default_config)