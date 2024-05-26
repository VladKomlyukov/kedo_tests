import psycopg2
from data_config.config import Config, load_config


# загружаем конфиг с данными для подключения к БД
config: Config = load_config()

# инициализируем переменные для подключения к БД
dbname = config.db.dbname
user = config.db.db_user
password = config.db.db_password
host = config.db.db_host
port = config.db.db_port


# пытаемся подключиться к базе данных
connection = psycopg2.connect(dbname=dbname,
                                  user=user,
                                  password=password,
                                  host=host,
                                  port=port)

# устанавливаем автокоммит, чтобы выражения sql автоматически выполнялись при каждом вызове метода cursor.execute()
connection.autocommit = True

def select_confirmation_code(Employee_id: str) -> str:
    # с помощью метода cursor происходит работа с запросами в БД
    # конструкция with позволяет автоматически закрывать соединение с БД
    # иначе пришлось бы сначала создать курсор cursor = connection.cursor
    # и после каждого запроса писать cursor.close() и connection.close()
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT "ConfirmationCode" FROM "RequestCertificates" WHERE "EmployeeId" = %s AND '
            '"RequestCertificateStatus" = %s', (f'{Employee_id}', 4))
        result = cursor.fetchone()
        return result[0]