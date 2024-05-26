import json
from typing import Union

import requests as r
from data.data import (BASE_URL_V3, VARIABLES, document_type_body_generate, document_body_generate,
                       document_body_member_generate, file_data_generate, payloads_data_generate,
                       document_route_body_generate, document_body_signature_generate)



class DocstorageClient:
    """API сервиса Docstorage"""

    class Documents:
        """Документы"""

        def get_employee_inbox_documents(self, headers: dict) -> tuple:
            """Получить список входящих док-ов для текущего пользователя"""
            response = r.get(f'{BASE_URL_V3}/docstorage/Documents/EmploeeInbox', headers=headers)
            return response.status_code, response.json(), response.url

        def get_tenant_inbox_documents(self, headers: dict) -> tuple:
            """Получить список входящих док-ов на тенант"""
            response = r.get(f'{BASE_URL_V3}/docstorage/Documents/inbox', headers=headers)
            return response.status_code, response.json(), response.url

        def get_tenant_inbox_agreement_required_documents(self, headers: dict) -> tuple:
            """Получить список док-ов на согласовании где получатель тенант"""
            response = r.get(f'{BASE_URL_V3}/docstorage/Documents/viewing', headers=headers)
            return response.status_code, response.json(), response.url

        def get_employee_sent_list(self, headers: dict) -> tuple:
            """Получить список исходящих док-ов текущего пользователя"""
            response = r.get(f'{BASE_URL_V3}/docstorage/Documents/EmployeeSent', headers=headers)
            return response.status_code, response.json(), response.url

        def post_document(self, headers: dict, is_tenant: bool) -> tuple:
            """Создать документ"""
            data = json.dumps(document_body_generate(is_tenant))
            response = r.post(f'{BASE_URL_V3}/docstorage/Documents', headers=headers, data=data)
            VARIABLES['Created_document_Id'] = response.text
            return response.status_code, response.text, response.url

        def get_document(self, headers: dict) -> tuple:
            """Получить документ по Id"""
            response = r.get(f'{BASE_URL_V3}/docstorage/Documents/{VARIABLES["Created_document_Id"]}',
                             headers=headers)
            return response.status_code, response.json(), response.url

        def put_document(self, headers: dict, command: str) -> tuple:
            """Обновить участника маршрута"""
            data = json.dumps(document_body_member_generate(command))
            response = r.put(f'{BASE_URL_V3}/docstorage/Documents', headers=headers, data=data)
            return response.status_code, response.text, response.url

        def post_attach_file_to_document(self, headers: dict) -> tuple:
            """Закрепить файл к документу по Id"""
            file = file_data_generate(file_name='pdf_a_1.pdf', string_file_name='uploadedFile', type='application/pdf')
            payload = payloads_data_generate(command='source_attach_type_for_document')
            response = r.post(f'{BASE_URL_V3}/docstorage/Documents/{VARIABLES["Created_document_Id"]}/attached-files',
                              headers=headers, params=payload, files=file)
            VARIABLES['Created_attach_file_for_document'] = response.text
            return response.status_code, response.text, response.url

        def post_route_stage(self, headers: dict, method: str) -> tuple:
            """Задать маршрут для документа по Id
            :param str method: метод запроса для генерации тестовых данных
            """
            data = json.dumps(document_route_body_generate(method))
            response = r.post(f'{BASE_URL_V3}/docstorage/Documents/{VARIABLES["Created_document_Id"]}/route-stages',
                              headers=headers, data=data)
            return response.status_code, response.text, response.url

        def put_route_stage(self, headers: dict, method: str) -> tuple:
            """Изменить маршрут для документа по Id
            :param str method: метод запроса для генерации тестовых данных
            """
            data = json.dumps(document_route_body_generate(method))
            response = r.put(f'{BASE_URL_V3}/docstorage/Documents/{VARIABLES["Created_document_Id"]}/route-stages',
                             headers=headers, data=data)
            return response.status_code, response.text, response.url

        def post_sign_document(self, headers: dict) -> tuple:
            """Подписать документ"""
            data = json.dumps(document_body_signature_generate())
            response = r.post(f'{BASE_URL_V3}/docstorage/Documents/{VARIABLES["Created_document_Id"]}/signatures',
                              headers=headers, data=data)
            return response.status_code, response.text, response.url

        def post_withdrawals_document(self, headers: dict) -> tuple:
            """Отозвать документ"""
            data = json.dumps(payloads_data_generate(command='comment'))
            response = r.post(f'{BASE_URL_V3}/docstorage/Documents/{VARIABLES["Created_document_Id"]}/withdrawals',
                              headers=headers, data=data)
            return response.status_code, response.text, response.url

        def post_rejections_document(self, headers: dict) -> tuple:
            """Отклонить документ"""
            data = json.dumps(payloads_data_generate(command='comment'))
            response = r.post(f'{BASE_URL_V3}/docstorage/Documents/{VARIABLES["Created_document_Id"]}/rejections',
                              headers=headers, data=data)
            return response.status_code, response.text, response.url


    class DocumentTypes:
        """Типы документов"""

        def get_document_types(self, headers: dict) -> tuple:
            """Получить список типов документов"""
            response = r.get(f'{BASE_URL_V3}/docstorage/DocumentTypes?Offset=0&Count=1000', headers=headers)
            return response.status_code, response.json(), response.url

        def post_document_type(self, headers: dict, method: str) -> tuple:
            """Создать тип документа
            :param str method: метод запроса для генерации тестовых данных
            """
            data = json.dumps(document_type_body_generate(method))
            response = r.post(f'{BASE_URL_V3}/docstorage/DocumentTypes', headers=headers, data=data)
            VARIABLES['Created_document_type_Id'] = response.text
            return response.status_code, response.text, response.url

        def put_document_type(self, headers: dict, method: str) -> tuple:
            """Изменить тип документа
            :param str method: метод запроса для генерации тестовых данных
            """
            data = json.dumps(document_type_body_generate(method))
            response = r.put(f'{BASE_URL_V3}/docstorage/DocumentTypes/{VARIABLES["Created_document_type_Id"]}',
                             headers=headers, data=data)
            return response.status_code, response.text, response.url

        def delete_document_type(self, headers: dict) -> tuple:
            """Удалить тип документа"""
            response = r.delete(f'{BASE_URL_V3}/docstorage/DocumentTypes/{VARIABLES["Created_document_type_Id"]}',
                                headers=headers)
            return response.status_code, response.text, response.url

