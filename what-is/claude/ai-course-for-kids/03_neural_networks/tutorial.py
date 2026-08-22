"""
Module 3: NEURAL NETWORKS
Build a tiny neural network completely from scratch (just numpy -- no
scikit-learn shortcuts) and watch it learn the XOR pattern, a classic
"can't be solved with a single straight line" problem that needs a real
network (an input layer + a hidden layer) to solve.

XOR truth table (the pattern we want it to learn):
  0, 0 -> 0
  0, 1 -> 1
  1, 0 -> 1
  1, 1 -> 0

Requires: numpy, matplotlib (see requirements.txt)
"""

import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    # Squashes any number into a range between 0 and 1 -- like a neuron
    # "firing" more or less strongly.
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


def build_training_data():
    # Inputs: two numbers (0 or 1). Outputs: the XOR result.
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])
    return X, y


def train_neural_network(X, y, hidden_neurons=4, epochs=10000, learning_rate=0.5, seed=42):
    rng = np.random.default_rng(seed)

    input_neurons = X.shape[1]
    output_neurons = y.shape[1]

    # Randomly initialize weights -- this is the "before any learning" state,
    # just like the human line throwing randomly at first.
    weights_input_hidden = rng.uniform(-1, 1, (input_neurons, hidden_neurons))
    weights_hidden_output = rng.uniform(-1, 1, (hidden_neurons, output_neurons))

    loss_history = []

    for epoch in range(epochs):
        # ---- Forward pass: make a prediction ----
        hidden_layer_input = np.dot(X, weights_input_hidden)
        hidden_layer_output = sigmoid(hidden_layer_input)

        output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
        predicted_output = sigmoid(output_layer_input)

        # ---- How wrong were we? ----
        error = y - predicted_output
        loss_history.append(np.mean(np.abs(error)))

        # ---- Backward pass: adjust weights a little (this is "training") ----
        output_delta = error * sigmoid_derivative(predicted_output)
        hidden_error = output_delta.dot(weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(hidden_layer_output)

        weights_hidden_output += hidden_layer_output.T.dot(output_delta) * learning_rate
        weights_input_hidden += X.T.dot(hidden_delta) * learning_rate

    return weights_input_hidden, weights_hidden_output, loss_history


def predict(X, weights_input_hidden, weights_hidden_output):
    hidden_layer_output = sigmoid(np.dot(X, weights_input_hidden))
    return sigmoid(np.dot(hidden_layer_output, weights_hidden_output))


def plot_learning_curve(loss_history):
    plt.plot(loss_history)
    plt.xlabel("Training round (epoch)")
    plt.ylabel("Average error")
    plt.title("Watch the network get less wrong over time")
    plt.show()


def run_demo():
    X, y = build_training_data()
    w_ih, w_ho, loss_history = train_neural_network(X, y)

    print("Predictions after training (compare to the XOR truth table):")
    predictions = predict(X, w_ih, w_ho)
    for inputs, target, pred in zip(X, y, predictions):
        print(f"  Input: {inputs} -> Target: {target[0]} -> Network says: {pred[0]:.3f}")

    plot_learning_curve(loss_history)


if __name__ == "__main__":
    run_demo()
