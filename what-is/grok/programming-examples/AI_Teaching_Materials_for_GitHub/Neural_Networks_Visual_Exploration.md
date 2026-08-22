# Explore Neural Networks Visually

**A simple, picture-based guide for children (ages 8–14)**  
*Companion to the AI Teaching Guide*

---

## 01 · The Big Idea

**A neural network is a computer system inspired by the brain.**

| 1. Brain cells talk | 2. Computers copy the idea | 3. They learn from examples |
|---------------------|----------------------------|-----------------------------|
| In your brain, tiny cells called **neurons** send signals to each other. | Artificial neurons are simple math units that pass numbers to each other. | By seeing many examples, the network gets better at recognizing patterns. |

---

## 02 · One Neuron

**Meet one artificial neuron**

It receives numbers, multiplies them by “weights”, adds them up, and decides whether to “fire”.

```
Input 1 (e.g. color)  ──× weight──┐
                                  │
Input 2 (e.g. size)   ──× weight──┼──►  NEURON  ──► Output signal
                                  │   (adds &      (number between
Input 3 (e.g. shape)  ──× weight──┘    activates)   0 and 1)
```

---

## 03 · Layers

**Neurons are organized in layers**

| Input Layer          | Hidden Layer(s)       | Output Layer          |
|----------------------|-----------------------|-----------------------|
| Receives the data    | Finds patterns        | Gives the answer      |
| (e.g. Pixel 1, 2, 3) | (many neurons)        | (e.g. Cat / Dog)      |

Data flows from left → right through these layers.

---

## 04 · Forward Pass

**Information flows from left to right**

This is called the **“forward pass”**. Each neuron receives signals, does a little math, and sends a new signal forward.

```
   INPUT          HIDDEN          OUTPUT
     ●              ●               ●
     ●  ────────►   ●  ────────►    ●
     ●              ●
                    ●
  Data enters                    Answer comes out
```

---

## 05 · How It Learns

**The network learns by adjusting its weights**

| BEFORE training                          | AFTER training                              |
|------------------------------------------|---------------------------------------------|
| Weights are random.                      | Weights have been adjusted                  |
| The network makes wild guesses.          | using thousands of examples.                |
| Example: “Is this a cat?” → 40% yes      | Example: “Is this a cat?” → 95% yes         |
| (often wrong)                            | (usually correct)                           |
| The computer measures the error          | This process is called                      |
| and slowly changes the weights.          | **“training”** or **“learning”**.           |

---

## 06 · Example: Recognizing a Handwritten Digit

1. **Image** — 28×28 pixels become 784 input numbers  
2. **Hidden layers** — Find edges, curves, and patterns  
3. **Output** — 10 numbers (one for each digit 0–9)  
4. **Answer** — Highest score wins: “This is a 7”

---

## 07 · Try It Yourself – Be the Neuron!

**Classroom (or family) game — no computer needed**

1. **Inputs**  
   Three children hold up cards with numbers (e.g. 2, 5, 1).

2. **Weights**  
   The “neuron” child multiplies each number by a secret weight you give them (e.g. ×3, ×0.5, ×2).

3. **Add & decide**  
   Add the results. If the total is above a threshold (say 10), the neuron “fires” (jumps or says “Yes!”).

4. **Change weights**  
   Try different weights and see how the decision changes.  
   This is exactly how training works!

---

## 08 · Five Things to Remember

1. A neural network is made of simple units (**neurons**) connected in **layers**.
2. Information flows from **input → hidden layers → output**.
3. Learning means adjusting the connection strengths (**weights**) using examples.
4. More data and better examples usually make the network smarter.
5. Neural networks power many of the AI tools you already use — image recognition, chatbots, and more.

---

*Neural Networks · Visual Exploration for Kids*
