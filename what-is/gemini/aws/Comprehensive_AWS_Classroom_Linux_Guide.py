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
