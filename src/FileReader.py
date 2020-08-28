"""
Date: 09/24/2019
"""
from src.Item import Item


class FileReader:
    def __init__(self):
        self.data = []

    def read_file(self):
        path = input("Please input the file name：")
        self.data = []
        with open(path, 'rt') as f:
            index = 1
            for eachLine in f.readlines():
                line = eachLine.strip().replace('\n', '')
                arr = line.split(',')
                item = Item(int(arr[0]), int(arr[1]), index)
                self.data.append(item)
                index += 1

