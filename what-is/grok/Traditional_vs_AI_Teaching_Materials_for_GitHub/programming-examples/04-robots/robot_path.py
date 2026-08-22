# Tiny robot that navigates a 1-D path
# 0 = empty, 1 = obstacle, 2 = charging station

path = [0, 0, 1, 0, 0, 2, 0, 1, 0]
position = 0
battery = 5

print("Robot starting at position 0. Battery =", battery)

while position < len(path) - 1 and battery > 0:
    sensor = path[position + 1]   # look one step ahead
    print(f"At {position}. Looking ahead: {sensor}")
    
    if sensor == 1:
        print("  Obstacle! Turning around is not possible here – stop.")
        break
    elif sensor == 2:
        print("  Charging station found! Battery refilled.")
        battery = 5
        position += 1
    else:
        print("  Path clear. Moving forward.")
        position += 1
        battery -= 1

print("Final position:", position, "Battery left:", battery)
