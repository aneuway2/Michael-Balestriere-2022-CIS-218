"""
Michael Balestriere
Week 5 - Make a function or two
"""

degrees_celsius = float(
    input("Enter the degrees in Celsius to be converted to Fahrenheit - ")
)

temp_dict = {
    0: "0 degrees Celsius is the freezing point of water",
    100: "100 degrees Celsius is the boiling point of water",
    "freezing": "Your temp is below freezing",
    "warm": "your temp is above freezing",
}

if temp_dict.get(degrees_celsius):
    print(temp_dict.get(degrees_celsius))
if degrees_celsius <= 0:
    print(temp_dict.get("freezing"))
else:
    print(temp_dict.get("warm"))


def celsius_to_fahrenheit(degrees_celsius=0):
    """converts celsius to fahrenheit"""
    fahrenheit_temp = (degrees_celsius * 1.8) + 32
    print(f"{fahrenheit_temp} is your number converted to Fahreheit")
    return fahrenheit_temp


def test_celsius_to_fahrenheit():
    """test function"""
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(5) == 41
    assert celsius_to_fahrenheit(2) == 35.6


celsius_to_fahrenheit(degrees_celsius)
test_celsius_to_fahrenheit()
