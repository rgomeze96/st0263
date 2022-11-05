# Lab 5-3

<hr>

To complete lab 5-3 the python library MRJob in order to utilize the MapReduce framework, execute the following commands:

1. Create a python virtual environment:

```
python -m venv venv
```

2. Activate the virtual environment:

```
.\venv\Scripts\activate
```

3. Install MRJob

```
pip install mrjob
```

you should see the following results:

![image](https://user-images.githubusercontent.com/47034545/200095268-6f283913-c74a-4541-9d63-bb894361e8c5.png)


We will use the files provided by the professor in order to complete the lab.

## Part 1

<hr>
We will use the dataset dataempleados.txt for the following commands:

### 1.1 Annual Salary of employees based on Socioeconomic status

Command to run:
```
python MR1-1.py ./datasets/dataempleados.txt
```
the result should be the following:
![image](https://user-images.githubusercontent.com/47034545/200095353-960078dc-d2d3-4abf-a262-de043cca6447.png)

### 1.2 Average salary among all employees

Command to run:
```
python MR1-2.py ./datasets/dataempleados.txt
```
Results:
![image](https://user-images.githubusercontent.com/47034545/200095453-0f3c6e95-2d4f-40c5-8ecb-359ef686d958.png)

### 1.3 Number of SE per Employee throughout the dataset

Command to run:
```
python MR1-3.py ./datasets/dataempleados.txt
```

<hr>

Part 2

<hr>

Dataset for stocks, daily reports of the average price of each stock, located in the file dataempresas.txt


