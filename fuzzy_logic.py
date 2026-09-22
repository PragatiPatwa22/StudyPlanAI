import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


difficulty = ctrl.Antecedent(
    np.arange(0, 101, 1),
    "difficulty"
)

urgency = ctrl.Antecedent(
    np.arange(0, 101, 1),
    "urgency"
)

weakness = ctrl.Antecedent(
    np.arange(0, 101, 1),
    "weakness"
)

priority = ctrl.Consequent(
    np.arange(0, 101, 1),
    "priority"
)


difficulty["low"] = fuzz.trimf(
    difficulty.universe,
    [0, 0, 50]
)

difficulty["medium"] = fuzz.trimf(
    difficulty.universe,
    [25, 50, 75]
)

difficulty["high"] = fuzz.trimf(
    difficulty.universe,
    [50, 100, 100]
)


urgency["low"] = fuzz.trimf(
    urgency.universe,
    [0, 0, 50]
)

urgency["medium"] = fuzz.trimf(
    urgency.universe,
    [25, 50, 75]
)

urgency["high"] = fuzz.trimf(
    urgency.universe,
    [50, 100, 100]
)


weakness["low"] = fuzz.trimf(
    weakness.universe,
    [0, 0, 50]
)

weakness["medium"] = fuzz.trimf(
    weakness.universe,
    [25, 50, 75]
)

weakness["high"] = fuzz.trimf(
    weakness.universe,
    [50, 100, 100]
)


priority["low"] = fuzz.trimf(
    priority.universe,
    [0, 0, 40]
)

priority["medium"] = fuzz.trimf(
    priority.universe,
    [25, 50, 75]
)

priority["high"] = fuzz.trimf(
    priority.universe,
    [60, 100, 100]
)


rule1 = ctrl.Rule(
    difficulty["high"] | urgency["high"] | weakness["high"],
    priority["high"]
)

rule2 = ctrl.Rule(
    difficulty["medium"] & urgency["medium"],
    priority["medium"]
)

rule3 = ctrl.Rule(
    weakness["medium"] & urgency["medium"],
    priority["medium"]
)

rule4 = ctrl.Rule(
    difficulty["low"] & urgency["low"] & weakness["low"],
    priority["low"]
)

rule5 = ctrl.Rule(
    difficulty["low"] & urgency["medium"],
    priority["medium"]
)

rule6 = ctrl.Rule(
    difficulty["medium"] & urgency["high"],
    priority["high"]
)

rule7 = ctrl.Rule(
    difficulty["high"] & weakness["high"],
    priority["high"]
)


priority_control = ctrl.ControlSystem([
    rule1,
    rule2,
    rule3,
    rule4,
    rule5,
    rule6,
    rule7
])


def calculate_priority(
    difficulty_value,
    urgency_value,
    weakness_value
):

    simulation = ctrl.ControlSystemSimulation(
        priority_control
    )

    simulation.input["difficulty"] = difficulty_value
    simulation.input["urgency"] = urgency_value
    simulation.input["weakness"] = weakness_value

    simulation.compute()

    result = simulation.output["priority"]

    return result