**[🔗 Jump to MARVEL report continuation](#rolling-update)**

# Cloud Computing


## Task 1: Working with Git and GitHub basics


In this task, Git and GitHub workflows were practiced to understand collaborative software development. Actions such as editing, staging, committing, pushing, along with creation of branches and pull requests were performed.


### Understanding Version Control and Distributed Repositories

Version control helps track changes in source code over time. Git is a distributed version control system that allows multiple developers to work collaboratively on the same project.


**Commands Used:**

```
git init
git status
git add .
git commit -m "commit message"
git remote add origin <repo-link>
git push -u origin main
```

**Screenshots:**

![GitBash (Initialize & Add)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/GitBash-SS-1.png)
![GitBash (Commit & Push)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/GitBash-SS-2.png)

---

### Solving Merge Conflicts using Git Rebase

Git rebase helps integrate changes from one branch into another while maintaining a cleaner commit history.


**Commands Used:**

```
git rebase main
git rebase --continue
```

**Screenshots:**

![GitBash (Rebase) - 1](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/GitBash-SS-5.png)
![Git (Rebase) - 2](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/GitBash-SS-6.png)
![Git (Rebase) - 3](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/GitBash-SS-7.png)

---

### Creating and Managing Branches

Branches are used to develop features independently without affecting the main branch.


**Commands Used:**

```
git checkout -b feature-branch
git branch
```

**Screenshots:**

![GitBash (Branching)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/GitBash-SS-3.png)
![GitBash (Merging)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/GitBash-SS-4.png)

---

### Open Source Contribution

An open-source repository was explored and contributions were made through commits and pull requests.


**Screenshots:**

![GitHub (Repository)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/GitHub-SS-1.png)
![GitHub (Pull Request)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/GitHub-SS-2.png)

---

### Using Git Revert and Git Cherry-Pick

Git revert is used to undo commits safely, while git cherry-pick applies selected commits from one branch to another.


**Commands Used:**

```
git revert <commit-id>
git cherry-pick <commit-id>
```

**Screenshots:**

![GitBash (Revert)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/GitBash-SS-9.png)
![GitBash (Cherry-Pick)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/GitBash-SS-10.png)

---

### Customized Git Workflow using Git Config

Git config allows customisation of user identity and workflow settings. It can also be used to view the details, if already set.


**Commands Used:**

```
git config --global user.name
git config --global user.email
```

**Screenshot:**

![GitBash (Config)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/GitBash-SS-11.png)

---

## Task 2: Exploring Docker Fundamentals


### Difference Between Containers and Virtual Machines

| Feature          | Containers              | Virtual Machines       |
| ---------------- | ----------------------- | ---------------------- |
| Operating System | Share host OS kernel    | Each VM has its own OS |
| Size             | Lightweight             | Heavyweight            |
| Startup Time     | Starts in seconds       | Takes minutes          |
| Performance      | Faster                  | Comparatively slower   |
| Resource Usage   | Uses fewer resources    | Uses more CPU and RAM  |
| Isolation        | Process-level isolation | Full system isolation  |
| Portability      | Highly portable         | Less portable          |
| Example          | Docker                  | VirtualBox, VMware     |


---

### Pulling Docker Images from Docker Hub

Docker images were pulled from Docker Hub and stored locally in the system.


**Commands Used:**

```
docker pull nginx
docker images
```

**Screenshot:**

![Docker Images](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Docker-1.png)

---

### Running Containers using Docker CLI

An nginx container was created and executed locally using Docker CLI commands. Port mapping was used to access the application through the browser.


**Commands Used:**

```
docker run -d --name mynginx -p 8080:80 nginx
docker ps
```

**Screenshot:**

![Docker nginx](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Docker-2.png)

---

### Viewing Logs and Inspecting Container State

Docker logs and inspect commands were used to monitor container activity and understand container status information.


**Commands Used:**

```
docker logs mynginx --tail 5
docker inspect mynginx --format='Status: {{.State.Status}}'
```

**Screenshot:**

![Docker (Logs and Container State)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Docker-3.png)

---

### Managing Container Lifecycle

Container lifecycle operations such as restart, stop, and remove were performed successfully.


**Commands Used:**

```
docker restart mynginx
docker stop mynginx
docker rm mynginx
docker rmi nginx
```

**Screenshots:**

![Docker (Container Lifecycle) - 1](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Docker-4.png)
![Docker (Container Lifecycle) - 2](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Docker-5.png)
![Docker (Container Lifecycle) - 3](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Docker-6.png)

---

## Task 3: Dockerizing a Simple Application


A simple static website was containerized using Docker. A Dockerfile was created using the nginx base image. The HTML file was copied into the nginx web server directory using the COPY instruction.


### Dockerfile

```
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
```


**Commands Used:**

```
docker build -t mywebsite .
docker run -d --name website-container -p 8080:80 mywebsite
docker ps
docker rm -f website-container
docker rmi mywebsite
```

**Screenshots:**

![Docker Build](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Dockerfile-1.png)
![Docker Run](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Dockerfile-2.png)

---

## Task 4: Launch and Manage an AWS EC2 Instance


AWS EC2 was explored by launching a Linux virtual machine and configuring its network access. A security group was configured to allow SSH on port 22 and HTTP on port 80. The instance was accessed securely using an SSH key pair (`.pem` file).

### Connecting to the EC2 Instance

The instance was connected using SSH with the generated key pair.

**Command Used:**

```bash
ssh -i "clcy-ec2-key.pem" ec2-user@<public-dns>
```

The connection was established successfully and the Amazon Linux environment was accessed.

### Installing and Managing Nginx

Nginx was installed and configured as a web server on the EC2 instance.


**Commands Used:**

```bash
sudo dnf update -y
sudo dnf install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
```

The Nginx service was successfully started and verified as active.

### Accessing Nginx through the Public IP

The EC2 instance's public IP was used to access the Nginx web server through a browser. The Nginx welcome page was displayed successfully, confirming that the instance was reachable over HTTP.

### EC2 CPU and Memory

EC2 instance types determine the available vCPUs, memory, and other resources. CPU credits on burstable instances such as the `t3.micro` allow the instance to temporarily use CPU performance above its baseline when required.

### Screenshots

![EC2 (nginx Status)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/AWS-EC2-1.png)
![EC2 (Instance Summary)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/AWS-EC2-2.png)
![EC2 (nginx Welcome Page)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/AWS-EC2-3.png)

---

## Task 5: Kubernetes Basics and Writing Pod Specs


Kubernetes was explored using Minikube to understand basic container orchestration concepts and deploy a simple Nginx container.


### Understanding Kubernetes Concepts

The following core concepts were studied:

* **Cluster:** A collection of machines that work together to run containerized workloads.
* **Node:** A machine within the Kubernetes cluster that runs Pods.
* **Pod:** The smallest deployable unit in Kubernetes, which contains one or more containers. In this task, the Pod contained an Nginx container.
* **Control Plane:** The components responsible for managing the Kubernetes cluster, including scheduling and maintaining the desired state of workloads.

Minikube was used to create a local Kubernetes cluster for the task.

### Creating a Pod Manifest

A Pod specification was created using a YAML manifest to deploy an Nginx container.

```pod.yaml
apiVersion: v1
kind: Pod
metadata:
    name: nginx-pod
spec:
    containers:
        - name: nginx
        image: nginx:latest
```

### Applying the Manifest

The Minikube cluster was started using the Docker driver and the Pod manifest was deployed using kubectl.


**Commands Used:**

```
minikube start --driver=docker
minikube status
minikube kubectl -- apply -f pod.yaml
```

The manifest was successfully applied and the nginx-pod was created.

### Inspecting the Pod

The Pod's status was verified and additional information was obtained using kubectl.


**Commands Used:**

```
minikube kubectl -- get pods
minikube kubectl -- describe pod nginx-pod
minikube kubectl -- logs nginx-pod
```

The Pod reached the Running state with the Nginx container marked as ready. The describe command was used to inspect the Pod's configuration, container state, assigned IP, node, and events. The logs confirmed that the Nginx container initialized successfully.

### Screenshots

![K8S (minikube Status)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Kubernetes-1.png)
![K8S (Pod Manifest)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Kubernetes-2.png)
![K8S (Pod Logs)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Kubernetes-3.png)

---

## Task 6: Manage AWS S3 and IAM with CLI


AWS IAM and S3 were explored using the AWS CLI. An IAM user was created and configured with S3 permissions, and the AWS CLI was configured to interact with AWS services. S3 bucket and object operations were performed, followed by applying a restricted IAM policy to demonstrate least-privilege access.

### AWS CLI and S3 Operations

The AWS CLI was configured with IAM credentials and used to manage an S3 bucket. A test file was created, uploaded to the bucket, listed, downloaded, and deleted.


**Commands Used:**

```
aws s3 mb s3://clcy-s3-bucket-silversquare22 --region ap-southeast-2
aws s3 cp test.txt s3://clcy-s3-bucket-silversquare22/
aws s3 ls s3://clcy-s3-bucket-silversquare22/
aws s3 cp s3://clcy-s3-bucket-silversquare22/test.txt test-downloaded.txt
aws s3 rm s3://clcy-s3-bucket-silversquare22/test.txt
aws s3 rb s3://clcy-s3-bucket-silversquare22/
```

The S3 object operations were successfully performed using the CLI, demonstrating basic cloud storage management.

### IAM Least-Privilege Policy

A custom `CLCY-S3-LimitedAccess` policy was applied to restrict the IAM user's S3 permissions. The policy allows listing the specified bucket and reading, writing, and deleting objects, without granting unrestricted bucket-management permissions.

The restricted permissions were validated by attempting operations outside the policy scope. Bucket creation and deletion were denied with `AccessDenied`, demonstrating the effect of least-privilege access control.

### Screenshots

![S3 (Bucket Lifecycle)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/AWS-IAM-S3-1.png)
![S3 (Custom Policy Details)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/AWS-IAM-S3-2.png)
![S3 (Access Denied)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/AWS-IAM-S3-3.png)
![S3 (Policy Restriction Application)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/AWS-IAM-S3-4.png)

---

## Task 7: Deploying a Containerised Application on Kubernetes


### Creating a Deployment

A Deployment was created to manage multiple replicas of the Nginx application.

```deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: nginx-deployment
spec:
    replicas: 3
    selector:
        matchLabels:
        app: nginx
    template:
        metadata:
            labels:
                app: nginx
        spec:
            containers:
                - name: nginx
                image: nginx:1.27
                ports:
                    - containerPort: 80
```

The Deployment was configured with 3 replicas, allowing Kubernetes to maintain three instances of the Nginx application.


**Commands Used:**

```
minikube kubectl -- apply -f deployment.yaml
minikube kubectl -- get deployment
minikube kubectl -- get pods
```

The Deployment was successfully created and all three replicas were verified to be running.

### Exposing the Deployment using ClusterIP

A ClusterIP Service was created to provide internal access to the Nginx Pods.

```service-clusterip.yaml
apiVersion: v1
kind: Service
metadata:
    name: nginx-clusterip
spec:
    selector:
        app: nginx
    ports:
        - port: 80
        targetPort: 80
```


**Commands Used:**

```
minikube kubectl -- apply -f service-clusterip.yaml
minikube kubectl -- get services
```

The Service was successfully created with the default ClusterIP type.

### Exposing the Application using NodePort

A NodePort Service was created to make the application accessible from the local machine.

```service-nodeport.yaml
apiVersion: v1
kind: Service
metadata:
    name: nginx-nodeport
spec:
    type: NodePort
    selector:
        app: nginx
    ports:
        - port: 80
        targetPort: 80
        nodePort: 30080
```


**Commands Used:**

```
minikube kubectl -- apply -f service-nodeport.yaml
minikube kubectl -- get services
minikube service nginx-nodeport --url
```

The NodePort Service exposed the Nginx application externally, and the generated URL was accessed through a web browser. The Nginx welcome page was successfully displayed.

### Scaling the Deployment

The Deployment was scaled both up and down using `kubectl`.

Scale up from 3 to 5 replicas:

```
minikube kubectl -- scale deployment nginx-deployment --replicas=5
minikube kubectl -- get pods
```

Scale down from 5 to 2 replicas:

```
minikube kubectl -- scale deployment nginx-deployment --replicas=2
minikube kubectl -- get pods
```

The number of running Pods was successfully increased to five and subsequently reduced to two.

### Rolling Update

A rolling update was performed by changing the Nginx image version in `deployment.yaml` from:

```
nginx:1.27
```

to:

```
nginx:1.28
```

The updated Deployment was then applied:

```
minikube kubectl -- apply -f deployment.yaml
minikube kubectl -- rollout status deployment/nginx-deployment
```

The rollout completed successfully, demonstrating how Kubernetes updates Pods managed by a Deployment while maintaining the desired replica count.

### Screenshots

![K8S (Apply YAML Files)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Kubernetes-Deploy-1.png)
![K8S (nginx Welcome Page)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Kubernetes-Deploy-2.png)
![K8S (Scaling Deployment)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Kubernetes-Deploy-3.png)
![K8S (Deployment Status)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Kubernetes-Deploy-4.png)

---

## Task 8: Use Kubernetes Secrets and Environment Variables


Kubernetes ConfigMaps and Secrets were used to manage application configuration and sensitive AWS credentials separately. A ConfigMap was created for non-sensitive values, while an AWS credential Secret was injected into a Deployment as environment variables. The Pod was verified to receive the configuration and credentials without exposing the actual secret values.

### ConfigMap and Deployment

The ConfigMap was applied and the `aws-env-test` Deployment was created successfully. The resulting Pod was running successfully.

![K8S (ConfigMap)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/K8S8-1.png)

### Verifying Environment Variables

The Pod was accessed using `kubectl exec` to verify the injected values. The ConfigMap values were displayed, while the AWS credentials were checked only for their presence using `SET`, keeping the actual credentials hidden.

![K8S (Verify env Variables)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/K8S8-2.png)

---

## Task 9: Deploy an App to Push Files from Kubernetes to S3


A Flask-based file-upload application was containerized using Docker and deployed on Minikube. The application used AWS credentials provided through Kubernetes Secrets and was exposed using a NodePort service. A test file was uploaded through the application and verified in the S3 bucket, demonstrating the complete Kubernetes-to-S3 workflow.

### Containerizing and Deploying the Application

The Flask application was built into a Docker image named `s3-upload-app:1.0` and deployed as a Kubernetes Pod.

![K8S (Containerize & Deploy)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/K8S9-1.png)
![K8S (Pod Details)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/K8S9-2.png)

### Exposing the Application

A NodePort Service was created for the application, allowing the Flask interface to be accessed through the Minikube-generated local URL.

![K8S (NodePort)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/K8S9-3.png)

### Uploading and Verifying the File

The Flask application successfully received the uploaded file, as shown by the successful `POST` request in the application logs.

![K8S (Upload Logs)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/K8S9-4.png)

The application interface confirmed that `test-upload.txt` was uploaded successfully.

![K8S (Webpage UI)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/K8S9-5.png)

Finally, the uploaded file was verified in the AWS S3 bucket, confirming that the file was successfully transferred from the Kubernetes-hosted application to cloud storage.

![K8S (S3 Bucket in AWS Console)](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/K8S9-6.png)

---

# Cybersecurity


## Task 1: Introduction to Computer Networking

Studied the fundamentals of computer networking and understood how computers and devices communicate with each other through connected networks. Learned about the importance of communication protocols and data sharing in modern networks.

---

## Task 2: Internet

Explored the working of the Internet and understood how global communication takes place between interconnected devices. Learned about web communication, protocols, and Internet-based services.

---

## Task 3: IP Address

Understood the concept of IP addresses and their role in uniquely identifying devices in a network. Learned the difference between public and private IP addresses and their importance in communication.

---

## Task 4: Ports

Learned how ports are used to establish communication between applications and network services. Studied commonly used ports such as HTTP (80) and HTTPS (443).

---

## Task 5: Packets and Frames

Studied how data is divided into packets and transmitted across networks. Understood the role of frames in data link layer communication and how encapsulation helps in reliable data transfer.

---

## Task 6: Networking Devices

Explored various networking devices including routers, switches, hubs, modems, and access points. Understood their functions and importance in establishing and managing network communication.

---

## Task 7: DNS

Studied the Domain Name System (DNS) and understood how domain names are translated into IP addresses. Learned how DNS makes it possible to access network services using human-readable names instead of numerical IP addresses.

---

## Task 8: DHCP

Learned how DHCP automatically provides devices with essential network configuration such as IP address, subnet mask, default gateway, and DNS server. Studied the DORA process - Discover, Offer, Request, and Acknowledge, and how devices obtain and renew IP addresses.

---

## Task 9: ICMP

Studied ICMP and its role in network diagnostics and error reporting. Learned how ping uses ICMP Echo Request/Reply messages to test connectivity and how traceroute uses TTL and ICMP responses to identify network hops.

---

## Task 10: HTTP(S)

Explored HTTP and HTTPS and how browsers communicate with web servers. Learned how HTTPS uses SSL/TLS to secure communication and examined HTTP requests, status codes, and TLS certificate information using browser Developer Tools.

---

## Task 11: Protocols: Other Important Models

Studied the OSI model and its seven layers, along with the roles of TCP, UDP, and IP in network communication. Understood how data is encapsulated through the layers, from application data to segments, packets, frames, and finally transmitted bits.

---

## Task 12: Introduction to Windows

Explored the Windows operating system and its basic administration features. Learned about file organization, Windows Updates, application installation and removal, system settings, and using Task Manager to monitor processes and system resources.

---

## Task 13: Windows PowerShell

Studied PowerShell as a command-line shell and scripting environment for system administration and automation. Learned how PowerShell works with objects rather than plain text, its relationship with the .NET framework, and the evolution from Windows PowerShell to the cross-platform PowerShell Core.

---

## Task 14: PowerShell vs CMD

Compared Windows Command Prompt and PowerShell in terms of functionality, scripting, automation, and system administration. Learned how PowerShell provides more advanced capabilities through cmdlets, object-based data handling, and remote administration.

---

## Task 15: Windows System32

Explored the Windows directory structure and the purpose of environment variables such as %windir%. Learned about the System32 directory and its role in storing critical Windows system files and utilities.

---

## Task 16: Windows User Accounts & UAC

Learned about Administrator and Standard User accounts and how their privileges differ. Explored Windows user profiles, the C:\Users directory, local user and group management, and the role of permissions in controlling system access.

---

## Task 17: Windows Security

Studied Windows' built-in security features, including virus and threat protection, application and browser protection, and device security. Also learned how the Windows Firewall controls network traffic and the differences between Domain, Private, and Public network profiles.

---

## Task 18: Introduction to Linux

Introduced Linux and its use across servers, automotive systems, retail infrastructure, and other systems requiring reliability and efficiency. Learned about Linux distributions such as Ubuntu and Debian and the flexibility provided by its open-source nature.

---

## Task 19: Linux File Systems

Learned fundamental Linux file and directory management commands including touch, mkdir, cp, mv, rm, and file. Practiced creating, copying, moving, renaming, deleting, and identifying files and directories using the command line.

---

## Task 20: Cryptography - Part 1

Studied the fundamentals of cryptography and its role in maintaining confidentiality, integrity, and authenticity. Learned the relationship between plaintext, ciphertext, ciphers, keys, encryption, and decryption, along with the importance of cryptography in secure digital communication.

---

## Task 21: Cryptography - Part 2

Studied symmetric and asymmetric encryption, including AES, RSA, 3DES and ECC. Learned about shared keys, public/private keys, and the mathematical problems underlying asymmetric encryption.

---

## Task 22: Cipher Breaker Challenge

Studied classical ciphers including **Caesar, Vigenère and substitution ciphers**. Built a Python script supporting Caesar shift 13, Vigenère with the key `MARVEL`, and the substitution mapping `A→D, B→E`.

### Cipher Concepts

Caesar encryption uses `C = (P + K) mod 26`, where `P` is the plaintext value, `K` is the shift, and `C` is the ciphertext value. Vigenère uses changing shifts based on a repeating keyword, making simple brute-force attacks harder than Caesar. For `CYBERSECURITY` with key `KEY`, the ciphertext is `MCZOVQOGSBMRI`.

The MARVEL challenge used the ciphertext `HIQR{QRCPBAvat_ZNXRAG}` with ROT13.

[🔗 View Python File](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Caesar-Cipher.py)

---

## Task 23: CyberSecurity Principles - CIA

Introduced the **CIA Triad**:

* **Confidentiality:** Prevents unauthorized access.
* **Integrity:** Prevents unauthorized modification.
* **Availability:** Ensures access when required.

---

## Task 24: CIA Triad - Explanation

Explored real-world examples of Confidentiality, Integrity and Availability and understood how encryption, access controls, and reliable infrastructure help protect these principles.

---

## Task 25: Red Teaming

Introduced offensive security and ethical hacking. Learned how penetration testing proactively identifies vulnerabilities by testing systems from an attacker's perspective within an authorized scope.

---

## Task 26: Red Teaming - Practical

Learned key concepts including red teaming, penetration testing, vulnerabilities, exploits and scope. Practised basic web enumeration by checking potential hidden paths and learned how **Gobuster** can automate directory discovery.

---

## Room Completion Screenshot

![Room Completion](https://github.com/SilverSquare-22/CLCY-Report-Level-1/blob/main/Room-Completed.png)

