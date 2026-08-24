"""
Module 3: NEURAL NETWORKS
This tutorial uses scikit-learn's REAL, ESTABLISHED neural network
implementation (MLPClassifier -- "Multi-Layer Perceptron"), the same kind of
model used in production systems, not a toy we invented for teaching.

We train it on XOR, a classic pattern that a single straight line can't
solve (you need a hidden layer of neurons to solve it -- this is exactly why
neural networks were invented).

XOR truth table (the pattern we want it to learn):
  0, 0 -> 0
  0, 1 -> 1
  1, 0 -> 1
  1, 1 -> 0

We will NOT explain here exactly how .fit() finds its weights -- that's the
entire subject of Module 4: Backpropagation, where we rebuild this same
training process by hand.

Requires: scikit-learn (see requirements.txt)
"""

import numpy as np
from sklearn.neural_network import MLPClassifier


def build_training_data():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])
    return X, y


def train_real_neural_network(X, y):
    # This IS a real neural network -- one hidden layer of 4 neurons,
    # trained with the same core algorithm (backpropagation + gradient
    # descent) used by every major deep learning framework.
    model = MLPClassifier(
        hidden_layer_sizes=(4,),
        activation="tanh",
        max_iter=5000,
        random_state=0,
    )
    model.fit(X, y)  # <-- this single line runs backpropagation internally
    return model


def inspect_learned_weights(model):
    print("The network's learned weights (nobody typed these numbers --")
    print("they emerged from training, exactly like Module 2's slope/intercept,")
    print("just with many more numbers because there are many more connections):\n")
    for i, layer_weights in enumerate(model.coefs_):
        print(f"  Layer {i + 1} weight matrix, shape {layer_weights.shape}:")
        print(f"  {np.round(layer_weights, 3)}\n")


def run_demo():
    X, y = build_training_data()
    model = train_real_neural_network(X, y)

    print("Predictions after training (compare to the XOR truth table):")
    predictions = model.predict(X)
    for inputs, target, pred in zip(X, y, predictions):
        match = "correct" if pred == target else "WRONG"
        print(f"  Input: {inputs} -> Target: {target} -> Network says: {pred}  [{match}]")

    print()
    inspect_learned_weights(model)

    print("Curious HOW .fit() found these numbers? That's Module 4: Backpropagation --")
    print("we rebuild this exact training process by hand, one gradient at a time.")


if __name__ == "__main__":
    run_demo()
