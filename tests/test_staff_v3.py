import jsonschema
import pytest
from assertpy import assert_that

import api.api_staff_v3 as api_staff
import data.schema_v3 as schema
from data.data import headers_sender_v3


class ApiCpients:
    """класс с объектами api"""
    staff = api_staff.ApiStaffClient.Employees()


@pytest.mark.employees
class TestEmployees(ApiCpients):
    """Получение информации о текущем сотруднике"""
    def test_get_employee_personal_info(self):
        status_code, response_data = self.staff.get_employee_personal_info(headers=headers_sender_v3)
        assert_that(status_code).is_equal_to(200)
        try:
            jsonschema.validate(response_data, schema.employee_personal_info_schema_v3)
        except jsonschema.exceptions.ValidationError as e:
            assert False, f'The response is not matching to json-schema: {e}'

    def test_get_employees(self):
        status_code, response_data = self.staff.get_employees(headers=headers_sender_v3)
        assert_that(status_code).is_equal_to(200)
        try:
            jsonschema.validate(response_data, schema.employees_schema_v3)
        except jsonschema.exceptions.ValidationError as e:
            assert False, f'The response is not matching to json-schema: {e}'

    def test_post_employee(self):
        status_code = self.staff.post_employee(headers=headers_sender_v3, resident=True)
        assert_that(status_code).is_equal_to(200)

    def test_post_employee_not_resident(self):
        status_code = self.staff.post_employee(headers=headers_sender_v3, resident=False)
        assert_that(status_code).is_equal_to(200)

    def test_get_employee_by_id(self):
        status_code, response_data = self.staff.get_employee_by_id(headers=headers_sender_v3, resident=True)
        assert_that(status_code).is_equal_to(200)
        try:
            jsonschema.validate(response_data, schema.employee_by_id_schema_schema_v3)
        except jsonschema.exceptions.ValidationError as e:
            assert False, f'The response is not matching to json-schema: {e}'

    def test_get_employee_by_id_not_resident(self):
        status_code, response_data = self.staff.get_employee_by_id(headers=headers_sender_v3, resident=False)
        assert_that(status_code).is_equal_to(200)
        try:
            jsonschema.validate(response_data, schema.employee_by_id_schema_v3_not_resident)
        except jsonschema.exceptions.ValidationError as e:
            assert False, f'The response is not matching to json-schema: {e}'

    def test_put_employee_by_id(self):
        status_code, response_data = self.staff.get_employee_by_id(headers=headers_sender_v3, resident=True)
        assert_that(status_code).is_equal_to(200)

    def test_put_employee_by_id_not_resident(self):
        status_code, response_data = self.staff.get_employee_by_id(headers=headers_sender_v3, resident=False)
        assert_that(status_code).is_equal_to(200)

    def test_get_certificates(self):
        status_code, response_data = self.staff.get_employee_certificates(headers=headers_sender_v3)
        assert_that(status_code).is_equal_to(200)
        try:
            jsonschema.validate(response_data, schema.certificates_id_schema_schema_v3)
        except jsonschema.exceptions.ValidationError as e:
            assert False, f'The response is not matching to json-schema: {e}'