import json
from typing import Union

import requests as r

from data.data import BASE_URL_V3, put_employee_body_generate, employee_body_generate, VARIABLES


class ApiStaffClient:
    """API сервиса Staff"""

    class Employees:
        """Сотрудники"""

        def get_employee_personal_info(self, headers: dict) -> Union[int, str, tuple]:
            """Получение перс. данных"""
            response = r.get(f'{BASE_URL_V3}/staff/Employees/PersonalInfo', headers=headers)
            data = response.json()
            VARIABLES['Employee_Id_current_user'] = data['Id']
            return response.status_code, response.json()

        def get_employees(self, headers: dict) -> Union[int, str, tuple]:
            """Получть информацию о сотрудниках"""
            response = r.get(f'{BASE_URL_V3}/staff/Employees', headers=headers)
            return response.status_code, response.json()

        def post_employee(self, headers: dict, resident: bool) -> Union[int, str, tuple]:
            """Создание сотрудника
            :param bool resident: сотрудник - резидент / нерезидент
            """
            data = json.dumps(employee_body_generate(resident))
            response = r.post(f'{BASE_URL_V3}/staff/Employees', headers=headers, data=data)
            if resident:
                VARIABLES["Created_Employee_Id"] = response.text
            else:
                VARIABLES["Created_Employee_Id_not_resident"] = response.text
            return response.status_code

        def get_employee_by_id(self, headers: dict, resident: bool) -> Union[int, str, tuple]:
            """Получение информации о Сотруднике по Id
            :param bool resident: сотрудник - резидент / нерезидент
            """
            if resident:
                response = r.get(f'{BASE_URL_V3}/staff/Employees/{VARIABLES["Created_Employee_Id"]}',
                                 headers=headers)
                VARIABLES["Created_Employee_Id_info"] = response.json()
                return response.status_code, response.json()
            else:
                response = r.get(f'{BASE_URL_V3}/staff/Employees/{VARIABLES["Created_Employee_Id_not_resident"]}',
                                 headers=headers)
                VARIABLES["Created_Employee_Id_info_not_resident"] = response.json()
                return response.status_code, response.json()

        def get_employee_by_id_current_user(self, headers: dict) -> Union[int, str, dict]:
            """Получить информацию о текущем сотруднике по Id"""
            response = r.get(f'{BASE_URL_V3}/staff/Employees/{VARIABLES["Employee_Id_current_user"]}',
                             headers=headers)
            status_code = response.status_code
            data = response.json()
            VARIABLES['Subdivision_Id'] = data['EmployeeWorkplaces'][0]['Subdivision']['Id']
            VARIABLES['JobTitle_Id'] = data['EmployeeWorkplaces'][0]['JobTitle']['Id']
            VARIABLES["Employee_Id_current_user_info"] = data
            return status_code

        def put_employee_by_id(self, headers: dict, resident: bool) -> Union[int, str, tuple]:
            """Изменение информации о Сотруднике по Id
            :param bool resident: сотрудник - резидент / нерезидент
            """
            if resident:
                data = json.dumps(put_employee_body_generate(employee_info_data=VARIABLES["Created_Employee_Id_info"],
                                                             is_resident=resident))
                response = r.put(f'{BASE_URL_V3}/staff/Employees/{VARIABLES["Created_Employee_Id"]}',
                                 headers=headers, data=data)
                return response.status_code, response.text
            else:
                data = json.dumps(put_employee_body_generate(employee_info_data=
                                                             VARIABLES["Created_Employee_Id_info_not_resident"],
                                                             is_resident=resident))
                response = r.put(f'{BASE_URL_V3}/staff/Employees/{VARIABLES["Created_Employee_Id_not_resident"]}',
                                 headers=headers, data=data)
                return response.status_code, response.text

        def get_employee_certificates(self, headers: dict) -> Union[int, str, tuple]:
            """Получить сертификаты пользователя"""
            response = r.get(f'{BASE_URL_V3}/staff/Employees/Certificates', headers=headers)
            data = response.json()
            for el in range(len(data)):
                if data[el]['CertificateStatus'] == 'Issued':
                    VARIABLES['Certificate_Id'] = data[el]['ExternalId']
                    break
            else:
                print('Issued Certificate was not found')
            return response.status_code, response.json()
