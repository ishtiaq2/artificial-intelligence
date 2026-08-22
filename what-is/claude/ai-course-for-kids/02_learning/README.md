# Module 2: Learning

## Teacher Script
Machine Learning flips Module 1 on its head: instead of a human writing the rules, the computer
**finds the rules itself** by looking at many examples. This became practical through the 2000s–2010s
and is the foundation everything else in this course builds on.

## Kid-Friendly Analogy
"Imagine you've eaten 500 different meals in your life. Without anyone telling you the rule, you've
*learned* that food with a certain smell is usually spoiled. That's machine learning — pattern-spotting
from experience, not from being told a rule by someone else."

## Key Vocabulary
- **Data** — the examples we learn from
- **Training** — the process of learning from data
- **Model** — the "brain" that results after training
- **Prediction** — the model's guess about something new it hasn't seen before

## Unplugged/No-Code Activity: Teach a Computer to Sort Fruit (20 min)
Use Google's free **Teachable Machine** (https://teachablemachine.withgoogle.com):
1. "Get Started" → "Image Project" → "Standard image model."
2. Create two classes: `Apple` and `Banana`.
3. Capture ~30 webcam photos of each under its class.
4. Click **Train Model** — this *is* the learning step.
5. Test it live in the "Preview" pane.

**Try it with only 3 photos instead of 30** — it gets confused. Ask why (not enough data to learn the
*real* pattern — it may have latched onto something irrelevant, like background color).

## Hands-On Tutorial: `tutorial.py`
Real Python machine learning: train a linear regression model to predict ice cream sales from
temperature, then use it to predict a value it has never seen.

## Data & Bias Checkpoint
Ask: **"What if we only trained this on hot-country data, then used it for a cold country?"** The
model's predictions are only as good as how well the training data represents the real world it will
be used in.

## Discussion Questions
- Name 3 things in daily life that use prediction (Netflix, weather apps, Google Maps ETA).
- What could go wrong if training data only included red apples — would the model recognize a green one?
