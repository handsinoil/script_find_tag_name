#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from subprocess import call as start_file


# TODO 1. input_tag_and_directory( принимает тег для поиска, директорию, где искать)
def input_tag_and_directory():
    # arguments_for_search = sys.argv
    if len(sys.argv) < 2:
        print('Использование для Linux: python3 findtag.py [имя тега] [адрес директории поиска, '
              'по умолчанию ищет в текущей]' + '\n' +
              'Использование для Windows: py findtag.py [имя тега] '
              '[адрес директории поиска, по умолчанию ищет в текущей]')
        sys.exit()
    elif len(sys.argv) < 3:
        print('Для поиска будет использована текущая директория')
        return sys.argv[1], os.getcwd()

    return sys.argv[1], sys.argv[2]


# TODO 2. search_files_tag(принимает тег для поиска и адрес директории, в которой нужно искать)
def search_files(directory_search_tag, directory_path):
    file_list = os.listdir(directory_path)
    result_file_list = []
    files = {}

    for file in file_list:
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path) and directory_search_tag in file:
            result_file_list.append(file)
            files[file] = ['file', file_path]
        elif os.path.isdir(file_path):
            dir_list = os.listdir(file_path)
            for item in dir_list:
                file_list.append(os.path.join(file_path, item))

    if len(result_file_list) == 0:
        print('Соответствий не найдено.')
        return None, None
    else:
        print('Найдены следующие соответствия:')
        result_list = sorted(result_file_list)
        for i in range(len(result_list)):
            print(f'{i}. {result_list[i]}\n')
        return result_list, files


# TODO 3. file_select
def file_select(result_list, files):
    if len(result_list) > 0:
        file_number = int(input('Выберите номер файла для открытия: '))
        file = files[result_list[file_number]]
        return file

    print('Ничего не найдено.')
    return None, None


# TODO 4. open_in_file
def open_file(file, search_tag, directory_path) -> str:

    if 'linux' in sys.platform:
        arg_for_opened = "xdg-open " + directory_path+file
        start_file([arg_for_opened], shell=True)
        print("Открыт файл с тегом ", search_tag)
    else:
        arg_for_opened = directory_path + file
        os.system("start " + arg_for_opened)
        print("Открыт файл с тегом ", search_tag)

              


def main() -> None:
    directory_search_tag, directory_path = input_tag_and_directory()
    result_list, files = search_files(directory_search_tag, directory_path)
    file, search_tag = file_select(result_list, files)
    open_file(file, sys.argv[1], directory_path)


if __name__ == "__main__":
    main()
