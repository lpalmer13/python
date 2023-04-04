import math

temperature = float(input('What is the temperature? '))
wind_speed = int(input('What is the wind speed? '))
unit = input('Fahrenheit or Celsius (F/C)? ')

def compute_wind_chill(temperature):
    wind_chill_temperature = 35.74 + (0.6215 * temperature) - (35.75 * wind_speed ** 0.16) + (0.4275 * temperature * wind_speed ** 0.16)
    return wind_chill_temperature
    
total_wind_chill_temperature = compute_wind_chill(temperature)
print(f'At temperature {temperature}{unit}, and wind speed {wind_speed}mph, the windchill is: {total_wind_chill_temperature:.2f}{unit}')

