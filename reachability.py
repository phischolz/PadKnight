from horsepad import HorsePad


def reachability_recursive(pad: HorsePad, maxsteps: int):
    result = 1
    if maxsteps <= 1:
        return result
    else:
        for vertical in (-2, -1, 1, 2):
            for horizontal in (-2, -1, 1, 2):
                if abs(vertical) + abs(horizontal) == 3:
                    offset = (vertical, horizontal)
                    if pad.move(offset):
                        result += reachability_recursive(pad, maxsteps - 1)
                        offset = (-vertical, -horizontal)
                        pad.move(offset)
    return result



