# MANUAL

# Дерево проекта
```
|--api                # директория с методами к api проекта
|  |--api_administrative_v1.py
|  |--api_administrative_v3.py
|  |--api_docstorage_v1.py
|  |--api_docstorage_v3.py
|  |--api_saga_v1.py
|  |--api_staff_v1.py
|  |--api_staff_v3.py
|--baseclasses
|--|--response.py     # файл с методами для работы с response
|--data
|  |--data.py         # файл с функциями для генерации данных и переменными
|  |--db.py           # файл подключения к БД
|  |--schema_v3.py    # файл со json-схемой на v3
|--data_config
|  |--.env.example    # пример env-файла с переменным окружением (токен и ссылка на проект)
|  |--config.py       # конфиг для обработки информации из переменных окружений env-файла
|--test_data          # директория с файлами для тестов
|  |--pdf_a_1.pdf
|  |--test_1234.jpg
|--tests              # тесты
|  |--test_administrative_v1.py
|  |--test_administrative_v3.py
|  |--test_docstorage_v1.py
|  |--test_docstorage_v3.py
|  |--test_saga_v1.py
|  |--test_staff_v1.py
|  |--test_staff_v3.py
|--conftest.py        # фикстуры
|--pytest.ini         # файл для инициализации тестов pytest
|--requirements.txt   # зависимости
```

**ВАЖНО!** Перед запуском тестов обязательно устанавливаем виртуальное окружение и зависимости:

**Установка виртуального окружения:**
```shell
python -m venv venv
```
**Активация виртуального окружения:**

 Активация виртуального окружения в bash:
```bash
source venv/bin/activate
```

На Windows в командной строке терминала cmd нужно выполнить:
```commandline
venv\Scripts\activate.bat
```
На Windows в командной строке терминала Power Shell:
```shell
venv\Scripts\activate.ps1
```
Устанавливаем зависимости:
```bash
pip install -r requirements.txt
```

# Переменные

Файл **.env.example** содержит переменные для запуска тестов. После скачивания репозитория на 
локальную машину, необходимо создать копию файла с названием **.env** и заполнить переменные своими значениями.

В переменные с названием **TOKEN** вставляем токены пользователей с типом **"Development"**, в переменную 
**BASE_URL_STAGE** 
вставляем ссылку на api 
STAGE-стенда, в переменные employee_workplace_Id_... вставляем соответствующие id рабочих мест. 
Перед запуском тестов необходимо заполнить все переменные в файле **.env** и пробросить порт к БД Stage-стенда.

# Запуск тестов
Все тесты находятся в директории tests. Для запуска тестов необходимо использовать команды pytest:
- если мы не передали никакого аргумента в команду, а написали просто pytest, тест-раннер начнёт поиск в текущей директории
- как аргумент можно передать файл, путь к директории или любую комбинацию директорий и файлов, например: 

```bash
pytest tests
// найти все тесты в директории tests

pytest test_staff_v1.py
// найти и выполнить все тесты в файле

pytest tests/test_staff_v1.py::TestCreateEmployee::test_get_countries
// найти тест с именем test_get_countries класса TestCreateEmployee в указанном файле в указанной директории и выполнить

```
- дальше происходит рекурсивный поиск: то есть PyTest обойдет все вложенные директории, во всех директориях PyTest ищет файлы, которые удовлетворяют правилу  test_*.py или *_test.py (то есть начинаются на test_ или заканчиваются _test и имеют расширение .py)
- внутри всех этих файлов находит тестовые функции по следующему правилу:
- все тесты, название которых начинается с test, которые находятся вне классов
- все тесты, название которых начинается с test внутри классов, имя которых начинается с Test (и без метода __init__ внутри класса)

Если запустить PyTest с параметром **-v (verbose**, то есть подробный), то в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения: 
```bash
pytest -v tests\test_staff_v1.py
```
Если добавить параметр **-s** , то можно увидеть текст, который выводится командой **print()** :
```bash
pytest -s tests\test_staff_v1.py
```
Также, тесты имеют специальные маркеры, которые указаны в файле pytest.ini. Например, мы можем запустить тесты, которые проверяют только запросы к Employees:
```bash
pytest -m employees tests\test_staff_v1.py
```
Все эти параметры можно использовать вместе:
```bash
pytest -s -v -m employees tests\test_staff_v1.py
```
### Инверсия
Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию. Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:
```bash
pytest -s -v -m "not employees" tests\test_staff_v1.py
```
### Объединение тестов с разными маркировками
Для запуска тестов с разными метками можно использовать логическое ИЛИ. Запустим employees и workplaces-тесты:
```bash
pytest -s -v -m "employees or workplaces" tests\test_staff_v1.py
```
Можно использовать две маркировки для одного набора тестов в ситуации, когда, например, нам нужно запустить определенный набор среди всех тестов помеченных как employees:
```bash
@pytest.mark.employess
@pytest.mark.last
```
Чтобы запустить набор с маркером 'last' среди тестов employees - необходимо запустить команду c логическим И:
```bash
pytest -s -v -m "employess and last" tests\test_staff_v1.py
```
Тесты "employees" запустятся только для last

### XFail-тесты
Если в результате прогона какой-то из тестов падает, но нам нужно завершить прогон и убедиться, что остальные тесты прошли, мы можем пометить упавший тест как ожидаемо-падающий. 

Для этого необходимо добавить маркировку ```@pytest.mark.xfail``` для падающего теста. 

Упавший тест будет отмечен как **xfail**, но результат прогона тестов помечен как успешный.
Когда баг починят, мы это узнаем, ﻿﻿так как теперь тест будет отмечен как XPASS (“unexpectedly passing” — неожиданно проходит). После этого маркировку xfail для теста можно удалить.

К маркировке xfail можно добавлять параметр reason. 
```python
@pytest.mark.xfail(reason="fixing this bug right now")
```
Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rx.

Команда для запуска тестов:
```bash
pytest -rx -v test_staff_v1.py
```
# Conftest.py — конфигурация тестов
Используется для хранения часто употребимых фикстур и хранения глобальных настроек. conftest.py должен лежать в директории верхнего уровня в проекте с тестами. Нельзя хранить несколько conftest.py файлов во вложенных директориях.

### Параметризация тестов
PyTest позволяет запустить один и тот же тест с разными входными параметрами. Для этого используется декоратор ```@pytest.mark.parametrize()```
```python
        # метод, где мы указываем параметр path (передаем его в сам метод get_employees и добавляем его в ссылку)
        def get_employees(self, path):
            try:
                response = r.get(f'{BASE_URL}/staff/Employees{path}', headers=headers)
                status_code = response.status_code
                data = response.json()
                assert status_code == 200, (f'Test failed. Status code is {status_code}\n'
                                            f'response: {response.text}')
            except HTTPError as e:
                print('Error: ', e)
        # тест, где мы указываем наш параметр path, который должен изменяться, и список значений параметра
        @pytest.mark.parametrize('path', ['?WorkingOnly=true', '?WorkingOnly=false', '?Offset=0&Count=2000'])
        # и передаем path из декоратора в функцию test_get_employees в качестве аргумента, и далее в метод get_employees
        def test_get_employees(self, path):
          self.employees.get_employees(path)
```
Можно задавать параметризацию также для всего тестового класса, чтобы все тесты в классе запустились с заданными параметрами. В таком случае отметка о параметризации должна быть перед объявлением класса.

### Conftest.py и передача параметров в командной строке

В файл Conftest.py можно создавать фикстуры с собственными параметрами, которые мы можем передавать в командной строке при запуске тестов:

Это делается с помощью встроенной функции pytest_addoption и фикстуры request. Сначала необходимо добавить в файле conftest обработчик опции в функции pytest_addoption, затем написать фикстуру.
```python
# обработчик
def pytest_addoption(parser):
    parser.addoption('--request_type', action='store', default=None,
                     help="Choose type of request: post or get")
# фикстура
@pytest.fixture
def test_get_employees(request):
    option_name = request.config.getoption("request_type")
    if option_name == 'get':
      response = r.get(f'{BASE_URL}/staff/Employees?Offset=0&Count=2000', headers=headers)
    elif option_name == 'post':
      response = r.post(f'{BASE_URL}/staff/Employees?Offset=0&Count=2000', headers=headers)
    else:
      raise pytest.UsageError("--request_type should be get or post")
```
Если запустить тесты без параметра, то получим ошибку:
```bash
pytest -s -v test_get_employees.py

_pytest.config.UsageError: --request_type should be get or post
```
Можно задать значение параметра по умолчанию, чтобы в командной строке не обязательно было указывать параметр **--request_type**, например, так:

```python
parser.addoption('--request_type', action='store', default="get",
                 help="Choose type of request: post or get")
```

Запуск теста с параметром:
```bash
pytest -s -v --request_type=post test_get_employees.py
```

### Перезапуск тестов
Для проверки, что тест действительно упал, можно использовать плагин  ```pytest-rerunfailures```. Установка 
плагина: ```pip install pytest-rerunfailures```.

Чтобы указать количество перезапусков для каждого из упавших тестов, нужно добавить в командную строку параметр: ```--reruns n```, где n — это количество перезапусков. Если при повторных запусках тесты пройдут успешно, то и прогон тестов будет считаться успешным.

Количество перезапусков отображается в отчёте, благодаря чему можно позже анализировать проблемные тесты.﻿﻿ Дополнительно указываем параметр "--tb=line", чтобы результаты тестов выводились в мини-табличке.
```bash
pytest -v --tb=line --reruns 1 test_get_employees.py
```
Результаты теста будет выглядеть: "1 failed, 1 passed, 1 rerun in 9.20s﻿"
