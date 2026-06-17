import logging

logger_app = logging.getLogger('app')
logger_app_api = logging.getLogger('app.api')
logger_app_database = logging.getLogger('app.database')
logger_app_database_my_sql = logging.getLogger('app.database.my_sql')
logger_app_database_postgres = logging.getLogger('app.database.postgres')

logger_auth = logging.getLogger('auth')
logger_auth_user = logging.getLogger('auth.user')
