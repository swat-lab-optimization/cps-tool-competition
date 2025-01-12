import math

class KinematicModel:
    def __init__(self, x, y, yaw, speed):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.speed = speed

    def update(self, steering, acceleration, delta_time):
        # Calculate the new yaw angle
        self.yaw += steering * delta_time

        # Calculate the new speed
        self.speed += acceleration * delta_time

        # Calculate the new x and y position
        self.x += self.speed * math.cos(self.yaw) * delta_time
        self.y += self.speed * math.sin(self.yaw) * delta_time
