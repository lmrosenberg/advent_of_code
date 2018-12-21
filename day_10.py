import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--testing', default=False, type=bool)
args = parser.parse_args()

sample = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>"""


def processing(input, testing=False):
    positions = dict()
    velocity = dict()

    if testing:
        for point, line in enumerate(input.splitlines()):
            positions[point] = (int(line[10:12]), int(line[14:16]))
            velocity[point] = (int(line[28:30]), int(line[31:34]))

    else:
        for point, line in enumerate(input.splitlines()):
                positions[point] = (int(line[10:16]), int(line[18:24]))
                velocity[point] = (int(line[36:38]), int(line[39:42]))


    return positions, velocity


def graph_it(current_postions):
    xs = [i[0] for i in current_postions.values()]
    ys = [i[1] for i in current_postions.values()]

    plt.scatter(x=xs, y=ys, c='black', marker='o')
    plt.show()


def move_points(current_positions, velocity):
    for point in current_positions.keys():
        current_positions[point] = (current_positions[point][0] + velocity[point][0],
                                    current_positions[point][1] + velocity[point][1])
    return current_positions


def main():
    if args.testing:
        input = sample
    else:
        with open('inputs/day_10.txt') as file:
            input = file.read()

    positions, velocity = processing(input)
    while 1 == 1:
        graph_it(positions)
        positions = move_points(positions, velocity)


if __name__ == "__main__":
    main()
