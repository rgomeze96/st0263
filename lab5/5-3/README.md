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

# Part 1

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
Results:

![image](https://user-images.githubusercontent.com/47034545/200096255-e0b389d3-42eb-4f38-adde-1fd1d208f227.png)

# Part 2

Dataset for stocks, daily reports of the average price of each stock, located in the file dataempresas.txt

## 2.1
By stock value, filtered low to high
Command to run:
```
python MR2-1.py ./datasets/dataempresas.txt
```
Results:

![image](https://user-images.githubusercontent.com/47034545/200096268-8fd18718-ca7e-4a34-ac15-6a3924d1d28b.png)


## 2.2
Stocks that have always raised in price or are extremely steady
Command to run:
```
python MR2-2.py ./datasets/dataempresas.txt
```
Results:

![image](https://user-images.githubusercontent.com/47034545/200096283-51e15bc6-e003-460e-aa9c-1bb7e7b898d5.png)

## 2.3
Black day: Day in which the largest number of stocks have the lowest value (an economic crash), assume inflation independent of time
Command to run:
```
python MR2-3.py ./datasets/dataempresas.txt
```
Results:

![image](https://user-images.githubusercontent.com/47034545/200096293-3aabb11f-0efc-403b-80ae-7e1d81a03dfc.png)


# Part 3

Dataset with film ratings, located in datapeliculas.txt

## 3.1
Number of movies viewed by each user, average rating value
Command to run:
```
python MR3-1.py ./datasets/datapeliculas.txt
```
Results:

![image](https://user-images.githubusercontent.com/47034545/200096326-f7dc3319-beca-4f84-bc47-26c2224c546d.png)

## 3.2
Day that the most amount of movies were seen
Command to run:
```
python MR3-2.py ./datasets/datapeliculas.txt
```
Results:

![image](https://user-images.githubusercontent.com/47034545/200096338-c63fb8ff-cb92-438b-8d57-3459825b4fc8.png)

## 3.3
Day that the least amount of movies were seen
Command to run:
```
python MR3-3.py ./datasets/datapeliculas.txt
```
Results:

![image](https://user-images.githubusercontent.com/47034545/200096350-22a0f64f-a7db-402f-8ccb-34e413d5e894.png)

## 3.4
Number of users who watched the same movie and same average rating
Command to run:
```
python MR3-4.py ./datasets/datapeliculas.txt
```
Results:

![image](https://user-images.githubusercontent.com/47034545/200096359-a537dd70-13bc-4190-9199-8a397564ea1e.png)


## 3.5
Day on which users have given the worst evaluation on average.
Command to run:
```
python MR3-5.py ./datasets/datapeliculas.txt
```
Results:

![image](https://user-images.githubusercontent.com/47034545/200096367-491ff5f0-6b1a-4ff6-980d-b6b8240b7a3e.png)

## 3.6
Day on which users have given the best evaluation.
Command to run:
```
python MR3-6.py ./datasets/datapeliculas.txt
```
Results:

![image](https://user-images.githubusercontent.com/47034545/200096380-3009f1a6-65dc-49b7-b78d-4e0e046e4cd7.png)


## 3.7
The best and worst film evaluated by genre.
Command to run:
```
python MR3-7.py ./datasets/datapeliculas.txt
```
Results:

![image](https://user-images.githubusercontent.com/47034545/200096393-90753ae8-775a-4a6c-966d-25cf535db8b8.png)

