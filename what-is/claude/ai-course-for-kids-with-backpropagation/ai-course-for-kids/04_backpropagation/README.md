# Module 4: Backpropagation

## Teacher Script
This is the module that finally answers the question every earlier module has been dodging: **how,
exactly, does a computer find the right weights?** The answer is an algorithm called
**backpropagation**, combined with **gradient descent**. It's the single most important algorithm in
modern AI — it's what actually runs inside `.fit()` calls in Module 2 and Module 3, and (at an
enormously larger scale) inside every large language model, image generator, and self-driving system
in existence today.

The core idea, precisely:
1. **Forward pass** — run the network on an example, get a prediction.
2. **Loss** — measure exactly how wrong that prediction was, with a formula.
3. **Backward pass** — using calculus (the chain rule), calculate exactly how much *each individual
   weight* contributed to that error. This is "backpropagation" — the error signal is propagated
   *backward*, from the output layer toward the input layer.
4. **Update** — nudge every weight a small amount in the direction that would have reduced the error
   (this is "gradient descent"). Repeat thousands of times.

## Teen-Friendly Analogy
"Imagine your team loses a relay race, and you want to know who to blame. You can't just yell at
everyone equally — the anchor runner who dropped the baton at the very end probably deserves more of
the blame than the first runner who ran a great leg. Backpropagation is a precise, mathematical way of
figuring out exactly how much each 'runner' (weight) is responsible for the final result, working
backward from the finish line to the start — and then adjusting each one by exactly that much."

## Key Vocabulary
- **Loss function** — a formula that measures how wrong a prediction is (bigger = worse)
- **Gradient** — a number telling you which direction, and how strongly, to change a weight to reduce the loss
- **Gradient descent** — repeatedly nudging weights in the direction that reduces loss
- **Learning rate** — how big a step to take on each update (too big = overshoot, too small = painfully slow)
- **Chain rule** — the calculus rule that lets us calculate each layer's contribution to the final error
- **Epoch** — one full pass of training over all the data

## Unplugged Activity: "The Blame Chain" Game (20 min)
This is a direct sequel to Module 3's signal-passing game, but now focused on the *backward* pass:
1. Line up 4–5 students. Give the first student a starting number and have each student apply their
   own chosen multiplier, passing the result down the line (same as Module 3's game).
2. Compare the final result to a target number written on the board. Calculate the **error** (target
   minus final result).
3. Now work **backward**: starting from the *last* student, each person must estimate how much *their*
   multiplier contributed to the final error, and adjust their multiplier slightly — but they can only
   see the error handed to them by the student after them in the line, not the original error directly.
4. Repeat forward-then-backward 3–4 rounds and watch the final result get closer to the target each time.
5. Debrief: this back-to-front, one-student-at-a-time correction process is *exactly* what
   backpropagation does inside a neural network — except with precise calculus instead of estimates,
   and thousands of rounds instead of 3–4.

## Hands-On Tutorial: `tutorial.py`
Two parts, building from the simplest possible case to a full network:
- **Part A:** a single artificial neuron learning `y = 3x + 1` from 5 example points. Every gradient
  is computed with an explicit calculus formula printed in the code — no library, no shortcuts. Watch
  the weight and bias gradually converge toward the true values, one small step at a time.
- **Part B:** a full 2-layer network solving the XOR problem from Module 3 — but instead of calling
  scikit-learn's `.fit()`, we implement the entire forward pass, loss calculation, backward pass, and
  weight update ourselves using only `numpy`. This is genuinely the same algorithm — just written out
  by hand instead of hidden inside a library.

## Data & Bias Checkpoint
Ask: **"Backpropagation only tells the network how to get better at the examples it's shown. If those
examples are unfair or unrepresentative, will backpropagation fix that?"** No — it will faithfully,
mathematically optimize toward whatever the training data rewards, bias and all. Backpropagation makes
a network good at minimizing loss on its data; it says nothing about whether that data was fair or
complete.

## Discussion Questions
- In Part A, what would happen if the learning rate were much bigger? Try changing `learning_rate` in
  the code and see if training breaks.
- Real large language models have billions of weights. Backpropagation still applies the exact same
  four steps (forward, loss, backward, update) — why do you think that's remarkable?
- Why do you think this algorithm is called "back"-propagation instead of just "propagation"?
