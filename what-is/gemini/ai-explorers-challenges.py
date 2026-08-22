import os
import zipfile

# Create directory structure for the new repo
repo_name = "AI-Explorers-Final-Challenges"
os.makedirs(repo_name, exist_ok=True)
os.makedirs(f"{repo_name}/projects", exist_ok=True)

# 1. README.md
readme_content = """# 🏆 AI Explorers: Capstone Challenge Projects

Welcome to the **Final Challenges** repository! This is where your students put everything they've learned to the test. 

These projects are designed to combine all 7 stages of our AI learning journey:
**Rules → Learning → Neural Networks → Creating → Reasoning → Acting → The Future**

## The Projects

### 1. The Eco-Robot Simulator (`eco_robot_simulator.py`)
Students code an autonomous agent that cleans up a digital ocean. It uses **Rules** to navigate, **Learning** to identify trash vs. fish, **Reasoning** to plan its route, and **Creating** to write a final mission report.

### 2. Smart Virtual Pet (`smart_virtual_pet.py`)
Students build a text-based AI pet that uses **Rules** for its health, **Learning** to understand what food the user feeds it most, **Creating** to generate unique greetings, and **Acting** to "sleep" when its battery is low. 

## How to Use
1. Have students open these `.py` files in their JupyterLab environment.
2. The code contains missing parts marked as `TODO`. 
3. Students must use their knowledge from the 7-stage course to complete the apps!
"""
with open(f"{repo_name}/README.md", "w") as f:
    f.write(readme_content)

# 2. Project 1: Eco-Robot
eco_robot_code = """# 🌊 AI Eco-Robot Simulator
# Combines: Rules, Learning, Creating, Reasoning, Acting
import random

def eco_robot():
    print("🤖 Eco-Robot Initialized. Mission: Clean the Ocean.")
    
    # 1. Rules & Acting: Sensor Input
    obstacle_distance = random.uniform(0.5, 5.0)
    if obstacle_distance < 1.0:
        print(f"Action: Obstacle at {obstacle_distance:.1f}m. Turning to avoid.")
    else:
        print("Action: Path clear. Moving forward.")
        
    # 2. Learning / Neural Net concept: Classifying objects
    detected_object = random.choice(["Plastic Bottle", "Sea Turtle", "Soda Can", "Dolphin"])
    print(f"\\nScanner detected: {detected_object}")
    
    # TODO: Write a RULE (if/else) that picks up plastic/cans but ignores animals!
    if "Plastic" in detected_object or "Can" in detected_object:
        print("Reasoning: This is human trash. Action: Collecting!")
    else:
        print("Reasoning: This is wildlife. Action: Taking a photo and leaving it alone.")
        
    # 3. Creating: Generating a report
    print("\\nGenerating Mission Report...")
    # TODO: Use Generative AI logic to create a random success message!
    reports = ["The ocean is a bit cleaner today!", "Mission success, returning to base.", "Nature says thank you!"]
    print(f"Generative Report: {random.choice(reports)}")
    
    # 4. The Future: Ethics
    print("\\n[Human Check]: Did the robot make the right ethical choice today?")

# Run the simulation
eco_robot()
"""
with open(f"{repo_name}/projects/eco_robot_simulator.py", "w") as f:
    f.write(eco_robot_code)

# 3. Project 2: Smart Virtual Pet
virtual_pet_code = """# 🐕 Smart Virtual Pet
# Combines: Rules, Learning, Creating, Acting
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.favorite_word = ""

    def learn_word(self, word):
        # AI Learning Phase
        self.favorite_word = word
        print(f"🧠 {self.name} learned a new pattern: '{word}'!")

    def chat(self):
        # AI Creating Phase
        if self.favorite_word:
            print(f"🗣️ {self.name} says: I love {self.favorite_word}! Bark!")
        else:
            print(f"🗣️ {self.name} says: Hello human! Teach me something.")

    def act(self):
        # AI Rules & Acting Phase
        self.energy -= 20
        if self.energy < 50:
            print(f"⚡ {self.name}'s energy is {self.energy}. Action: Going to sleep to recharge.")
            self.energy = 100
        else:
            print(f"⚡ {self.name} is playing! Energy left: {self.energy}")

# Let's test the pet!
my_pet = VirtualPet("Robo-Dog")
my_pet.chat()
my_pet.learn_word("Data")
my_pet.chat()
my_pet.act()
my_pet.act()
my_pet.act()
"""
with open(f"{repo_name}/projects/smart_virtual_pet.py", "w") as f:
    f.write(virtual_pet_code)

# Zip the repository directory
zip_filename = "AI-Explorers-Final-Challenges.zip"
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(repo_name):
        for file in files:
            zipf.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(repo_name, '..')))

print(f"Created zip archive: {zip_filename}")
