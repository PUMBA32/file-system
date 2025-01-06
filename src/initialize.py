import json


class Initialize: 
    def __init__(self) -> None:
        # add your own path to root.json
        self.__JSON_ROOT_PATH: str = "D:\\Coding\\PYTHON\\big_projects\\file system\\root.json"
    
    
    def start(self) -> None:
        pass


    def search_root(self) -> bool:
        with open(self.__JSON_ROOT_PATH, 'r+', encoding='utf-8') as file:
            data = json.load(file)
        
        if data['path'] == None: return False
        
        self.root: str = data['path']
        return True
            


    def set_new_root(self) -> str: 
        pass


    def get_root(self) -> str:
        return self.__ROOT_PATH