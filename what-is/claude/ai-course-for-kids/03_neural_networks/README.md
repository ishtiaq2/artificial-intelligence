# Module 3: Neural Networks

## Teacher Script
Module 2 showed *that* a computer can learn a pattern. This module opens the black box and shows
**how**. Neural networks are loosely inspired by brain cells (neurons) connected together — each
connection has a "weight" (importance), and the network adjusts those weights during training until
its predictions get better. This is the engine underneath almost everything from here on: Creating,
Reasoning, and Acting are all powered by (much bigger) neural networks.

## Kid-Friendly Analogy
"Imagine a row of kids passing a ball down a line, and each kid decides how hard to throw it to the
next person. At first they throw randomly. Every time the ball misses the target at the end, they
each adjust how hard they throw, just a little. After thousands of tries, the whole line learns
exactly how to get the ball to the target — even though no single kid was ever *told* the right
amount of force. That adjusting-a-little-each-time process is how a neural network learns; each
'kid' is like a neuron, and 'how hard they throw' is a weight."

## Key Vocabulary
- **Neuron (node)** — a small unit that takes inputs, combines them, and produces an output
- **Weight** — a number representing how important/strong a connection is
- **Layer** — a group of neurons; networks are organized in layers (input → hidden → output)
- **Training / backpropagation** — the process of adjusting weights based on how wrong a prediction was

## Unplugged Activity: "Human Neural Network" Signal-Passing Game (20 min)
1. Line up 5–6 students in a row (this is one "layer" passing to the next).
2. Give the first student a number (e.g., "7"). Each student must pass a new number to the next
   person using a rule they choose (e.g., "double it," "add 3") — like a weight.
3. The last student announces the final number. Compare it to a "target" number written on the board
   beforehand.
4. If it doesn't match, each student is allowed to **tweak their own rule slightly** and the class
   tries again. Repeat 3–4 rounds.
5. Debrief: nobody was told the "correct" rule up front — the class *converged* toward the target
   through repeated small adjustments. That's training a neural network, played out with humans.

## Hands-On Tutorial: `tutorial.py`
Build a tiny neural network completely from scratch using only `numpy` (no shortcuts, no black-box
library) to solve a simple pattern-recognition problem. Watch its error decrease as it trains.

## Data & Bias Checkpoint
Ask: **"If the human line in our unplugged game only ever practiced with even numbers, would it work
correctly on an odd number?"** Neural networks only get good at what they've actually practiced on —
this is the same idea as Module 2's data checkpoint, but now visible inside the "brain" itself.

## Discussion Questions
- Why do you think it's called a "neural" network? What's similar to, and different from, a real brain?
- What do you think happens if a network has too few neurons? Too many?
