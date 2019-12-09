def get_segments(paths):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    points = []
    for p in paths:
        instr = p[0]
        val = int(p[1:])
        if instr == 'U':
            y2 += val
        elif instr == 'D':
            y2 -= val
        elif instr == 'R':
            x2 += val
        elif instr == 'L':
            x2 -= val
        else:
            raise RuntimeError('unknown direction {}'.format(instr))
        points.append((x1, y1, x2, y2))
        x1 = x2
        y1 = y2
    return points


def horizontal(segment):
    if segment[0] == segment[2]:
        return False
    return True


def between(val, lim1, lim2):
    if lim1 <= val <= lim2:
        return True
    elif lim2 <= val <= lim1:
        return True
    return False


def get_intersections(circ1, circ2):
    intersections = []
    for seg1 in circ1:
        for seg2 in circ2:
            if horizontal(seg1) and not horizontal(seg2):
                if between(seg1[1], seg2[1], seg2[3]) and between(seg2[0], seg1[0], seg1[2]):
                    intersections.append((seg1[1], seg2[0]))
            elif not horizontal(seg1) and horizontal(seg2):
                if between(seg2[1], seg1[1], seg1[3]) and between(seg1[0], seg2[0], seg2[2]):
                    intersections.append((seg2[1], seg1[0]))
    return intersections


def main():
    with open("input") as file:
        circuit1 = file.readline().split(',')
        circuit2 = file.readline().split(',')

    print(circuit1)
    print(circuit2)
    segments1 = get_segments(circuit1)
    segments2 = get_segments(circuit2)
    print(segments1)
    print(segments2)

    intersections = get_intersections(segments1, segments2)
    print(intersections)

    distances = list(map(lambda x: abs(x[0]) + abs(x[1]), intersections))
    print(distances)

    minvalue = min(filter(lambda x: x > 0, distances))

    print(minvalue)


main()
