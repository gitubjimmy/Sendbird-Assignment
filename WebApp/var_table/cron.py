from django.db import connection
from .models import Variables
import sys
import schedule
import threading
import time
from django.utils import timezone

def refresh_variables():
    with connection.cursor() as cursor:
        print("refresing variable information...")
        cursor.execute("show variables")
        var_list = cursor.fetchall()
        for var in var_list:
            query = Variables.objects.filter(name=var[0])
            if len(query)==0:
                var_model = Variables(name=var[0], value=var[1])
                var_model.save()
            else:
                var_model = query[0]
                var_model.previous = var_model.value
                if var_model.value != var[1]:
                    var_model.value = var[1]
                    var_model.recently_modified = True
                    var_model.last_modified = timezone.now()
                else:
                    var_model.recently_modified = False
                var_model.save()
        print("finished refresing!")

def run_continuously(interval=1):
    """Continuously run, while executing pending jobs at each
    elapsed time interval.
    @return cease_continuous_run: threading. Event which can
    be set to cease continuous run. Please note that it is
    *intended behavior that run_continuously() does not run
    missed jobs*. For example, if you've registered a job that
    should run every minute and you set a continuous run
    interval of one hour then your job won't be run 60 times
    at each interval but only once.
    """
    try:
        cease_continuous_run = threading.Event()

        class ScheduleThread(threading.Thread):
            @classmethod
            def run(cls):
                while not cease_continuous_run.is_set():
                    schedule.run_pending()
                    time.sleep(interval)

        continuous_thread = ScheduleThread()
        continuous_thread.start()
        return cease_continuous_run
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

def start_scheduler():
    schedule.every(1).minutes.do(refresh_variables)
    stop_run_continuously = run_continuously()
