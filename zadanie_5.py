import os
import logging
from collections import namedtuple
import sys


logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def gather_directory_info(path):
    """Собирает информацию о содержимом указанной директории."""
    
    if not os.path.isdir(path):
        logging.error(f"Указанный путь не является директорией: {path}")
        print(f"Указанный путь не является директорией: {path}")
        return []

    info_list = []

    for entry in os.scandir(path):
        if entry.is_file():
            name, extension = os.path.splitext(entry.name)
            is_directory = False
        else:
            name = entry.name
            extension = ''
            is_directory = True

        parent_directory = os.path.basename(os.path.dirname(entry.path))
        file_info = FileInfo(name=name, extension=extension, is_directory=is_directory, parent_directory=parent_directory)
        info_list.append(file_info)

        
        logging.info(f"Собранная информация: {file_info}")

    return info_list

def main():
    if len(sys.argv) != 2:
        print("Использование: python zadanie_5.py [путь_до_директории]")
        sys.exit(1)

    directory_path = sys.argv[1]
    info = gather_directory_info(directory_path)

    if info:
        print("Собранная информация:")
        for item in info:
            print(item)

if __name__ == "__main__":
    main()