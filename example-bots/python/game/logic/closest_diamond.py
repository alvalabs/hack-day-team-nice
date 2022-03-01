import random
from ..util import get_direction, position_equals


class ClosestDiamondLogic(object):
    def __init__(self):
        self.goal_position = None
        self.previous_position = (None, None)
        self.turn_direction = 1

    def next_move(self, board_bot, board):
        props = board_bot["properties"]
        current_position = board_bot["position"]

        # Analyze new state
        if props["diamonds"] == 5:
            # Move to base if we are full of diamonds
            base = props["base"]
            self.goal_position = base
        elif self.goal_position is None or position_equals(
            current_position, self.goal_position
        ):
            # Move towards a random diamond on board
            tries = len(board.diamonds)
            index = self.closest_diamond(current_position, board.diamonds)

            while tries > 0:
              diamond = board.diamonds[index]
              # Check if we can pick this diamond up before moving to it
              worth = diamond["properties"]["points"]
              space_left = props["inventorySize"] - props["diamonds"]
              if diamond["properties"]["points"] > space_left:
                # Nope, no space left in inventory. Try another one
                index = (index + 1) % len(board.diamonds)
                tries -= 1
              else:
                # Ok walk towards this diamond
                self.goal_position = board.diamonds[index].get('position')
                break


        if self.goal_position:
            current_position = board_bot["position"]
            cur_x = current_position["x"]
            cur_y = current_position["y"]

            # Calculate move according to goal position
            delta_x, delta_y = get_direction(
                current_position["x"],
                current_position["y"],
                self.goal_position["x"],
                self.goal_position["y"],
            )

            if (cur_x, cur_y) == self.previous_position:
                # We did not manage to move, lets take a turn to hopefully get out stuck position
                if delta_x != 0:
                    delta_y = delta_x * self.turn_direction
                    delta_x = 0
                elif delta_y != 0:
                    delta_x = delta_y * self.turn_direction
                    delta_y = 0
                # Switch turn direction for next time
                self.turn_direction = -self.turn_direction
            self.previous_position = (cur_x, cur_y)

            return delta_x, delta_y

        return 0, 0

    @staticmethod
    def closest_diamond(self, current_position, diamonds):
        diamond_distances = []
        for i in enumerate(diamonds):
            diamond_position = diamonds[i].get('position')
            distance = self.manhattan_distance(current_position, diamond_position)
            diamond_distances.append((distance, diamond_position["x"], diamond_position["y"], i))

        diamond_distances.sort(key=self.sort_distance)

        (distance, diamondX, diamondY, i) = diamond_distances[0]
        return i

    @staticmethod
    def sort_distance(e):
        (distance, diamondX, diamondY) = e
        return distance

    @staticmethod
    def manhattan_distance(point1, point2):
        print('diamond position' + point2)
        distance = 0
        for x1, x2 in zip(point1, point2):
            difference = x2 - x1
            absolute_difference = abs(difference)
            distance += absolute_difference

        return distance