## Student: Rafael Gomez Elkin, rgomeze@eafit.edu.co
## Class: Tópicos Especiales de Telemática
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

<hr>
Lab 5-2
<hr>

Connect to the EMR Cluster using PuTTY:
![image](https://user-images.githubusercontent.com/47034545/200091079-c1e526c9-57a9-4351-8748-fd6b1a56a4f3.png)

Check that the proper hadoop files are there:
![image](https://user-images.githubusercontent.com/47034545/200091124-08207399-9bb7-41a2-8ab2-1b69361176da.png)

Upload the datasets that the professor provided

Results:

![image](https://user-images.githubusercontent.com/47034545/200097842-64ecc8ce-54b4-4697-b47e-bd9e2290a8e2.png)

Make sure the files are there using hdfs command:

![image](https://user-images.githubusercontent.com/47034545/200097864-a488ed87-fb6a-4694-bee7-02c9e691d4e4.png)

## Other hdfs commands

Show disk usage:
```
hdfs dfs -du: ver uso de disco en bytes
```
Results:

![image](https://user-images.githubusercontent.com/47034545/200097909-89213bc5-0634-44c2-a15e-dce7491c1b0b.png)

Show content of file:
```
hdfs dfs -cat datasets/otros/dataempleados.txt
```
Results:

![image](https://user-images.githubusercontent.com/47034545/200097936-eaf800b6-1f53-445a-be72-df666192235c.png)

