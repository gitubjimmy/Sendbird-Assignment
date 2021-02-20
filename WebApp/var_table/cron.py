from django.db import connection
from .models import Variables

def refresh_variables():
    with connection.cursor() as cursor:
        cursor.execute("show variables")
        var_list = cursor.fetchall()
        for var in var_list:
            print(var)
            var_model = Variables(name=var[0], value=var[1], type="session")
            var_model.save()
