import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--testing', default=False, type=bool)
args = parser.parse_args()


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


def move_points(current_positions):
    for point in current_positions.keys():
        current_positions[point] = (current_positions[point][0] + velocity[point][0],
                                    current_positions[point][1] + velocity[point][1])
    #return current_positions

if args.testing:
    input = sample
else:
    with open('inputs/day_10.txt') as file:
        input = file.read()
positions, velocity = processing(input, args.testing)

fig, ax = plt.subplots(figsize=(5, 3))

xs = [i[0] for i in positions.values()]
ys = [i[1] for i in positions.values()]

scat = ax.scatter(x=xs, y=ys, c='black', marker='o')
anim = FuncAnimation(
    fig, move_points, interval=100, frames=100)

plt.draw()
plt.show()
