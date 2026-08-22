routes = {
    "Forest Path": {"distance": 5, "time": 45},
    "City Road": {"distance": 8, "time": 25},
    "River Trail": {"distance": 6, "time": 35},
}

preference = input("Choose a goal (shortest/fastest): ").lower()

if preference == "shortest":
    best_route = min(routes, key=lambda route: routes[route]["distance"])
    reason = "it has the shortest distance"
elif preference == "fastest":
    best_route = min(routes, key=lambda route: routes[route]["time"])
    reason = "it has the shortest travel time"
else:
    best_route = None

if best_route:
    print(f"Best route: {best_route}")
    print(f"Reason: {reason}.")
else:
    print("Please choose either 'shortest' or 'fastest'.")
