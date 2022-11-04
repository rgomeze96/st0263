Tópicos de Telemática ST0263
Lab 4
Rafael Gomez

1. Brief Description:
Create, deploy and manage a monolithic application with load balancing, distributed data all utilizing docker containers. Also must use LetsEncrypt to create a valid SSL certificate for the domain.
<hr>
1.1 Aspects of the lab to be implemented (Load Balancer, Wordpress 1 and 2, NFS and a MySQL Database).
Assign a domain that is directed to the IP of the load balancer.
Create an SSL certificate for the domain.
<hr>
2. General Design Information
Use Docker containers for the installation of Wordpress, MySQL y Nginx.

![image](https://user-images.githubusercontent.com/47034545/198078658-cb56fa1a-59b9-4a5c-86c2-d8d9dad3d7a7.png)

<hr>

3. Description and steps for implementing the lab:
IP address and Domain
Elastic IP Address of Load Balancer: 35.188.138.142
Dominio: rgomeze-lab4.tk
Dominio con certificacion: https://rgomeze-lab4.tk
Technical Details
GCP: Cloud Service to deploy the instances
Docker: Container to deploy MySQL, Nginx and Wordpress.
Nginx: Web Server
Certbot | Let's Encrypt: Services to create and assign SSL certificate
How to configure the GCP instances to meet the lab requirements
Create 5 separate Ubuntu instances in GCP:
Access the GCP console (console.cloud.google.com)
Click on Compute Engine.
Click on Create Instancia.
Configure the instance for ec2-micro, Ubuntu 64-bitand allow HTTP y HTTPS traffic.
Click on Create.
<hr>

![image](https://user-images.githubusercontent.com/47034545/198077099-6a2c36d3-f847-4173-b14d-11b0374d5816.png)

<hr>
Assign an Elastic IP address for each instance:
Click on Navigation.
Click on VPC Network.
Click on IP addresses.
Click on Reserve External Static Address
<hr>

![image](https://user-images.githubusercontent.com/47034545/198077286-0de4432a-2df1-4f75-8ba8-f2cbd2122137.png)

<hr>
Configure Google Cloud DNS:
Enter Cloud DNS in the Search Bar.
Click Create Zone.

![image](https://user-images.githubusercontent.com/47034545/198077393-73fd5710-493a-4422-9f91-89e62f316b93.png)

<hr>
Add A and CNAME registers for the domain.

![image](https://user-images.githubusercontent.com/47034545/198077511-1248878a-6e37-4f77-8a43-275e97e17d4d.png)

<hr>
Configure nameserver in Freenom for the domain:
Click on Manage domain
Click on Management tools -> Nameservers
Add the NS domains provided by Google Cloud.

![image](https://user-images.githubusercontent.com/47034545/198077782-22feb8de-f40e-4c08-a787-dbaf2a1d341e.png)

<hr>

#Configure Load Balancer:
1. Connect using SSH to the GCP instance:
Access the GCP Console.
Click on Compute Engine.
Click on VM Instances.
Clickon the SSH button.
2. Install certbot, letsencrypt and nginx:
Enter the following commands:

```
sudo apt update
sudo apt install python3-pip
sudo -H pip3 install certbot
sudo apt install letsencrypt -y
sudo apt install nginx -y
```

3. Configure the nginx.conf file
Modify the configuration file:

```
sudo nano /etc/nginx/nginx.conf
Overwrite the existing text with the following:

worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

events {
    worker_connections  1024;  ## Default: 1024
}
http {
    server {
        listen  80 default_server;
        server_name _;
        location ~ /\.well-known/acme-challenge/ {
            allow all;
            root /var/www/letsencrypt;
            try_files $uri = 404;
            break;
        }
    }
}
```
Save the configuration file:

```
sudo mkdir -p /var/www/letsencrypt
sudo nginx -t
sudo service nginx reload
```

4. Create the SSL certificate
Execute the following commands for the SSL certificate (ej. www):

```
sudo letsencrypt certonly -a webroot --webroot-path=/var/www/letsencrypt -m rgomeze@eafit.edu.co --agree-tos -d rgomeze-lab4.tk
```

For wildcards enter the following commands:

```
sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.rgomeze-lab4.tk --manual --preferred-challenges dns-01 certonly
```

IMPORTANT: Must wait until the DNS is updated before hitting enter.
<hr>
5. Configuration Files:
Create a folder for the certificates:
```
mkdir -p nginx/ssl
```
Copy the files to the folder that was just created:
```
sudo su
cp /etc/letsencrypt/live/rgomeze-lab4.tk/* /home/gomezr6993/nginx/ssl/
```

Create the configuration file: options-ssl-nginx.conf:
```
sudo nano /etc/letsencrypt/options-ssl-nginx.conf
```

Copy and paste the following text in the file that was just created:

```
ssl_session_cache shared:le_nginx_SSL:10m;
ssl_session_timeout 1440m;
ssl_session_tickets off;
ssl_protocols TLSv1.2 TLSv1.3;
ssl_prefer_server_ciphers off;
ssl_ciphers "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384";
```

Copiar el archivo options-ssl-nginx.conf:

```
cp /etc/letsencrypt/options-ssl-nginx.conf /home/gomezr6993/nginx/ssl/
```

Access the directory nginx/ssl and copy the filess-dhparams.pem:

```
cd nginx/ssl
openssl dhparam -out ssl-dhparams.pem 512
```

Run the following commands:

```
DOMAIN='rgomeze-lab4.tk' bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/letsencrypt/$DOMAIN.pem'
cp /etc/letsencrypt/live/rgomeze-lab4.tk/* /home/gomezr6993/nginx/ssl/
exit
```

<hr>
6. Docker configuration
Instalar docker, docker-compose y git:

```
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo apt install git -y
```

Initialize and run Docker:

```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker sceballosp
sudo reboot
```

Clone the repo from the professor:

```
git clone https://github.com/st0263eafit/st0263-2022-2.git
cd st0263-2022-2/docker-nginx-wordpress-ssl-letsencrypt
sudo cp docker-compose.yml /home/sceballosp/nginx
sudo cp nginx.conf /home/sceballosp/nginx
sudo cp ssl.conf /home/sceballosp/nginx
```

Detener nginx:

```
ps ax | grep nginx
netstat -an | grep 80
sudo systemctl disable nginx
sudo systemctl stop nginx
```

Delete the contents of the file and paste the following text: (change the IPs to wordpress instances, private not public IPs)

```
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;
events {
  worker_connections  1024;  ## Default: 1024
}
http {
  upstream loadbalancer{
    server 10.128.0.12:80 weight=5;
    server 10.128.0.13:80 weight=5;
  }
  server {
    listen 80;
    listen [::]:80;
    server_name _;
    rewrite ^ https://$host$request_uri permanent;
  }
  server {
    listen 443 ssl http2 default_server;
    listen [::]:443 ssl http2 default_server;
    server_name _;
    # enable subfolder method reverse proxy confs
    #include /config/nginx/proxy-confs/*.subfolder.conf;
    # all ssl related config moved to ssl.conf
    include /etc/nginx/ssl.conf;
    client_max_body_size 0;
    location / {
      proxy_pass http://loadbalancer;
      proxy_redirect off;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Host $host;
      proxy_set_header X-Forwarded-Server $host;
      proxy_set_header X-Forwarded-Proto $scheme;
    }
  }
}
```

Delete the contents of docker-compose.yml y replace with the following:

```
version: '3'
services:
  nginx:
    container_name: nginx
    image: nginx
    volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf:ro
    - ./ssl:/etc/nginx/ssl
    - ./ssl.conf:/etc/nginx/ssl.conf
    ports:
    - 80:80
    - 443:443
```

Then initialize and start Docker:

```
docker-compose up --build -d
```

<hr>
NFS Server Configuration:
1. Install NFS server:

```
sudo apt update
sudo apt install nfs-kernel-server
```

Create folder for NFS file transfers

```
sudo mkdir -p /mnt/nfs_share
sudo chown -R nobody:nogroup /mnt/nfs_share/
sudo chmod 777 /mnt/nfs_share/
```

Access exports file:

```
sudo nano /etc/exports
```

Add the following content to the end of the previous file: 

```
/mnt/nfs_share 10.128.0.0/20(rw,sync,no_subtree_check)
```

Update the firewall rules for the NFS server:

```
sudo exportfs -a
sudo systemctl restart nfs-kernel-server
sudo ufw allow from 10.128.0.0/20 to any port nfs
sudo ufw enable
sudo ufw status
```

2. Install NFS on the Wordpress Instances:

```
sudo apt update
sudo apt install nginx -y
```

Install NFS for each instance:

```
sudo apt install nfs-common -y
```

Access the fstab file in the directory: /etc/fstab and add the following line:

```
10.128.0.10:/mnt/nfs_share /var/www/html nfs auto 0 0
```

Create folder to locate the files to be shared in both instances:

```
sudo mkdir -p /mnt/nfs_clientshare
```

Connect both instances to the NFS server:

```
sudo mount 10.128.0.10:/mnt/nfs_share /mnt/nfs_clientshare
```

Verify that everything is working well:

In the NFS server:
```
cd /mnt/nfs_share/
sudo touch sample1.text sample2.text
En los wordpress:
ls -l /mnt/nfs_clientshare/
```

The results should be the following:
![image](https://user-images.githubusercontent.com/47034545/197642783-fe93b80e-b794-49e7-82ab-81c472c4315b.png)
![image](https://user-images.githubusercontent.com/47034545/197642828-826e461c-8a5c-4688-a4c3-a24cc3a63e3e.png)

Configure instance for SQL Database:
Install docker y docker-compose:
```
sudo apt install docker.io -y
sudo apt install docker-compose -y
```

Create a folder for the Docker container config:

```
mkdir Docker
```
Access the folder that was just created and create the following files with the following content

Create a Dockerfile with:
FROM mysql:8.0

docker-compose.yaml with:
```
version: "3"
services:
  mysql:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: dbserver
    restart: always
    ports:
      - 3306:3306
    environment:
      MYSQL_ROOT_PASSWORD: "1234"
      MYSQL_DATABASE: "wordpress_db"
    volumes:
      - ./schemas:/var/lib/mysql:rw
volumes:
  schemas: {}
```

Initialize and enable Docker:

```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker gomezr6993
```

Execute and start the MySQL container:
```
sudo docker-compose up --build -d
sudo docker exec -it dbserver mysql  -p
```

Create the database and users:
![image](https://user-images.githubusercontent.com/47034545/197642725-2b547f93-8bf3-450b-8345-d21eb9d65d91.png)

Configuration for the wordpress for each instance:

Install docker y docker-compose:

```
sudo apt install docker.io -y
sudo apt install docker-compose -y

sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker sceballosp
Stop the NGINX service:

sudo systemctl disable nginx
sudo systemctl stop nginx
```

Create a folder for the docker configuration:

```
mkdir Docker
```

Access the folder and create the following file with the following content:

docker-compose.yaml with:
```
version: '3'
services:
  wordpress:
    container_name: wordpress
    image: wordpress:latest
    restart: always
    environment:
      WORDPRESS_DB_HOST: 10.128.0.54:3306
      WORDPRESS_DB_USER: wordpress_1
      WORDPRESS_DB_PASSWORD: 1234
      WORDPRESS_DB_NAME: wordpress_db
    volumes:
      - /var/www/html:/var/www/html
    ports:
      - 80:80
volumes:
  wordpress:
```
Execute and run the container:

```
sudo docker-compose up --build -d
```

Now everything should be working, enter https://rgomeze-lab4.tk

![image](https://user-images.githubusercontent.com/47034545/197642647-d64b975c-77a9-43a8-bcc2-e3d542803ec6.png)
