"""
Module 4: BACKPROPAGATION
Module 3 used a real library (scikit-learn) and just called .fit(). This
module opens the hood and rebuilds that exact training process by hand, so
you can see backpropagation happening, one number at a time.

PART A: a single neuron, learning y = w*x + b, with every gradient written
out explicitly using real calculus -- no shortcuts, no library.

PART B: a full 2-layer network (the same XOR problem from Module 3), trained
with backpropagation implemented entirely with numpy. This is genuinely the
same algorithm that powers scikit-learn's MLPClassifier and, at a vastly
larger scale, every modern deep learning framework (PyTorch, TensorFlow).

Requires: numpy, matplotlib (see requirements.txt)
"""

import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# PART A: Backpropagation on a single neuron (the simplest possible case)
# ---------------------------------------------------------------------------
#
# Our tiny neuron computes: prediction = w * x + b
# Our loss (how wrong we are) is the squared error: loss = (prediction - y)^2
#
# Calculus tells us exactly how to reduce that loss:
#   d(loss)/d(w) = 2 * (prediction - y) * x      <-- the "gradient" for w
#   d(loss)/d(b) = 2 * (prediction - y)           <-- the "gradient" for b
#
# The gradient tells us WHICH DIRECTION makes the loss worse. We move the
# opposite direction, by a small amount (the "learning rate"). This is
# gradient descent, and computing those two derivative formulas above IS
# backpropagation for this tiny one-neuron case.

def train_single_neuron(x_values, y_values, learning_rate=0.02, steps=60, print_every=10):
    w, b = 0.0, 0.0  # start with random-ish (here, zero) weight and bias
    history = []

    for step in range(steps):
        # ---- forward pass: predict for ALL training points at once ----
        predictions = w * x_values + b
        loss = np.mean((predictions - y_values) ** 2)

        # ---- backward pass: average the gradient across every example ----
        gradient_w = np.mean(2 * (predictions - y_values) * x_values)
        gradient_b = np.mean(2 * (predictions - y_values))

        # ---- update: move weights AGAINST the gradient to reduce loss ----
        w -= learning_rate * gradient_w
        b -= learning_rate * gradient_b

        history.append((step, loss, w, b))
        if step % print_every == 0 or step == steps - 1:
            print(f"  Step {step:2d}: loss={loss:7.3f}  gradient_w={gradient_w:7.3f}  "
                  f"new w={w:6.3f}  new b={b:6.3f}")

    return w, b, history


def run_part_a():
    print("=== PART A: One neuron learning y = 3*x + 1 from 5 examples ===\n")
    print("Training data (x, y): (0,1) (1,4) (2,7) (3,10) (4,13)")
    print("Watch w and b start at 0 and GRADUALLY get nudged toward the true")
    print("values 3 and 1, one small gradient step at a time -- nobody tells")
    print("the neuron 'w should end up near 3':\n")
    x_values = np.array([0, 1, 2, 3, 4], dtype=float)
    y_values = 3 * x_values + 1
    final_w, final_b, history = train_single_neuron(x_values, y_values)
    print(f"\nFinal learned rule: prediction = {final_w:.2f} * x + {final_b:.2f}")
    print("(Compare to the true rule we were secretly fitting: y = 3*x + 1)")
    return history


def plot_part_a_loss(history):
    steps = [h[0] for h in history]
    losses = [h[1] for h in history]
    plt.plot(steps, losses, marker="o")
    plt.xlabel("Training step")
    plt.ylabel("Loss")
    plt.title("Backpropagation in action: loss falling step by step")
    plt.show()


# ---------------------------------------------------------------------------
# PART B: Full backpropagation through a 2-layer network, solving XOR
# ---------------------------------------------------------------------------

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


def build_xor_data():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])
    return X, y


def train_network_with_backprop(X, y, hidden_neurons=4, epochs=10000, learning_rate=0.5, seed=42):
    rng = np.random.default_rng(seed)
    input_neurons = X.shape[1]
    output_neurons = y.shape[1]

    weights_input_hidden = rng.uniform(-1, 1, (input_neurons, hidden_neurons))
    weights_hidden_output = rng.uniform(-1, 1, (hidden_neurons, output_neurons))

    loss_history = []

    for epoch in range(epochs):
        # ---- FORWARD PASS: make a prediction ----
        hidden_layer_output = sigmoid(np.dot(X, weights_input_hidden))
        predicted_output = sigmoid(np.dot(hidden_layer_output, weights_hidden_output))

        # ---- how wrong were we? ----
        error = y - predicted_output
        loss_history.append(np.mean(np.abs(error)))

        # ---- BACKWARD PASS: this IS backpropagation ----
        # Step 1: how much did the output layer contribute to the error?
        output_delta = error * sigmoid_derivative(predicted_output)

        # Step 2: propagate that error BACKWARD into the hidden layer,
        # weighted by how much each hidden neuron influenced the output
        # (this "passing the blame backward" is where the name comes from)
        hidden_error = output_delta.dot(weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(hidden_layer_output)

        # ---- UPDATE: nudge every weight against its gradient ----
        weights_hidden_output += hidden_layer_output.T.dot(output_delta) * learning_rate
        weights_input_hidden += X.T.dot(hidden_delta) * learning_rate

    return weights_input_hidden, weights_hidden_output, loss_history


def predict(X, weights_input_hidden, weights_hidden_output):
    hidden_layer_output = sigmoid(np.dot(X, weights_input_hidden))
    return sigmoid(np.dot(hidden_layer_output, weights_hidden_output))


def run_part_b():
    print("\n=== PART B: A full network learning XOR via backpropagation ===\n")
    X, y = build_xor_data()
    w_ih, w_ho, loss_history = train_network_with_backprop(X, y)

    print("Predictions after training (compare to the XOR truth table):")
    predictions = predict(X, w_ih, w_ho)
    for inputs, target, pred in zip(X, y, predictions):
        print(f"  Input: {inputs} -> Target: {target[0]} -> Network says: {pred[0]:.3f}")

    print("\nThese weights were found by the exact same idea as Part A --")
    print("just applied automatically, thousands of times, across a whole network:")
    print("  weights_input_hidden =\n", np.round(w_ih, 3))
    print("  weights_hidden_output =\n", np.round(w_ho, 3))

    return loss_history


def plot_part_b_loss(loss_history):
    plt.plot(loss_history)
    plt.xlabel("Training round (epoch)")
    plt.ylabel("Average error")
    plt.title("A full network's error falling via backpropagation")
    plt.show()


def run_demo():
    history_a = run_part_a()
    plot_part_a_loss(history_a)

    loss_history_b = run_part_b()
    plot_part_b_loss(loss_history_b)

    print("\nDiscuss: Part A had 2 numbers to learn (w, b). Part B had 12 (two")
    print("weight matrices). Real large language models have BILLIONS of")
    print("numbers -- but the core update rule is the exact same gradient-descent")
    print("idea you just watched happen by hand.")


if __name__ == "__main__":
    run_demo()
