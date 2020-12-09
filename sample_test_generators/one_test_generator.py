import numpy as np
import math


class OneTestGenerator():
    """
        Generates a single test to show how to control the shape of the road by controlling the positio of the
        road points. We assume a map of 200x200
    """

    def __init__(self, time_budget=None, executor=None, map_size=None):
        self.time_budget = time_budget
        self.executor = executor
        self.map_size = map_size

    def start(self):
        print("Starting test generation")

        test = []

        # Create a vertical segment starting close to the left edge of the map
        x = 10.0
        y = 10.0
        length = 100.0
        interpolation_points = int(length / 10.0)
        for y in np.linspace(y, y + length, num=interpolation_points):
            test.append((x, y))

        # Create the 90-deg right turn
        radius = 20.0

        center_x = x + radius
        center_y = y

        interpolation_points = 5
        angles_in_deg = np.linspace(-60.0, 0.0, num=interpolation_points)

        for angle_in_rads in [ math.radians(a) for a in angles_in_deg]:
            x = math.sin(angle_in_rads) * radius + center_x
            y = math.cos(angle_in_rads) * radius + center_y
            test.append((x, y))

        # Create an horizontal segment, make sure the points line up with previous segment
        x += radius / 2.0
        length = 30.0
        interpolation_points = int(length / 10.0)
        for x in np.linspace(x, x + length, num=interpolation_points):
            test.append((x, y))

        # Now we add a final road point "below" the last one just to illustrate how the interpolation works
        y -= 50.0
        test.append((x, y, -28.0, 8.0))

        # Send the test for execution
        test_outcome, description, execution_data = self.executor.execute_test(test)

        # Print test outcome
        print(test_outcome, description)

