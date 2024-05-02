import json
import time
from typing import Union

import requests as r

from data.data import BASE_URL_V1, VARIABLES, employee_body_generate


class ApiSagaClient:
    """API сервиса Saga"""
    class EmployeeSaga:
        def get_all_sagas(self, headers: dict) -> Union[int, str, dict, tuple]:
            """Получить список саг"""
            response = r.get(f'{BASE_URL_V1}/sagas/EmployeeSaga', headers=headers)
            data = response.json()
            for el in range(len(data)):
                if data[el]['Snils']:
                    VARIABLES['Saga_User_Snils'] = data[el]['Snils']
                    return response.status_code, VARIABLES['Saga_User_Snils']

        def get_saga_with_snils(self, headers: dict) -> Union[int, str, dict, tuple]:
            """Получить сагу по СНИЛСу"""
            response = r.get(f'{BASE_URL_V1}/sagas/EmployeeSaga/LastBySnils/{VARIABLES["Saga_User_Snils"]}',
                             headers=headers)
            return response.status_code

        def post_employee_saga(self, headers: dict, resident: bool) -> Union[int, str, dict, tuple]:
            """Запустить сагу для создания сотрудника
            :param bool resident: сотрудник резидент или нерезидент
            """
            data = json.dumps(employee_body_generate(resident))
            response = r.post(f'{BASE_URL_V1}/sagas/EmployeeSaga', headers=headers, data=data)
            VARIABLES['Saga_Id'] = str(response.text)
            return response.status_code


        def get_employee_saga_with_saga_id(self, headers: dict) -> Union[int, str, dict, tuple]:
            """Получить сагу по Id саги"""
            for _ in range(3):
                response = r.get(f"{BASE_URL_V1}/sagas/EmployeeSaga/{VARIABLES['Saga_Id']}", headers=headers)
                data = response.json()
                if data['EmployeeId']:
                    VARIABLES['Created_Employee_Id'] = data['EmployeeId']
                    return response.status_code, VARIABLES['Created_Employee_Id']
                else:
                    time.sleep(5)
                    continue
