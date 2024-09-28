import math

# Function to calculate tire volume
def calculate_tire_volume(width, aspect_ratio, diameter):
    # Formula for tire volume in liters
    volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return volume

# Get input from the user
width = float(input("Enter the width of the tire in millimeters (e.g., 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g., 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))

# Calculate the tire volume
volume = calculate_tire_volume(width, aspect_ratio, diameter)

# Display the result
print(f"The approximate volume of the tire is {volume:.2f} liters.")
