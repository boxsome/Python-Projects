# **Find Cost of Tile to Cover W x H Floor** - Calculate the total cost of tile it would take to
# cover a floor plan of width and length, using a cost entered by the user.
# I am going to assume the question meant to give width and length as opposed to width and length
import math


class TileCostCalculator(object):

    """Class representing cost of one tile with the specified dimensions.
        Used to calculate cost and number of tiles needed for a room.

    Attributes:
        l: length of tile
        w: width of tile
        tile_cost: cost of one tile
    """
    def __init__(self, w, l, tile_cost):
        self._w = w
        self._l = l
        self._tile_cost = tile_cost

    def get_total_cost(self, room_width, room_length):
        """Get total cost of tiles for a room with given dimensions."""
        return round(self._tile_cost * self.get_num_tiles(room_width, room_length), 2)

    def get_num_tiles(self, room_width, room_length):
        """Get total number of tiles needed for a room with given dimensions."""
        return math.ceil((room_width * room_length) / (self._l * self._w))

    #Properties and their setters
    @property
    def l(self):
        return self._l

    @l.setter
    def l(self, value):
        if not isinstance(value, float):
            raise TypeError("Height must be a positive number.")
        elif value <= 0:
            raise ValueError("Height cannot be 0 or negative.")

        self._l = value

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value):
        if not isinstance(value, float):
            raise TypeError("Width must be a positive number.")
        elif value <= 0:
            raise ValueError("Width cannot be 0 or negative.")

        self._w = value

    @property
    def tile_cost(self):
        return self._tile_cost

    @tile_cost.setter
    def tile_cost(self, value):
        if not isinstance(value, float):
            raise TypeError("Tile cost must be a positive number.")
        elif value <= 0:
            raise ValueError("Tile cost cannot be 0 or negative.")

        self._tile_cost = value


if __name__ == "__main__":
    print("Please enter space separated values for: tile-width tile-length tile-cost")
    tile_input = input()
    print("Please enter space separated values for: room-width room-length")
    room_input = input()

    tile_w, tile_l, tile_cost = map(float, tile_input.split(" "))
    room_w, room_l = map(float, room_input.split(" "))

    tile_cost_calc = TileCostCalculator(tile_w, tile_l, tile_cost)
    print("Tile cost is: {:.2f}".format(tile_cost_calc.get_total_cost(room_w, room_l)))
