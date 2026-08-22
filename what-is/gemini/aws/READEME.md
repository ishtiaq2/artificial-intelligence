```python
import os

file_name = "Comprehensive_AWS_Classroom_Linux_Guide.md"

md_content = """# 🚀 The Complete AWS AI Classroom Deployment Guide (Linux to Linux)

This comprehensive guide will walk you through setting up an AWS EC2 instance from scratch, securely connecting to it from your local Linux machine, and deploying your containerized AI classroom.

---

## Phase 1: AWS Setup & Launching the Instance

1. **Log in to AWS:** Go to the [AWS Management Console](https://console.aws.amazon.com/) and search for **EC2**.
2. **Launch Instance:** Click the orange **Launch instance** button [cite: 2].
3. **Name your Server:** Under "Name and tags," enter a name like `AI-Classroom-Server` [cite: 2].
4. **Choose the OS:** Under "Application and OS Images (Amazon Machine Image)," select **Ubuntu** [cite: 2]. Ensure the version selected is the **Ubuntu Server 24.04 LTS** (Free tier eligible) [cite: 2, 4].
5. **Select Instance Type:** Choose **t2.micro** (or t3.micro depending on your region). This is eligible for the AWS Free Tier and provides 1 vCPU and 1 GB of RAM [cite: 2, 4].
6. **Create a Key Pair:** 
    * Under "Key pair (login)", click **Create new key pair** [cite: 2].
    * Name it something like `ai-classroom-key`.
    * Choose **RSA** and **.pem** format.
    * Click Create. Your browser will download the `.pem` file. **Keep this safe; it is the only way into your server!** [cite: 2]
7. **Network Settings (Security Group):**
    * Check **Allow SSH traffic from** and set it to **Anywhere (0.0.0.0/0)** or your specific IP [cite: 2].
    * Check **Allow HTTP traffic from the internet**.
8. **Configure Storage:** Increase the default 8GB storage to **20GB** [cite: 2]. (You get up to 30GB free on the Free Tier).
9. **Launch:** Click the **Launch instance** button [cite: 2]. Wait a minute for the instance state to change to "Running" [cite: 2].

---

## Phase 2: Connecting from Your Local Linux Machine (Crash Course)

To connect to your new server, you need its **Public IPv4 address**, which you can find by clicking on your instance in the EC2 Dashboard.

### Step 1: Secure the Key Pair
AWS enforces strict security on SSH keys. If your downloaded `.pem` file is readable by other users on your local machine, the connection will be rejected. 
Open your local Linux terminal and run:
```bash
# Navigate to where the key was downloaded (usually Downloads)
cd ~/Downloads

# Restrict permissions so only YOU can read it
chmod 400 ai-classroom-key.pem

```

### Step 2: SSH into the Server

Use the `ssh` command, specifying the identity file (`-i`) and the default Ubuntu user (`ubuntu`).

```bash
ssh -i ai-classroom-key.pem ubuntu@<YOUR_PUBLIC_IP>

```

*When prompted with `The authenticity of host ... can't be established`, type **yes** and press Enter [cite: 1, 5].*
You are now logged into your remote AWS server!

---

## Phase 3: Preparing the Server Environment

Because the Free Tier `t2.micro` only has 1GB of RAM, we must add "Swap memory" (virtual RAM on the hard drive) so our 10 Podman containers don't crash the server.

### 1. Add Swap Space

Run these commands one by one on your AWS server:

```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

```

### 2. Install Podman and Nginx

Update the server and install the necessary routing and container tools:

```bash
sudo apt update -y
sudo apt install -y podman nginx

```

---

## Phase 4: Deploying the AI Classroom

### 1. Transfer or Recreate the Deployment Files

On your AWS server, recreate your infrastructure folder.

```bash
mkdir -p ~/ai-classroom/infrastructure
cd ~/ai-classroom/infrastructure

```

*(Note: You can use `nano Containerfile` and `nano deploy_students.sh` to paste in the code from our previous steps, or use `git clone` if you uploaded your files to GitHub).*

### 2. Execute the Deployment

Make the script executable and run it to spin up the 10 student labs:

```bash
chmod +x deploy_students.sh
./deploy_students.sh

```

---

## Phase 5: Nginx Routing (The nip.io Trick)

Since you don't have a custom domain name, we will use a free dynamic DNS service called `nip.io` to route traffic to the students.

1. Open the Nginx configuration file:

```bash
sudo nano /etc/nginx/conf.d/ai_classroom.conf

```

2. Paste the following configuration, replacing `YOUR_PUBLIC_IP` with your actual EC2 IPv4 address (e.g., `54.12.34.56`):

```nginx
server {
    listen 80;
    server_name ~^student(?<id>\\d+)\\.YOUR_PUBLIC_IP\\.nip\\.io$;

    location / {
        proxy_pass [http://127.0.0.1:80](http://127.0.0.1:80)$id;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 86400;
    }
}

```

3. Save the file (`Ctrl+O`, `Enter`, `Ctrl+X`) and restart Nginx:

```bash
sudo systemctl restart nginx

```

---

## 🏁 Classroom is Ready!

Your students can now access their environments from any browser in the world:

* **Student 1 URL:** `http://student1.<YOUR_PUBLIC_IP>.nip.io`
* **Student 1 Password:** `learn01`
"""

with open(file_name, "w") as f:
f.write(md_content)

```

I have generated a new, completely comprehensive step-by-step guide tailored for your Linux-based setup, covering everything from the very first click in AWS to having your students log in.

[Download the Comprehensive_AWS_Classroom_Linux_Guide.md](code-generated-file-2623e28a-70f8-4669-9a5d-f51a86bc65ff)

### Quick Summary of the SSH Crash Course
Connecting to AWS from a Linux terminal relies heavily on correct file permissions. If your key file (`.pem`) is too exposed, the connection will fail for security reasons.

Here is the basic flow once your AWS instance is running:
1.  **Download the key:** When you launch the instance, you download a `.pem` file. Keep it in a secure folder like `~/Downloads`.
2.  **Fix Permissions:** Run `chmod 400 your-key.pem` to ensure only you can read it.
3.  **Connect:** Run `ssh -i your-key.pem ubuntu@<your-aws-ip>`.
4.  **Confirm:** Type `yes` when asked about the host authenticity[cite: 1].

> **Helpful Visual Resource:** If you want to see this exact SSH process demonstrated visually, I highly recommend checking out this excellent tutorial video on YouTube: [How to Create Ubuntu 24.0.4 EC2 in AWS Cloud | How to connect to EC2 Instance from local machine?](https://www.youtube.com/watch?v=sDb8W7CtikQ)

By adding the **Swap Memory** step included in the `.md` file, your Free Tier instance will be more than capable of hosting all 10 Podman containers securely.

Is there anything else you need to configure before you start teaching this amazing AI course?
http://googleusercontent.com/youtube_content/1

```
