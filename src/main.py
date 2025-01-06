'''
class Look - просмотр директорий и файлов, родительский класс
class Writer - запись
class Reader - чтение
class Folders - работа с папками
class FileReader(Reader) - чтение файлов 
class FileWriter(Writer) - запись файлов
class Initialize - ищет в root.json путь до родительской директории, если его нет, то спрашивает у пользователя
и записывает его, если есть, то открывает интерфейс с него
'''

from initialize import Initialize


def main() -> None:
    init: Initialize = Initialize()    
    init.start()


if __name__ == '__main__':
    main()