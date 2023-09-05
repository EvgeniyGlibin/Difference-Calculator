<p><strong>Проект "Вычислитель отличий".</strong></p>

Вычислитель отличий - библиотека, которая сравнивает два файла конфигурации и выводит результат сравнения в одном из трёх форматов. Файлы конфигурации могут иметь формат json или yaml. Форматы результата сравнения: "stylish", "plain" или "json".

Для установки бибилиотеки необходимо ввести значение в командную строку: "команда"

Для получения информации по работе с библиотекой необходимо ввести команду <kbd>gendiff --help(-h)</kbd>

Для сравненя двух файлов конфигураций необходимо ввести команду <kbd>gendiff file_path1 file_path2</kbd>. где <kbd>file_path1</kbd> и <kbd>file_path2</kbd> - это пути к необходимым файлам. По умолчанию результат сравнения двух файлов будет иметь формат "stylish". Для изменения формата вывода необходимо указать опцию --format(-f) и выбрать требуемый формат.
Например: <kbd>gendiff --format plain file_path1 file_path2</kbd>.


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
