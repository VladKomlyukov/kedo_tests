import json
from typing import Union

import requests as r

from data.data import (BASE_URL_V1, VARIABLES, document_type_body_generate, route_body_generate, document_body_generate,
                       payloads_data_generate, document_route_body_generate, document_body_signature_generate,
                       file_data_generate)


class DocstorageClient:
    """API сервиса Docstorage"""

    class Documents:
        """Документы"""

        def post_document(self, headers: dict, is_tenant: bool) -> Union[int, str]:
            """Создать документ
            :param bool is_tenant: является ли тенантом
            """
            data = json.dumps(document_body_generate(is_tenant))
            response = r.post(f'{BASE_URL_V1}/docstorage/Documents', headers=headers, data=data)
            VARIABLES['Created_document_Id'] = response.text
            return response.status_code

        def get_document(self, headers: dict) -> Union[int, str, dict, tuple]:
            """Получить документ по Id"""
            response = r.get(f'{BASE_URL_V1}/docstorage/Documents/{VARIABLES["Created_document_Id"]}', headers=headers)
            return response.status_code

        def post_attach_file_to_document(self, headers: dict) -> Union[int, str]:
            """Закрепить файл к документу по Id"""
            file = file_data_generate(file_name='pdf_a_1.pdf', string_file_name='uploadedFile', type='application/pdf')
            payload = payloads_data_generate(command='source_attach_type_for_document')
            response = r.post(f'{BASE_URL_V1}/docstorage/Documents/{VARIABLES["Created_document_Id"]}/attached-files',
                              headers=headers, params=payload, files=file)
            VARIABLES['Created_attach_file_for_document'] = response.text
            return response.status_code

        def post_route_stage(self, headers: dict, method: str) -> Union[int, str]:
            """Задать маршрут для документа по Id
            :param str method: метод запроса для генерации тестовых данных
            """
            data = json.dumps(document_route_body_generate(method))
            response = r.post(f'{BASE_URL_V1}/docstorage/Documents/{VARIABLES["Created_document_Id"]}/route-stages',
                              headers=headers, data=data)
            return response.status_code


        def put_route_stage(self, headers: dict, method: str) -> Union[int, str]:
            """Изменить маршрут для документа по Id
            :param str method: метод запроса для генерации тестовых данных
            """
            data = json.dumps(document_route_body_generate(method))
            response = r.put(f'{BASE_URL_V1}/docstorage/Documents/{VARIABLES["Created_document_Id"]}/route-stages',
                             headers=headers, data=data)
            return response.status_code

        def post_sign_document(self, headers: dict) -> Union[int, str]:
            """Подписать документ"""
            data = json.dumps(document_body_signature_generate())
            response = r.post(f'{BASE_URL_V1}/docstorage/Documents/{VARIABLES["Created_document_Id"]}/signatures',
                              headers=headers, data=data)
            return response.status_code

        def post_withdrawals_document(self, headers: dict) -> Union[int, str]:
            """Отозвать документ"""
            data = json.dumps(payloads_data_generate(command='comment'))
            response = r.post(f'{BASE_URL_V1}/docstorage/Documents/{VARIABLES["Created_document_Id"]}/withdrawals',
                              headers=headers, data=data)
            return response.status_code

        def post_rejections_document(self, headers: dict) -> Union[int, str]:
            """Отклонить документ"""
            data = json.dumps(payloads_data_generate(command='comment'))
            response = r.post(f'{BASE_URL_V1}/docstorage/Documents/{VARIABLES["Created_document_Id"]}/rejections',
                              headers=headers, data=data)
            return response.status_code


    class Routes:
        """Шаблоны документов"""
        def get_routes(self, headers: dict) -> tuple:
            """Получить все шаблоны маршрутов"""
            response = r.get(f'{BASE_URL_V1}/docstorage/Routes/Routes', headers=headers)
            return response.status_code, response.json()

        def post_route(self, headers: dict,  method: str) -> Union[int, str]:
            """Cоздать шаблон маршрута док-та
            :param str method: метод запроса для генерации тестовых данных
            """
            data = json.dumps(route_body_generate(method))
            response = r.post(f'{BASE_URL_V1}/docstorage/Routes/Routes', headers=headers, data=data)
            VARIABLES['Created_route_Id'] = response.text
            return response.status_code

        def get_route_by_id(self, headers: dict) -> Union[int, str, dict, tuple]:
            """Получить шаблон маршрута док-та по id"""
            response = r.get(f'{BASE_URL_V1}/docstorage/Routes/Routes/{VARIABLES["Created_route_Id"]}', headers=headers)
            return response.status_code

        def put_route_by_id(self, headers: dict, method: str) -> tuple:
            """Изменить шаблон маршрута док-та по id
            :param str method: метод запроса для генерации тестовых данных
            """
            data = json.dumps(route_body_generate(method))
            response = r.put(f'{BASE_URL_V1}/docstorage/Routes/Routes/{VARIABLES["Created_route_Id"]}',
                             headers=headers, data=data)
            return response.status_code, response.text

        def delete_route_by_id(self, headers: dict) -> Union[int, str]:
            """Удалить шаблон маршрута док-та по id"""
            response = r.delete(f'{BASE_URL_V1}/docstorage/Routes/Routes/{VARIABLES["Created_route_Id"]}',
                                headers=headers)
            return response.status_code

    class DocumentTypes:
        """Типы документов"""
        def get_document_types(self, headers: dict) -> Union[int, str, dict, tuple]:
            """Получить все типы документов"""
            response = r.get(f'{BASE_URL_V1}/docstorage/DocumentTypes?Offset=0&Count=1000', headers=headers)
            return response.status_code, response.json()

        def post_document_type(self, headers: dict, method: str) -> Union[int, str]:
            """Создать тип документа
            :param str method: метод запроса для генерации тестовых данных
            """
            data = json.dumps(document_type_body_generate(method))
            response = r.post(f'{BASE_URL_V1}/docstorage/DocumentTypes', headers=headers, data=data)
            VARIABLES['Created_document_type_Id'] = response.text
            return response.status_code

        def put_document_type(self, headers: dict, method: str) -> tuple:
            """Изменить тип документа
            :param str method: метод запроса для генерации тестовых данных
            """
            data = json.dumps(document_type_body_generate(method))
            response = r.put(f'{BASE_URL_V1}/docstorage/DocumentTypes/{VARIABLES["Created_document_type_Id"]}',
                             headers=headers, data=data)
            return response.status_code, response.text

        def delete_document_type(self, headers: dict) -> Union[int, str]:
            """Удалить тип документа"""
            response = r.delete(f'{BASE_URL_V1}/docstorage/DocumentTypes/{VARIABLES["Created_document_type_Id"]}',
                                headers=headers)
            return response.status_code
