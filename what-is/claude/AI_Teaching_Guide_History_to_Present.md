# Teaching AI to Kids: From History to Today
### A Complete Course Guide — 5 Modules, with Tutorials & Hands-On Projects

**Audience:** Ages 10–14 (adaptable up or down), no coding experience required
**Format:** 5 modules, ~60–90 minutes each, can run weekly or as a single-day camp
**Tools needed:** A laptop/tablet with a browser (we use free, no-install tools: Google Colab for code, Teachable Machine, and a chatbot interface). No paid software required.

---

## How This Guide Is Organized

Your five keywords map perfectly onto the real history of AI, so we'll use them as the five modules:

| Module | Era | Keyword | Big Idea |
|---|---|---|---|
| 1 | 1950s–2010s | Predictive AI + Machine Learning | Computers finding patterns and predicting |
| 2 | 2020 | Generative AI (LLMs) | Computers *creating* new text, images, etc. |
| 3 | 2022 | Agentic AI | AI that acts like an assistant / chatbot |
| 4 | Ongoing | Robots | AI controlling machines in the physical world |
| 5 | Future | AGI | AI that reasons like a human |

Each module below has: **(a)** a short teacher script/explanation, **(b)** simple analogies for kids, **(c)** a hands-on tutorial with step-by-step instructions, and **(d)** discussion questions. A capstone project ties it all together at the end.

---

## Before You Start: One Big Idea to Anchor Everything

Write this on the board on Day 1 and refer back to it every module:

> **AI is a computer program that gets better at a task by learning from examples, instead of being told exact rules by a programmer.**

Contrast this with "normal" programming:
- **Normal program:** `if temperature > 30: say "It's hot"` — a human wrote the exact rule.
- **AI program:** show the computer 10,000 examples of hot/cold days, and it *figures out* the rule itself.

This single distinction is the thread that connects all five modules.

---

## Module 1: Predictive AI & Machine Learning

### Teacher Script
Machine Learning (ML) is the "grandparent" of everything else in this course. It started becoming practical in the 2000s–2010s. The core idea: **feed a computer lots of past data, and it learns to predict the future** — will it rain tomorrow, is this email spam, what movie will you like next?

### Kid-Friendly Analogy
"Imagine you've eaten 500 different meals in your life. Without anyone telling you the rule, you've *learned* that food with a certain smell is usually spoiled. That's machine learning — pattern-spotting from experience, not from being told a rule."

### Key Vocabulary
- **Data** — the examples we learn from
- **Training** — the process of learning from data
- **Model** — the "brain" that results after training
- **Prediction** — the model's guess about something new

### Hands-On Tutorial 1A: "Teach a Computer to Sort Fruit" (No Code — 20 min)
Use **Google's Teachable Machine** (free, browser-based, https://teachablemachine.withgoogle.com):

1. Go to Teachable Machine → "Get Started" → "Image Project" → "Standard image model."
2. Create two classes: `Apple` and `Banana`.
3. Use the webcam to capture ~30 photos of an apple (or a picture of one) under "Class 1," and ~30 photos of a banana under "Class 2."
4. Click **Train Model** — watch the progress bar (this *is* the "learning" step).
5. Once trained, hold up the fruit again in the "Preview" pane — the model predicts which one it is, live, with a confidence percentage.

**Discussion prompt:** What happens if you only show it 3 photos instead of 30? Try it. Ask: *why did it get confused?* (Answer: not enough data to learn the real pattern — it may have learned something irrelevant, like "banana = yellow background.")

### Hands-On Tutorial 1B: "Predict Ice Cream Sales" (Real Code — 30 min)
This introduces actual Python ML using Google Colab (colab.research.google.com — free, nothing to install, runs in the browser).

**Step 1 — Open a new Colab notebook.**

**Step 2 — Create some data** (temperature vs. ice creams sold) and paste into a code cell:

```python
# Our "training data": temperature (°C) and ice creams sold that day
temperature = [15, 18, 20, 22, 25, 28, 30, 32, 35]
ice_creams_sold = [50, 65, 75, 90, 110, 130, 150, 170, 200]

# Let's plot it so kids can SEE the pattern
import matplotlib.pyplot as plt
plt.scatter(temperature, ice_creams_sold)
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice Creams Sold")
plt.title("Do hotter days sell more ice cream?")
plt.show()
```

Run the cell (Shift+Enter). Ask the class: "What pattern do you see?" (Answer: as temperature goes up, sales go up — a straight-ish line.)

**Step 3 — Train a real ML model (Linear Regression):**

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Reshape data into the format scikit-learn expects
X = np.array(temperature).reshape(-1, 1)
y = np.array(ice_creams_sold)

# Create and train the model
model = LinearRegression()
model.fit(X, y)   # <-- this is the "learning" step

print("Training complete!")
```

**Step 4 — Make a prediction for a NEW temperature the model has never seen:**

```python
new_temp = np.array([[27]])
predicted_sales = model.predict(new_temp)
print(f"At 27°C, the model predicts we'll sell about {predicted_sales[0]:.0f} ice creams.")
```

**Step 5 — Visualize the model's "learned rule" as a line through the data:**

```python
plt.scatter(temperature, ice_creams_sold, label="Real data")
plt.plot(temperature, model.predict(X), color="red", label="What the AI learned")
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice Creams Sold")
plt.legend()
plt.show()
```

**Wrap-up talking point:** the red line *is* the "model." It was never explicitly programmed — it emerged from the data. This is the foundation every other module builds on.

### Discussion Questions (Module 1)
- Can you think of 3 things in daily life that use prediction (Netflix, weather apps, Google Maps ETA)?
- What could go wrong if the training data is biased (e.g., only trained on red apples — will it recognize a green apple)?

---

## Module 2: Generative AI (2020) — Large Language Models

### Teacher Script
Around 2020, AI crossed a threshold: instead of just predicting a number or a label (Module 1), models like **GPT-3** could **generate brand-new content** — paragraphs, poems, code — by predicting *the next word*, over and over, extremely well. This is called a **Large Language Model (LLM)**.

### Kid-Friendly Analogy
"Imagine the world's best 'autocomplete' on your phone keyboard — but instead of suggesting one word, it's read basically the entire internet, and can write whole essays, one word at a time, each word chosen because it's the most likely next word given everything before it."

### Key Vocabulary
- **LLM (Large Language Model)** — an AI trained on huge amounts of text to predict/generate language
- **Token** — a chunk of text (roughly a word or part of a word) the model reads/writes at a time
- **Prompt** — the instruction or question you give the model
- **Generative** — creating something new, rather than just classifying/predicting a number

### Hands-On Tutorial 2A: "Next-Word Guessing Game" (No Code — 15 min, builds intuition first)
Before touching any AI tool, play this unplugged game:
1. Write a sentence on the board with the last word missing: "The dog ran across the ___."
2. Have students shout out guesses. Notice how everyone predicts something *plausible* (park, road, field) — not random words like "purple."
3. Explain: an LLM does exactly this, one word at a time, thousands of times per second, trained on billions of sentences instead of just classroom guesses.

### Hands-On Tutorial 2B: "Prompt Engineering Lab" (No Code — 25 min)
Using any available chat AI interface (with adult supervision and school-appropriate settings):
1. Have students write a **vague** prompt: `"Write about a dog."`
2. Then a **detailed** prompt: `"Write a 3-sentence story about a nervous puppy's first day at school, in a funny tone."`
3. Compare outputs as a class. This teaches that **the quality of output depends heavily on the quality of the prompt** — a core real-world AI literacy skill.
4. Challenge: can they get the AI to write a poem, then a rap, then a formal letter — same topic, three styles?

### Hands-On Tutorial 2C: "Build a Tiny Text Generator" (Real Code — 30 min)
This demystifies "predicting the next word" with actual code, using a simple statistical model (a Markov chain) — this can be built with no API key needed, so every student can run it:

```python
import random

# Training "data" — any block of text works. Try a short story or nursery rhyme.
text = """the cat sat on the mat the cat likes the mat
the dog sat on the rug the dog likes the rug
the cat and the dog sat on the mat together"""

words = text.split()

# Step 1: learn which words tend to follow which words
next_word_map = {}
for i in range(len(words) - 1):
    current_word = words[i]
    following_word = words[i + 1]
    next_word_map.setdefault(current_word, []).append(following_word)

# Step 2: generate new text by picking a plausible "next word" each time
def generate(start_word, length=10):
    current = start_word
    result = [current]
    for _ in range(length):
        choices = next_word_map.get(current)
        if not choices:
            break
        current = random.choice(choices)
        result.append(current)
    return " ".join(result)

print(generate("the", length=12))
```

Run it a few times — the output changes each time (like a real LLM's "creativity"). Explain: **real LLMs use the same core idea** (predict the next token from patterns in training data), just at a vastly bigger scale, using neural networks instead of a simple word-map.

### Discussion Questions (Module 2)
- Why might an LLM sometimes state something false confidently ("hallucination")? (It's predicting *plausible* text, not looking up *true* facts.)
- What's the difference between a search engine and an LLM?

---

## Module 3: Agentic AI (2022) — Assistants & Chatbots

### Teacher Script
By 2022, LLMs got wrapped into products like ChatGPT — LLMs that could hold a *conversation* and act as an **assistant**, remembering context and following instructions. This is often called **Agentic AI**: AI that doesn't just generate text once, but can take actions, use tools, and pursue a goal across multiple steps (e.g., search the web, run code, book something).

### Kid-Friendly Analogy
"Module 2's AI is like a very smart writer who forgets everything the moment they finish a sentence. Module 3's AI is like a personal assistant who remembers what you asked five minutes ago, can look things up for you, and can actually *do* tasks, not just talk about them."

### Key Vocabulary
- **Chatbot** — software that talks with a user in a conversation
- **Agent** — an AI system that can take actions/use tools to achieve a goal, not just respond with text
- **Context** — the conversation history the AI "remembers" during a chat
- **Tool use** — when an AI calls another program (calculator, search, calendar) to help complete a task

### Hands-On Tutorial 3A: "Build a Simple Rule-Based Chatbot" (Real Code — 25 min)
This is the "before" picture — a classic rule-based chatbot, so students can contrast it with a real AI chatbot afterward:

```python
def simple_chatbot(user_message):
    message = user_message.lower()
    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"
    elif "name" in message:
        return "I'm ChatBot Junior, a simple rule-based assistant!"
    elif "weather" in message:
        return "I can't check real weather — I only know the rules I was given!"
    elif "bye" in message:
        return "Goodbye! Thanks for chatting."
    else:
        return "Sorry, I don't understand that yet. I only know a few phrases!"

# Try it out:
print(simple_chatbot("Hi there!"))
print(simple_chatbot("What's your name?"))
print(simple_chatbot("Can you tell me a joke?"))
```

Have students add 3 new `elif` rules of their own (e.g., a joke, a math fact). Then ask: **"What happens if someone phrases something in a way you didn't code for?"** — it breaks. This is the core limitation rule-based bots have, which LLM-based agents largely solve because they *generalize* instead of matching exact rules.

### Hands-On Tutorial 3B: "Agent vs. Chatbot" Live Comparison (No Code — 20 min)
Using a real assistant AI (with supervision), have students:
1. Ask it a simple factual question (chatbot behavior: answer from what it knows).
2. Ask it something that requires an external tool, e.g., "What's 3,482 × 917?" and observe whether it uses a "tool" like a calculator, or "search the web for today's date" — if the interface shows tool use, point it out explicitly ("see, it's calling a calculator program, not just guessing").
3. Discuss: this "calling a tool to get a real answer instead of guessing" is the essence of **agentic AI**.

### Discussion Questions (Module 3)
- What tools would you want your own AI agent to be able to use (calendar? camera? robot arm?) — and why?
- What's one task an agent should NOT be allowed to do without asking you first? (Great segue into AI safety.)

---

## Module 4: Robots — AI in the Physical World

### Teacher Script
So far, everything happened on a screen. Robotics is where AI's "brain" gets connected to a "body" — sensors (cameras, lidar) feed data in, and motors act it out. Two big real-world examples: **self-driving cars** and **surgical robots**.

### Kid-Friendly Analogy
"A self-driving car is Module 1 (predicting: 'is that a pedestrian?'), Module 2/3 combined with cameras and motors instead of a keyboard and screen. It's 'sense → think → act,' over and over, many times per second."

### Key Vocabulary
- **Sensor** — how a robot perceives the world (camera, lidar, microphone)
- **Actuator** — how a robot acts on the world (motor, wheel, robotic arm)
- **Sense-think-act loop** — the repeating cycle robots use to operate
- **Autonomy** — how much a robot can do without human control

### Hands-On Tutorial 4A: "Sense-Think-Act" Unplugged Simulation (No Code — 20 min)
1. Tape a simple maze/path on the floor with obstacles (chairs, cones).
2. One student is the "robot" (blindfolded or eyes closed), another is the "sensor" who can only say one word at a time: "wall," "clear," "turn."
3. The "robot" must navigate using only those single-word sensor reports — no more.
4. Debrief: this is literally how a robot vacuum or self-driving car works — limited sensor input, constant small decisions, no long-term "seeing the whole picture" the way a human does when looking at a map.

### Hands-On Tutorial 4B: "Code a Virtual Robot's Decision Rules" (Real Code — 30 min)
A simplified simulation of a self-driving car's decision-making, in Python (no hardware needed):

```python
import random

def self_driving_decision(distance_to_object_m, is_pedestrian_detected, current_speed_kmh):
    """A simplified rule-based decision system — real self-driving cars use
    ML models trained on millions of miles of data instead of simple rules,
    but the sense -> think -> act structure is the same."""
    if is_pedestrian_detected:
        return "STOP immediately"
    elif distance_to_object_m < 5:
        return "Brake hard"
    elif distance_to_object_m < 20:
        return "Slow down"
    else:
        return f"Continue at {current_speed_kmh} km/h"

# Simulate a few "sensor readings" coming in over time
scenarios = [
    {"distance_to_object_m": 50, "is_pedestrian_detected": False, "current_speed_kmh": 60},
    {"distance_to_object_m": 15, "is_pedestrian_detected": False, "current_speed_kmh": 60},
    {"distance_to_object_m": 8,  "is_pedestrian_detected": True,  "current_speed_kmh": 40},
]

for i, sensor_reading in enumerate(scenarios, start=1):
    decision = self_driving_decision(**sensor_reading)
    print(f"Frame {i}: sensors={sensor_reading} -> Decision: {decision}")
```

Extend it: have students add a rule for "icy road" or "red light detected." Emphasize: **real self-driving systems use ML models (Module 1) trained on huge datasets, not hand-written if/else rules** — this toy version is a simplification to teach the *structure* of the decision loop.

### Discussion Questions (Module 4)
- What's a mistake a self-driving car's "sensor" could make (fog, glare, a plastic bag blowing across the road)? What should the car do when it's unsure?
- Surgical robots are usually *controlled by* a human surgeon, with AI assisting for precision — why might full robot autonomy in surgery be more sensitive than in a vacuum cleaner?

---

## Module 5: AGI — Artificial General Intelligence

### Teacher Script
Everything so far — predicting numbers, generating text, chatting, driving — is called **Narrow AI**: very good at one type of task. **AGI (Artificial General Intelligence)** is a hypothetical/future AI that can reason, learn, and adapt across *any* task the way a human can — not yet achieved, and a topic of active research and debate.

### Kid-Friendly Analogy
"A chess AI can beat any human at chess but can't tie its shoes. A self-driving car can drive but can't write a poem. You, a human, can do both — and learn a brand new skill you've never tried before, just by understanding instructions. AGI would be an AI that's flexible like that."

### Key Vocabulary
- **Narrow AI** — AI good at one specific task (everything covered so far)
- **AGI** — hypothetical AI with human-like general reasoning across any task
- **Reasoning** — the ability to work through new problems logically, not just pattern-match to training data

### Hands-On Tutorial 5A: "Narrow vs. General" Sorting Activity (No Code — 15 min)
Give students a list of 15 real AI systems (translation apps, chess engines, spam filters, recommendation algorithms, self-driving cars, voice assistants, etc.) and have them sort into "Narrow AI" (all of them, today) vs. "would need to be AGI" (a system that could do all 15 tasks plus anything new you throw at it). This makes concrete that **every AI system that exists today is narrow.**

### Hands-On Tutorial 5B: Class Debate — "Are We Close to AGI?" (No Code — 30 min)
Split the class into two teams researching (using search, supervised) real, current expert opinions:
- **Team A:** arguments that AGI could arrive soon
- **Team B:** arguments for major remaining obstacles (reasoning limits, lack of embodiment, energy costs, safety)

This builds **AI literacy and critical thinking** — the goal isn't to reach a "correct" answer, but to show students that even experts disagree, and that evaluating evidence matters more than picking a side.

### Discussion Questions (Module 5)
- If AGI were achieved, what jobs or tasks do you think would change first?
- What rules or safety measures would you want in place *before* a general-purpose AI was given control of something important?

---

## Capstone Project: "Design Your Own AI System" (60–90 min)

Students work in pairs/small groups to design (on paper or a slide) a fictional AI product, answering:
1. **Which module(s) does it use?** (Predictive? Generative? Agentic? Robotic? Would it need AGI?)
2. **What data would it need to be trained on?**
3. **What could go wrong** if the training data were biased or incomplete?
4. **One safety rule** they'd build in before letting it act autonomously.

Groups present in 2 minutes each. This forces synthesis across all five modules and surfaces AI ethics naturally.

---

## Assessment Ideas
- **Quick check per module:** 3-question exit ticket (a multiple-choice quiz tool works well here if you're using a digital platform).
- **Portfolio:** save each module's Colab notebook — by the end, students have a personal "AI notebook" they built themselves.
- **Capstone rubric:** clarity of the idea (25%), correct use of AI vocabulary (25%), data/bias awareness (25%), safety consideration (25%).

---

## Full Materials Checklist
- [ ] Laptop/tablet + browser per student (or pairs)
- [ ] Google account for Colab (or use Colab without login for view-only, but running code needs a free login)
- [ ] Access to Teachable Machine (teachablemachine.withgoogle.com)
- [ ] Access to a supervised chat AI interface for Modules 2 & 3
- [ ] Printed maze/tape for Module 4's unplugged activity
- [ ] Sticky notes / whiteboard for Module 5 debate

---

## Suggested Pacing (5-week version, 1 module/week)

| Week | Module | Unplugged Activity | Coding Tutorial |
|---|---|---|---|
| 1 | Predictive AI/ML | Fruit sorting (Teachable Machine) | Ice cream sales predictor |
| 2 | Generative AI | Next-word guessing game | Tiny text generator |
| 3 | Agentic AI | Agent vs. chatbot comparison | Rule-based chatbot |
| 4 | Robots | Sense-think-act blindfold maze | Virtual self-driving decisions |
| 5 | AGI + Capstone | Narrow vs. general sorting, debate | Capstone presentations |

This can also be compressed into a single-day camp (roughly 6–7 hours with breaks) by trimming discussion time.
