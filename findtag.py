#! python
import sys, os
# TODO 1. input_tag_and_directory( принимает тег для поиска, директорию, где искать, тег для поиска внутри файла)
def input_tag_and_directory():
    #arguments_for_search = sys.argv
    if len(sys.argv) < 2:
        print('Использование для Linux: python3 findtag.py [имя тега] [адрес директории поиска, '
              'по умолчанию ищет в текущей]'+'\n'+'Использование для Windows: py findtag.py [имя тега] '
              '[адрес директории поиска, '
              'по умолчанию ищет в текущей]')
        sys.exit()
    elif len(sys.argv) < 3:
        print('Для поиска будет использована текущая директория')
        return sys.argv[1]

    return sys.argv[1], sys.argv[2]

# TODO 2. search_files_tag()
# TODO 3. file_select
# TODO 4. open_in_file

if __name__ == "__main__":
    #input_tag_and_directory()
    search_files(input_tag_and_directory)
    file_select()
    open_in_file()
