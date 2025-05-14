import pytest
from workout_planner import calculate_bmi, workout_plan

def test_bmi_calculation():
    assert calculate_bmi(70, 170) == 24.22
    assert calculate_bmi(50, 160) == 19.53
    assert "Input Error" in calculate_bmi(-10, 170)
    assert "Input Error" in calculate_bmi("abc", 170)
    assert "Input Error" in calculate_bmi("", "")

def test_workout_plan():
    assert "light" in workout_plan(17)
    assert "moderate" in workout_plan(22)
    assert "intense" in workout_plan(27)
    assert "cardio" in workout_plan(31)
    assert "Input Error" in workout_plan("Input Error: Weight and height must be positive numbers.")
