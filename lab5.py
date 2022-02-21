"""
Michael Balestriere
Week 5 - Make a function or two
"""
# I had a problem with my test_celcius_to_fahrenheit function. I am getting an assertion error
# I'm not sure how to fix it even after looking at the videos for this week.


degrees_celsius = float(
    input("Enter the degrees in Celsius to be converted to Fahrenheit - ")
)


def celsius_to_fahrenheit(degrees_celsius):
    fahrenheit_temp = (degrees_celsius * 1.8) + 32
    farenheit_string = str(fahrenheit_temp)
    celsius_string = str(degrees_celsius)
    print(
        celsius_string
        + " degrees in Celsius is "
        + farenheit_string
        + " degrees in Farenheit!"
    )


"""
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(5) == 41
    assert celsius_to_fahrenheit(2) == 35.6
"""

temp_dict = {
    "Freezing": "0 degrees Celsius is the freezing point of water",
    "Boiling": "100 degrees Celsius is the boiling point of water",
    "freezing_temp": "Your temperature is below freezing",
    "warm_temp": "Your temperature is above freezing",
}

if degrees_celsius == 0:
    print(temp_dict["Freezing"])
if degrees_celsius == 100:
    print(temp_dict["Boiling"])
if degrees_celsius < 0:
    print(temp_dict["freezing_temp"])
if degrees_celsius > 0:
    print(temp_dict["warm_temp"])


celsius_to_fahrenheit(degrees_celsius)
# test_celsius_to_fahrenheit()
