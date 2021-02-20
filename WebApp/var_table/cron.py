from django.db import connection
from .models import Variables
from schedule import Scheduler
import time
import threading

def refresh_variables():
    with connection.cursor() as cursor:
        cursor.execute("show variables")
        var_list = cursor.fetchall()
        for var in var_list:
            print(var)
            var_model = Variables(name=var[0], value=var[1])
            var_model.save()

def run_continuously(self, interval=1):
    """Continuously run, while executing pending jobs at each elapsed
    time interval.
    @return cease_continuous_run: threading.Event which can be set to
    cease continuous run.
    Please note that it is *intended behavior that run_continuously()
    does not run missed jobs*. For example, if you've registered a job
    that should run every minute and you set a continuous run interval
    of one hour then your job won't be run 60 times at each interval but
    only once.
    """

    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run

Scheduler.run_continuously = run_continuously

def start_scheduler():
    scheduler = Scheduler()
    schedule.every(1).minutes.do(refresh_variables)
    scheduler.run_continuously()
