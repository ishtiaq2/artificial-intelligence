# Module 1: Rules

## Teacher Script
Before we can appreciate "AI," kids need a clear picture of what a computer does **without** it:
follows exact instructions, written entirely by a human. This is the oldest form of "smart-seeming"
software — expert systems, rule-based chatbots, decision trees — all just carefully organized
if/else logic. It's the baseline we'll contrast every later module against.

## Kid-Friendly Analogy
"A rules-based program is like a strict recipe. If you don't have an ingredient, it doesn't
improvise — it just breaks, or gives up. It can only do exactly what the recipe says, nothing more."

## Key Vocabulary
- **Rule** — an exact instruction a programmer writes ("if X, then Y")
- **Rule-based system** — software built entirely from many such rules
- **Expert system** — an older style of AI that encoded a human expert's rules directly

## Unplugged Activity: "20 Questions, But With Fixed Rules" (15 min)
1. One student thinks of an animal. The class can only ask from a **fixed list of 10 pre-written
   yes/no questions** (e.g., "Does it have fur?", "Does it live in water?") — no free-form questions
   allowed.
2. After a few rounds, introduce an animal that the fixed questions can't distinguish (e.g., two
   different birds). The class gets stuck.
3. Debrief: **this is the core weakness of rule-based systems** — they only handle what they were
   explicitly programmed to handle. Anything outside the rules breaks them. This sets up Module 2
   (Learning) perfectly.

## Hands-On Tutorial: `tutorial.py`
Run it and try to "break" the chatbot by asking something it wasn't given a rule for. Then have
students add 2–3 new `elif` rules of their own.

## Data & Bias Checkpoint
Ask: **"Whose rules are these?"** A rule-based system only reflects the biases and blind spots of
the person who wrote the rules — there's no data involved at all yet, only a human's assumptions.
This becomes an interesting contrast once we reach Module 2, where the "rules" come from data instead.

## Discussion Questions
- Can you think of a rule-based system you use every day (a vending machine, a thermostat, a traffic light)?
- Why might a rule-based system be *more* trustworthy than a learning-based one in some situations
  (e.g., a nuclear reactor shutoff switch)?
