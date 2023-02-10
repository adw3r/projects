from time import sleep
from multiprocessing import Process

from module.config import SCRIPTS_FOLDER
from scripts import *


def spam():
    for file in globals()[SCRIPTS_FOLDER].__all__:
        process = Process(target=globals()[file].main)
        process.start()
        sleep(.5)


if __name__ == '__main__':
    spam()
