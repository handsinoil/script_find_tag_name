#!/usr/bin/env python3
import os
import sys


# TODO 1. input_tag_and_directory( принимает тег для поиска, директорию, где искать, тег для поиска внутри файла)
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
        return sys.argv[1]

    return sys.argv[1], sys.argv[2]


# TODO 2. search_files_tag(принимает тег для поиска и адрес директории, в которой нужно искать) на данный момент ищет
# только в указанной директории, без поддиректорий.
def search_files(directory_search_tag, directory_path):
    file_list = os.listdir(directory_path)
    result_file_list = []
    for file in file_list:
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path) and directory_search_tag in file:
            result_file_list.append(file)
    print('Найдены следующие файлы:')
    for i in range(len(result_file_list)):
        print(f'{i}. {result_file_list[i]}')
    return sorted(result_file_list)


# TODO 3. file_select
# TODO 4. open_in_file

def main() -> None:
    search_files(input_tag_and_directory)
    

if __name__ == "__main__":
    main()
