# Traditional Programming vs AI Programming

**Why the examples you saw earlier feel like “normal programming”**

---

## The Big Difference

| | Traditional Programming | AI / Machine Learning |
|---|-------------------------|-----------------------|
| **Who writes the rules?** | The human programmer | The computer discovers the rules |
| **What do we give the computer?** | Clear instructions (if-else, loops, formulas) | Many examples (data + correct answers) |
| **How does it decide?** | Follows the exact rules we wrote | Finds patterns in the examples |
| **What happens with a new situation?** | Works only if we already wrote a rule for it | Can often guess correctly even for cases it has never seen |
| **Example** | `if color == "yellow" and size == "medium": return "banana"` | Show 1000 pictures of bananas and other fruits → the computer figures out what makes a banana look like a banana |

---

## Simple Analogy

**Traditional programming** is like giving a friend a very detailed recipe:

> “If the fruit is yellow and curved and medium-sized → call it a banana.”

**AI programming** is like showing the friend hundreds of real fruits and saying:

> “These are bananas. These are not. Now you try to figure out the pattern.”

After seeing enough examples, the friend (the AI) can usually recognise a new banana even if it is a bit different from the ones you showed.

---

## Why we still showed simple if-else examples

We started with rule-based code because:

1. It is easy to understand.
2. It lets children see the **idea** of “making a decision”.
3. It creates a clear contrast: “This is how humans write rules. Now let’s see how a computer can **learn** the rules.”

The next examples will show the real AI style: **data → learning → prediction**.

---

## What “AI code” usually looks like

In real AI projects the code does three main things:

1. **Prepare data** – collect and clean examples
2. **Train** – let the computer find patterns (this is the learning part)
3. **Predict** – use the learned patterns on new data

The “intelligence” is not in the `if` statements.  
It is in the **numbers (weights)** that the training process discovers.

That is why a neural network after training can recognise cats, translate languages, or play games — the programmer never wrote rules for every possible situation.
