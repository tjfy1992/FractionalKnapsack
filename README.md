# FractionalKnapsack
The python implementation of the greedy algorithm that solves fractional knapsack

Item.py : The class of item to be put into the knapsack.
PriorityQueue.py: The implementation of a priority queue by heapq. Each element in the priority queue is an item. Each item has a priority which equals to its value, aka benefit/weight(keep 3 decimal places for fractional part). In the priority queue, the item with higher priority gets out first. Each item also has a unique id, so that when the priorities of two item are the same, the item with larger id gets out first.

FileReader.py: The class of a file reader. The file reader reads from a txt file, and initialize the list of Items with the data it reads.

FractionalKnapsack.py: The implementation of fractional knapsack algorithm. The output format is:
[(1.0, 5), (2.0, 3), (6.0, 4), (1.0, 2)]
which means 1.0 unit of item 5, 2.0 units of item 3, 6.0 units of item 4 and 1.0 unit of item 2. 

test_item.py: The unit test for Item.py.

test_priorityQueue.py: The unit test for PriorityQueue.py

test_fractionalKnapsack.py: The unit test for the work flow of fractional knapsack, including the file reader.

In FractionalKnapsack.py, in the constructor function, there is a statement which receives user input as the max weight of the knapsack. The way to take input the item number, weight and benefit is by reading a file whose path is specified by the user. The function is written in FileReader.py: in function read_file, the user needs to input the path of the input file. In test_fractionalKnapsack.py, I mocked the built-in input function so that the values(weight and input file path) can be assigned within the test functions. A tear-down function is written in the end to restore the built-in function. The input files are as following:

test01.txt: a text file showing the number of items and the weight and benifit of each item. The meaning of each line is: (weight, benefit). The number of lines is the number of items. Each line number represents the item's id.
Here are the information provided by test01.txt:
id	weight	benefit
1	4	12
2	8	32
3	2	40
4	6	30
5	1	50

test02.txt: another text file with same format and different data.
Here are the information provided by test02.txt:
id	weight	benefit
1	4	16
2	8	24
3	2	12
4	6	36
5	1	50
6	3	24


The above programs are written within PyCharm for Windows, with Python's version 3.7.4 x64, and pytest-5.1.2.
To run the programs, in PyCharm, 
click File ->  open -> select the project named "FractionalKnapsack-master";
At the terminal, get into the current directory, and run "pytest".

In test_fractionalKnapsack.py, there are 6 tests on the fractional knapsack: 
test_knapsack_01(), test_knapsack_02() and test_knapsack_03() take test01.txt as input;
test_knapsack_04(), test_knapsack_05() and test_knapsack_06() take test02.txt as input.

test_knapsack_01(): max_weight = 10, input=test01.txt
The expected result is: 1.0 unit of item 5, 2.0 units of item 3, 6.0 units of item 4 and 1.0 unit of item 2
expected output: [(1.0, 5), (2.0, 3), (6.0, 4), (1.0, 2)]

test_knapsack_02(): max_weight = 15, input=test01.txt
The expected result is: 1.0 unit of item 5, 2.0 units of item 3, 6.0 units of item 4 and 6.0 units of item 2
expected output: [(1.0, 5), (2.0, 3), (6.0, 4), (6.0, 2)]

test_knapsack_03(): max_weight = 12.6, input=test01.txt
The expected result is: 1.0 unit of item 5, 2.0 units of item 3, 6.0 units of item 4 and 3.6 units of item 2
expected output: [(1.0, 5), (2.0, 3), (6.0, 4), (3.6, 2)]

test_knapsack_04(): max_weight = 10, input=test02.txt
The expected result is: 1.0 unit of item 5, 3.0 units of item 6, 2.0 units of item 3 and 4.0 units of item 4
expected output: [(1.0, 5), (3.0, 6), (2.0, 3), (4.0, 4)]

test_knapsack_05(): max_weight = 16, input=test02.txt
The expected result is: 1.0 unit of item 5, 3.0 units of item 6, 2.0 units of item 3, 6.0 unit of item 4 and 4.0 units of item 1
expected output: [(1.0, 5), (3.0, 6), (2.0, 3), (6.0, 4), (4.0, 1)]

test_knapsack_06(): max_weight = 13.4, input=test02.txt
The expected result is: 1.0 unit of item 5, 3.0 units of item 6, 2.0 units of item 3, 6.0 unit of item 4 and 1.4 units of item 1
expected output: [(1.0, 5), (3.0, 6), (2.0, 3), (6.0, 4), (1.4, 1)]
