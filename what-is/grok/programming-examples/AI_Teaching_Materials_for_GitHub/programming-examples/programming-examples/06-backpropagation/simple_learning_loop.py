# Super-simple "learning" loop
# Goal: make the number get closer to the target
# This is NOT a real neural network – it only illustrates the idea of error + adjustment

target = 10
current = 0
learning_rate = 0.3   # how big a step we take each time

print("Target is", target)
for step in range(15):
    error = target - current
    print(f"Step {step+1:2d}: current={current:5.2f}  error={error:5.2f}")
    # Move a little bit toward the target
    current = current + learning_rate * error

print("Final value:", round(current, 2))
