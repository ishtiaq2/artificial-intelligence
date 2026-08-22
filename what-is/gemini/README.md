Here is a teaching guide based on your handwritten outline. It breaks down the history and evolution of AI into structured modules designed for young learners.

---

## Module 1: Predictive Machine Learning & Generative AI

* **Predictive AI & Machine Learning:** Explain that classic ML acts like a pattern spotter. It looks at historical data to predict future outcomes (e.g., predicting rain or recommending movies).
* *Analogy:* Teaching a computer to distinguish apples from oranges by showing it thousands of labeled pictures.


* **Generative AI & LLMs (2020+):** Move from predicting categories to *creating* original text and art by predicting the very next word or pixel.
* *Unplugged Activity:* Play "Next Word Story"—each student adds one logical word to complete a sentence, showing how Large Language Models (LLMs) generate text step-by-step.



---

## Module 2: Agentic AI & Chatbots

* **Agentic AI (2022+):** Differentiate between basic chatbots (answering simple questions) and **AI Agents** (systems that can plan, make decisions, and use tools to achieve a goal, like booking an appointment).
* *Hands-on Exercise:* Have kids write out step-by-step instructions (an algorithm) for a robot to make a peanut butter sandwich, highlighting how agents follow rules and handle unexpected errors.

---

## Module 3: Physical Robotics & Artificial General Intelligence (AGI)

* **Robots in the Physical World:** Explain how AI connects to physical sensors and motors for self-driving cars, drone delivery, and surgical assistants where high precision is critical.
* **Artificial General Intelligence (AGI):** Compare "Narrow AI" (doing one task, like playing chess) with AGI (a future concept where AI can reason, adapt, and learn across *any* domain like a human).
* *Discussion:* Host a lighthearted "Turing Test" debate: can a computer ever feel emotions, or is it just following code?

---

## Module 4: Hands-On Python Coding Starter

You can run this simple Python project with students using **Google Colab** or **Replit** to show how different AI concepts function in code:

```python
# Kids' Mini AI Classifier & Assistant Simulator

def mini_ai_agent(user_prompt):
    text = user_prompt.lower()
    
    # 1. Predictive ML Simulation (Rule-based classification)
    if "rain" in text or "temperature" in text:
        return "[Predictive AI]: Weather data indicates a 90% chance of rain!"
    
    # 2. Generative AI Simulation (Text Generation)
    elif "story" in text or "write" in text:
        return "[Generative AI]: Once upon a time, a friendly robot learned to paint the sky..."
    
    # 3. Physical Robotics Simulation
    elif "obstacle" in text or "drive" in text:
        return "[Robotics AI]: Sensor detected an object 2 meters ahead. Applying brakes!"
    
    # 4. AGI / Reasoning Simulation
    else:
        return "[AGI Goal]: Processing complex query... Learning human context to help you solve this!"

# Try calling the function
print(mini_ai_agent("Write me a short story"))
print(mini_ai_agent("There is an obstacle ahead while I drive"))

```

---

What target age group are you designing this course for, and would you like to focus more on block-based tools (like Scratch) or text-based coding (like Python)?

Python is an excellent choice for 10-year-olds because its syntax reads almost like plain English! Here is a structured, text-based coding guide that walks your students through your AI timeline.

## 1. Predictive Machine Learning

* **The Concept:** Explain that early AI learned to spot patterns in existing data to make predictions, much like a weather app forecasting rain based on historical cloud data.
* **Python Hands-on:** Teach kids how basic algorithms use thresholds to predict outcomes based on data inputs.

```python
def predict_success(study_hours):
    # The predictive model analyzes the data
    if study_hours > 5:
        return "Prediction: High chance of passing!"
    else:
        return "Prediction: Keep studying!"

print(predict_success(7))

```

## 2. Generative AI & Chatbots

* **The Concept:** Introduce the 2020 breakthrough of Large Language Models (LLMs). Explain that these models generate entirely new text by calculating the most likely next word, powering the chatbots we use today.
* **Python Hands-on:** Build a keyword-based chatbot to simulate how an assistant generates responses to specific prompts.

```python
import random

def generative_bot(user_input):
    ideas = ["a dragon who loves math.", "a robot exploring Mars."]
    if "story" in user_input.lower():
        return "Generated Story: Once there was " + random.choice(ideas)
    return "I am ready to chat!"

print(generative_bot("Tell me a story!"))

```

## 3. Agentic AI & Physical Robots

* **The Concept:** Discuss how Agentic AI (2022+) goes beyond chatting to make independent decisions and take actions. Explain how this same logic helps physical robots navigate self-driving cars or assist in precise surgeries.
* **Python Hands-on:** Code a simulation of a self-driving car's sensor system making autonomous decisions.

```python
def autonomous_car(sensor_data):
    # The AI agent takes action based on its environment
    if sensor_data == "obstacle":
        return "Agent Action: Brakes applied!"
    return "Agent Action: Driving forward safely."

print(autonomous_car("obstacle"))

```

## 4. Artificial General Intelligence (AGI)

* **The Concept:** Explain that AGI does not exist yet. It represents a future milestone where computers will be able to reason, learn, and adapt to completely new situations just as well as a human being.
* **Discussion Activity:** Have the students step away from the keyboards and debate whether an AGI could ever truly feel human emotions, or if it will always just be executing complex code.

---

Which Python environment (like Replit, Google Colab, or a local IDE) are you planning to use with your classroom?

Using **Podman** is a fantastic choice for teaching! Containerizing the setup isolates dependencies so every student gets a clean, identical environment without installation headaches.

For kids aged 10 and above, launching **JupyterLab** inside a Podman container gives them an interactive, visual Python sandbox right in their web browser.

---

## 1. Setup Guide: Podman Container Environment

Create a simple file named `Containerfile` (or `Dockerfile`) in your main teaching directory:

```dockerfile
FROM python:3.11-slim

# Set workspace directory inside container
WORKDIR /workspace

# Install JupyterLab for visual Python coding
RUN pip install --no-cache-dir jupyterlab pandas matplotlib

EXPOSE 8888

# Launch Jupyter without requiring a password token for classroom ease
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]

```

---

## 2. Classroom Execution Workflow

* **Build the image:** Run `podman build -t ai-kids-lab .` on student workstations or a shared lab machine.
* **Launch the container:** Execute `podman run -d -p 8888:8888 -v ./lessons:/workspace/lessons:Z --name ai_lab ai-kids-lab`. *(Note: The `:Z` flag ensures proper SELinux file permissions when mounting local folders in Podman).*
* **Access the interface:** Have students open `http://localhost:8888` in any browser to write and run Python interactively.

---

## 3. Hands-On Python Scripts for Students

Once inside JupyterLab, students can run these container-friendly code snippets for each module:

* **1. Predictive ML (Pattern Recognition):**
```python
def predict_weather(temp, humidity):
    return "Rain Likely 🌧️" if temp > 20 and humidity > 70 else "Clear Skies ☀️"

print("Prediction:", predict_weather(temp=25, humidity=85))

```


* **2. Generative AI (LLM Simulation):**
```python
import random
prompts = {"robot": ["paints a picture.", "dances with cats.", "learns Python."]}

def generate_story(subject):
    return f"The {subject} " + random.choice(prompts.get(subject, ["explores space."]))

print(generate_story("robot"))

```


* **3. Agentic AI & Robotics (Autonomous Decision Loop):**
```python
def robot_agent(sensor_data):
    if sensor_data["battery"] < 15:
        return "Action: Low battery. Navigating to charging station."
    elif sensor_data["obstacle_distance"] < 1.0:
        return "Action: Obstacle detected! Turning right 90 degrees."
    return "Action: Path clear. Moving forward."

print(robot_agent({"battery": 80, "obstacle_distance": 0.5}))

```


* **4. AGI Concept (Reasoning Challenge):**
```python
# Narrow AI vs. General AI demonstration
def narrow_calculator(task, a, b):
    if task == "add": return a + b
    return "Error: I am a narrow AI and only know math! I cannot write poems."

print(narrow_calculator("write_poem", 5, 3))

```



---

## 4. Teaching Tips for Podman Lessons

* **Instant Resets:** If a student accidentally corrupts code or environment files, simply execute `podman restart ai_lab` for an immediate clean state.
* **Rootless Execution:** Emphasize to students that Podman runs rootless by default, making it much safer for school networks than traditional container engines.

---

Will your students be running Podman locally on their individual lab computers, or will you host the containers on a central server for them to connect to?

Hosting from a central server simplifies classroom administration. The recommended deployment strategy creates **an isolated Podman container per student**. This prevents an infinite loop or code crash from one student impacting the rest of the class.

```
                  ┌─ Central Server (Podman Host) ──────────────┐
┌──────────┐      │  ┌──────────────────┐                       │
│ Student 1├─────►│  │ Container: st-01 │ Port 8001             │
└──────────┘      │  └──────────────────┘                       │
┌──────────┐      │  ┌──────────────────┐                       │
│ Student 2├─────►│  │ Container: st-02 │ Port 8002             │
└──────────┘      │  └──────────────────┘                       │
                  └─────────────────────────────────────────────┘

```

---

## Server Setup & Automation Script

Deploy a lightweight image and launch dedicated student workspaces automatically using a shell script on your server.

### 1. The Base Image (`Containerfile`)

Save this file on the server to build the basic student image:

```dockerfile
FROM python:3.11-slim
WORKDIR /workspace
RUN pip install --no-cache-dir jupyterlab pandas matplotlib
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

```

### 2. Student Provisioning Script (`deploy_lab.sh`)

Execute this script on the server to build the environment and assign isolated ports and password tokens to each student:

```bash
#!/bin/bash
IMAGE_NAME="ai-kids-lab"
podman build -t $IMAGE_NAME .

# Generate workspaces for 10 students
for i in {1..10}; do
  PORT=$((8000 + i))
  STUDENT_ID=$(printf "%02d" $i)
  
  # Create a persistent folder on the host for each student's work
  mkdir -p ./student_data/student_${STUDENT_ID}
  
  # Run isolated rootless container with resource constraints
  podman run -d \
    --name student_${STUDENT_ID} \
    -p ${PORT}:8888 \
    -v ./student_data/student_${STUDENT_ID}:/workspace:Z \
    --memory 512m \
    --cpus 1.0 \
    $IMAGE_NAME \
    jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token="learn${STUDENT_ID}"
done

echo "Classroom ready! Access student ports 8001 through 8010."

```

---

## Student Access & Operational Management

* **Classroom Access:** Provide each student with an assigned URL. Student 1 connects to `http://<SERVER-IP>:8001` using password token `learn01`, while Student 2 connects to `http://<SERVER-IP>:8002` with `learn02`.
* **Data Persistence:** Student files are saved locally on the host server under `./student_data/student_XX`, ensuring work persists across container restarts.
* **Server Protection:** Setting memory (`512m`) and CPU limits (`1.0`) prevents any runaway script from taking down the central host.

---

## Essential Administrator Commands

* **View student activity:** `podman ps`
* **Reset a single student container:** `podman restart student_03`
* **Stop all lab containers after class:** `podman stop $(podman ps -q --filter name=student_)`

---

Would you like help setting up a local domain reverse proxy (like Nginx) so students log in via readable addresses (e.g., `student1.lab.local`) instead of numeric ports?


Setting up readable URLs is a brilliant idea! It removes the friction of typing clunky IP addresses and ports, letting your students jump straight into learning AI concepts.

To achieve this, we will use **Nginx** as a reverse proxy. Nginx will listen for requests like `student1.lab.local` and seamlessly forward them to the correct Podman port (e.g., `8001`).

### 1. Local Network DNS Preparation

For custom `.local` domains to work, the students' computers must know where to find your server.

* **Central Router/DNS:** The easiest classroom method is to add a wildcard DNS record (`*.lab.local`) pointing to your server's IP address within your school's router or local DNS server (like Pi-hole).
* **Alternative (Hosts File):** If a local DNS server is unavailable, you can manually edit the `hosts` file on each student's computer to point `student1.lab.local` to the server's IP, though this is tedious for large classes.

### 2. Nginx Reverse Proxy Configuration

Since JupyterLab relies on WebSockets for its interactive Python terminal, the Nginx configuration must explicitly allow WebSocket upgrades.

Create a new configuration file on your server at `/etc/nginx/conf.d/jupyter_lab.conf` and paste this code:

```nginx
server {
    listen 80;
    # Uses a regular expression to capture the student ID number
    server_name ~^student(?<id>\d+)\.lab\.local$;

    location / {
        # Dynamically routes student1 to port 8001, student2 to 8002, etc.
        proxy_pass http://127.0.0.1:80$id;
        
        # Standard proxy headers
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        
        # Crucial for JupyterLab WebSockets (the Python kernel connection)
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 86400;
    }
}

```

### 3. Activating the Proxy

Once your configuration is saved, run the following commands on your server to test and activate Nginx:

* **Test the syntax:** `sudo nginx -t` (This ensures you have no typos).
* **Restart Nginx:** `sudo systemctl restart nginx`
* **Enable on boot:** `sudo systemctl enable nginx`

Now, when Student 5 types `[http://student5.lab.local](http://student5.lab.local)` into their browser, Nginx will automatically route them to their isolated Podman container on port `8005`.

---

Does your classroom use Windows, macOS, or Chromebooks to connect to this central server?

Here is your complete master guide for running your AI course on a Linux server using **Podman** containers, **Nginx**, and **Python**.

---

## 1. Infrastructure Setup on Linux Host

Run these setup scripts directly on your central Linux server.

### Step 1: Podman Container Template (`Containerfile`)

Create a file named `Containerfile` on your Linux host:

```dockerfile
FROM python:3.11-slim

WORKDIR /workspace

# Install essential libraries for kids' projects
RUN pip install --no-cache-dir jupyterlab pandas matplotlib

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

```

---

### Step 2: Deployment Script (`deploy_students.sh`)

Create and execute this shell script to spin up 10 student environments with resource limits and isolated data storage:

```bash
#!/bin/bash
IMAGE_NAME="ai-kids-lab"

# 1. Build the base container image
podman build -t $IMAGE_NAME .

# 2. Deploy isolated containers for students 1 through 10
for i in {1..10}; do
  PORT=$((8000 + i))
  STUDENT_ID=$(printf "%02d" $i)
  
  # Create persistent folder on Linux host for each student
  mkdir -p ./student_data/student_${STUDENT_ID}
  
  # Run rootless container with 512MB RAM and 1 CPU cap
  podman run -d \
    --name student_${STUDENT_ID} \
    -p 127.0.0.1:${PORT}:8888 \
    -v ./student_data/student_${STUDENT_ID}:/workspace:Z \
    --memory 512m \
    --cpus 1.0 \
    $IMAGE_NAME \
    jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token="learn${STUDENT_ID}"
done

echo "Deployment complete! 10 student instances running internally on ports 8001-8010."

```

---

### Step 3: Nginx Reverse Proxy Configuration

Create `/etc/nginx/conf.d/ai_classroom.conf` on your Linux server:

```nginx
server {
    listen 80;
    server_name ~^student(?<id>\d+)\.lab\.local$;

    location / {
        # Proxy request to student's local port (e.g., student1 -> port 8001)
        proxy_pass http://127.0.0.1:80$id;
        
        # WebSocket support essential for interactive Python kernels
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 86400;
    }
}

```

Reload Nginx: `sudo nginx -t && sudo systemctl reload nginx`

---

## 2. Classroom Curriculum & Python Projects

Students access their environment by navigating to `[http://student1.lab.local](http://student1.lab.local)` on their local network (logging in with password token `learn01`).

```
  ┌─────────────────────────────────────────────────────────────┐
  │                   AI History Timeline                       │
  │  Predictive ML  ►  Generative AI  ►  Agentic AI  ►   AGI    │
  │  (Data Patterns)   (Content Creation) (Autonomous) (Future) │
  └─────────────────────────────────────────────────────────────┘

```

---

### Lesson 1: Predictive Machine Learning (Pattern Recognition)

* **Theory:** Explain that classic machine learning looks at past numbers to make smart guesses about the future.
* **Hands-on Code (Jupyter Notebook):**

```python
# Predictive Weather Model Simulator
def predict_weather(temperature, humidity):
    # Rule-based pattern matching simulating a machine learning classifier
    if temperature > 22 and humidity > 70:
        return "Prediction: High chance of Rain 🌧️"
    elif temperature < 5:
        return "Prediction: High chance of Snow ❄️"
    else:
        return "Prediction: Clear Skies ☀️"

# Students test different data inputs
print(predict_weather(temperature=26, humidity=80))
print(predict_weather(temperature=2, humidity=40))

```

---

### Lesson 2: Generative AI & LLMs (Creation)

* **Theory:** Modern AI (2020+) generates original text, images, and audio by calculating the most logical next element.
* **Hands-on Code (Jupyter Notebook):**

```python
import random

# Large Language Model Simulation: Next-Word Generator
story_dictionary = {
    "robot": ["built a rocket", "learned to paint", "cooked spaghetti"],
    "dragon": ["played video games", "opened a bakery", "flew to Mars"]
}

def generate_text(prompt_subject):
    subject = prompt_subject.lower()
    if subject in story_dictionary:
        action = random.choice(story_dictionary[subject])
        return f"Generative AI Story: Once upon a time, a friendly {subject} {action}!"
    return "Generative AI: I need a prompt like 'robot' or 'dragon'!"

print(generate_text("robot"))

```

---

### Lesson 3: Agentic AI & Robotics (Autonomous Action)

* **Theory:** Agentic AI (2022+) acts independently to complete complex goals, like navigating self-driving cars or aiding surgical robots.
* **Hands-on Code (Jupyter Notebook):**

```python
# Self-Driving Car Sensor & Action Decision Loop
def autonomous_car_agent(sensor_inputs):
    distance_to_obstacle = sensor_inputs["front_sensor_meters"]
    battery_level = sensor_inputs["battery_percent"]
    
    # Priority decision logic
    if battery_level < 10:
        return "CRITICAL ACTION: Low Battery. Rerouting to Charging Station."
    elif distance_to_obstacle < 2.0:
        return f"EMERGENCY ACTION: Obstacle detected at {distance_to_obstacle}m! Applying Brakes."
    else:
        return "ROUTINE ACTION: Path clear. Accelerating safely."

# Test scenarios
car_status = {"front_sensor_meters": 1.2, "battery_percent": 85}
print(autonomous_car_agent(car_status))

```

---

### Lesson 4: Artificial General Intelligence (AGI)

* **Theory:** Discuss Narrow AI (tools that excel at one task) versus AGI (hypothetical systems that reason across any domain like a human).
* **Hands-on Code (Jupyter Notebook):**

```python
def check_ai_capability(task_type):
    # Narrow AI capabilities vs AGI concept
    narrow_tasks = ["play_chess", "translate_language", "detect_objects"]
    
    if task_type in narrow_tasks:
        return f"Narrow AI status: I can do '{task_type}' perfectly!"
    else:
        return f"AGI status: Handling '{task_type}' requires human-level general reasoning across multiple skills."

print(check_ai_capability("play_chess"))
print(check_ai_capability("cook_dinner_while_telling_jokes"))

```

---

## 3. Server Management Commands for the Teacher

* **View running student containers:** `podman ps`
* **Monitor real-time server RAM/CPU usage:** `podman stats`
* **Reset a stuck student workspace:** `podman restart student_03`
* **Stop all student containers at the end of class:** `podman stop $(podman ps -q --filter name=student_)`

---

Would you like to include an interactive visual library like `matplotlib` in the curriculum so students can generate graphs for their predictive AI models?

Adding `matplotlib` is a brilliant way to make abstract data concrete for 10-year-olds. Seeing the AI visually "draw a line through the dots" makes the concept of predictive patterns instantly understandable.

Here is how to integrate data visualization into your first lesson.

### Integrating Matplotlib into Predictive ML

For this updated lesson, students will chart historical data (hours spent studying) against outcomes (test scores) to see how Predictive AI visually identifies trends.

> **Teaching Tip:** Before running the code, ask the students to look at the table below and guess what score someone would get if they studied for 4 hours.

| Study Hours (Past Data) | Test Score (Past Result) |
| --- | --- |
| 1 | 30 |
| 2 | 50 |
| 3 | 70 |
| 5 | 95 |

### The Python Code: Drawing the Prediction

Have students copy and run this snippet in their JupyterLab notebooks. It plots the past data and draws a predictive trend line.

```python
import matplotlib.pyplot as plt

# 1. Our Historical Data (The experiences the AI learns from)
study_hours = [1, 2, 3, 5]
test_scores = [30, 50, 70, 95]

# 2. Plotting the actual data points as dots
plt.scatter(study_hours, test_scores, color='blue', label='Past Student Data')

# 3. Drawing our Predictive AI line
# The AI discovers a mathematical pattern: Score = 20 * Hours + 10
predicted_hours = [0, 1, 2, 3, 4, 5, 6]
predicted_scores = [(20 * h) + 10 for h in predicted_hours]

plt.plot(predicted_hours, predicted_scores, color='red', linestyle='--', label='AI Prediction Line')

# 4. Making the chart look nice
plt.title("Predictive AI: Study Hours vs. Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Test Score")
plt.legend()
plt.grid(True)

# Show the graph!
plt.show()

```

### Classroom Exploration Activities

Once the graph appears on their screen, guide the students through these interactive steps:

* **Change the Future:** Ask them to add a `6` to the `study_hours` list and a `110` to the `test_scores` list. What happens to the blue dots?
* **Tweak the Algorithm:** Have them change the mathematical formula `$Score = 20 \times Hours + 10$` inside the list comprehension to something else, like `15 * h`, and observe how the red prediction line shifts.
* **Real-World Connections:** Brainstorm other datasets they could plot (e.g., player level vs. video game boss health, or temperature vs. ice cream sales).

---

Since `matplotlib` was already included in the `pip install` command of our previous `Containerfile`, your Linux server is fully prepared to run this without any further infrastructure configuration.

Would you like to explore adding a simple external dataset file (like a CSV) so students can learn how AI reads massive amounts of data using the `pandas` library next?

Introducing `pandas` to your students is a huge step! You can explain that `pandas` acts like a super-powered digital spreadsheet for Python. While humans use tools like Excel to look at data, AI uses `pandas` to instantly read and analyze thousands of rows at once.

Here is how you can guide them through building a real data pipeline.

## 1. Creating the CSV Dataset

Before writing the Python code, the students need a data file to analyze. Have them right-click in their JupyterLab file browser, create a new text file named `ice_cream_sales.csv`, and type in this data:

```csv
temperature,sales
15,10
18,25
20,40
22,55
25,75
28,90
30,110

```

* Explain that **CSV** stands for "Comma-Separated Values," which is the standard way AI engineers store raw spreadsheet data.

## 2. Reading and Plotting the Data

Now, students will use `pandas` to load the CSV file and pass that information to `matplotlib` to draw the graph. Have them run this code in a new notebook cell:

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. The AI reads the CSV file using pandas
dataset = pd.read_csv('ice_cream_sales.csv')

# 2. Print the table to the screen so students can verify it loaded
print("Data loaded successfully:")
print(dataset)

# 3. Plotting the data directly from the pandas columns
plt.scatter(dataset['temperature'], dataset['sales'], color='orange', s=100)

# 4. Adding titles and labels
plt.title("AI Data Analysis: Temperature vs. Sales")
plt.xlabel("Temperature (Celsius)")
plt.ylabel("Number of Ice Creams Sold")
plt.grid(True)

# Show the final graph
plt.show()

```

## 3. Classroom Data Challenges

Once the students successfully load the graph, you can challenge them to manipulate the data like real data scientists:

* **Create a Heatwave:** Have them open the `ice_cream_sales.csv` file, add a new row for an extreme temperature (e.g., 40 degrees with 300 sales), save the file, and re-run their Python code to see the graph update instantly.
* **Spot the Outlier:** Ask them to intentionally add a "bad" data point—like 35 degrees but only 5 sales (maybe it was raining!). This visually demonstrates to students how messy real-world data can confuse predictive AI patterns.
* **Flip the Axes:** Challenge them to edit the `plt.scatter()` line in their code to swap the X and Y axes, making the graph display sideways.

Would you like me to draft a short review quiz to help you assess what the students have learned after they complete this first data module?






