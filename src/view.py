import os
import sys


class View: 
    @staticmethod
    def cls() -> None:
        os.system("cls" if sys.platform == 'win32' else 'clear')
        