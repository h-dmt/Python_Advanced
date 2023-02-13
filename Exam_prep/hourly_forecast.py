# Write a function called forecast that stores information about the weather, and returns sorted
# information for all locations. The function will receive a different number of arguments.
# The arguments will be passed as tuples with two elements - the first one is the location,
# and the second one is the weather:
#     • Location name: string
#         ◦ any string
#     • Weather: string
#         ◦ "Sunny"
#         ◦ "Rainy"
#         ◦ "Cloudy"
# First, sort all locations by weather. First are positioned the locations with sunny weather,
# next are the locations with cloudy weather, and last are the locations with rainy
# weather. For each sequence of locations (e.g. all sunny locations), sort them by their name in ascending
# order (alphabetically).

def forecast(*args):
    forecasts = {'Sunny': [], 'Cloudy': [], 'Rainy': []}
    output_print = []
    for city, weather in args:
        forecasts[weather].append(city)
    for weather in forecasts:
        for city in sorted(forecasts[weather]):
            output_print.append(f"{city} - {weather}")
    return '\n'.join(output_print)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))