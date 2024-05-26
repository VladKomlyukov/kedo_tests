import pytest
import jsonschema
from assertpy import assert_that
from baseclasses.response import Response
import data.schema_v3 as schema
import api.api_docstorage_v3 as api_docstorage
import api.api_staff_v3 as api_staff
from data.data import (VARIABLES, headers_sender_v3, headers_form_data_sender_v3, headers_recipient_v3,
                       headers_coordinator_v3, headers_second_coordinator_v3, headers_not_resident_v3)


class ApiClients:
    """класс с объектами api"""
    document = api_docstorage.DocstorageClient.Documents()
    employees = api_staff.ApiStaffClient.Employees()
    doc_types = api_docstorage.DocstorageClient.DocumentTypes()
    response = Response()


@pytest.mark.document
class TestGetListDocuments(ApiClients):
    """Получение списка входящих/исходящих документов"""

    def test_get_employee_documents(self):
        status_code, response_data, response_url = self.document.get_employee_inbox_documents(headers=headers_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        for el in range(len(response_data)):
            assert_that(response_data[el]["Recipients"]).is_none()
        self.response.assert_jsonschema(response_data, schema.docstorage_employee_inbox_schema_v3)

    def test_get_tenant_documents(self):
        status_code, response_data, response_url = self.document.get_tenant_inbox_documents(headers=headers_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        for el in range(len(response_data)):
            assert_that(response_data[el]["Recipients"][0]["RecipientTenant"]).is_true()
        self.response.assert_jsonschema(response_data, schema.docstorage_tenant_inbox_schema_v3)

    def test_get_tenant_inbox_agreement_required_documents(self):
        status_code, response_data, response_url = self.document.get_tenant_inbox_agreement_required_documents(
            headers=headers_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        for el in range(len(response_data)):
            assert_that(response_data[el]["Status"]).described_as(response_data).is_equal_to("AgreementRequired")
        self.response.assert_jsonschema(response_data, schema.tenant_inbox_agreement_required_schema_v3)

    def test_get_employee_sent_list(self):
        self.employees.get_employee_personal_info(headers=headers_sender_v3)
        status_code, response_data, response_url = self.document.get_employee_sent_list(headers=headers_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        for el in range(len(response_data)):
            assert_that(response_data[el]["Sender"]["Employee"]["Id"]).is_equal_to(
                VARIABLES['Employee_Id_current_user'])
        self.response.assert_jsonschema(response_data, schema.employee_sent_list)

@pytest.mark.document
class TestCreateDocumentAndSend(ApiClients):
    """тест - создание, подписание и отправка документа"""
    def test_post_document(self):
        # подготовка тестовых данных: получение перс. данных и создание типа документа
        self.employees.get_employee_personal_info(headers=headers_sender_v3)
        self.employees.get_employee_by_id_current_user(headers=headers_sender_v3)
        self.doc_types.post_document_type(headers=headers_sender_v3, method='post')
        # выполнение теста
        status_code, response_data, response_url = self.document.post_document(headers=headers_sender_v3,
                                                                              is_tenant=False)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_document(self):
        status_code, response_data, response_url = self.document.get_document(headers=headers_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_attach_file_to_document(self):
        status_code, response_data, response_url = self.document.post_attach_file_to_document(
            headers=headers_form_data_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_route_stage(self):
        status_code, response_data, response_url = self.document.post_route_stage(headers=headers_sender_v3,
                                                                             method='post_v3')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document(self):
        self.employees.get_employee_certificates(headers=headers_sender_v3)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_put_route_stage(self):
        status_code, response_data, response_url = self.document.put_route_stage(headers=headers_sender_v3,
                                                                              method='put_v3')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_coordinator(self):
        self.employees.get_employee_certificates(headers=headers_coordinator_v3)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_coordinator_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_second_coordinator(self):
        self.employees.get_employee_certificates(headers=headers_second_coordinator_v3)
        status_code, response_data, response_url = self.document.post_sign_document(
            headers=headers_second_coordinator_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_recipient(self):
        self.employees.get_employee_certificates(headers=headers_recipient_v3)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_recipient_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)


@pytest.mark.document
class TestCreateDocumentAndWithdraw(ApiClients):
    """тест - создание и отзыв документа"""
    def test_post_document(self):
        # подготовка тестовых данных: получение перс. данных и создание типа документа
        self.employees.get_employee_personal_info(headers=headers_sender_v3)
        self.employees.get_employee_by_id_current_user(headers=headers_sender_v3)
        self.doc_types.post_document_type(headers=headers_sender_v3, method='post')
        # выполнение теста
        status_code, response_data, response_url = self.document.post_document(headers=headers_sender_v3,
                                                                              is_tenant=False)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_attach_file_to_document(self):
        status_code, response_data, response_url = self.document.post_attach_file_to_document(
            headers=headers_form_data_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_route_stage(self):
        status_code, response_data, response_url = self.document.post_route_stage(headers=headers_sender_v3,
                                                                             method='post_v3')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document(self):
        self.employees.get_employee_certificates(headers=headers_sender_v3)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_withdrawals_document(self):
        status_code, response_data, response_url = self.document.post_withdrawals_document(headers=headers_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

@pytest.mark.document
class TestCreateDocumentAndReject(ApiClients):
    """тест - создание и отклонение документа"""
    def test_post_document(self):
        # подготовка тестовых данных: получение перс. данных и создание типа документа
        self.employees.get_employee_personal_info(headers=headers_sender_v3)
        self.employees.get_employee_by_id_current_user(headers=headers_sender_v3)
        self.doc_types.post_document_type(headers=headers_sender_v3, method='post')
        # выполнение теста
        status_code, response_data, response_url = self.document.post_document(headers=headers_sender_v3,
                                                                              is_tenant=False)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_attach_file_to_document(self):
        status_code, response_data, response_url = self.document.post_attach_file_to_document(
            headers=headers_form_data_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_route_stage(self):
        status_code, response_data, response_url = self.document.post_route_stage(headers=headers_sender_v3,
                                                                             method='post_v3')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_sender(self):
        self.employees.get_employee_certificates(headers=headers_sender_v3)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_coordinator(self):
        self.employees.get_employee_certificates(headers=headers_not_resident_v3)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_not_resident_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_rejections_document(self):
        status_code, response_data, response_url = self.document.post_rejections_document(headers=headers_recipient_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

@pytest.mark.document
class TestCreateDocumentForTenant(ApiClients):
    """тест - создание, подписание и отправка документа на тенант"""
    def test_post_document(self):
        # подготовка тестовых данных: получение перс. данных и создание типа документа
        self.employees.get_employee_personal_info(headers=headers_sender_v3)
        self.employees.get_employee_by_id_current_user(headers=headers_sender_v3)
        self.doc_types.post_document_type(headers=headers_sender_v3, method='post')
        # выполнение теста
        status_code, response_data, response_url = self.document.post_document(headers=headers_sender_v3,
                                                                               is_tenant=True)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_attach_file_to_document(self):
        status_code, response_data, response_url = self.document.post_attach_file_to_document(
            headers=headers_form_data_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_route_stage(self):
        status_code, response_data, response_url = self.document.post_route_stage(headers=headers_sender_v3,
                                                                     method='post_for_tenant')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document(self):
        self.employees.get_employee_certificates(headers=headers_sender_v3)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_put_route_stage(self):
        status_code, response_data, response_url = self.document.put_route_stage(headers=headers_sender_v3,
                                                                      method='put_for_tenant')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_coordinator(self):
        self.employees.get_employee_certificates(headers=headers_not_resident_v3)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_not_resident_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_sign_document_as_recipient_tenant(self):
        self.employees.get_employee_certificates(headers=headers_sender_v3)
        status_code, response_data, response_url = self.document.post_sign_document(headers=headers_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)


@pytest.mark.document_types
class TestCreateDocumentType(ApiClients):
    """тест - CRUD для типов документов"""

    def test_post_document_type(self):
        status_code, response_data, response_url = self.doc_types.post_document_type(headers=headers_sender_v3,
                                                                                method='post')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_document_type(self):
        status_code, response_data, response_url = self.doc_types.get_document_types(headers=headers_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        if VARIABLES['Created_document_type_Id']:
            for el in range(len(response_data)):
                if response_data[el]['Id'] == (VARIABLES['Created_document_type_Id']):
                    break
            else:
                raise AssertionError('Created_document_type_Id not found in list of types')
        self.response.assert_jsonschema(response_data, schema.document_type_schema_v3)

    def test_put_document_type(self):
        status_code, response_data, response_url = self.doc_types.put_document_type(headers=headers_sender_v3,
                                                                                 method='put')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_delete_document_type(self):
        status_code, response_data, response_url = self.doc_types.delete_document_type(headers=headers_sender_v3)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
