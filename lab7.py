"""
Michael Balestriere
week 7 - calculate BMI
"""


def calculate_bmi(weight, height):
    """bmi conversion"""
    bmi = round((weight / height**2) * 703, 1)
    print(f"Your bmi is {bmi}")
    return bmi


def bmi_to_cat(bmi):
    """returns bmi category"""
    if bmi <= 18.4:
        print("You are Underweight")
        return "Underweight"
    if 18.5 <= bmi <= 24.9:
        print("You are Healthy")
        return "Healthy"
    if 25.0 <= bmi <= 29.9:
        print("You are Overweight")
        return "Overweight"
    if bmi >= 30.0:
        print("You are Obese")
        return "Obese"


def test_calculate_bmi():
    """test bmi"""
    assert calculate_bmi(135, 68) == 20.5
    assert calculate_bmi(100, 60) == 19.5
    assert calculate_bmi(175, 72) == 23.7
    assert calculate_bmi(225, 77) == 26.7
    assert calculate_bmi(150, 65) == 25.0
    print("All checks match part 1 chart!")


def test_bmi_to_cat():
    """test cat"""
    assert bmi_to_cat(18) == "Underweight"
    assert bmi_to_cat(20.5) == "Healthy"
    assert bmi_to_cat(27.7) == "Overweight"
    assert bmi_to_cat(33) == "Obese"
    print("All categories check")


def main():
    """runs all"""
    test_calculate_bmi()
    test_bmi_to_cat()
    weight = float(input("Enter you weight "))
    height = float(input("Enter your height in inches "))
    bmi = calculate_bmi(weight, height)
    cat = bmi_to_cat(bmi)


main()
