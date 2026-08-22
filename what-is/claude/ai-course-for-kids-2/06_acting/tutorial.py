"""
Module 6: ACTING
Two demos:
  1. A tiny tool-using "agent" that decides when to call a calculator tool
     instead of guessing -- the core idea behind real AI agents.
  2. A simplified sense-think-act loop for a self-driving car.

Both use the same underlying pattern: SENSE (get input) -> THINK (decide)
-> ACT (do something about it).
"""

import re


# ---------------------------------------------------------------------------
# Part 1: A tiny tool-using agent
# ---------------------------------------------------------------------------

def calculator_tool(expression):
    """A real 'tool' the agent can call -- guaranteed correct, unlike guessing."""
    # Only allow safe arithmetic characters for this classroom demo.
    if not re.fullmatch(r"[0-9+\-*/(). ]+", expression):
        return "Error: unsafe expression"
    return eval(expression)  # safe here because input is restricted above


def agent_respond(user_message):
    """A simplified agent: THINKS about whether it needs a tool, then ACTS."""
    math_pattern = re.search(r"[\d\s+\-*/().]{3,}", user_message)

    if math_pattern:
        # THINK: "this looks like math -- I shouldn't guess, I should use a tool"
        expression = math_pattern.group().strip()
        result = calculator_tool(expression)  # ACT: call the tool
        return f"I used the calculator tool for '{expression}' -> {result}"
    else:
        # THINK: "this is just conversation -- I can answer directly, no tool needed"
        return "That's not a math question, so I'll just answer directly: I'm a simple demo agent!"


def run_agent_demo():
    print("=== Part 1: Tool-Using Agent ===\n")
    test_messages = [
        "What is 3482 * 917?",
        "Hi, how are you?",
        "Can you compute (15 + 5) / 4 for me?",
    ]
    for msg in test_messages:
        print(f"You: {msg}")
        print(f"Agent: {agent_respond(msg)}\n")


# ---------------------------------------------------------------------------
# Part 2: Sense-think-act loop for a simplified self-driving car
# ---------------------------------------------------------------------------

def self_driving_decision(distance_to_object_m, is_pedestrian_detected, current_speed_kmh):
    """A simplified rule-based decision system -- real self-driving cars use
    ML models (Module 2/3) trained on millions of miles of data instead of
    simple hand-written rules, but the sense -> think -> act structure is the same."""
    if is_pedestrian_detected:
        return "STOP immediately"
    elif distance_to_object_m < 5:
        return "Brake hard"
    elif distance_to_object_m < 20:
        return "Slow down"
    else:
        return f"Continue at {current_speed_kmh} km/h"


def run_self_driving_demo():
    print("=== Part 2: Self-Driving Sense-Think-Act Loop ===\n")
    # Each dict below is one "frame" of sensor readings coming in over time.
    scenarios = [
        {"distance_to_object_m": 50, "is_pedestrian_detected": False, "current_speed_kmh": 60},
        {"distance_to_object_m": 15, "is_pedestrian_detected": False, "current_speed_kmh": 60},
        {"distance_to_object_m": 8, "is_pedestrian_detected": True, "current_speed_kmh": 40},
    ]

    for i, sensor_reading in enumerate(scenarios, start=1):
        decision = self_driving_decision(**sensor_reading)
        print(f"Frame {i}: sensors={sensor_reading} -> Decision: {decision}")

    print("\nTODO for students: add a rule for 'icy_road' or 'red_light_detected'!")


if __name__ == "__main__":
    run_agent_demo()
    print()
    run_self_driving_demo()
