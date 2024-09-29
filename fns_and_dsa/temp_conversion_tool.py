CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9


def convert_to_celsius(fahrenheit):
 
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 

def convert_to_fahrenheit(celsius):
   
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def get_temperature_input():
  
    temp_input = input("Enter the temperature to convert: ")
    try:
        temperature = float(temp_input)
        return temperature
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def get_unit_input():
   
    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if unit_input not in ['C', 'F']:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    return unit_input

def main():
   
    print("=== Temperature Conversion Tool ===")
    
    try:
        temperature = get_temperature_input()
        unit = get_unit_input()
        
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:  
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
    
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()


