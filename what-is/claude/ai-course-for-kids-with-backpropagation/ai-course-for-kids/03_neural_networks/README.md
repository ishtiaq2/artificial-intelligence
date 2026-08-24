# Module 3: Neural Networks

## Teacher Script
Module 2 showed that a computer can learn a simple rule (a slope and intercept). Neural networks
extend that idea to learn far more complex patterns, using layers of connected "neurons" — loosely
inspired by brain cells. Each connection has a "weight" (importance), and training adjusts those
weights until predictions improve. In this module, we use a **real, established implementation** —
scikit-learn's `MLPClassifier` — the same category of model used in production systems, not a
simplified toy.

## Kid/Teen-Friendly Analogy
"A single neuron is like one person voting on a decision by weighing a few pieces of evidence. A
neural network is a whole committee of these voters, arranged in layers — the first layer votes on
raw evidence, and the next layer votes on what the first layer decided. Training is the process of
each 'voter' learning how much weight to give each piece of evidence, based on getting many decisions
right or wrong over time."

## Key Vocabulary
- **Neuron (node)** — a small unit that takes inputs, combines them, and produces an output
- **Weight** — a number representing how important/strong a connection is
- **Layer** — a group of neurons; networks are organized in layers (input → hidden → output)
- **Hidden layer** — a layer between input and output that lets the network learn non-obvious patterns
- **Activation function** — a small function (like `tanh` or `sigmoid`) that decides how strongly a neuron "fires"

## Unplugged Activity: "Human Neural Network" Signal-Passing Game (20 min)
1. Line up 5–6 students in a row (this is one "layer" passing to the next).
2. Give the first student a number (e.g., "7"). Each student must pass a new number to the next
   person using a rule they choose (e.g., "double it," "add 3") — like a weight.
3. The last student announces the final number. Compare it to a "target" number written on the board
   beforehand.
4. If it doesn't match, each student is allowed to **tweak their own rule slightly** and the class
   tries again. Repeat 3–4 rounds.
5. Debrief: nobody was told the "correct" rule up front — the class *converged* toward the target
   through repeated small adjustments. Module 4 (Backpropagation) explains, in exact mathematical
   terms, how each "voter" should adjust their rule — this game is the intuition; the next module is
   the mechanism.

## Hands-On Tutorial: `tutorial.py`
Train scikit-learn's real `MLPClassifier` on the XOR problem (a pattern that can't be solved with a
single straight line, which is exactly why hidden layers exist). The tutorial prints the network's
learned weight matrices — real numbers nobody typed — and deliberately does **not** explain how
`.fit()` found them. That question is answered fully in the next module.

## Data & Bias Checkpoint
Ask: **"If we only trained this network on 4 examples (like XOR), would you trust it to make an
important real-world decision?"** Real neural networks are typically trained on thousands to billions
of examples — 4 is enough to teach a toy pattern, nowhere near enough for anything that matters.

## Discussion Questions
- Why do you think it's called a "neural" network? What's similar to, and different from, a real brain?
- Module 2's model had 2 learned numbers (slope, intercept). This network has more. What do you think
  happens as networks get bigger — is more always better?
