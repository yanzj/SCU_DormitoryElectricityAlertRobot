# 机器人入口
from wxpy import *

from src.main.core.controller import Controller


def main():


    app = Controller()
    app.init()
    app.run()
    pass


if __name__ == '__main__':
    main()
    pass