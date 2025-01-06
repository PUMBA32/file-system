import json
import os

from view import View
from typing import Dict, List


class Initialize(View): 
    def __init__(self) -> None:
        # измените путь на свой полный путь до root.json
        self.__JSON_ROOT_PATH: str = "D:\\Coding\\PYTHON\\big_projects\\file system\\root.json"
        self.root_path: str = self.__search_root()

        if self.root_path == None:
            self.root_path = self.__set_new_root()
        
        self.current_path: str = self.root_path


    def __search_root(self) -> str | None:
        if os.path.exists(self.__JSON_ROOT_PATH):  # Если путь до файла существует
            
            # чтение данных из файла root.json
            with open(self.__JSON_ROOT_PATH, 'r+', encoding='utf-8') as file:
                data = json.load(file)
 
            return data['path']
        return None
        

    def __write_into_json(self, data: Dict[str, str]) -> None:
        # Пересоздание файла root.json и запись в него пути
        with open(self.__JSON_ROOT_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file)            


    def __set_new_root(self) -> str: 
        super().cls()  # Очистка консоли
        inp: str = input("There is still no path to root dir. Enter new root path: ").strip()  # Получение нового пути до корневой директории 
        self.__write_into_json({"path": inp})  # Запись нового пути в root.json
        super().cls()
        print("[i] Path before root was updated!\n")
        return inp
    

    def __get_back_dir_path(self) -> str:
        arr: List[str] = self.current_path.split("\\")
        arr.pop(len(arr)-2)
        return "\\".join(arr)


    def __select_file(self) -> None:
        print("Это файл")


    def __select_folder(self) -> None:
        print("Это папка")



    def start(self) -> None: 
        while 1:
            if not os.path.exists(self.current_path):  # Если путь до корневой директории не существует
                self.root_path = self.__set_new_root()
                
            file_list: List[str] = super().show_folder_content(self.current_path)
            
            inp: str = input(">>> ").strip()

            if inp == "cd ...": 
                self.current_path = self.__get_back_dir_path()
            else:
                try: 
                    ind: int = int(inp)
                except ValueError as ex:
                    super().cls()
                    print(f"[!] Error: {ex}")
                    print(f"[!] Enter number to select the file\n")
                else:
                    if 0 < ind <= len(file_list): 
                        new_path: str = os.path.join(self.current_path, file_list[ind-1])
                        print(new_path)
                        if not os.path.isdir(new_path):  # Если путь не является путем до директории 
                            self.__select_file()
                        else:  # Если путь является путем до директории
                            self.__select_folder()
                        input()