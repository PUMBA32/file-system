import json
import os

from view import View
from typing import Dict


class Initialize(View): 
    def __init__(self) -> None:
        # измените путь на свой полный путь до root.json
        self.__JSON_ROOT_PATH: str = "D:\\Coding\\PYTHON\\big_projects\\file system\\root.json"
        self.root_path: str = self.__search_root()

        if self.root_path == None:
            self.root_path = self.__set_new_root()
            super().cls()
            print("[i] Path before root was updated!\n")


    def __search_root(self) -> str | None:
        if os.path.exists(self.__JSON_ROOT_PATH):  # Если путь до файла существует
            
            # чтение из данных из файла root.json
            with open(self.__JSON_ROOT_PATH, 'r+', encoding='utf-8') as file:
                data = json.load(file)
 
            return data['path']
        return None
        

    def __write_into_json(self, data: Dict[str, str]) -> None:
        # Пересоздание файла root и запись в него пути
        with open(self.__JSON_ROOT_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file)            


    def __set_new_root(self) -> str: 
        super().cls()  # Очистка консоли
        inp: str = input("Enter new root path: ").strip()  # Получение нового пути до root 
        self.__write_into_json({"path": inp})  # Запись нового пути в root.json
        return inp


    def start(self) -> None:
        print(self.root_path)
