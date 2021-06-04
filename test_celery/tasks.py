from __future__ import absolute_import
from test_celery.celery import app
from celery import Task, states
from celery.exceptions import Ignore
import time

class DebugTask(Task):
    abstract = True

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        # exc (Exception) - The exception raised by the task.
        # args (Tuple) - Original arguments for the task that failed.
        # kwargs (Dict) - Original keyword arguments for the task that failed.
        print('{0!r} failed: {1!r}'.format(task_id, exc))

@app.task(name='test_celery.tasks.longtime_add', bind=True)
def longtime_add(self, x, y):
    print ('long time task begins')
    # sleep 5 seconds
    time.sleep(5)
    print ('long time task finished')
    return x + y

@app.task(name="test_celery.tasks.more_complex", bind=True)
def more_complex(self, a, b, c):
    print ('more complex begins')
    time.sleep(5)
    print ('more complex finished')
    return a * b + c

@app.task(name="test_celery.tasks.capitals", bind=True)
def capital_cities(self, **kwargs): 
    # initialize an empty list to store the result
    result = []
    for key, value in kwargs.items():
        time.sleep(5)
        result.append("The capital city of {} is {} ".format (key,value))

    return result

@app.task(name="test_celery.tasks.simulation", bind=True)
def run_simulation(self, a, b):
    if True:
        # manually update the task state
        self.update_state(
            state = states.FAILURE,
            meta = 'REASON FOR FAILURE'
        )

        # ignore the task so no other state is recorded
        raise Ignore()