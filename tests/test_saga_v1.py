import pytest
from assertpy import assert_that

import api.api_saga_v1 as api_saga
from data.data import headers_sender


class ApiClients:
    """класс с объектами api"""
    employee_saga = api_saga.ApiSagaClient.EmployeeSaga()


@pytest.mark.employees
class TestGetSagaInfo(ApiClients):
    """тест - получение информации из саги"""
    def test_get_all_sagas(self):
        status_code, saga_user_snils = self.employee_saga.get_all_sagas(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)
        assert_that(saga_user_snils).is_not_empty()

    def test_get_saga_with_snils(self):
        status_code = self.employee_saga.get_saga_with_snils(headers=headers_sender)
        assert_that(status_code).is_equal_to(200)