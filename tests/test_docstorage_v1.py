import pytest
from assertpy import assert_that
from baseclasses.response import Response

import api.api_docstorage_v1 as api_docstorage
import api.api_staff_v1 as api_staff
from data.data import (VARIABLES, headers_sender, headers_recipient, headers_not_resident, headers_form_data_sender,
                       headers_coordinator, headers_second_coordinator)


class ApiClients:
    """класс с объектами api"""
    doc_types = api_docstorage.DocstorageClient.DocumentTypes()
    routes = api_docstorage.DocstorageClient.Routes()
    document = api_docstorage.DocstorageClient.Documents()
    employees = api_staff.ApiStaffClient.Employees()
    response = Response()


@pytest.mark.document
class TestCreateDocumentAndSend(ApiClients):
    """тест - создание, подписание и отправка документа"""
    def test_post_document(self):
        # подготовка тестовых данных: получение перс. данных и создание типа документа
        self.employees.get_employee_personal_info(headers=headers_sender)
        self.employees.get_employee_by_id_current_user(headers=headers_sender)
        self.doc_types.post_document_type(headers=headers_sender, method='post')
        # выполнение теста
        status_code, response_data, response_url = self.document.post_document(headers=headers_sender, is_tenant=False)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_document(self):
        status_code, response_data, response_url = self.document.get_document(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_attach_file_to_document(self):
        status_code, response_data, response_url = self.document.post_attach_file_to_document(
            headers=headers_form_data_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_route_stage(self):
        status_code, response_data, response_url = self.document.post_route_stage(headers=headers_sender, method='post')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document(self):
        self.employees.get_employee_certificates(headers=headers_sender)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_put_route_stage(self):
        status_code, response_data, response_url = self.document.put_route_stage(headers=headers_sender, method='put')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_post_sign_document_as_coordinator(self):
        self.employees.get_employee_certificates(headers=headers_sender)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_recipient(self):
        self.employees.get_employee_certificates(headers=headers_recipient)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_recipient)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

@pytest.mark.document
class TestCreateDocumentAndWithdraw(ApiClients):
    """тест - создание и отзыв документа"""
    def test_post_document(self):
        # подготовка тестовых данных: получение перс. данных и создание типа документа
        self.employees.get_employee_personal_info(headers=headers_sender)
        self.employees.get_employee_by_id_current_user(headers=headers_sender)
        self.doc_types.post_document_type(headers=headers_sender, method='post')
        # выполнение теста
        status_code, response_data, response_url = self.document.post_document(headers=headers_sender, is_tenant=False)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_attach_file_to_document(self):
        status_code, response_data, response_url = self.document.post_attach_file_to_document(
            headers=headers_form_data_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_route_stage(self):
        status_code, response_data, response_url = self.document.post_route_stage(headers=headers_sender, method='post')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document(self):
        self.employees.get_employee_certificates(headers=headers_sender)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_withdrawals_document(self):
        status_code, response_data, response_url = self.document.post_withdrawals_document(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)


@pytest.mark.document
class TestCreateDocumentAndReject(ApiClients):
    """тест - создание и отклонение документа"""
    def test_post_document(self):
        # подготовка тестовых данных: получение перс. данных и создание типа документа
        self.employees.get_employee_personal_info(headers=headers_sender)
        self.employees.get_employee_by_id_current_user(headers=headers_sender)
        self.doc_types.post_document_type(headers=headers_sender, method='post')
        # выполнение теста
        status_code, response_data, response_url = self.document.post_document(headers=headers_sender, is_tenant=False)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_attach_file_to_document(self):
        status_code, response_data, response_url = self.document.post_attach_file_to_document(
            headers=headers_form_data_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_route_stage(self):
        status_code, response_data, response_url = self.document.post_route_stage(headers=headers_sender, method='post')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_sender(self):
        self.employees.get_employee_certificates(headers=headers_sender)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_coordinator(self):
        self.employees.get_employee_certificates(headers=headers_not_resident)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_not_resident)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_rejections_document(self):
        status_code, response_data, response_url = self.document.post_rejections_document(headers=headers_recipient)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)


@pytest.mark.document
class TestCreateDocumentForTenant(ApiClients):
    """тест - создание, подписание и отправка документа на тенант"""
    def test_post_document(self):
        # подготовка тестовых данных: получение перс. данных и создание типа документа
        self.employees.get_employee_personal_info(headers=headers_sender)
        self.employees.get_employee_by_id_current_user(headers=headers_sender)
        self.doc_types.post_document_type(headers=headers_sender, method='post')
        # выполнение теста
        status_code, response_data, response_url = self.document.post_document(headers=headers_sender, is_tenant=True)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_attach_file_to_document(self):
        status_code, response_data, response_url = self.document.post_attach_file_to_document(
            headers=headers_form_data_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_route_stage(self):
        status_code, response_data, response_url = self.document.post_route_stage(headers=headers_sender,
                                                                        method='post_for_tenant')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document(self):
        self.employees.get_employee_certificates(headers=headers_sender)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_put_route_stage(self):
        status_code, response_data, response_url = self.document.put_route_stage(headers=headers_sender,
                                                                         method='put_for_tenant')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_post_sign_document_as_coordinator(self):
        self.employees.get_employee_certificates(headers=headers_not_resident)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_not_resident)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_recipient_tenant(self):
        self.employees.get_employee_certificates(headers=headers_sender)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

@pytest.mark.document
class TestCreateDocumentForTenantWithThreeCoordinators(ApiClients):
    """Создание, подписание и отправка документа на тенант с 3-мя этапами согласования"""
    def test_post_document(self):
        # подготовка тестовых данных: получение перс. данных и создание типа документа
        self.employees.get_employee_personal_info(headers=headers_sender)
        self.employees.get_employee_by_id_current_user(headers=headers_sender)
        self.doc_types.post_document_type(headers=headers_sender, method='post')
        # выполнение теста
        status_code, response_data, response_url = self.document.post_document(headers=headers_sender, is_tenant=True)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_attach_file_to_document(self):
        status_code, response_data, response_url = self.document.post_attach_file_to_document(
            headers=headers_form_data_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_route_stage(self):
        status_code, response_data, response_url = self.document.post_route_stage(headers=headers_sender,
                                                                 method='post_three_cordinators')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document(self):
        self.employees.get_employee_certificates(headers=headers_sender)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_coordinator(self):
        self.employees.get_employee_certificates(headers=headers_coordinator)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_coordinator)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_second_coordinator(self):
        self.employees.get_employee_certificates(headers=headers_second_coordinator)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_second_coordinator)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_put_route_stage(self):
        status_code, response_data, response_url = self.document.put_route_stage(headers=headers_sender,
                                                                  method='put_three_cordinators')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_post_sign_document_as_coordinator_again(self):
        self.employees.get_employee_certificates(headers=headers_coordinator)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_coordinator)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_recipient_tenant(self):
        self.employees.get_employee_certificates(headers=headers_sender)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)


@pytest.mark.document_types
class TestCreateDocumentType(ApiClients):
    """тест - CRUD для типов документов"""
    def test_post_document_type(self):
        status_code, response_data, response_url = self.doc_types.post_document_type(headers=headers_sender,
                                                                                   method='post')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_document_types(self):
        status_code, response_data, response_url = self.doc_types.get_document_types(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        if VARIABLES['Created_document_type_Id']:
            for el in range(len(response_data)):
                if response_data[el]['Id'] == (VARIABLES['Created_document_type_Id']):
                    break
            else:
                raise AssertionError('Created_document_type_Id not found in list of types')

    def test_put_document_type(self):
        status_code, response_data, response_url = self.doc_types.put_document_type(headers=headers_sender,
                                                                                    method='put')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')


    def test_delete_document_type(self):
        status_code, response_data, response_url = self.doc_types.delete_document_type(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)


@pytest.mark.routes
class TestCreateRoute(ApiClients):
    """тест CRUD для шаблонов маршрутов"""
    def test_post_route(self):
        # подготовка тестовых данных: получение перс. данных и создание типа документа
        self.employees.get_employee_personal_info(headers=headers_sender)
        self.employees.get_employee_by_id_current_user(headers=headers_sender)
        self.doc_types.post_document_type(headers=headers_sender, method='post')
        # выполнение теста
        status_code, response_data, response_url = self.routes.post_route(headers=headers_sender, method='post')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_all_routes(self):
        status_code, response_data, response_url = self.routes.get_routes(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        if VARIABLES['Created_route_Id']:
            for el in range(len(response_data)):
                if response_data[el]['Id'] == (VARIABLES['Created_route_Id']):
                    break
            else:
                raise AssertionError('Created_route_Id not found in list of routes')


    def test_get_route_by_id(self):
        status_code, response_data, response_url = self.routes.get_route_by_id(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_put_route_by_id(self):
        status_code, response_data, response_url = self.routes.put_route_by_id(headers=headers_sender, method='put')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_delete_route_by_id(self):
        self.doc_types.delete_document_type(headers_sender)
        status_code, response_data, response_url = self.routes.delete_route_by_id(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)