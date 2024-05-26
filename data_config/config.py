from dataclasses import dataclass

from environs import Env


@dataclass
class StageData:
    """датакласс StageData содержит типы данных для STAGE стенда"""
    token_sender: str
    token_recipient: str
    token_not_resident: str
    token_coordinator: str
    token_second_coordinator: str
    token_sender_v3: str
    token_recipient_v3: str
    token_not_resident_v3: str
    token_coordinator_v3: str
    token_second_coordinator_v3: str
    base_url_v1: str
    base_url_v3: str
    phone_number_sender: str
    phone_number_recipient: str
    phone_number_not_resident: str
    phone_number_coordinator: str
    phone_number_second_coordinator: str
    password: str
    employee_workplace_Id_sender: str
    employee_workplace_Id_recipient: str
    employee_workplace_Id_not_resident: str
    employee_workplace_Id_coordinator: str
    employee_workplace_Id_second_coordinator: str

@dataclass
class Secrets:
    """датакласс Secrets содержит типа данных для генерации токена"""
    client_id: str
    client_secret: str
    redirect_uri: str
    authorization_base_url: str
    token_url: str
    audience: str
    issuer: str
    key_kedo: str
    key_dev: str

@dataclass
class DataBaseConfigStage:
    """датакласс DataBaseConfigStage содержит типы дынных для подключения БД"""
    dbname: str
    db_host: str
    db_user: str
    db_password: str
    db_port: str

@dataclass
class TokenData:
    """датакласс содержит данные для генерации токена любому сотруднику в тенанте"""
    token: str
    base_url: str
    issuer: str
    employee_workplace_id: str
    employee_id: str


@dataclass
class Config:
    """датакласс Config содержит ссылки на объекты с типами данных"""
    stage: StageData
    db: DataBaseConfigStage
    secrets: Secrets
    token_data: TokenData

def load_config(path: str | None = None) -> Config:
    """Загрузка переменных окружения из файла .env
    :param str path: путь до файла с переменными окружения
    :param None path: если путь к файлу не предоставлен, используется значение по-умолчанию None
    """
    env = Env()
    env.read_env(path)
    return Config(
        stage=StageData(
            token_sender=env('TOKEN_STAGE_SENDER'),
            token_recipient=env('TOKEN_STAGE_RECIPIENT'),
            token_not_resident=env('TOKEN_STAGE_NOT_RESIDENT'),
            token_coordinator=env('TOKEN_STAGE_COORDINATOR'),
            token_second_coordinator=env('TOKEN_STAGE_SECOND_COORDINATOR'),
            token_sender_v3=env('TOKEN_STAGE_SENDER_V3'),
            token_recipient_v3=env('TOKEN_STAGE_RECIPIENT_V3'),
            token_not_resident_v3=env('TOKEN_STAGE_NOT_RESIDENT_V3'),
            token_coordinator_v3=env('TOKEN_STAGE_COORDINATOR_V3'),
            token_second_coordinator_v3=env('TOKEN_STAGE_SECOND_COORDINATOR_V3'),
            base_url_v1=env('BASE_URL_STAGE_V1'),
            base_url_v3=env('BASE_URL_STAGE_V3'),
            phone_number_sender=env('PHONE_NUMBER_SENDER'),
            phone_number_recipient=env('PHONE_NUMBER_RECIPIENT'),
            phone_number_not_resident=env('PHONE_NUMBER_NOT_RESIDENT'),
            phone_number_coordinator=env('PHONE_NUMBER_COORDINATOR'),
            phone_number_second_coordinator=env('PHONE_NUMBER_SECOND_COORDINATOR'),
            password=env('PASSWORD'),
            employee_workplace_Id_sender=env('employee_workplace_Id_sender'),
            employee_workplace_Id_recipient=env('employee_workplace_Id_recipient'),
            employee_workplace_Id_not_resident=env('employee_workplace_Id_not_resident'),
            employee_workplace_Id_coordinator=env('employee_workplace_Id_coordinator'),
            employee_workplace_Id_second_coordinator=env('employee_workplace_Id_second_coordinator')
        ),
        db=DataBaseConfigStage(
            dbname=env('DBNAME'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD'),
            db_port=env('PORT')
        ),
        secrets=Secrets(
            client_id=env('CLIENT_ID'),
            client_secret=env('CLIENT_SECRET'),
            redirect_uri=env('REDIRECT_URI'),
            authorization_base_url=env('AUTHORIZATION_BASE_URL'),
            token_url=env('TOKEN_URL'),
            audience=env('AUDIENCE'),
            issuer=env('ISSUER'),
            key_kedo=env('KEY_KEDO'),
            key_dev=env('KEY_DEV')
        ),
        token_data=TokenData(
            token=env('TOKEN_RECRUITER'),
            base_url=env('BASE_URL'),
            issuer=env('ISSUER'),
            employee_workplace_id=env('employee_workplace_Id'),
            employee_id=env('employee_Id'),
        )
    )
