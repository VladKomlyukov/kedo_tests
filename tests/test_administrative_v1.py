import pytest
from assertpy import assert_that

import api.api_administrative_v1 as api_admin
import api.api_staff_v1 as api_staff
from data.data import headers_sender


class ApiClients:
    """класс с объектами api"""
    workplaces = api_admin.ApiAdministrativeClient.Workplaces()
    job_titles = api_admin.ApiAdministrativeClient.JobTitles()
    subdivisions = api_admin.ApiAdministrativeClient.Subdivisions()
    rbacs = api_admin.ApiAdministrativeClient.Rbacs()
    employees = api_staff.ApiStaffClient.Employees()

@pytest.mark.workplaces
class TestCreateEmployeeWorkplace(ApiClients):
    """тест - создание рабочего места"""

    def test_get_employee_workplaces(self):
        status_code = self.workplaces.get_employee_workplaces(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_get_employee_workplace_by_id(self):
        # подготовка тестовых данных: получение перс. данных
        self.employees.get_employee_personal_info(headers=headers_sender)
        self.employees.get_employee_by_id_current_user(headers=headers_sender)
        # выполнение теста
        status_code = self.workplaces.get_employee_workplace_by_id(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_post_employee_workplace(self):
        status_code = self.workplaces.post_employee_workplace(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_post_employee_workplace_set_date_work(self):
        status_code, response_text = self.workplaces.post_employee_workplace_set_end_date_work(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)
        assert_that(response_text).is_equal_to('True')

    def test_delete_employee_workplace(self):
        status_code = self.workplaces.delete_employee_workplace(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

@pytest.mark.jobTitles
class TestCreateJobTitle(ApiClients):
    """тест - создание должности"""
    def test_get_job_titles(self):
        status_code = self.job_titles.get_job_titles(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_post_job_title(self):
        status_code = self.job_titles.post_job_title(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_put_job_title(self):
        status_code = self.job_titles.put_job_title(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_delete_job_title(self):
        status_code = self.job_titles.delete_job_title(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)


@pytest.mark.subdivisions
class TestCreateSubdivisions(ApiClients):
    """тест - создание подразделения"""
    def test_get_subdivisions(self):
        status_code = self.subdivisions.get_subdivisions(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_post_subdivision(self):
        # подготовка данных для теста: получение перс. данных
        self.employees.get_employee_personal_info(headers=headers_sender)
        status_code = self.subdivisions.post_subdivision(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_patch_subdivisions(self):
        status_code = self.subdivisions.patch_subdivision(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_get_subdivision_by_id(self):
        status_code = self.subdivisions.get_subdivision_by_id(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_delete_subdivision(self):
        status_code = self.subdivisions.delete_subdivisions(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)


@pytest.mark.rbacs
class TestCreateRbacs(ApiClients):
    """тест - добавление роли к должности в подразделении"""
    def test_get_rbacs(self):
        status_code = self.rbacs.get_rbacs(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_post_rbac(self):
        # подготовка тестовых данных: получение перс. данных, создание подразделения, создание должности
        self.employees.get_employee_personal_info(headers=headers_sender)
        self.subdivisions.post_subdivision(headers=headers_sender)
        self.job_titles.post_job_title(headers=headers_sender)
        # выполнение теста
        status_code = self.rbacs.post_rbac(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_get_rbac_for_subdivision_job_title(self):
        status_code = self.rbacs.get_rbac_for_subdivision_job_title(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_put_rbac(self):
        status_code = self.rbacs.put_rbac(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)

    def test_delete_rbac(self):
        self.rbacs.delete_rbac(headers=headers_sender)
        # удаляем данные, созданные для теста (подразделение и должность)
        self.subdivisions.delete_subdivisions(headers=headers_sender)
        self.job_titles.delete_job_title(headers=headers_sender)

