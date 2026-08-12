# Cloud Computing


## 1: Working with Git and GitHub basics (Task 1)


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

![SS1](GitBash-SS-1.png)
![SS2](GitBash-SS-2.png)

---

### Solving Merge Conflicts using Git Rebase

Git rebase helps integrate changes from one branch into another while maintaining a cleaner commit history.

**Commands Used:**

```
git rebase main
git rebase --continue
```

**Screenshots:**

![SS5](GitBash-SS-5.png)
![SS6](GitBash-SS-6.png)
![SS7](GitBash-SS-7.png)

---

### Creating and Managing Branches

Branches are used to develop features independently without affecting the main branch.

**Commands Used:

```
git checkout -b feature-branch
git branch
```

**Screenshots:**

![SS3](GitBash-SS-3.png)
![SS4](GitBash-SS-4.png)

---

### Open Source Contribution

An open-source repository was explored and contributions were made through commits and pull requests.


**Screenshots:**

![GSS1](GitHub-SS-1.png)
![GSS2](GitHub-SS-2.png)

---

### Using Git Revert and Git Cherry-Pick

Git revert is used to undo commits safely, while git cherry-pick applies selected commits from one branch to another.

**Commands Used:**

```
git revert <commit-id>
git cherry-pick <commit-id>
```

**Screenshots:**

![SS9](GitBash-SS-9.png)
![SS10](GitBash-SS-10.png)

---

### Customized Git Workflow using Git Config

Git config allows customisation of user identity and workflow settings. It can also be used to view the details, if already set.

**Commands Used:**

```
git config --global user.name
git config --global user.email
```

**Screenshots:**

![SS11](GitBash-SS-11.png)

---

## 2: Exploring Docker Fundamentals (Task 2)


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

![DSS1](Docker-1.png)

---

### Running Containers using Docker CLI

An nginx container was created and executed locally using Docker CLI commands. Port mapping was used to access the application through the browser.

**Commands Used:**

```
docker run -d --name mynginx -p 8080:80 nginx
docker ps
```

**Screenshots:**

![DSS2](Docker-2.jpg)

---

### Viewing Logs and Inspecting Container State

Docker logs and inspect commands were used to monitor container activity and understand container status information.

**Commands Used:**

```
docker logs mynginx --tail 5
docker inspect mynginx --format='Status: {{.State.Status}}'
```

Screenshot:

![DSS3](Docker-3.png)

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

Screenshots:

![DSS4](Docker-4.jpg)
![DSS5](Docker-5.jpg)
![DSS6](Docker-6.png)

---

## 3: Dockerizing a Simple Application (Task 3)


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

![DFSS1](Dockerfile-1.png)
![DFSS2](Dockerfile-2.jpg)

---

## 4: Kubernetes Basics and Writing Pod Specs (Task 5)


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

![K8S1](Kubernetes-1.png)
![K8S2](Kubernetes-2.png)
![K8S3](Kubernetes-3.png)

---

## 5: Deploying a Containerised Application on Kubernetes (Task 7)


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

![K8SD1](Kubernetes-Deploy-1.png)
![K8SD2](Kubernetes-Deploy-2.png)
![K8SD3](Kubernetes-Deploy-3.png)
![K8SD4](Kubernetes-Deploy-4.png)

---

# Cybersecurity


## 1: Introduction to Computer Networking (Task 1)

Studied the fundamentals of computer networking and understood how computers and devices communicate with each other through connected networks. Learned about the importance of communication protocols and data sharing in modern networks.

---

## 2: Internet (Task 2)

Explored the working of the Internet and understood how global communication takes place between interconnected devices. Learned about web communication, protocols, and Internet-based services.

---

## 3: IP Address (Task 3)

Understood the concept of IP addresses and their role in uniquely identifying devices in a network. Learned the difference between public and private IP addresses and their importance in communication.

---

## 4: Ports (Task 4)

Learned how ports are used to establish communication between applications and network services. Studied commonly used ports such as HTTP (80) and HTTPS (443).

---

## 5: Packets and Frames (Task 5)

Studied how data is divided into packets and transmitted across networks. Understood the role of frames in data link layer communication and how encapsulation helps in reliable data transfer.

---

## 6: Networking Devices (Task 6)

Explored various networking devices including routers, switches, hubs, modems, and access points. Understood their functions and importance in establishing and managing network communication.

---

## 7: DNS (Task 7)

Studied the Domain Name System (DNS) and understood how domain names are translated into IP addresses. Learned how DNS makes it possible to access network services using human-readable names instead of numerical IP addresses.

---

## 8: DHCP (Task 8)

Learned how DHCP automatically provides devices with essential network configuration such as IP address, subnet mask, default gateway, and DNS server. Studied the DORA process - Discover, Offer, Request, and Acknowledge, and how devices obtain and renew IP addresses.

---

## 9: ICMP (Task 9)

Studied ICMP and its role in network diagnostics and error reporting. Learned how ping uses ICMP Echo Request/Reply messages to test connectivity and how traceroute uses TTL and ICMP responses to identify network hops.

---

## 10: HTTP(S) (Task 10)

Explored HTTP and HTTPS and how browsers communicate with web servers. Learned how HTTPS uses SSL/TLS to secure communication and examined HTTP requests, status codes, and TLS certificate information using browser Developer Tools.

---

## 11: Protocols: Other Important Models (Task 11)

Studied the OSI model and its seven layers, along with the roles of TCP, UDP, and IP in network communication. Understood how data is encapsulated through the layers, from application data to segments, packets, frames, and finally transmitted bits.

---

## 12: Introduction to Windows (Task 12)

Explored the Windows operating system and its basic administration features. Learned about file organization, Windows Updates, application installation and removal, system settings, and using Task Manager to monitor processes and system resources.

---

## 13: Windows PowerShell (Task 13)

Studied PowerShell as a command-line shell and scripting environment for system administration and automation. Learned how PowerShell works with objects rather than plain text, its relationship with the .NET framework, and the evolution from Windows PowerShell to the cross-platform PowerShell Core.

---

## 14: PowerShell vs CMD (Task 14)

Compared Windows Command Prompt and PowerShell in terms of functionality, scripting, automation, and system administration. Learned how PowerShell provides more advanced capabilities through cmdlets, object-based data handling, and remote administration.

---

## 15: Windows System32 (Task 15)

Explored the Windows directory structure and the purpose of environment variables such as %windir%. Learned about the System32 directory and its role in storing critical Windows system files and utilities.

---

## 16: Windows User Accounts & UAC (Task 16)

Learned about Administrator and Standard User accounts and how their privileges differ. Explored Windows user profiles, the C:\Users directory, local user and group management, and the role of permissions in controlling system access.

---

## 17: Windows Security (Task 17)

Studied Windows' built-in security features, including virus and threat protection, application and browser protection, and device security. Also learned how the Windows Firewall controls network traffic and the differences between Domain, Private, and Public network profiles.

---

## 18: Introduction to Linux (Task 18)

Introduced Linux and its use across servers, automotive systems, retail infrastructure, and other systems requiring reliability and efficiency. Learned about Linux distributions such as Ubuntu and Debian and the flexibility provided by its open-source nature.

---

## 19: Linux File Systems (Task 19)

Learned fundamental Linux file and directory management commands including touch, mkdir, cp, mv, rm, and file. Practiced creating, copying, moving, renaming, deleting, and identifying files and directories using the command line.

---

## 20: Cryptography - Part 1 (Task 20)

Studied the fundamentals of cryptography and its role in maintaining confidentiality, integrity, and authenticity. Learned the relationship between plaintext, ciphertext, ciphers, keys, encryption, and decryption, along with the importance of cryptography in secure digital communication.

---

## 21: Cryptography - Part 2 (Task 21)

Studied symmetric and asymmetric encryption, including AES, RSA, 3DES and ECC. Learned about shared keys, public/private keys, and the mathematical problems underlying asymmetric encryption.

---

## 22: CyberSecurity Principles - CIA (Task 23)

Introduced the **CIA Triad**:

* **Confidentiality:** Prevents unauthorized access.
* **Integrity:** Prevents unauthorized modification.
* **Availability:** Ensures access when required.

---

## 23: CIA Triad - Explanation (Task 24)

Explored real-world examples of Confidentiality, Integrity and Availability and understood how encryption, access controls, and reliable infrastructure help protect these principles.

---

## 24: Red Teaming (Task 25)

Introduced offensive security and ethical hacking. Learned how penetration testing proactively identifies vulnerabilities by testing systems from an attacker's perspective within an authorized scope.

---

## 25: Red Teaming - Practical (Task 26)

Learned key concepts including red teaming, penetration testing, vulnerabilities, exploits and scope. Practised basic web enumeration by checking potential hidden paths and learned how **Gobuster** can automate directory discovery.
