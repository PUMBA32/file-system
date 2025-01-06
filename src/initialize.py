import json
import os

from view import View
from typing import Dict, List, Optional


class File:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    
    def delete_file(self) -> None:
        os.remove(self.filepath)


    def show_file_content(self) -> None:
        with open(self.filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            print(f'{i+1} -  {line}', end="")
        input("\n\nEnter any key to go back: ")


class Initialize(View): 
    def __init__(self) -> None:
        # измените путь на свой полный путь до root.json
        self.__JSON_ROOT_PATH: str = "D:\\Coding\\PYTHON\\big_projects\\file system\\root.json"
        self.root_path: str = self.__search_root()

        if self.root_path == None:
            self.root_path = self.__set_new_root()
        
        self.current_path: str = self.root_path


    def __search_root(self) -> Optional[str]:
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


    def __select_file(self, filepath: str) -> None:
        super().print_file_menu(filepath)
        choice: str = input(">>> ").strip()

        file: File = File(filepath)

        match choice:
            case "1": file.delete_file()
            case "2": file.show_file_content()
            case _: ...

    
    def __create(self, arr_inp: List[str]) -> None: 
        super().cls()

        if len(arr_inp) > 2 and arr_inp[1] == 'folder': 
            folder_path: str = os.path.join(self.current_path, " ".join(arr_inp[2:]))
            os.mkdir(folder_path)
        if len(arr_inp) > 2 and arr_inp[1] == 'file':
            filepath: str = os.path.join(self.current_path, " ".join(arr_inp[2:]))
            try:
                _ =  open(filepath, 'w', encoding='utf-8')
            except Exception as ex:
                print(f"[!] Error: {ex}")

    
    def __delete(self, arr_inp: List[str]) -> None:
        if len(arr_inp) >= 2:
            path: str = os.path.join(self.current_path, " ".join(arr_inp[1:]))
            os.remove(path)


    def start(self) -> None: 
        while 1:
            if not os.path.exists(self.root_path):  # Если путь до корневой директории не существует
                self.root_path = self.__set_new_root()

            if not os.path.exists(self.current_path):
                self.current_path = self.root_path

            file_list: List[str] = super().show_folder_content(self.current_path)
            
            inp: str = input(">>> ").strip()

            arr_inp: List[str] = inp.split(" ")
            if len(arr_inp) > 0:
                match arr_inp[0]:
                    case "add": self.__create(arr_inp)
                    case "delete": self.__delete(arr_inp)
                    case "help": super().help()
                    case "exit": return  
                

            if inp == "...": 
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
                            self.__select_file(new_path)
                        else:  # Если путь является путем до директории
                            self.current_path = new_path
            
