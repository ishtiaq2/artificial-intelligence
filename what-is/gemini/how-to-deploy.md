```python
import os

file_name = "AWS_Classroom_Deployment_Guide.md"

md_content = """# ☁️ AWS Free Tier Deployment Guide: AI Classroom

Deploying your AI classroom on AWS for free is a great way to make it accessible from anywhere. We will use the **AWS EC2 Free Tier (t2.micro)**. 

⚠️ **Crucial Note on Free Tier RAM:** The free t2.micro instance only has 1GB of RAM. Running 10 JupyterLab containers will crash it unless we add "Swap space" (virtual memory on the hard drive). This guide includes that critical step!

## Step 1: Launch the AWS EC2 Instance
1. Log into your AWS Console and go to **EC2**.
2. Click **Launch Instance**.
3. **Name:** `AI-Classroom-Server`
4. **OS Image:** Select **Ubuntu Server 24.04 LTS** (Free tier eligible).
5. **Instance Type:** `t2.micro` (or `t3.micro`).
6. **Key Pair:** Create a new key pair (e.g., `ai-key.pem`) and download it. You need this to log in!
7. **Network Settings:** Check the boxes for **Allow SSH traffic**, **Allow HTTP traffic**, and **Allow HTTPS traffic**.
8. **Storage:** Increase the free storage from 8GB to **20GB**.
9. Click **Launch**.

## Step 2: Connect and Prepare the Server
Once the instance is running, copy its **Public IPv4 address**. Connect via SSH using your terminal:
`ssh -i ai-key.pem ubuntu@<YOUR_PUBLIC_IP>`

### Add Swap Memory (Prevents crashing!)
Run these commands to add 4GB of virtual memory:
```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

```

### Install Podman and Nginx

```bash
sudo apt update -y
sudo apt install -y podman nginx

```

## Step 3: Deploy the Classroom

1. Upload your `infrastructure` folder to the server (you can use `git clone` if you uploaded it to GitHub).
2. Navigate to the folder: `cd infrastructure`
3. Make the script executable: `chmod +x deploy_students.sh`
4. Run it: `./deploy_students.sh`

## Step 4: The Public DNS Trick (nip.io)

Since you are on the public internet, `*.lab.local` won't work automatically for your students. Instead, use a free wildcard DNS service like `nip.io`.

Edit your Nginx config (`sudo nano /etc/nginx/conf.d/ai_classroom.conf`):

```nginx
server {
    listen 80;
    # Replace YOUR_PUBLIC_IP with your actual AWS IP address (e.g., 54.12.34.56)
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

Save, exit, and restart Nginx: `sudo systemctl restart nginx`

## Step 5: Students Log In

Your students can now access their labs from any computer using this URL format:

* **Student 1:** `http://student1.<YOUR_PUBLIC_IP>.nip.io` (Password: `learn01`)
* **Student 2:** `http://student2.<YOUR_PUBLIC_IP>.nip.io` (Password: `learn02`)
"""

with open(file_name, "w") as f:
f.write(md_content)

```

Here is the step-by-step guide you requested for deploying your classroom on AWS for free!

[Download the AWS_Classroom_Deployment_Guide.md](code-generated-file-80a88b2b-1202-4f40-9266-5c69a7ab772e)

### Understanding the Free Tier Limitations

Hosting on AWS is an excellent idea so students can access their work from home, but the Free Tier has a specific hardware constraint we must address.

*   **The RAM Limit:** The free `t2.micro` instance only provides 1GB of RAM. Launching 10 JupyterLab containers simultaneously will overload the server and crash it.
*   **The Solution (Swap Space):** In the markdown guide, I included a critical step to create a "Swap file." This tells the Linux server to use a portion of the hard drive as emergency RAM, ensuring all 10 students can run their code without crashing the host.

### The Domain Name Trick

Because your server will now be on the public internet, the local network `*.lab.local` routing we discussed earlier will not work. 

*   **Using nip.io:** Instead of buying a domain name, the guide teaches you how to use `nip.io`, a free, zero-configuration DNS tool. 
*   **How it works:** If your AWS server's IP is `54.12.34.56`, Nginx will automatically route `[http://student1.54.12.34.56.nip.io](http://student1.54.12.34.56.nip.io)` directly to Student 1's container. No extra setup is required!

---

Are you familiar with using SSH keys to connect to remote Linux servers, or would you like a quick crash course on how to log into your new AWS instance once you launch it?

```
