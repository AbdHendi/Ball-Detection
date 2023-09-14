import numpy as np


class Blob:
    def __init__(self):
        self.centers = []
        self.y_positions = []

    def add(self, curr_center, centers_max_len=50):
        self.centers.append(curr_center)
        self.y_positions.append(curr_center[1])
        if len(self.centers) > centers_max_len:
            # pop the oldest center
            self.centers.pop(0)
            # pop the oldest y-coordinate
            self.y_positions.pop(0)

    def compute_speed(self):
        """
        Calculate the average speed of a blob
        :return: average speed
        """
        if len(self.centers) < 2:
            return 0
        distances = [np.linalg.norm(np.array(self.centers[i]) - np.array(self.centers[i - 1])) for i in
                     range(1, len(self.centers))]
        avg_speed = sum(distances) / len(distances)
        return avg_speed

    def compute_spread(self):
        """
        Calculate the spread of the movement
        :return: spread value
        """
        if not self.centers:
            return 0
        xs = [x for x, y in self.centers]
        ys = [y for x, y in self.centers]
        spread = np.std(xs) + np.std(ys)
        return spread

    def detect_bounce(self, threshold=580):
        # Check if we have enough points to determine bounce
        if len(self.y_positions) < 2:
            return False

        # If the ball was moving down and then moved up without reaching the bottom
        moving_down = self.y_positions[-2] < self.y_positions[-1]
        moved_up = self.y_positions[-1] > self.y_positions[-2]

        if moving_down and moved_up and self.y_positions[-1] < threshold:
            return True

        return False
