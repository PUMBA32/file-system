import os
import sys

from typing import List


class View: 
    @staticmethod
    def cls() -> None:
        os.system("cls" if sys.platform == 'win32' else 'clear')

    
    @staticmethod
    def show_folder_content(path: str) -> List[str]:
        files: List[str] = os.listdir(path)
        
        View.cls()
        print(f"Current path: {path}\n")
        for i, file in enumerate(files):
            print(f"[{i+1}] {file}")
        print("...\n")

        return files

    
    @staticmethod
    def print_file_menu(filename: str) -> None:
        View.cls()
        print(f'file: {filename}')
        print("[1] - delete file")
        print("[2] - read file")
        print("...") 

    
    @staticmethod
    def help() -> None: 
        View.cls()
        print("1. add file <filename> - creating new empty file with any extension")
        print("2. add folder <foldername> - creating new empty folder with any extension")
        print("3. exit - exit from program")
        print("...")
        input()

        