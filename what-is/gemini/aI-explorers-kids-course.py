import os
import zipfile

# Create directory structure for the repo
repo_name = "AI-Explorers-Kids-Course"
os.makedirs(repo_name, exist_ok=True)
os.makedirs(f"{repo_name}/lessons", exist_ok=True)
os.makedirs(f"{repo_name}/infrastructure", exist_ok=True)

# 1. README.md
readme_content = """# 🚀 AI Explorers: A Python Journey for Kids

Welcome to the **AI Explorers** repository! As an AI, I helped structure this course to teach children (ages 10 and up) the fundamental concepts of Artificial Intelligence. By transitioning from basic rule-based programming to understanding how modern AI reasons and acts, students gain hands-on experience using Python in a secure, containerized lab environment.

## Course Overview

Our curriculum demystifies AI by mapping its historical evolution to how kids naturally learn. We move step-by-step from giving explicit computer instructions to exploring data-driven learning, neural networks, and finally, the ethical considerations of future Artificial General Intelligence (AGI).

## The 7-Stage Learning Journey

| Stage | Core Concept | Python Activity |
| :--- | :--- | :--- |
| **1. Rules** | Classic symbolic AI and manual coding. | `if/else` logic and decision trees. |
| **2. Learning** | Predictive ML and finding data patterns. | Charting CSV data with `pandas` & `matplotlib`. |
| **3. Neural Networks** | How computer "brains" process inputs. | Arrays and weight/bias calculations. |
| **4. Creating** | Generative AI and predicting the next element. | Text generation (LLM simulation). |
| **5. Reasoning** | Chain-of-thought and complex problem solving. | Step-by-step logical AI prompting. |
| **6. Acting** | Agentic AI, physical robotics, and tool use. | Sensor loops and autonomous decision scripts. |
| **7. The Future** | AGI, ethics, bias, and human alignment. | Analyzing biased datasets and classroom debate. |

## Tech Stack & Architecture

This course relies on a centralized Linux server infrastructure to ensure a frictionless experience for students in a classroom setting:

*   **Podman:** Runs isolated, rootless containers for every student, ensuring host system safety and identical environments.
*   **JupyterLab:** Provides a web-based, interactive Python environment requiring zero local installation on student laptops.
*   **Nginx Reverse Proxy:** Routes readable URLs (e.g., `student1.lab.local`) to specific student containers using WebSockets.
*   **Python 3.11:** The core programming language, utilizing standard data science libraries for hands-on activities.

## Getting Started

To deploy this classroom environment on your central Linux server:

1. Clone this repository to your Linux host machine.
2. Review the `infrastructure/Containerfile` and execute the `deploy_students.sh` script to provision memory-capped student containers.
3. Configure your Nginx proxy using the provided `ai_classroom.conf` template.

> **Note:** Ensure your local network DNS router points the `.lab.local` wildcard to your server's IP address so students can access their workspaces.
"""
with open(f"{repo_name}/README.md", "w") as f:
    f.write(readme_content)

# 2. Infrastructure Files
containerfile_content = """FROM python:3.11-slim
WORKDIR /workspace
RUN pip install --no-cache-dir jupyterlab pandas matplotlib
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
"""
with open(f"{repo_name}/infrastructure/Containerfile", "w") as f:
    f.write(containerfile_content)

deploy_script = """#!/bin/bash
IMAGE_NAME="ai-kids-lab"
podman build -t $IMAGE_NAME .
for i in {1..10}; do
  PORT=$((8000 + i))
  STUDENT_ID=$(printf "%02d" $i)
  mkdir -p ./student_data/student_${STUDENT_ID}
  podman run -d --name student_${STUDENT_ID} -p 127.0.0.1:${PORT}:8888 -v ./student_data/student_${STUDENT_ID}:/workspace:Z --memory 512m --cpus 1.0 $IMAGE_NAME jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token="learn${STUDENT_ID}"
done
echo "Deployment complete! 10 student instances running on ports 8001-8010."
"""
with open(f"{repo_name}/infrastructure/deploy_students.sh", "w") as f:
    f.write(deploy_script)

nginx_conf = """server {
    listen 80;
    server_name ~^student(?<id>\\d+)\\.lab\\.local$;
    location / {
        proxy_pass http://127.0.0.1:80$id;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 86400;
    }
}
"""
with open(f"{repo_name}/infrastructure/ai_classroom.conf", "w") as f:
    f.write(nginx_conf)

# 3. Lesson Files (Jupyter Notebook equivalents saved as .py scripts for ease)

lesson1 = """# Stage 1: Rules - Classical Programming
def tic_tac_toe_bot(board):
    if "center" == "empty":
        return "Play center"
    elif "corner" == "empty":
        return "Play corner"
    else:
        return "Play any open space"

print("Bot Action:", tic_tac_toe_bot("empty_center"))
"""
with open(f"{repo_name}/lessons/1_Rules.py", "w") as f:
    f.write(lesson1)

lesson2 = """# Stage 2: Learning - Predictive AI
import pandas as pd
import matplotlib.pyplot as plt

data = {'temperature': [15, 18, 20, 22, 25, 28, 30], 'sales': [10, 25, 40, 55, 75, 90, 110]}
df = pd.DataFrame(data)

plt.scatter(df['temperature'], df['sales'], color='orange')
plt.title("AI Data Analysis: Temperature vs. Sales")
plt.xlabel("Temperature (C)")
plt.ylabel("Ice Creams Sold")
# plt.show() # Uncomment to view in Jupyter
print(df)
"""
with open(f"{repo_name}/lessons/2_Learning.py", "w") as f:
    f.write(lesson2)

lesson3 = """# Stage 3: Neural Networks - Basic Concept
def simple_neuron(inputs, weights):
    # A tiny simulation of a brain cell processing clues
    total_signal = sum(i * w for i, w in zip(inputs, weights))
    if total_signal > 10: # Threshold to "fire"
        return "Neuron Fired! Pattern Detected."
    return "Neuron Quiet."

print(simple_neuron([2, 5, 1], [1, 2, 0.5]))
"""
with open(f"{repo_name}/lessons/3_Neural_Networks.py", "w") as f:
    f.write(lesson3)

lesson4 = """# Stage 4: Creating - Generative AI
import random

dictionary = {"robot": ["built a rocket", "learned to paint"], "dragon": ["flew to Mars", "baked a cake"]}

def generate_story(subject):
    if subject in dictionary:
        action = random.choice(dictionary[subject])
        return f"Generative AI Story: Once upon a time, a {subject} {action}!"
    return "Please give me 'robot' or 'dragon'!"

print(generate_story("robot"))
"""
with open(f"{repo_name}/lessons/4_Creating.py", "w") as f:
    f.write(lesson4)

lesson5 = """# Stage 5: Reasoning - Chain of Thought Simulation
def reasoning_ai(math_problem):
    print("AI is reasoning step-by-step...")
    print("Step 1: Analyzing the problem: 5 + 3 * 2")
    print("Step 2: Remembering order of operations (multiply first).")
    print("Step 3: Calculating 3 * 2 = 6")
    print("Step 4: Calculating 5 + 6 = 11")
    return "Final Answer: 11"

print(reasoning_ai("5 + 3 * 2"))
"""
with open(f"{repo_name}/lessons/5_Reasoning.py", "w") as f:
    f.write(lesson5)

lesson6 = """# Stage 6: Acting - Autonomous Agents
def robot_agent(sensor_inputs):
    distance = sensor_inputs["front_sensor_meters"]
    battery = sensor_inputs["battery_percent"]
    
    if battery < 10:
        return "CRITICAL ACTION: Rerouting to Charging Station."
    elif distance < 2.0:
        return f"EMERGENCY ACTION: Obstacle detected at {distance}m! Applying Brakes."
    else:
        return "ROUTINE ACTION: Path clear. Accelerating safely."

car_status = {"front_sensor_meters": 1.2, "battery_percent": 85}
print(robot_agent(car_status))
"""
with open(f"{repo_name}/lessons/6_Acting.py", "w") as f:
    f.write(lesson6)

lesson7 = """# Stage 7: The Future - AGI & Ethics
def check_ai_capability(task_type):
    narrow_tasks = ["play_chess", "detect_objects"]
    
    if task_type in narrow_tasks:
        return f"Narrow AI: I can do '{task_type}' perfectly!"
    else:
        return f"AGI Concept: Handling '{task_type}' requires human-level general reasoning."

print(check_ai_capability("play_chess"))
print(check_ai_capability("cook_dinner_while_telling_jokes"))
"""
with open(f"{repo_name}/lessons/7_The_Future.py", "w") as f:
    f.write(lesson7)

# Zip the repository directory
zip_filename = "AI-Explorers-Kids-Course.zip"
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(repo_name):
        for file in files:
            zipf.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(repo_name, '..')))

print(f"Created zip archive: {zip_filename}")
