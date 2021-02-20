from django.apps import AppConfig
import os

class VarTableConfig(AppConfig):
    name = 'var_table'
    
    def ready(self):
        from . import cron

        if os.environ.get('RUN_MAIN', None) != 'true':
            cron.start_scheduler()
