import numpy as np


class HorsePad:
    """
    Implementation of a chess-style board by using a ndarray, encoding reachable fields with values >=0.
    Therefore, the shape of the board doesn't have to be square.

    *   The board also memorizes a 'cursor' position which can be changed via respective methods.
    *   Changing of values is only possible at the current location.
    *   (Locations marked negative therefore stay unreachable forever)
    """

    def __init__(self, pad: np.ndarray = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [-1, 0, -1]]),
                 start_position: tuple = (0, 0)):
        """

        :param pad: Configuration of the board. Values <0 are interpreted as unreachable (not part of the board)
        :param start_position: first position of the cursor.
        """

        # TODO clean up assertions
        assert all(shape > 0 for shape in pad.shape), "Shape invalid"
        assert pad.ndim == 2, "Dimensions invalid"
        self.__pad = pad

        assert self.is_within(start_position), "Starting point invalid"
        self.__loc = start_position

        return

    def is_within(self, loc: tuple):
        """returns true, iff given location is on the board."""

        if self.__pad.shape[0] > loc[0] >= 0 & loc[1] >= 0 and loc[1] < self.__pad.shape[1] and \
                self.__pad[loc[0], loc[1]] >= 0:
            return True
        else:
            return False

    #
    def loc(self, offset: tuple =(0, 0)):
        """returns current location, offset by given tuple.
        *Warning: result my be invalid location!"""
        return tuple(sum(x) for x in zip(self.__loc, offset))

    def move(self, offset):
        """attempts to move cursor by given offset. Returns true, iff it successfully changed cursor"""
        trg_loc = self.loc(offset)
        if self.is_within(trg_loc):
            self.__loc = trg_loc
            return True
        else:
            return False
