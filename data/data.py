import datetime
import random
from faker import Faker
from datetime import datetime, timedelta, timezone
from data_config.config import Config, load_config
import os

# загружаем конфиг в переменную config
config: Config = load_config()

# инициализируем токен и урл
TOKEN_SENDER: str = config.stage.token_sender
TOKEN_RECIPIENT: str = config.stage.token_recipient
TOKEN_NOT_RESIDENT: str = config.stage.token_not_resident
TOKEN_COORDINATOR: str = config.stage.token_coordinator
TOKEN_SECOND_COORDINATOR: str = config.stage.token_second_coordinator
TOKEN_SENDER_V3: str = config.stage.token_sender_v3
TOKEN_RECIPIENT_V3: str = config.stage.token_recipient_v3
TOKEN_NOT_RESIDENT_V3: str = config.stage.token_not_resident_v3
TOKEN_COORDINATOR_V3: str = config.stage.token_coordinator_v3
TOKEN_SECOND_COORDINATOR_V3: str = config.stage.token_second_coordinator_v3
BASE_URL_V1: str = config.stage.base_url_v1
BASE_URL_V3: str = config.stage.base_url_v3
employee_workplace_Id_sender: str = config.stage.employee_workplace_Id_sender
employee_workplace_Id_recipient: str = config.stage.employee_workplace_Id_recipient
employee_workplace_Id_not_resident: str = config.stage.employee_workplace_Id_not_resident
employee_workplace_Id_coordinator: str = config.stage.employee_workplace_Id_coordinator
employee_workplace_Id_second_coordinator: str = config.stage.employee_workplace_Id_second_coordinator

# явное обозначение ключей и значений в словаре VARIABLES является информативным
VARIABLES: dict = {
    "country_code": None,  # код страны
    "Employee_Id_current_user": None,  # EmployeeId текущего User'а
    "Employee_Id_current_user_info": None,  # информация о текущем сотруднике
    "Created_Employee_Id": None,  # EmployeeId нового созданного сотрудника
    "Created_Employee_Id_not_resident": None,  # EmployeeId нового созданного сотрудника нерезидента
    "Created_Employee_Id_info": None,  # информация о новом созданном сотруднике
    "Created_Employee_Id_info_not_resident": None,  # информация о новом созданном сотруднике нерезиденте
    "Subdivision_Id": None,  # SubdivisionId для тестов с подразделениями
    "JobTitle_Id": None,  # JobTitle Id для тестов с должностями
    "Created_JobTitle_Id": None,  # JobTitle Id добавленный в результате создания должности
    "Tenant_of_current_user": None,  # Tenant Id текущего пользователя
    "Created_Subdivision_Id": None,  # Subdivision Id добавленный в результате создания подразделения
    "Saga_User_Snils": None,  # Снилс саги из get-запроса ко всем сагам
    "Request_certificate_Id": None,  # Id запроса на выпуск сертификата
    "Created_document_type_Id": None,  # Id созданного типа документа
    "Created_document_Id": None,  # Id созданного документа
    "Created_attach_file_for_document": None,  # Id прикрепленного файла к созданному документу
    "Created_route_Id": None,  # Id созданного типа документа
    "Certificate_Id": None  # Id созданного сертификата
}

# хедеры для Отправителя
headers_sender: dict = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {TOKEN_SENDER}',
    'employeeworkplaceid': f'{employee_workplace_Id_sender}',
    'kedo-gateway-token-type': 'Development'
}

# хедеры Получателя
headers_recipient: dict = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {TOKEN_RECIPIENT}',
    'employeeworkplaceid': f'{employee_workplace_Id_recipient}',
    'kedo-gateway-token-type': 'Development'
}

# хедеры для отправки файла Отправителем
headers_form_data_sender: dict = {
    'Authorization': f'Bearer {TOKEN_SENDER}',
    'employeeworkplaceid': f'{employee_workplace_Id_sender}',
    'kedo-gateway-token-type': 'Development',
}

# хедеры для отправки файла Нерезидентом
headers_form_data_not_resident: dict = {
    'Authorization': f'Bearer {TOKEN_NOT_RESIDENT}',
    'employeeworkplaceid': f'{employee_workplace_Id_not_resident}',
    'kedo-gateway-token-type': 'Development',
}

# хедеры Нерезидента
headers_not_resident: dict = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {TOKEN_NOT_RESIDENT}',
    'employeeworkplaceid': f'{employee_workplace_Id_not_resident}',
    'kedo-gateway-token-type': 'Development'
}

# хедеры для Согласованта
headers_coordinator: dict = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {TOKEN_COORDINATOR}',
    'employeeworkplaceid': f'{employee_workplace_Id_coordinator}',
    'kedo-gateway-token-type': 'Development'
}

# хедеры для второго Согласованта
headers_second_coordinator: dict = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {TOKEN_SECOND_COORDINATOR}',
    'employeeworkplaceid': f'{employee_workplace_Id_second_coordinator}',
    'kedo-gateway-token-type': 'Development'
}

# хедеры для Отправителя v3
headers_sender_v3: dict = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {TOKEN_SENDER_V3}',
    'employeeworkplaceid': f'{employee_workplace_Id_sender}',
    'kedo-gateway-token-type': 'IntegrationApi'
}

# хедеры для отправки файла Отправителем v3
headers_form_data_sender_v3: dict = {
    'Authorization': f'Bearer {TOKEN_SENDER_V3}',
    'employeeworkplaceid': f'{employee_workplace_Id_sender}',
    'kedo-gateway-token-type': 'IntegrationApi',
}

# хедеры Получателя v3
headers_recipient_v3: dict = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {TOKEN_RECIPIENT_V3}',
    'employeeworkplaceid': f'{employee_workplace_Id_recipient}',
    'kedo-gateway-token-type': 'IntegrationApi'
}

# хедеры для Согласованта v3
headers_coordinator_v3: dict = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {TOKEN_COORDINATOR_V3}',
    'employeeworkplaceid': f'{employee_workplace_Id_coordinator}',
    'kedo-gateway-token-type': 'IntegrationApi'
}

# хедеры для второго Согласованта v3
headers_second_coordinator_v3: dict = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {TOKEN_SECOND_COORDINATOR_V3}',
    'employeeworkplaceid': f'{employee_workplace_Id_second_coordinator}',
    'kedo-gateway-token-type': 'IntegrationApi'
}

# хедеры Нерезидента
headers_not_resident_v3: dict = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {TOKEN_NOT_RESIDENT_V3}',
    'employeeworkplaceid': f'{employee_workplace_Id_not_resident}',
    'kedo-gateway-token-type': 'IntegrationApi'
}


def put_employee_body_generate(employee_info_data: dict, is_resident: bool) -> dict:
    """Генерация данных для изменения employee из полученного EmployeeId
    :param str employee_info_data: персональные данные сотрудника
    :param bool is_resident: сотрудник - резидент / нерезидент
    :return: тело запроса
    """
    fake = Faker(['ru_RU'])
    if is_resident:
        employee_put_data = {
            "FirstName": fake.first_name_male(),
            "LastName": employee_info_data['LastName'],
            "MiddleName": employee_info_data['MiddleName'],
            "BirthDate": '1965-12-09',
            "Gender": employee_info_data['Gender'],
            "PassportSerial": employee_info_data['PersonalInfo']['PassportSerial'],
            "PassportNumber": employee_info_data['PersonalInfo']['PassportNumber'],
            "PassportIssuer": employee_info_data['PersonalInfo']['PassportIssuer'],
            "RegistrationAddress": employee_info_data['PersonalInfo']['RegistrationAddress'],
            "PlaceOfResidence": employee_info_data['PersonalInfo']['PlaceOfResidence'],
            "CountryCode": None,
            "IssuerSubdivisionCode": employee_info_data['PersonalInfo']['IssuerSubdivisionCode'],
            "DateOfIssued": '2013-06-30',
            "DateOfExpiration": employee_info_data['PersonalInfo']['DateOfExpiration'],
            "IsResident": employee_info_data['PersonalInfo']['IsResident'],
            "Snils": employee_info_data['PersonalInfo']['Snils'],
            "Inn": employee_info_data['PersonalInfo']['Inn'],
            "Email": employee_info_data['Contacts'][0]['Email'],
            "BirthAddress": employee_info_data['PersonalInfo']['BirthAddress']
        }
        return employee_put_data
    else:
        employee_put_data = {
            "FirstName": fake.first_name_male(),
            "LastName": employee_info_data['LastName'],
            "MiddleName": employee_info_data['MiddleName'],
            "BirthDate": '1965-12-09',
            "Gender": employee_info_data['Gender'],
            "PassportSerial": employee_info_data['PersonalInfo']['PassportSerial'],
            "PassportNumber": employee_info_data['PersonalInfo']['PassportNumber'],
            "PassportIssuer": employee_info_data['PersonalInfo']['PassportIssuer'],
            "RegistrationAddress": employee_info_data['PersonalInfo']['RegistrationAddress'],
            "PlaceOfResidence": employee_info_data['PersonalInfo']['PlaceOfResidence'],
            "CountryCode": employee_info_data['PersonalInfo']['CountryCode'],
            "IssuerSubdivisionCode": employee_info_data['PersonalInfo']['IssuerSubdivisionCode'],
            "DateOfIssued": '2013-06-30',
            "DateOfExpiration": employee_info_data['PersonalInfo']['DateOfExpiration'],
            "IsResident": employee_info_data['PersonalInfo']['IsResident'],
            "Snils": employee_info_data['PersonalInfo']['Snils'],
            "Inn": employee_info_data['PersonalInfo']['Inn'],
            "Email": employee_info_data['Contacts'][0]['Email'],
            "BirthAddress": employee_info_data['PersonalInfo']['BirthAddress']
        }
        return employee_put_data


def snils_generator() -> str:
    """Генерация СНИЛС
    :return: снилс в виде 000-000-000 00
    """
    numbers: list = []
    control_digit: int = 0

    while control_digit not in list(range(10, 100)):
        numbers = [random.randint(1, 9) for el in range(1, 9)]
        numbers.insert(0, 1)
        new_numbers: list = []
        for i in range(len(numbers)):
            new_numbers.append(numbers[i] * (9 - i))
        control_digit = sum(new_numbers) % 101

    numbers.insert(3, '-')
    numbers.insert(7, '-')

    snils = [str(el) for el in numbers]
    snils = ''.join(snils) + ' ' + str(control_digit)

    return snils


def phone_generator() -> str:
    """Генерация номера телефона
    :return: номер телефона в виде 79001110011
    """
    numbers = [str(random.randint(1, 9)) for el in range(9)]
    numbers.insert(0, '79')
    return ''.join(numbers)


def employee_body_generate(resident: bool) -> dict:
    """Генерация генерации body для создания рабочего места
    :param bool resident: сотрудник - резидент / нерезидент
    :return: тело запроса
    """
    fake = Faker(['ru_RU'])
    if resident:
        employee_body: dict = {
            "FirstName": fake.first_name_male(),
            "LastName": fake.last_name_male(),
            "MiddleName": fake.middle_name_male(),
            "BirthDate": "1965-12-09T00:00:00Z",
            "Gender": "Male",
            "PassportSerial": str(random.randint(1234, 9999)),
            "PassportNumber": str(random.randint(123456, 999999)),
            "PassportIssuer": "УФМС",
            "BirthAddress": "г. Сочи",
            "RegistrationAddress": "г. Санкт-Петербург, ул. Садовая, д. 2",
            "PlaceOfResidence": "г. Санкт-Петербург, ул. Садовая, д. 2",
            "CountryCode": None,
            "IssuerSubdivisionCode": str(random.randint(123456, 999999)),
            "DateOfIssued": "2023-02-01T00:00:00Z",
            "DateOfExpiration": None,
            "IsResident": True,
            "Snils": snils_generator(),
            "Inn": fake.individuals_inn(),
            "PhoneNumber": phone_generator(),
            "Email": fake.ascii_email()
        }
        return employee_body
    else:
        employee_body: dict = {
            "FirstName": fake.first_name_male(),
            "LastName": fake.last_name_male(),
            "MiddleName": fake.middle_name_male(),
            "BirthDate": "1965-12-09T00:00:00Z",
            "Gender": "Male",
            "PassportSerial": None,
            "PassportNumber": "TA" + str(random.randint(123456, 999999)),
            "PassportIssuer": None,
            "BirthAddress": "г. Сочи",
            "RegistrationAddress": "г. Санкт-Петербург, ул. Садовая, д. 2",
            "PlaceOfResidence": None,
            "CountryCode": "762",
            "IssuerSubdivisionCode": None,
            "DateOfIssued": "2024-01-01T00:00:00Z",
            "DateOfExpiration": str((datetime.now(tz=timezone.utc)) + timedelta(days=365)),
            "IsResident": False,
            "Snils": snils_generator(),
            "Inn": fake.individuals_inn(),
            "PhoneNumber": phone_generator(),
            "Email": fake.ascii_email()
        }
        return employee_body


def employee_workplace_body_generate() -> dict:
    """Генерации body для создания рабочего места
    :return: тело запроса
    """
    employee_workplace_body: dict = {
        "PersonalCode": random.randint(112233, 999999),
        "SubdivisionId": VARIABLES['Subdivision_Id'],
        "JobTitleId": VARIABLES['JobTitle_Id'],
        "WorkBegan": str(datetime.now(tz=timezone.utc) - timedelta(days=10)),
        "WorkEnded": ""
    }
    return employee_workplace_body


def document_body_generate(is_tenant: bool) -> dict:
    """Генерация body для создания документа
    :param is_tenant: документ для тенанта
    :return: тело запроса
    """
    if not is_tenant:
        document_body: dict = {
            "DocumentTypeId": VARIABLES['Created_document_type_Id'],
            "Comment": "HELLO, world!",
            "RecipientIds": [
                employee_workplace_Id_recipient
            ],
        }
        return document_body
    elif is_tenant:
        document_body: dict = {
            "DocumentTypeId": VARIABLES['Created_document_type_Id'],
            "Comment": "HELLO, world!",
            "RecipientIds": None,
            "IsRecipientTenant": True
        }
        return document_body


def document_body_member_generate(command: str) -> dict:
    """Генерация body для замены старого участника маршрута
    на нового участника
    :param str command: команда соответствующая ключу в словаре
    """
    all_commands: dict = {
        "positive_put_route_member": {
            "DocumentIds": [
                VARIABLES['Created_document_type_Id']
            ],
            "OldEmployeeWorkplaceId": employee_workplace_Id_not_resident,
            "NewEmployeeWorkplaceId": employee_workplace_Id_coordinator
        }
    }
    for key in all_commands:
        if command == key:
            return all_commands[key]


def document_route_body_generate(method: str) -> dict:
    """Генерация body для создания маршрута в документе
    :param method: метод запроса
    :return: тело запроса
    """
    # создание стандартного маршрута
    if method == 'post':
        route_body: dict = {
            "RouteStages": [
                {
                    "RoutingRole": "Sender",
                    "RoutingStrategy": "Sequential",
                    "SignatureType": "SES, UUES",
                    "RouteMembers": []
                },
                {
                    "RouteMembers":
                        [
                            {
                                "EmployeeWorkplaceId": employee_workplace_Id_not_resident,
                                "SignatureType": "SES, UUES",
                                "RecipientTenant": False
                            }
                        ],
                    "SignatureType": "SES, UUES",
                    "RoutingRole": "Coordinator",
                    "RoutingStrategy": "ParallelOne"
                },
                {
                    "RoutingRole": "Recipient",
                    "RoutingStrategy": "ParallelEveryone",
                    "SignatureType": "SES, UUES",
                    "RouteMembers": []
                }
            ]
        }
        return route_body
    # изменение стандартного маршрута, Отправитель становится Согласовантом
    elif method == 'put':
        route_body: dict = {
            "RouteStages": [
                {
                    "RouteMembers": [
                        {
                            "EmployeeWorkplaceId": employee_workplace_Id_sender,
                            "SignatureType": "UUES"
                        }
                    ],
                    "SignatureType": "UUES",
                    "RoutingRole": "Sender",
                    "RoutingStrategy": "Sequential",
                    "CurrentStatus": "Completed"
                },
                {
                    "RouteMembers": [
                        {
                            "EmployeeWorkplaceId": employee_workplace_Id_sender,
                            "SignatureType": "SES,UUES"
                        }
                    ],
                    "SignatureType": "SES,UUES",
                    "RoutingRole": "Coordinator",
                    "RoutingStrategy": "ParallelOne",
                    "CurrentStatus": "Active"
                },
                {
                    "RouteMembers": [
                        {
                            "EmployeeWorkplaceId": employee_workplace_Id_recipient,
                            "SignatureType": "SES, UUES",
                            "RecipientTenant": False
                        }
                    ],
                    "SignatureType": "SES, UUES",
                    "RoutingRole": "Recipient",
                    "RoutingStrategy": "ParallelEveryone",
                    "CurrentStatus": "Pending"
                }
            ]
        }
        return route_body
    # создание маршрута для отправки док-та на тенант
    elif method == 'post_for_tenant':
        route_body: dict = {
            "RouteStages": [
                {
                    "RoutingRole": "Sender",
                    "RoutingStrategy": "Sequential",
                    "SignatureType": "SES, UUES",
                    "RouteMembers": []
                },
                {
                    "RouteMembers": [
                        {
                            "EmployeeWorkplaceId": employee_workplace_Id_sender,
                            "SignatureType": "SES, UUES",
                            "RecipientTenant": False
                        }
                    ],
                    "SignatureType": "SES, UUES",
                    "RoutingRole": "Coordinator",
                    "RoutingStrategy": "ParallelOne"
                },
                {
                    "RoutingRole": "Recipient",
                    "RoutingStrategy": "ParallelOne",
                    "SignatureType": "SES, UUES",
                    "RouteMembers": []
                }
            ]
        }
        return route_body
    # изменение маршрута для отправки док-та на тенант
    elif method == 'put_for_tenant':
        route_body: dict = {
            "RouteStages": [
                {
                    "RoutingStrategy": "Sequential",
                    "RoutingRole": "Sender",
                    "SignatureType": "UUES",
                    "RouteMembers": [
                        {
                            "EmployeeWorkplaceId": employee_workplace_Id_sender,
                            "SignatureType": "UUES"
                        }
                    ]
                },
                {
                    "RoutingStrategy": "ParallelOne",
                    "RoutingRole": "Coordinator",
                    "SignatureType": "SES,UUES",
                    "RouteMembers": [
                        {
                            "EmployeeWorkplaceId": employee_workplace_Id_not_resident,
                            "SignatureType": "SES,UUES"
                        }
                    ]
                },
                {
                    "RoutingStrategy": "ParallelOne",
                    "RoutingRole": "Recipient",
                    "SignatureType": "SES,UUES",
                    "RouteMembers": [
                        {
                            "RecipientTenant": True,
                            "SignatureType": "SES,UUES"
                        }
                    ]
                }
            ]
        }
        return route_body
    # создание маршрута док-та на v3
    elif method == 'post_v3':
        route_body: dict = {
            "RouteStages": [
                {
                    "RoutingRole": "Sender",
                    "RoutingStrategy": "Sequential",
                    "SignatureType": "SES, UUES",
                    "RouteMembers": []
                },
                {
                    "RouteMembers":
                        [
                            {
                                "EmployeeWorkplaceId": employee_workplace_Id_not_resident,
                                "SignatureType": "SES, UUES",
                                "RecipientTenant": False
                            }
                        ],
                    "SignatureType": "SES, UUES",
                    "RoutingRole": "Coordinator",
                    "RoutingStrategy": "ParallelOne"
                },
                {
                    "RoutingRole": "Recipient",
                    "RoutingStrategy": "ParallelEveryone",
                    "SignatureType": "SES, UUES",
                    "RouteMembers": []
                }
            ]
        }
        return route_body
    # изменение маршрута док-та на v3
    elif method == 'put_v3':
        route_body: dict = {
              "RouteStages": [
                {
                  "RoutingStrategy": "Sequential",
                  "RoutingRole": "Sender",
                  "SignatureType": "UUES",
                  "RouteMembers": [
                    {
                      "EmployeeWorkplaceId": employee_workplace_Id_sender,
                      "SignatureType": "UUES"
                    }
                  ]
                },
                {
                  "RoutingStrategy": "ParallelOne",
                  "RoutingRole": "Coordinator",
                  "SignatureType": "SES, UUES",
                  "RouteMembers": [
                    {
                      "EmployeeWorkplaceId": employee_workplace_Id_coordinator,
                      "SignatureType": "SES, UUES"
                    }
                  ]
                },
                {
                  "RoutingStrategy": "ParallelOne",
                  "RoutingRole": "Coordinator",
                  "SignatureType": "UUES, SES",
                  "RouteMembers": [
                    {
                      "EmployeeWorkplaceId": employee_workplace_Id_second_coordinator,
                      "SignatureType": "UUES, SES"
                    }
                  ]
                },
                {
                  "RoutingStrategy": "ParallelEveryone",
                  "RoutingRole": "Recipient",
                  "SignatureType": "SES, UUES",
                  "RouteMembers": [
                    {
                      "EmployeeWorkplaceId": employee_workplace_Id_recipient,
                      "SignatureType": "SES, UUES"
                    }
                  ]
                }
              ]
            }
        return route_body
    # создание маршрута док-та с 3 этапами согласования
    elif method == 'post_three_cordinators':
        route_body: dict = {
              "RouteStages": [
                {
                  "RoutingRole": "Sender",
                  "RoutingStrategy": "Sequential",
                  "SignatureType": "SES, UUES",
                  "RouteMembers": []
                },
                {
                  "RouteMembers": [
                    {
                      "EmployeeWorkplaceId": employee_workplace_Id_coordinator,
                      "SignatureType": "SES",
                      "RecipientTenant": False
                    }
                  ],
                  "SignatureType": "SES",
                  "RoutingRole": "Coordinator",
                  "RoutingStrategy": "ParallelOne"
                },
                {
                  "RouteMembers": [
                    {
                      "EmployeeWorkplaceId": employee_workplace_Id_second_coordinator,
                      "SignatureType": "UUES, SES",
                      "RecipientTenant": False
                    },
                    {
                      "EmployeeWorkplaceId": employee_workplace_Id_not_resident,
                      "SignatureType": "UUES, SES",
                      "RecipientTenant": False
                    }
                  ],
                  "SignatureType": "UUES, SES",
                  "RoutingRole": "Coordinator",
                  "RoutingStrategy": "ParallelOne"
                },
                {
                  "RouteMembers": [
                    {
                      "EmployeeWorkplaceId": employee_workplace_Id_sender,
                      "SignatureType": "UUES",
                      "RecipientTenant": False
                    }
                  ],
                  "SignatureType": "UUES",
                  "RoutingRole": "Coordinator",
                  "RoutingStrategy": "ParallelOne"
                },
                {
                  "RoutingRole": "Recipient",
                  "RoutingStrategy": "ParallelOne",
                  "SignatureType": "SES, UUES",
                  "RouteMembers": []
                }
              ]
            }
        return route_body
    # изменение маршрута док-та с 3 этапами Согласования
    elif method == 'put_three_cordinators':
        route_body: dict = {
                "RouteStages": [
                    {
                        "RoutingStrategy": "Sequential",
                        "RoutingRole": "Sender",
                        "SignatureType": "UUES",
                        "RouteMembers": [
                            {
                                "EmployeeWorkplaceId": employee_workplace_Id_sender,
                                "SignatureType": "UUES"
                            }
                        ]
                    },
                    {
                        "RoutingStrategy": "ParallelOne",
                        "RoutingRole": "Coordinator",
                        "SignatureType": "SES",
                        "RouteMembers": [
                            {
                                "EmployeeWorkplaceId": employee_workplace_Id_coordinator,
                                "SignatureType": "SES"
                            }
                        ]
                    },
                    {
                        "RoutingStrategy": "ParallelOne",
                        "RoutingRole": "Coordinator",
                        "SignatureType": "SES, UUES",
                        "RouteMembers": [
                            {
                                "EmployeeWorkplaceId":  employee_workplace_Id_second_coordinator,
                                "SignatureType": "SES, UUES"
                            },
                            {
                                "EmployeeWorkplaceId": employee_workplace_Id_not_resident,
                                "SignatureType": "SES, UUES"
                            }
                        ]
                    },
                    {
                        "RoutingStrategy": "ParallelOne",
                        "RoutingRole": "Coordinator",
                        "SignatureType": "UUES",
                        "RouteMembers": [
                            {
                                "EmployeeWorkplaceId": employee_workplace_Id_sender,
                                "SignatureType": "UUES"
                            },
                            {
                                "EmployeeWorkplaceId": employee_workplace_Id_coordinator,
                                "SignatureType": "UUES"
                            }
                        ]
                    },
                    {
                        "RoutingStrategy": "ParallelOne",
                        "RoutingRole": "Recipient",
                        "SignatureType": "SES, UUES",
                        "RouteMembers": [
                            {
                                "RecipientTenant": True,
                                "SignatureType": "SES, UUES"
                            }
                        ]
                    }
                ]
            }
        return route_body


def document_body_signature_generate() -> dict:
    """Генерация body для подписания документа
    :return: тело запроса
    """
    body_signature: dict = {
        "SignatureType": "UUES",
        "FileBase64": None,
        "Signatures": [],
        "CertificateId": VARIABLES["Certificate_Id"]
    }
    return body_signature


def document_type_body_generate(method: str) -> dict:
    """Генерация body для создания типа документа
    :param method: метод запроса
    :return: тело запроса
    """
    fake = Faker(['ru_RU'])
    if method == 'post':
        document_type_body: dict = {
            "ShortName": f"{fake.word()} {fake.word()}",
            "MinTrudDocumentTypeId": "9e86fbb3-eac7-0108-6039-db4e6d63ad08",
            "SigningPeriod": "5.00:00:00",
            "SignatureTypeSender": "SES, UUES",
            "SignatureTypeReceiver": "SES, UUES",
            "SenderRole": "Employee"
        }
        return document_type_body
    elif method == 'put':
        document_type_body: dict = {
            "Id": VARIABLES["Created_document_type_Id"],
            "ShortName": f"{fake.word()} {fake.word()}",
            "MinTrudDocumentTypeId": "9e86fbb3-eac7-0108-6039-db4e6d63ad08",
            "SigningPeriod": "6.00:00:00",
            "SignatureTypeSender": "UUES",
            "SignatureTypeReceiver": "UUES",
            "SenderRole": "Recruiter"
        }
        return document_type_body


def route_body_generate(method: str) -> dict:
    """Генерация body для шаблона маршрута
    :param method: метод запроса
    :return: тело запроса
    """
    fake = Faker(['ru_RU'])
    if method == 'post':
        route_body: dict = {
            "Name": f"{fake.word()} {fake.word()}",
            "SenderSubdivisions": [f"{VARIABLES['Subdivision_Id']}"],
            "DocTypes": [f"{VARIABLES['Created_document_type_Id']}"],
            "RouteStages":
                [
                    {
                        "EmployeeWorkplaceId": None,
                        "SubdivisionId": None,
                        "JobTitleId": None,
                        "SignatureType": None,
                        "RoutingOrder": 0,
                        "RoutingRole": "Sender"
                    },
                    {
                        "EmployeeWorkplaceId": f"{employee_workplace_Id_not_resident}",
                        "SubdivisionId": "",
                        "JobTitleId": "",
                        "SignatureType": "UUES,SES",
                        "RoutingOrder": 1,
                        "RoutingRole": "Coordinator"
                    },
                    {
                        "EmployeeWorkplaceId": None,
                        "SubdivisionId": None,
                        "JobTitleId": None,
                        "SignatureType": None,
                        "RoutingOrder": 2,
                        "RoutingRole": "Recipient"
                    }
                ]
        }
        return route_body
    elif method == 'put':
        route_body: dict = {
            "Name": f"{fake.word()} {fake.word()}",
            "SenderSubdivisions": [f"{VARIABLES['Subdivision_Id']}"],
            "DocTypes": [f"{VARIABLES['Created_document_type_Id']}"],
            "RouteStages":
                [
                    {
                        "EmployeeWorkplaceId": None,
                        "SubdivisionId": None,
                        "JobTitleId": None,
                        "SignatureType": None,
                        "RoutingOrder": 0,
                        "RoutingRole": "Sender"
                    },
                    {
                        "EmployeeWorkplaceId": f"{employee_workplace_Id_recipient}",
                        "SubdivisionId": "",
                        "JobTitleId": "",
                        "SignatureType": "UUES,SES",
                        "RoutingOrder": 1,
                        "RoutingRole": "Coordinator"
                    },
                    {
                        "EmployeeWorkplaceId": None,
                        "SubdivisionId": None,
                        "JobTitleId": None,
                        "SignatureType": None,
                        "RoutingOrder": 2,
                        "RoutingRole": "Recipient"
                    }
                ]
        }
        return route_body


def payloads_data_generate(command: str) -> dict:
    """Генерация body по переданной команде
    :param command: команда - ключ в словаре с данными
    :return: тело запроса / query-параметры
    """
    all_commands: dict = {
        'set_end_data': {'workEnded': str(datetime.now(tz=timezone.utc) + timedelta(days=5))},
        'job_title_name': {"Name": "QA машина"},
        'put_job_title_name': {"Name": "Ты QA машина"},
        'create_subdivision': {"Name": "Подразделение тостеров",
                               "SubdivisionCode": 1,
                               "ParentId": "",
                               "NumberOfSubdivisions": 0,
                               "TenantId": VARIABLES['Tenant_of_current_user'],
                               "ExternalId": str(random.randint(1111, 9999))},
        'patch_subdivision': {"Id": VARIABLES["Created_Subdivision_Id"],
                              "Name": "Подразделение тостеров ТУТ",
                              "SubdivisionCode": 1,
                              "ParentId": "",
                              "ExternalId": str(random.randint(1111, 9999)),
                              },
        'create_rbac': {"SubdivisionId": VARIABLES["Created_Subdivision_Id"],
                        "JobTitleId": VARIABLES["Created_JobTitle_Id"],
                        "AccessRole": "Employee, Recruiter, Administrator"},
        'put_rbac': {"accessRole": "Employee"},
        'Local': {"identificationTypeValue": "Local"},
        'Gosuslugi': {"identificationTypeValue": "Gosuslugi"},
        'source_attach_type_for_document': {'attachType': 'Source'},
        'comment': {"Comment": "Отмена"},
        'avatar': {"Url": "https://t.me/i/userpic/160/4_LWKj3_aBrh8Xs-SKKq23RL_Ab0KJhtQM1oKHjh9kg.jpg"}
    }

    for key in all_commands:
        if command == key:
            return all_commands[key]


def file_data_generate(file_name: str, string_file_name: str, type: str) -> dict:
    """Генерация пути для тестового файла
    :param file_name: имя файла
    :param string_file_name: имя параметра в теле запроса для загрузки файла
    :param type: тип загружаемого файла
    :return: тело запроса
    """
    # получаем текущую директорию, относительно которой будем строить путь
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # строим абсолютный путь к файлу в директории test_data
    file_path = os.path.join(current_dir, '..', 'test_data', file_name)
    # подготавливаем словарь с файлом для передачи в запрос
    file = {string_file_name: (file_name, open(file_path, 'rb'), type)}
    return file


def return_status_code(status_code: int) -> None:
    """Возвращение описания кода ответа"""
    code_dict: dict[int, str] = {200: '--OK--', 201: '--OK--', 400: '--BAD_REQUEST--',
                                 401: '--UNAUTHORIZED--', 403: '--FORBIDDEN--', 415: '--MEDIATYPE--',
                                 500: '--BACKEND__', 502: '--BAD_GATEWAY--', 504: '--TIMEOUT--'}

    if status_code in code_dict.keys():
        return print(code_dict[status_code])


if __name__ == "__main__":
    pass
