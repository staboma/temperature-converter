class TemperatureConverter:
   
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    
    def celsius_to_kelvin(celsius):
        return celsius + 273.15
    
    
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15
    
    
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
    
    
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32

# Örnek kullanım
if __name__ == "__main__":
    temp_in_celsius = 25
    temp_in_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_in_celsius)
    temp_in_kelvin = TemperatureConverter.celsius_to_kelvin(temp_in_celsius)

    print(f"{temp_in_celsius} Celsius = {temp_in_fahrenheit} Fahrenheit")
    print(f"{temp_in_celsius} Celsius = {temp_in_kelvin} Kelvin")

    temp_in_fahrenheit = 77
    temp_in_celsius = TemperatureConverter.fahrenheit_to_celsius(temp_in_fahrenheit)
    temp_in_kelvin = TemperatureConverter.fahrenheit_to_kelvin(temp_in_fahrenheit)

    print(f"{temp_in_fahrenheit} Fahrenheit = {temp_in_celsius} Celsius")
    print(f"{temp_in_fahrenheit} Fahrenheit = {temp_in_kelvin} Kelvin")

    temp_in_kelvin = 298.15
    temp_in_celsius = TemperatureConverter.kelvin_to_celsius(temp_in_kelvin)
    temp_in_fahrenheit = TemperatureConverter.kelvin_to_fahrenheit(temp_in_kelvin)

    print(f"{temp_in_kelvin} Kelvin = {temp_in_celsius} Celsius")
    print(f"{temp_in_kelvin} Kelvin = {temp_in_fahrenheit} Fahrenheit")