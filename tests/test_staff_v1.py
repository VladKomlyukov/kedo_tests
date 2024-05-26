import pytest
from assertpy import assert_that
from baseclasses.response import Response
import api.api_saga_v1 as api_saga
import api.api_staff_v1 as api_staff
from data.data import headers_sender, headers_recipient, headers_not_resident, headers_form_data_sender


class ApiClients:
    """класс с объектами api"""
    employees = api_staff.ApiStaffClient.Employees()
    employee_saga = api_saga.ApiSagaClient.EmployeeSaga()
    job_title = api_staff.ApiStaffClient.JobTitle()
    users = api_staff.ApiStaffClient.Users()
    uueses = api_staff.ApiStaffClient.Uueses()
    response = Response()


@pytest.mark.employees
class TestCreateEmployee(ApiClients):
    """тест - создание сотрудника"""
    def test_get_countries(self):
        status_code, response_data, response_url = self.employees.get_countries(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_country(self):
        status_code, response_data, response_url = self.employees.get_country(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_employee_personal_info(self):
        status_code, response_data, response_url = self.employees.get_employee_personal_info(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    @pytest.mark.parametrize('path', ['&WorkingOnly=true', '&WorkingOnly=false'])
    def test_get_employees(self, path):
        status_code, response_data, response_url = self.employees.get_employees(path, headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        if path == '&WorkingOnly=true':
            for el in range(len(response_data)):
                assert_that(response_data[el]['Status']).is_not_equal_to('NotWorks')
        elif path == '&WorkingOnly=false':
            for el in range(len(response_data)):
                assert_that(response_data[el]['Status']).is_in('Works', 'NotWorks', 'NoUUES', 'NotActivated')

    def test_get_employee_certificates(self):
        status_code, response_data, response_url = self.employees.get_employee_certificates(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_employee_by_id(self):
        status_code, response_data, response_url = self.employees.get_employee_by_id_current_user(
            headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_employee(self):
        status_code, response_data, response_url = self.employee_saga.post_employee_saga(headers=headers_sender,
                                                                                   resident=True)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_employee_saga(self):
        status_code, created_employee_id, response_data, response_url = (
            self.employee_saga.get_employee_saga_with_saga_id(
            headers=headers_sender))
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(created_employee_id).is_not_empty()

    def test_put_employee(self):
        self.employees.get_employee_by_id_created_user(headers=headers_sender)
        status_code, response_data, response_url = self.employees.put_created_employee(headers=headers_sender,
                                                                                   resident=True)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_delete_employee(self):
        status_code, response_data, response_url = self.employees.delete_employee(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_job_title(self):
        status_code, response_data, response_url = self.job_title.get_job_title(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_put_avatar_url(self):
        status_code, response_data, response_url = self.users.put_avatar_url(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_delete_avatar(self):
        status_code, response_data, response_url = self.users.delete_avatar(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)


@pytest.mark.employees
class TestCreateNotResidentEmployee(ApiClients):
    """тест - создание иностранного сотрудника"""
    def test_post_employee_not_resident(self):
        status_code, response_data, response_url = self.employee_saga.post_employee_saga(headers=headers_sender,
                                                                                  resident=False)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_employee_saga(self):
        status_code, created_employee_id, response_data, response_url = (
            self.employee_saga.get_employee_saga_with_saga_id(
            headers=headers_sender))
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(created_employee_id).is_not_empty()

    def test_delete_employee(self):
        status_code, response_data, response_url = self.employees.delete_employee(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)



@pytest.mark.cert
class TestCancelCertificateIssueLocal(ApiClients):
    """тест - отмена выпуска сертификата"""
    def test_post_request_certificate_local(self):
        # подготавливаем тестовые данные: меняем данные текущего пользователя для выпуска УНЭП
        self.employees.get_employee_personal_info(headers=headers_sender)
        self.employees.get_employee_by_id_current_user(headers=headers_sender)
        self.employees.put_current_employee(headers=headers_sender, resident=True)
        # создаем запрос на выпуск унэп
        status_code, response_data, response_url = self.uueses.post_request_certificate(headers=headers_sender,
                                                                              issue_type='Local')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_request_certificate_type(self):
        status_code, response_data, response_url = self.uueses.get_request_certificate_type(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_request_certificate_passport(self):
        status_code, response_data, response_url = self.uueses.post_request_certificate_passport(
            headers=headers_form_data_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data['DownloadedFiles']).is_equal_to(1)

    def test_delete_request_certificate_passport(self):
        status_code, response_data, response_url = self.uueses.delete_request_certificate_passport(
            headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_post_request_certificate_passport_after_delete(self):
        status_code, response_data, response_url = self.uueses.post_request_certificate_passport(
            headers=headers_form_data_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data['DownloadedFiles']).is_equal_to(1)

    def test_get_request_certificate_with_id_local(self):
        status_code, response_data, response_url = self.uueses.get_request_certificate_with_id(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data['IdentificationTypeValue']).is_equal_to('Local')

    def test_get_personal_info_with_certificate_id_local(self):
        status_code, response_data, response_url = self.uueses.get_personal_info_with_certificate_id(
            headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_cancel_request_certificate_local(self):
        status_code, response_data, response_url = self.uueses.post_cancel_request_certificate(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')


@pytest.mark.cert
class TestCertificateIssueLocal(ApiClients):
    """тест - выпуск сертификата лично"""
    def test_post_request_certificate_local(self):
        # подготавливаем тестовые данные: меняем данные текущего пользователя для выпуска УНЭП
        self.employees.get_employee_personal_info(headers=headers_sender)
        self.employees.get_employee_by_id_current_user(headers=headers_sender)
        self.employees.put_current_employee(headers=headers_sender, resident=True)
        # создаем запрос на выпуск унэп
        status_code, response_data, response_url = self.uueses.post_request_certificate(headers=headers_sender,
                                                                              issue_type='Local')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_request_certificate_with_id_local(self):
        status_code, response_data, response_url = self.uueses.get_request_certificate_with_id(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data['IdentificationTypeValue']).is_equal_to('Local')

    def test_post_request_certificate_passport(self):
        status_code, response_data, response_url = self.uueses.post_request_certificate_passport(
            headers=headers_form_data_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data['DownloadedFiles']).is_equal_to(1)

    def test_get_personal_info_with_certificate_id_local(self):
        status_code, response_data, response_url = self.uueses.get_personal_info_with_certificate_id(
        headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_accept_personal_info_local(self):
        status_code, response_data, response_url = self.uueses.post_accept_personal_info(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_post_signature_blank_local(self):
        status_code, response_data, response_url = self.uueses.post_signature_blank(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_get_certificate_blank_local(self):
        status_code, response_data, response_url = self.uueses.get_certificate_blank(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_confirm_application_local(self):
        status_code, response_data, response_url = self.uueses.post_confirm_application(headers=headers_sender)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_check_employee_certificate_status(self):
        self.employees.check_employee_certificate_status(headers=headers_sender)


@pytest.mark.cert
class TestCertificateIssueGosuslugi(ApiClients):
    """тест - выпуск сертификата госуслуги"""

    def test_post_request_certificate_gosuslugi(self):
        # подготавливаем тестовые данные: меняем данные текущего пользователя для выпуска УНЭП
        self.employees.get_employee_personal_info(headers=headers_recipient)
        self.employees.get_employee_by_id_current_user(headers=headers_recipient)
        self.employees.put_current_employee(headers=headers_recipient, resident=True)
        # создаем запрос на выпуск унэп
        status_code, response_data, response_url = self.uueses.post_request_certificate(headers=headers_recipient,
                                                                       issue_type='Gosuslugi')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_get_request_certificate_with_id_gosuslugi(self):
        status_code, response_data, response_url = self.uueses.get_request_certificate_with_id(
            headers=headers_recipient)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data['IdentificationTypeValue']).is_equal_to('Gosuslugi')


    def test_get_personal_info_with_certificate_id_gosuslugi(self):
        status_code, response_data, response_url = self.uueses.get_personal_info_with_certificate_id(
            headers=headers_recipient)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_accept_personal_info_gosuslugi(self):
        status_code, response_data, response_url = self.uueses.post_accept_personal_info(headers=headers_recipient)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_post_signature_blank_gosuslugi(self):
        status_code, response_data, response_url = self.uueses.post_signature_blank(headers=headers_recipient)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_post_confirm_application_gosuslugi(self):
        status_code, response_data, response_url = self.uueses.post_confirm_application(headers=headers_recipient)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_check_employee_certificate_status(self):
        self.employees.check_employee_certificate_status(headers=headers_recipient)


@pytest.mark.cert
class TestCertificateIssueGosuslugiNotResident(ApiClients):
    """тест - выпуск унэп для иностранного сотрудника"""
    def test_post_request_certificate_gosuslugi_not_resident(self):
        # подготавливаем тестовые данные: меняем данные текущего пользователя для выпуска УНЭП
        self.employees.get_employee_personal_info(headers=headers_not_resident)
        self.employees.get_employee_by_id_current_user(headers=headers_not_resident)
        self.employees.put_current_employee(headers=headers_not_resident, resident=False)
        # создаем запрос на выпуск унэп
        status_code, response_data, response_url = self.uueses.post_request_certificate(headers=headers_not_resident,
                                                                    issue_type='Gosuslugi')
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)

    def test_post_accept_personal_info_gosuslugi_not_resident(self):
        status_code, response_data, response_url = self.uueses.post_accept_personal_info(headers=headers_not_resident)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_post_signature_blank_gosuslugi_not_resident(self):
        status_code, response_data, response_url = self.uueses.post_signature_blank(headers=headers_not_resident)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_post_confirm_application_gosuslugi_not_resident(self):
        status_code, response_data, response_url = self.uueses.post_confirm_application(headers=headers_not_resident)
        self.response.assert_status_code(status_code, response_data, response_url, expected_code=200)
        assert_that(response_data).is_equal_to('True')

    def test_check_employee_certificate_status(self):
        self.employees.check_employee_certificate_status(headers=headers_not_resident)
