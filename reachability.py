from horsepad import HorsePad
import numpy as np


def reachability_recursive(pad: HorsePad, maxsteps: int):
    """recursive solution to Knight-on-Dialpad-Challenge"""

    # immediate result at path-length = 1
    result = 1

    # recursion anchor
    if maxsteps <= 1:
        return result

    # recursion
    else:
        for vertical in (-2, -1, 1, 2):     # over all possible move directions
            for horizontal in (-2, -1, 1, 2):
                if abs(vertical) + abs(horizontal) == 3:

                    offset = (vertical, horizontal)
                    if pad.move(offset):    # true only if move valid

                        result += reachability_recursive(pad, maxsteps - 1)

                        offset = (-vertical, -horizontal)   # reset cursor position
                        pad.move(offset)
    return result


def reachability_dynamic(pad: HorsePad, max_steps: int):
    """Dynamic programming implementation of reachability_recursive.
    HorsePad is basically omitted here, as its structure wouldn't allow such a calculation

    The resulting Matrix (not returned) has the following content:
    * if you start at x,y with i total steps, you have matrix[i,x,y] unique paths"""

    # base case
    if max_steps <= 1:
        return 1

    matrix = np.tile(pad.get_pad(), (max_steps, 1, 1))

    # init every viable start with 1
    matrix[matrix >= 0] = 1

    # hierarchically calculate every path from its possible follow-ups
    for i in range(1, matrix.shape[0]):     # over all cells
        for x in range(matrix.shape[1]):
            for y in range(matrix.shape[2]):

                for vertical in (-2, -1, 1, 2):     # all possible movements
                    for horizontal in (-2, -1, 1, 2):
                        if abs(vertical) + abs(horizontal) == 3:
                            if(0 <= x+vertical < matrix.shape[1] and
                                    0 <= y+horizontal < matrix.shape[2]):

                                # if current and previous cells are valid, add previous to current
                                if matrix[i-1, x+vertical, y+horizontal] >= 1 and \
                                        matrix[i, x, y] >= 0:
                                    matrix[i, x, y] += matrix[i-1, x+vertical, y+horizontal]

    # returns target cell at final interval
    trg = pad.loc()
    return matrix[max_steps-1, trg[0], trg[1]]






