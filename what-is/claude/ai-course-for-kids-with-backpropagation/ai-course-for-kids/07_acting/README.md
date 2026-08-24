# Module 7: Acting

## Teacher Script
Reasoning (Module 6) is thinking — Acting is doing something about it. This module covers two forms
of "acting": **agentic AI** (using tools like a calculator, search engine, or calendar to complete a
task) and **robots** (using motors and sensors to act in the physical world, like self-driving cars
and surgical robots). Both follow the same loop: **sense → think → act**.

## Kid-Friendly Analogy
"A reasoning AI that can't act is like a smart friend giving you directions over the phone. An acting
AI is like that friend actually driving the car. Giving good directions (Module 6) and actually
steering the wheel (Module 7) are two different skills — a real agent needs both."

## Key Vocabulary
- **Agent** — an AI system that can take actions or use tools to achieve a goal, not just respond with text
- **Tool use** — when an AI calls another program (calculator, search, calendar) to help complete a task
- **Sensor** — how a robot perceives the world (camera, lidar, microphone)
- **Actuator** — how a robot acts on the world (motor, wheel, robotic arm)
- **Sense-think-act loop** — the repeating cycle both software agents and robots use to operate

## Unplugged Activity A: Sense-Think-Act Blindfold Maze (20 min)
1. Tape a simple maze/path on the floor with obstacles (chairs, cones).
2. One student is the "robot" (blindfolded), another is the "sensor," who can only say one word at a
   time: "wall," "clear," "turn."
3. The "robot" must navigate using only those single-word sensor reports.
4. Debrief: this is literally how a robot vacuum or self-driving car works — limited sensor input,
   constant small decisions, no big-picture view.

## Unplugged Activity B: Agent vs. Chatbot Live Comparison (15 min)
Using a real, supervised AI assistant:
1. Ask it a simple factual question (chatbot-style: answer from what it knows).
2. Ask it something that needs a tool, e.g. "What's 3,482 x 917?" — notice if it visibly uses a
   calculator tool instead of guessing.
3. Discuss: calling a real tool to get a verified answer, instead of guessing, is the essence of agentic AI.

## Hands-On Tutorial: `tutorial.py`
Three parts:
1. A tiny **tool-using agent** — decides when to call a `calculator` tool vs. answer directly.
2. A **hand-coded self-driving decision loop** — every threshold (`< 5`, `< 20`) was typed by a human.
   This is normal programming wearing a self-driving-car costume, included deliberately so students can
   compare it against Part 3.
3. A **trained decision tree** — the same decisions, but learned from 13 labelled examples. Run it and
   read the printed tree: its thresholds (e.g. 26.5 meters, 35 km/h) are numbers the training algorithm
   discovered on its own, not numbers a human typed. Real self-driving systems work this way (at a vastly
   larger scale), trained on millions of miles of real driving data.

## Data & Bias Checkpoint
Ask: **"What happens if a self-driving car's camera sensor has never seen snow before?"** Acting
systems inherit every blind spot from their training data (Module 2) — but now the consequences are
physical, not just a wrong text answer.

## Discussion Questions
- What tools would you want your own AI agent to be able to use (calendar? camera? robot arm?) — and why?
- What's one task an agent should NOT be allowed to do without asking you first?
- Surgical robots are usually *controlled by* a human surgeon, with AI assisting for precision — why
  might full robot autonomy in surgery be more sensitive than in a vacuum cleaner?
