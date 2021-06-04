broker_url = 'pyamqp://guest:guest@broker:5672/'
result_backend = 'db+mysql+pymysql://osmos:osmos@mariadb:3306/celerydb'
result_persistent = True
result_extended = True
task_store_errors_even_if_ignored = True