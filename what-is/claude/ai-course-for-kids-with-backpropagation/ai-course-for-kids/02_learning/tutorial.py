"""
Module 2: LEARNING
Train a real machine learning model (Linear Regression) to predict ice cream
sales from temperature. Unlike Module 1, nobody writes the "temperature -> sales"
rule by hand -- the model learns it from data.

Requires: matplotlib, numpy, scikit-learn (see requirements.txt)
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def load_training_data():
    # Our "training data": temperature (deg C) and ice creams sold that day
    temperature = [15, 18, 20, 22, 25, 28, 30, 32, 35]
    ice_creams_sold = [50, 65, 75, 90, 110, 130, 150, 170, 200]
    return np.array(temperature).reshape(-1, 1), np.array(ice_creams_sold)


def plot_raw_data(X, y):
    plt.scatter(X, y)
    plt.xlabel("Temperature (deg C)")
    plt.ylabel("Ice Creams Sold")
    plt.title("Do hotter days sell more ice cream?")
    plt.show()


def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)  # <-- this is the "learning" step
    print("Training complete!")

    # These two numbers are the ENTIRE "rule" the model learned. Nobody typed
    # them -- fit() searched for the slope and intercept that best fit the data.
    slope = model.coef_[0]
    intercept = model.intercept_
    print(f"Learned rule: sales = {slope:.2f} x temperature + {intercept:.2f}")
    print("Compare: in Module 1, a human would have had to type this formula")
    print("by hand. Here, nobody wrote it -- it was discovered from 9 data points.")
    return model


def predict_new_value(model, new_temp_celsius):
    new_temp = np.array([[new_temp_celsius]])
    predicted_sales = model.predict(new_temp)
    print(f"At {new_temp_celsius} deg C, the model predicts about "
          f"{predicted_sales[0]:.0f} ice creams sold.")
    return predicted_sales[0]


def plot_learned_line(model, X, y):
    plt.scatter(X, y, label="Real data")
    plt.plot(X, model.predict(X), color="red", label="What the AI learned")
    plt.xlabel("Temperature (deg C)")
    plt.ylabel("Ice Creams Sold")
    plt.legend()
    plt.title("The red line is the model's learned rule")
    plt.show()


def run_demo():
    X, y = load_training_data()
    plot_raw_data(X, y)
    model = train_model(X, y)
    predict_new_value(model, new_temp_celsius=27)
    plot_learned_line(model, X, y)


if __name__ == "__main__":
    run_demo()
