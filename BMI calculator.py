def calculate_bmi():
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))

        if weight <= 0 or height <= 0:
            print("⚠️ Please enter positive values for both weight and height.")
            return

        bmi = weight / (height ** 2)
        print(f"\n✅ Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"📊 BMI Category: {category}")

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")

# Run the BMI calculator
calculate_bmi()
