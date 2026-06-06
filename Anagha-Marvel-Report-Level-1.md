# Cloud Computing


## 1: Working with Git and GitHub basics (Task 1)


In this task, Git and GitHub workflows were practiced to understand collaborative software development. Actions such as editing, staging, committing, pushing, along with creation of branches and pull requests were performed.


### Understanding Version Control and Distributed Repositories

Version control helps track changes in source code over time. Git is a distributed version control system that allows multiple developers to work collaboratively on the same project.

### Commands Used


```
git init
git status
git add .
git commit -m "commit message"
git remote add origin <repo-link>
git push -u origin main
```


### Screenshots

![SS1](GitBash-SS-1.png)
![SS2](GitBash-SS-2.png)

---

### Solving Merge Conflicts using Git Rebase

Git rebase helps integrate changes from one branch into another while maintaining a cleaner commit history.

### Commands Used

```
git rebase main
git rebase --continue
```

### Screenshot

![SS5](GitBash-SS-5.png)
![SS6](GitBash-SS-6.png)
![SS7](GitBash-SS-7.png)

---

### Creating and Managing Branches

Branches are used to develop features independently without affecting the main branch.

### Commands Used

```
git checkout -b feature-branch
git branch
```

### Screenshot

![SS3](GitBash-SS-3.png)
![SS4](GitBash-SS-4.png)

---

### Open Source Contribution

An open-source repository was explored and contributions were made through commits and pull requests.


### Screenshot

![GSS1](GitHub-SS-1.png)
![GSS2](GitHub-SS-2.png)

---

### Using Git Revert and Git Cherry-Pick

Git revert is used to undo commits safely, while git cherry-pick applies selected commits from one branch to another.

### Commands Used

```
git revert <commit-id>
git cherry-pick <commit-id>
```

### Screenshot

![SS9](GitBash-SS-9.png)
![SS10](GitBash-SS-10.png)

---

### Customized Git Workflow using Git Config

Git config allows customisation of user identity and workflow settings. It can also be used to view the details, if already set.

### Commands Used

```
git config --global user.name
git config --global user.email
```

### Screenshot

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

### Commands Used

```
docker pull nginx
docker images
```

### Screenshot

![DSS1](Docker-1.png)

---

### Running Containers using Docker CLI

An nginx container was created and executed locally using Docker CLI commands. Port mapping was used to access the application through the browser.

### Commands Used

```
docker run -d --name mynginx -p 8080:80 nginx
docker ps
```

### Screenshot

![DSS2](Docker-2.jpg)

---

### Viewing Logs and Inspecting Container State

Docker logs and inspect commands were used to monitor container activity and understand container status information.

### Commands Used

```
docker logs mynginx --tail 5
docker inspect mynginx --format='Status: {{.State.Status}}'
```

### Screenshot

![DSS3](Docker-3.png)

---

### Managing Container Lifecycle

Container lifecycle operations such as restart, stop, and remove were performed successfully.

### Commands Used

```
docker restart mynginx
docker stop mynginx
docker rm mynginx
docker rmi nginx
```

### Screenshot

![DSS4](Docker-4.jpg)
![DSS5](Docker-5.jpg)
![DSS6](Docker-6.png)

---

## 3: Dockerizing a Simple Application (Task 3)


A simple static website was containerized using Docker. A Dockerfile was created using the nginx base image. The HTML file was copied into the nginx web server directory using the COPY instruction.


### Dockerfile

FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html


### Commands Used

1. docker build -t mywebsite .
2. docker run -d --name website-container -p 8080:80 mywebsite
3. docker ps
4. docker rm -f website-container
5. docker rmi mywebsite

### Screenshots

![DFSS1](Dockerfile-1.png)
![DFSS2](Dockerfile-2.jpg)

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