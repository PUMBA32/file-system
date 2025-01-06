'''
class Writer - запись
class Reader - чтение
class Folders - работа с папками
class FileReader(Reader) - чтение файлов 
class FileWriter(Writer) - запись файлов
'''

from initialize import Initialize


def main() -> None:
    init: Initialize = Initialize()    
    init.start()


if __name__ == '__main__':
    main()