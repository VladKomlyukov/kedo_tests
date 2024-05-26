import json
import time
from typing import Union

import requests as r

from data import db
from data.data import BASE_URL_V1, VARIABLES, put_employee_body_generate, payloads_data_generate, file_data_generate


class ApiStaffClient:
    """API сервиса Staff"""
    class Employees:
        """Сотрудники"""
        def get_countries(self, headers: dict) -> tuple:
            """Получить список стран"""
            response = r.get(f'{BASE_URL_V1}/staff/Countries', headers=headers)
            data = response.json()
            for el in range(len(data)):
                if data[el]['Name'] == 'Россия':
                    VARIABLES['country_code'] = data[0]['Id']
                    break
            return response.status_code, response.json(), response.url

        def get_country(self, headers: dict) -> tuple:
            """Получить страну по id страны"""
            response = r.get(f'{BASE_URL_V1}/staff/Countries/{VARIABLES["country_code"]}', headers=headers)
            return response.status_code, response.json(), response.url


        def get_employees(self, path: str, headers: dict) -> tuple:
            """Получить список всех сотрудников"""
            if path == '&WorkingOnly=true':
                response = r.get(f'{BASE_URL_V1}/staff/Employees?Offset=0&Count=2000{path}', headers=headers)
                return response.status_code, response.json(), response.url
            elif path == '&WorkingOnly=false':
                response = r.get(f'{BASE_URL_V1}/staff/Employees?Offset=0&Count=2000{path}', headers=headers)
                return response.status_code, response.json(), response.url

        def get_employee_personal_info(self, headers: dict) -> tuple:
            """Получить персональные данные сотрудника"""
            response = r.get(f'{BASE_URL_V1}/staff/Employees/PersonalInfo', headers=headers)
            status_code = response.status_code
            data = response.json()
            VARIABLES['Employee_Id_current_user'] = data['Id']
            VARIABLES['Tenant_of_current_user'] = data['EmployeeWorkplaces'][0]['Subdivision']['Tenant']['Id']
            return status_code, response.json(), response.url

        def get_employee_by_id_current_user(self, headers: dict) -> tuple:
            """Получить информацию о текущем сотруднике по Id"""
            response = r.get(f'{BASE_URL_V1}/staff/Employees/{VARIABLES["Employee_Id_current_user"]}',
                             headers=headers)
            status_code = response.status_code
            data = response.json()
            VARIABLES['Subdivision_Id'] = data['EmployeeWorkplaces'][0]['Subdivision']['Id']
            VARIABLES['JobTitle_Id'] = data['EmployeeWorkplaces'][0]['JobTitle']['Id']
            VARIABLES["Employee_Id_current_user_info"] = data
            return status_code, response.json(), response.url

        def get_employee_by_id_created_user(self, headers: dict) -> tuple:
            """Получить информацию о только что созданном сотруднике по Id"""
            response = r.get(f'{BASE_URL_V1}/staff/Employees/{VARIABLES["Created_Employee_Id"]}',
                             headers=headers)
            VARIABLES["Created_Employee_Id_info"] = response.json()
            return response.status_code, response.json(), response.url

        def get_employee_certificates(self, headers: dict) -> tuple:
            """Получить сертификаты сотрудника"""
            response = r.get(f'{BASE_URL_V1}/staff/Employees/Certificates', headers=headers)
            data = response.json()
            for el in range(len(data)):
                if data[el]['CertificateStatus'] == 'Issued':
                    VARIABLES['Certificate_Id'] = data[el]['ExternalId']
                    break
            else:
                print('Issued Certificate was not found')
            return response.status_code, response.json(), response.url

        def check_employee_certificate_status(self, headers: dict) -> None:
            """Проверка, что сертификат УНЭП выпущен"""
            certificate_is_issued = False
            attempts = 0
            while not certificate_is_issued:
                response = r.get(f'{BASE_URL_V1}/staff/Employees/Certificates', headers=headers)
                data = response.json()
                for el in range(len(data)):
                    if (data[el]['RequestCertificateId'] == VARIABLES['Request_certificate_Id'] and
                            data[el]['CertificateStatus'] == 'Issued'):
                        certificate_is_issued = True
                attempts += 1
                time.sleep(30)
                if attempts == 20:
                    raise AssertionError('Certificate was not issued after 5 minutes')


        def put_created_employee(self, headers: dict, resident: bool) -> tuple:
            """Изменить данные только что созданного сотрудника
            :param bool resident: сотрудник - резидент / нерезидент
            """
            data = json.dumps(put_employee_body_generate(employee_info_data=VARIABLES["Created_Employee_Id_info"],
                                                         is_resident=resident))
            response = r.put(f'{BASE_URL_V1}/staff/Employees/{VARIABLES["Created_Employee_Id"]}', headers=headers,
                             data=data)
            return response.status_code, response.text, response.url

        def put_current_employee(self, headers: dict, resident: bool) -> tuple:
            """Изменить данные текущего сотрудника
            :param bool resident: сотрудник - резидент / нерезидент
            """
            data = json.dumps(put_employee_body_generate(employee_info_data=VARIABLES['Employee_Id_current_user_info'],
                                                         is_resident=resident))
            response = r.put(f'{BASE_URL_V1}/staff/Employees/{VARIABLES["Employee_Id_current_user"]}',
                             headers=headers,
                             data=data)
            return response.status_code, response.text, response.url

        def delete_employee(self, headers: dict) -> tuple:
            """Удалить сотрудника"""
            response = r.delete(f'{BASE_URL_V1}/staff/Employees/{VARIABLES["Created_Employee_Id"]}',
                                headers=headers)
            return response.status_code, response.text, response.url

    class JobTitle:
        """Должности в staff"""
        def get_job_title(self, headers: dict) -> tuple:
            """Получить информацию о должности сотрудника"""
            response = r.get(f'{BASE_URL_V1}/staff/JobTitle', headers=headers)
            return response.status_code, response.json(), response.url

    class Users:
        """Пользователи в staff"""
        def put_avatar_url(self, headers: dict) -> tuple:
            """Изменить аватарку в профиле"""
            data = payloads_data_generate(command='avatar')
            response = r.put(f'{BASE_URL_V1}/staff/Users/AvatarUrl', headers=headers, data=json.dumps(data))
            return response.status_code, response.text, response.url

        def delete_avatar(self, headers: dict) -> tuple:
            """Удалить аватрку из профиля"""
            response = r.delete(f'{BASE_URL_V1}/staff/Users/AvatarUrl', headers=headers)
            return response.status_code, response.text, response.url

    class Uueses:
        """УНЭП"""
        def post_request_certificate(self, headers: dict, issue_type: str) -> tuple:
            """Создать запрос на выпуск УНЭП
            :param str issue_type: способ выпуска УНЭП
            """
            payload = payloads_data_generate(command=issue_type)
            response = r.post(f'{BASE_URL_V1}/staff/Uueses/RequestCertificates', headers=headers,
                              params=payload)
            VARIABLES['Request_certificate_Id'] = response.text
            return response.status_code, response.text, response.url

        def get_request_certificate_type(self, headers: dict) -> tuple:
            """Получить способы выпуска УНЭП"""
            response = r.get(f'{BASE_URL_V1}/staff/Uueses/RequestCertificates/IdentificationType', headers=headers)
            return response.status_code, response.text, response.url

        def get_request_certificate_with_id(self, headers: dict) -> tuple:
            """Получить сертификат по Id"""
            response = r.get(f'{BASE_URL_V1}/staff/Uueses/RequestCertificates/'
                             f'{VARIABLES["Request_certificate_Id"]}', headers=headers)
            return response.status_code, response.json(), response.url

        def get_personal_info_with_certificate_id(self, headers: dict) -> tuple:
            """Получить перс. данные по Id сертификата"""
            response = r.get(f'{BASE_URL_V1}/staff/Uueses/RequestCertificates/'
                             f'{VARIABLES["Request_certificate_Id"]}/GetPersonalInfo', headers=headers)
            return response.status_code, response.json(), response.url

        def post_request_certificate_passport(self, headers: dict) -> tuple:
            """Добавить скан паспорта к заявлению на выпуск сертификата"""
            file = file_data_generate(file_name='test_1234.jpg', string_file_name='uploadedFile', type='image/jpeg')
            response = r.post(f'{BASE_URL_V1}/staff/Uueses/RequestCertificates/'
                              f'{VARIABLES["Request_certificate_Id"]}/Passports',
                              headers=headers,
                              files=file)
            return response.status_code, response.json(), response.url

        def delete_request_certificate_passport(self, headers: dict) -> tuple:
            """Удалить скан паспорта из заявления на выпуск сертификата"""
            response = r.delete(f'{BASE_URL_V1}/staff/Uueses/RequestCertificates/'
                                f'{VARIABLES["Request_certificate_Id"]}/Passports', headers=headers)
            return response.status_code, response.text, response.url

        def post_accept_personal_info(self, headers: dict) -> tuple:
            """Подтвердить данные на выпуск сертификата"""
            response = r.post(f'{BASE_URL_V1}/staff/Uueses/RequestCertificates'
                              f'/{VARIABLES["Request_certificate_Id"]}/AcceptPersonalInfo',
                              headers=headers)
            return response.status_code, response.text, response.url

        def post_signature_blank(self, headers: dict) -> tuple:
            """Подтвердить бланк запроса на выпуск сертификата"""
            response = r.post(f'{BASE_URL_V1}/staff/Uueses/RequestCertificates'
                               f'/{VARIABLES["Request_certificate_Id"]}/SignatureBlank',
                               headers=headers)
            return response.status_code, response.text, response.url

        def post_confirm_application(self, headers: dict) -> tuple:
            """Подтвердить выпуск сертификата через смс"""
            code = db.select_confirmation_code(VARIABLES["Employee_Id_current_user"])
            response = r.post(f'{BASE_URL_V1}/staff/Uueses/RequestCertificates'
                              f'/{VARIABLES["Request_certificate_Id"]}/ConfirmationViaSms/{code}',
                              headers=headers)
            return response.status_code, response.text, response.url

        def get_certificate_blank(self, headers: dict) -> tuple:
            """Получить бланк запроса по id сертификата"""
            response = r.get(f'{BASE_URL_V1}/staff/Uueses/RequestCertificates'
                             f'/{VARIABLES["Request_certificate_Id"]}/RequestCertificateBlanks',
                             headers=headers)
            return response.status_code, response.text, response.url

        def post_cancel_request_certificate(self, headers: dict) -> tuple:
            """Отменить выпуск сертификата"""
            response = r.post(f'{BASE_URL_V1}/staff/Uueses/RequestCertificates/'
                              f'{VARIABLES["Request_certificate_Id"]}/Cancellations', headers=headers)
            return response.status_code, response.text, response.url

