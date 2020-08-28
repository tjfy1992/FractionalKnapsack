"""
Date: 09/24/2019
Class: CS5310
Assignment: Fractional Knapsack
Author(s): Zhongqiu Gao
test script for fractional knapsack
"""

from src.FractionalKnapsack import FractionalKnapsack
import src.FractionalKnapsack
from src.FileReader import FileReader
import src.FileReader

file_reader = FileReader()


def test_file_reader_instantiate():
    assert isinstance(file_reader, FileReader)


def test_knapsack_01():
    src.FileReader.input = lambda x: "test01.txt"
    file_reader.read_file()
    # max_weight = 10
    src.FractionalKnapsack.input = lambda x: "10"
    fractional_knapsack = FractionalKnapsack(file_reader.data)
    assert isinstance(fractional_knapsack, FractionalKnapsack)
    result_list = fractional_knapsack.knapsack_handler()
    # 1.0 unit of item 5, 2.0 units of item 3, 6.0 units of item 4 and 1.0 unit of item 2
    assert result_list == [(1.0, 5), (2.0, 3), (6.0, 4), (1.0, 2)]


def test_knapsack_02():
    src.FileReader.input = lambda x: "test01.txt"
    file_reader.read_file()
    # max_weight = 15
    src.FractionalKnapsack.input = lambda x: "15"
    fractional_knapsack = FractionalKnapsack(file_reader.data)
    assert isinstance(fractional_knapsack, FractionalKnapsack)
    result_list = fractional_knapsack.knapsack_handler()
    # 1.0 unit of item 5, 2.0 units of item 3, 6.0 units of item 4 and 6.0 units of item 2
    assert result_list == [(1.0, 5), (2.0, 3), (6.0, 4), (6.0, 2)]


def test_knapsack_03():
    src.FileReader.input = lambda x: "test01.txt"
    file_reader.read_file()
    # max_weight = 12.6
    src.FractionalKnapsack.input = lambda x: "12.6"
    fractional_knapsack = FractionalKnapsack(file_reader.data)
    assert isinstance(fractional_knapsack, FractionalKnapsack)
    result_list = fractional_knapsack.knapsack_handler()
    # 1.0 unit of item 5, 2.0 units of item 3, 6.0 units of item 4 and 3.6 units of item 2
    assert result_list == [(1.0, 5), (2.0, 3), (6.0, 4), (3.6, 2)]


def test_knapsack_04():
    src.FileReader.input = lambda x: "test02.txt"
    file_reader.read_file()
    src.FractionalKnapsack.input = lambda x: "10"
    fractional_knapsack = FractionalKnapsack(file_reader.data)
    assert isinstance(fractional_knapsack, FractionalKnapsack)
    result_list = fractional_knapsack.knapsack_handler()
    # 1.0 unit of item 5, 3.0 units of item 6, 2.0 units of item 3 and 4.0 units of item 4
    assert result_list == [(1.0, 5), (3.0, 6), (2.0, 3), (4.0, 4)]


def test_knapsack_05():
    src.FileReader.input = lambda x: "test02.txt"
    file_reader.read_file()
    src.FractionalKnapsack.input = lambda x: "16"
    fractional_knapsack = FractionalKnapsack(file_reader.data)
    assert isinstance(fractional_knapsack, FractionalKnapsack)
    result_list = fractional_knapsack.knapsack_handler()
    # 1.0 unit of item 5, 3.0 units of item 6, 2.0 units of item 3, 6.0 unit of item 4 and 4.0 units of item 1
    assert result_list == [(1.0, 5), (3.0, 6), (2.0, 3), (6.0, 4), (4.0, 1)]


def test_knapsack_06():
    src.FileReader.input = lambda x: "test02.txt"
    file_reader.read_file()
    src.FractionalKnapsack.input = lambda x: "13.4"
    fractional_knapsack = FractionalKnapsack(file_reader.data)
    assert isinstance(fractional_knapsack, FractionalKnapsack)
    result_list = fractional_knapsack.knapsack_handler()
    # 1.0 unit of item 5, 3.0 units of item 6, 2.0 units of item 3, 6.0 unit of item 4 and 1.4 units of item 1
    assert result_list == [(1.0, 5), (3.0, 6), (2.0, 3), (6.0, 4), (1.4, 1)]


def teardown_method():
    src.FractionalKnapsack.input = input
    src.FileReader.input = input

