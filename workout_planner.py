def calculate_bmi(weight, height_cm):
    try:
        weight = float(weight)
        height_cm = float(height_cm)

        if weight <= 0 or height_cm <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)

    except ValueError as e:
        return f"Input Error: {e}"


def workout_plan(bmi):
    try:
        if isinstance(bmi, str):
            return bmi

        if bmi < 18.5:
            return "Workout: 20 mins/day (light)\nDiet: High-protein meals"
        elif 18.5 <= bmi < 24.9:
            return "Workout: 30 mins/day (moderate)\nDiet: Balanced diet"
        elif 25 <= bmi < 29.9:
            return "Workout: 45 mins/day (intense)\nDiet: Low-carb meals"
        else:
            return "Workout: 60 mins/day (intense + cardio)\nDiet: Very low-carb, high-protein"
    except Exception as e:
        return f"Error in workout plan: {e}"
if __name__ == "__main__":
    print("=== Workout Time Planner ===")

    weight = input("Enter your weight in kg: ")
    height_cm = input("Enter your height in cm: ")

    bmi = calculate_bmi(weight, height_cm)
    print(f"\nYour BMI: {bmi}")

    plan = workout_plan(bmi)
    print(f"\n{plan}")
