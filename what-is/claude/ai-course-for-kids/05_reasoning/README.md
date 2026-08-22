# Module 5: Reasoning

## Teacher Script
Creating (Module 4) generates plausible text one word at a time — but some problems need more than
that: they need the AI to **break a problem into steps and work through it**, the way a person does
math on scratch paper instead of blurting out a guess. This "thinking in steps" is called **reasoning**
or **chain-of-thought**, and it's the planning half of what makes modern AI systems act like agents
(Module 6 is the doing half).

## Kid-Friendly Analogy
"If someone asks you '17 × 24' and you had to answer instantly with no thinking, you might guess
wrong. But if you're allowed to work it out step by step on paper first, you'll get it right far more
often. AI reasoning is the same idea — letting the model 'show its work' step by step, instead of
jumping straight to an answer, usually makes it more accurate."

## Key Vocabulary
- **Reasoning** — working through a problem in logical steps rather than answering instantly
- **Chain-of-thought** — a technique where an AI writes out its intermediate steps before the final answer
- **Planning** — figuring out what steps are needed *before* acting on any of them

## Unplugged Activity: "Think Aloud" Step-by-Step Puzzle Solving (20 min)
1. Give students a multi-step logic puzzle (e.g., a simple riddle or a word problem with 3 clues).
2. Round 1: they must answer **instantly**, no discussion, no writing anything down.
3. Round 2 (new puzzle, similar difficulty): they must write out **each reasoning step** before
   giving a final answer.
4. Compare accuracy between the two rounds as a class. This mirrors the difference between an LLM
   answering directly (Module 4-style) vs. reasoning step by step.

## Hands-On Tutorial: `tutorial.py`
Compares "answer immediately" vs. "reason step by step" on a simple word-problem style task, showing
how breaking a problem into explicit steps changes the outcome — a simplified, code-based illustration
of what chain-of-thought prompting does with real LLMs.

## Data & Bias Checkpoint
Ask: **"If an AI's step-by-step reasoning *looks* logical but is based on a false assumption early on,
what happens to the final answer?"** Reasoning only helps if each step is checked — a confident,
well-organized wrong path is still wrong. This is why humans should still review important AI decisions.

## Discussion Questions
- Can you think of a time YOU got a better answer by writing your steps down instead of guessing?
- Should an AI reasoning through a medical or safety decision be allowed to skip steps to be faster? Why/why not?
