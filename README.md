<p><strong>Проект "Вычислитель отличий".</strong></p>

Вычислитель отличий - библиотека, которая сравнивает два файла конфигурации и выводит результат сравнения в одном из трёх форматов.<br>
Файлы конфигурации могут иметь формат json или yaml.<br>
Форматы результата сравнения: <mark>"stylish", "plain" или "json"</mark>.<br>

Для установки бибилиотеки необходимо ввести значение в командную строку:<br>
<p><code>python3 -m pip install --user git+https://github.com/EvgeniyGlibin/python-project-50.git</code></p>

Для получения информации по работе с библиотекой необходимо ввести команду <code>gendiff --help(-h)</code>

Для сравненя двух файлов конфигураций необходимо ввести команду <code>gendiff file_path1 file_path2</code>,<br>
где <code>file_path1</code> и <code>file_path2</code> - это пути к необходимым файлам.<br>
По умолчанию результат сравнения двух файлов будет иметь формат "stylish". Для изменения формата вывода необходимо указать опцию <code>--format(-f)</code> и выбрать требуемый формат.<br>
Например: <code>gendiff --format plain file_path1 file_path2</code>.


### Hexlet tests and linter status:
[![Actions Status](https://github.com/EvgeniyGlibin/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/EvgeniyGlibin/python-project-50/actions)
###
[![Actions Status](https://github.com/EvgeniyGlibin/python-project-50/workflows/gendiff-check/badge.svg)](https://github.com/EvgeniyGlibin/python-project-50/actions)
###
[![Maintainability](https://api.codeclimate.com/v1/badges/ae288673048b7619f3a9/maintainability)](https://codeclimate.com/github/EvgeniyGlibin/python-project-50/maintainability)

###
[![Test Coverage](https://api.codeclimate.com/v1/badges/ae288673048b7619f3a9/test_coverage)](https://codeclimate.com/github/EvgeniyGlibin/python-project-50/test_coverage)

### Сравнение плоских файлов (JSON)
<a href="https://asciinema.org/a/598716" target="_blank"><img src="https://asciinema.org/a/598716.svg" /></a>

### Сравнение плоских файлов (YAML)
<a href="https://asciinema.org/a/598717" target="_blank"><img src="https://asciinema.org/a/598717.svg" /></a>

### Сравнение вложенных структур (JSON, YAML)
<a href="https://asciinema.org/a/599806" target="_blank"><img src="https://asciinema.org/a/599806.svg" /></a>

### Выбор формата Plain
<a href="https://asciinema.org/a/600821" target="_blank"><img src="https://asciinema.org/a/600821.svg" /></a>

### Выбор формата JSON
<a href="https://asciinema.org/a/600823" target="_blank"><img src="https://asciinema.org/a/600823.svg" /></a>
