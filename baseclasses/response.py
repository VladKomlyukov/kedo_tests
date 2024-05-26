from typing import Any

import jsonschema
from assertpy import assert_that


class Response:
    def assert_status_code(self, status_code: int, response_data: dict | str, response_url: str, expected_code: int) \
            -> None:
        """
        Метод проверки статус кода
        :param status_code: полученный код ответа на запрос
        :param response_data: полученное тело ответа на запрос
        :param response_url: урл запроса
        :param expected_code: ожидаемый код ответа для проверки
        :return: None
        """
        assert_that(status_code).described_as(f'\nRequest: {response_url},'
                                              f'\nResponse: {response_data}\n').is_equal_to(expected_code)

    def assert_jsonschema(self, response_data: dict, schema: dict) -> None:
        """
        Метод проверки json-схемы
        :param response_data: полученное тело ответа на запрос
        :param schema: json-схема для проверки
        :return: None
        """
        try:
            jsonschema.validate(response_data, schema)
        except jsonschema.exceptions.ValidationError as e:
            assert False, f'The response is not matching to json-schema: {e}'
