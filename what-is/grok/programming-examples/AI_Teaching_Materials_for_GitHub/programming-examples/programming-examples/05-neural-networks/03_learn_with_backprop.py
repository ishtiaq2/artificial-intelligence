"""
03 – Tiny Network that LEARNS (simple backpropagation)

We teach a 2→2→1 network to solve a tiny problem:
  Input [1, 0] should give ~1
  Input [0, 1] should give ~0

This is educational code – not production ML.
It shows the idea of:
  forward → measure error → go backward → update weights

Uses NumPy for cleaner math.
"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    # derivative of sigmoid, useful for backprop
    s = sigmoid(x)
    return s * (1 - s)

# ---------- Training data ----------
# Simple pattern we want the network to learn
X = np.array([
    [1.0, 0.0],
    [0.0, 1.0],
    [1.0, 1.0],
    [0.0, 0.0],
])
y = np.array([
    [1.0],
    [0.0],
    [1.0],
    [0.0],
])

# ---------- Network size ----------
n_input  = 2
n_hidden = 2
n_output = 1

# Random starting weights (small numbers)
np.random.seed(42)
W1 = np.random.randn(n_input, n_hidden) * 0.5   # input → hidden
b1 = np.zeros((1, n_hidden))
W2 = np.random.randn(n_hidden, n_output) * 0.5  # hidden → output
b2 = np.zeros((1, n_output))

learning_rate = 0.5
epochs = 2000

print("Training a tiny network to learn a simple pattern...\n")

for epoch in range(epochs):
    # ===== FORWARD PASS =====
    z1 = X @ W1 + b1          # weighted sum into hidden
    a1 = sigmoid(z1)          # hidden activations
    z2 = a1 @ W2 + b2         # weighted sum into output
    a2 = sigmoid(z2)          # final prediction

    # ===== ERROR =====
    error = y - a2
    loss = np.mean(error ** 2)

    # ===== BACKPROPAGATION =====
    # How much did the output layer contribute to the error?
    d_output = error * sigmoid_derivative(z2)
    
    # How much did the hidden layer contribute?
    d_hidden = (d_output @ W2.T) * sigmoid_derivative(z1)

    # ===== UPDATE WEIGHTS (nudge them a little) =====
    W2 += learning_rate * (a1.T @ d_output)
    b2 += learning_rate * np.sum(d_output, axis=0, keepdims=True)
    W1 += learning_rate * (X.T @ d_hidden)
    b1 += learning_rate * np.sum(d_hidden, axis=0, keepdims=True)

    if epoch % 400 == 0:
        print(f"Epoch {epoch:4d}  |  Loss: {loss:.4f}")

print("\n--- After training ---")
print("Predictions:")
for i in range(len(X)):
    pred = a2[i][0]
    print(f"  Input {X[i]}  →  predicted {pred:.3f}  (target was {y[i][0]})")
