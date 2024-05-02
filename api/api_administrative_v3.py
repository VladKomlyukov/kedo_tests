import json
from typing import Union
import requests as r

from data.data import BASE_URL_V3, VARIABLES, employee_workplace_body_generate, payloads_data_generate


class ApiAdministrativeClient:
    """API сервиса Administrative"""

    class Workplaces:
        """Рабочие места"""

        def get_employee_workplaces(self, headers: dict) -> Union[int, str, dict, tuple]:
            """Получить все рабочие места сотрудника"""
            response = r.get(f'{BASE_URL_V3}/administrative/Employees/EmployeeWorkplaces', headers=headers)
            return response.status_code, response.json()

        def get_employee_workplace_by_id(self, headers: dict) -> Union[int, str, dict, tuple]:
            """Получить рабочее место сотрудника по Id"""
            response = r.get(f"{BASE_URL_V3}/administrative/Employees/{VARIABLES['Employee_Id_current_user']}"
                             f"/EmployeeWorkplaces", headers=headers)
            return response.status_code, response.json()

        def post_employee_workplace(self, headers: dict) -> Union[int, str]:
            """Создать рабочее место"""
            data = json.dumps(employee_workplace_body_generate())
            response = r.post(
                f"{BASE_URL_V3}/administrative/Employees/{VARIABLES['Employee_Id_current_user']}/EmployeeWorkplaces",
                headers=headers, data=data)
            VARIABLES['Created_EmployeeWorkplace_Id'] = response.text
            return response.status_code

        def post_employee_workplace_set_end_date_work(self, headers: dict) -> Union[int, str, tuple]:
            """Добавить дату окончания рабочего места"""
            payload = payloads_data_generate(command='set_end_data')
            response = r.post(f"{BASE_URL_V3}/administrative/Employees/EmployeeWorkplaces/"
                              f"{VARIABLES['Created_EmployeeWorkplace_Id']}/SetDateWorkEnded", headers=headers,
                              params=payload)
            return response.status_code, response.text

        def delete_employee_workplace(self, headers: dict) -> Union[int, str]:
            """Удалить рабочее место"""
            response = r.delete(f"{BASE_URL_V3}/administrative/Employees/EmployeeWorkplaces/"
                                f"{VARIABLES['Created_EmployeeWorkplace_Id']}", headers=headers)
            return response.status_code

    class JobTitles:
        """Должности"""
        def get_job_titles(self, headers: dict) -> Union[int, str, dict, tuple]:
            """Получить список должностей"""
            response = r.get(f"{BASE_URL_V3}/administrative/JobTitles", headers=headers)
            return response.status_code, response.json()

        def post_job_title(self, headers: dict) -> Union[int, str, tuple]:
            """Создать должность"""
            data = json.dumps(payloads_data_generate(command='job_title_name'))
            response = r.post(f"{BASE_URL_V3}/administrative/JobTitles", headers=headers, data=data)
            VARIABLES['Created_JobTitle_Id'] = response.text
            return response.status_code

        def put_job_title(self, headers: dict) -> Union[int, str, tuple]:
            """Изменить должность"""
            data = json.dumps(payloads_data_generate(command='put_job_title_name'))
            response = r.put(f"{BASE_URL_V3}/administrative/JobTitles/{VARIABLES['Created_JobTitle_Id']}",
                             headers=headers, data=data)
            return response.status_code

        def delete_job_title(self, headers: dict) -> Union[int, str, tuple]:
            """Удалить должность"""
            response = r.delete(f"{BASE_URL_V3}/administrative/JobTitles/{VARIABLES['Created_JobTitle_Id']}",
                                headers=headers)
            return response.status_code

    class Subdivisions:
        """Подразделения"""
        def get_subdivisions(self, headers: dict) -> Union[int, str, dict, tuple]:
            """Получить список подразделений"""
            response = r.get(f"{BASE_URL_V3}/administrative/Subdivisions", headers=headers)
            return response.status_code, response.json()

        def post_subdivision(self, headers: dict) -> Union[int, str]:
            """Создать подразделение"""
            data = json.dumps(payloads_data_generate(command='create_subdivision'))
            response = r.post(f"{BASE_URL_V3}/administrative/Subdivisions", headers=headers, data=data)
            VARIABLES['Created_Subdivision_Id'] = response.text
            return response.status_code

        def patch_subdivision(self, headers: dict) -> Union[int, str]:
            """Обновить информацию о подразделении"""
            data = json.dumps(payloads_data_generate(command='patch_subdivision'))
            response = r.patch(f"{BASE_URL_V3}/administrative/Subdivisions", headers=headers, data=data)
            return response.status_code


        def delete_subdivisions(self, headers: dict) -> Union[int, str]:
            """Удалить подразделение"""
            response = r.delete(f"{BASE_URL_V3}/administrative/Subdivisions/{VARIABLES['Created_Subdivision_Id']}",
                                headers=headers)
            return response.status_code

