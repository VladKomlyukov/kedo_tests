import pytest
from assertpy import assert_that
from baseclasses.response import Response

import api.api_saga_v1 as api_saga
from data.data import headers_sender


class ApiClients:
    """класс с объектами api"""
    employee_saga = api_saga.ApiSagaClient.EmployeeSaga()
    response = Response()


@pytest.mark.employees
class TestGetSagaInfo(ApiClients):
    """тест - получение информации из саги"""
    def test_get_all_sagas(self):
        status_code, saga_user_snils, response_data, response_url = self.employee_saga.get_all_sagas(
            headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(saga_user_snils).is_not_empty()

    def test_get_saga_with_snils(self):
        status_code, response_data, response_url = self.employee_saga.get_saga_with_snils(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)