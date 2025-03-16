import random

# Constant settings
RADIUS = 1
NUM_POINTS = 1000000
AREA_FACTOR = 4
SQUARE_EXPONENT = 2
POINT_COUNT_INCREMENT = 1

INSIDE_CIRCLE = 0

# Randomly generate points and count those inside the circle
for i in range(NUM_POINTS):
    x = random.uniform(-RADIUS, RADIUS)
    y = random.uniform(-1, 1)
    if x**SQUARE_EXPONENT + y**2 <= RADIUS**SQUARE_EXPONENT:
        INSIDE_CIRCLE += POINT_COUNT_INCREMENT

# Estimate pi based on the number of points inside the circle
PI = (INSIDE_CIRCLE / NUM_POINTS) * AREA_FACTOR

print(f"Estimated value of pi is: {PI}")
