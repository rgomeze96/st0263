## Student: Rafael Gomez Elkin, rgomeze@eafit.edu.co
## Class: Tópicos Especiales de Telemática
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

<hr>
Lab 5-1-Aws-EMR Cluster
<hr>

## Create Cluster
Requirements: Must have created an instance with an elastic ip and have created a ppk key if in windows.

Click on the Create cluster button
![image](https://user-images.githubusercontent.com/47034545/200088173-b9ba5464-fe80-453f-86b4-4a4c1d34f384.png)
Create the EMR Cluster with the following settings
![emr-cluster-config](https://user-images.githubusercontent.com/47034545/200087996-91352cc8-c591-4322-af24-767f37be5b38.png)

AWS Glue Data settings:

![image](https://user-images.githubusercontent.com/47034545/200089009-01191019-acf6-444d-b1bb-b358ad9bc05e.png)


In the Edit Software Settings section enter the following code into the text area:
```
[{"classification":"jupyter-s3-conf","properties":{"s3.persistence.bucket":"notebooksrgomeze","s3.persistence.enabled":"true"}}]
```

Select the instance type as m4.xlarge and the purchasing option as Spot

![image](https://user-images.githubusercontent.com/47034545/200088579-dd0190a3-0317-479e-b647-5b38d43fec68.png)

I select 3 hours for the auto deletion in order to have a longer instance but to reduce cost 1 hour is recommended and at least 20GiB

![image](https://user-images.githubusercontent.com/47034545/200088652-7932cf11-84d4-44f9-928a-c5710e9b0b28.png)

Select the key that you created in the EC2 Instance

![image](https://user-images.githubusercontent.com/47034545/200088723-6bd10e93-6f27-4141-b66d-b22e79fc688a.png)

Click on Create cluster and wait about 20 minutes for the cluster to start in order to continue.

<hr>

## Create S3 Bucket

In the search bar type: s3

![image](https://user-images.githubusercontent.com/47034545/200089233-2aa30fb2-522e-4e15-b90d-28294b84768f.png)

Click on the button Create bucket and no settings need to be changed just enter in the name of the bucket that you entered in the Edit Software
settings text area

![image](https://user-images.githubusercontent.com/47034545/200089316-9d5133c6-8c92-42a7-b6e5-17cd99487181.png)

In the Block public access tab in the left menu:

![image](https://user-images.githubusercontent.com/47034545/200089546-fa9b6c9f-faa0-42d1-8f72-e20ec13c92ba.png)

Click on edit and make sure the following port ranges are entered:

![image](https://user-images.githubusercontent.com/47034545/200089577-b2ac1df0-340c-4493-967e-1dbd0ca13773.png)

<hr>

From there you can 

## Configure Master Group securtiy measures

Click on the the link for the master

![image](https://user-images.githubusercontent.com/47034545/200089961-aa8be433-f15b-4ccd-948d-10a4bd12721f.png)


From there click on the Edit inbound rules button:

![image](https://user-images.githubusercontent.com/47034545/200090030-0041043b-c4ab-4099-9fe4-e4a9ba2be6ef.png)

Port 8443 should be allowed from the master instance

![image](https://user-images.githubusercontent.com/47034545/200090275-aa524547-28ec-4ba0-83bc-12c1fba22b42.png)

Ports 8888, 9443 and 8890 should be allowed from anywhere and for SSH, AWS enters the config settings automatically, click on save.

![image](https://user-images.githubusercontent.com/47034545/200090343-9c3fa7b0-6b3c-4f0c-be6f-2763c9f20c85.png)

<hr>

## Connect using PuTTY

Now that the Cluster has started and is waiting:

![image](https://user-images.githubusercontent.com/47034545/200090580-b9ab1eed-a221-4040-a2b9-4832d4a2a323.png)

We can click on the cluster then on the link that says: Connect to the Master Node Using SSH:

![image](https://user-images.githubusercontent.com/47034545/200090682-728290b0-dad3-423c-addf-c65b8d996af0.png)


Now we can copy the Hostname field from the pop-up:
![image](https://user-images.githubusercontent.com/47034545/200090542-9a43f68a-cf7c-4ecf-af58-0e854e7850c3.png)

And put it into our PuTTY and select the PPK file you downloaded when you created the key in the EC2 Instance:
![image](https://user-images.githubusercontent.com/47034545/200090937-15a70335-b6e6-4140-b8c0-ecd0dfd20868.png)

In the PuTTY settings, go to: Connection -> SSH -> Auth -> Credentials and click on Browse for the private key file:

![image](https://user-images.githubusercontent.com/47034545/200090847-44544243-0cf0-44f3-9132-c002f07c4db1.png)

Now click on Connect then Accept in the pop-up and you will be in the terminal of the EMR Cluster:
![image](https://user-images.githubusercontent.com/47034545/200091079-c1e526c9-57a9-4351-8748-fd6b1a56a4f3.png)

Check that the proper hadoop files are there:
![image](https://user-images.githubusercontent.com/47034545/200091124-08207399-9bb7-41a2-8ab2-1b69361176da.png)

In the Cluster main menu there is a tab for Application user interfaces, click on it:
![image](https://user-images.githubusercontent.com/47034545/200091189-a7adc025-db81-40bb-a84b-3efdacd28049.png)

Copy and paste the HUE URL and Create an Account for Hue:
![image](https://user-images.githubusercontent.com/47034545/200091224-8842fe96-12fe-4ee1-bd66-52d6fcfa05a3.png)

You can then see the default hive database:
![image](https://user-images.githubusercontent.com/47034545/200091251-0f7f8e8e-13c5-4710-9382-f35f8f7a7e04.png)

You can then go to your jupyter notebook that you created in your s3 bucket, I uploaded a notebook from another class:
![image](https://user-images.githubusercontent.com/47034545/200091323-486bf5a2-29fd-4011-95f2-533b644e9353.png)

You then want to start a session in jupyterhub using username: jovyan and password: jupyter
![image](https://user-images.githubusercontent.com/47034545/200091385-33cf6a44-1126-43f1-9327-81bc6cfe9bd8.png)

And a session in Zeppelin:
![image](https://user-images.githubusercontent.com/47034545/200091408-fb0d10c3-04be-4b2d-be8b-8f7d9ca3ea15.png)

Then you can terminate the cluster.
