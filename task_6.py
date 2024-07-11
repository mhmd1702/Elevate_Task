def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Simple Measurement Converter")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")
    print("5. Liters to Gallons")
    print("6. Gallons to Liters")
    print("7. Celsius to Fahrenheit")
    print("8. Fahrenheit to Celsius")
    print("9. Exit")
    
    choice = input("Choose the type of conversion (1-9): ")
    
    if choice == '1':
        meters = get_float_input("Enter meters: ")
        print(f"{meters} meters is {meters_to_feet(meters):.2f} feet")
    elif choice == '2':
        feet = get_float_input("Enter feet: ")
        print(f"{feet} feet is {feet_to_meters(feet):.2f} meters")
    elif choice == '3':
        kilograms = get_float_input("Enter kilograms: ")
        print(f"{kilograms} kilograms is {kilograms_to_pounds(kilograms):.2f} pounds")
    elif choice == '4':
        pounds = get_float_input("Enter pounds: ")
        print(f"{pounds} pounds is {pounds_to_kilograms(pounds):.2f} kilograms")
    elif choice == '5':
        liters = get_float_input("Enter liters: ")
        print(f"{liters} liters is {liters_to_gallons(liters):.2f} gallons")
    elif choice == '6':
        gallons = get_float_input("Enter gallons: ")
        print(f"{gallons} gallons is {gallons_to_liters(gallons):.2f} liters")
    elif choice == '7':
        celsius = get_float_input("Enter Celsius: ")
        print(f"{celsius}°C is {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == '8':
        fahrenheit = get_float_input("Enter Fahrenheit: ")
        print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    elif choice == '9':
        print("Exiting...")
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == '__main__':
    main()
