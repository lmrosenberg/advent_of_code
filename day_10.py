import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse
import time

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


def processing(raw_text, testing=False):
    positions = []
    velocity = []

    if testing:
        for line in raw_text.splitlines():
            positions.append((int(line[10:12]), int(line[14:16])))
            velocity.append((int(line[28:30]), int(line[31:34])))

    else:
        for line in raw_text.splitlines():
            positions.append((int(line[10:16]), int(line[18:24])))
            velocity.append((int(line[36:38]), int(line[39:42])))

    points = np.array([positions, velocity])

    return points, positions, velocity


def move_points(frame_number):
    print(frame_number, ax.get_xlim()[0], ax.get_xlim()[1])

    if frame_number < 100:
        points[0] = points[0] + 100*points[1]
    elif frame_number < 176:
        points[0] = points[0] + 5*points[1]
    #elif frame_number < 150:
    #    points[0] = points[0] + points[1]
    else:
        if ax.get_xlim()[0] < 172.447870968:
            points[0] = points[0] + points[1]
        else:
            print(points[0][22], refpoint)
            exit()
    ax.clear()
    scat = ax.scatter(x=[x[0] for x in points[0]],
                      y=[x[1] for x in points[0]], c='black', marker='o',
                      label=frame_number)
    print("I'm doing something")


if args.testing:
    in_text = sample
else:
    with open('inputs/day_10.txt') as file:
        in_text = file.read()

points, positions, velocity = processing(in_text, args.testing)

refpoint = (points[0][22], points[1][22])

if args.testing:
    fig, ax = plt.subplots(figsize=(5, 3))

else:
    fig, ax = plt.subplots(figsize=(10, 10))

counter = 1
scat = ax.scatter(x=[x[0] for x in points[0]], y=[x[1] for x in points[0]],
                  c='black', marker='o')
anim = FuncAnimation(fig, move_points, interval=10)

plt.show()
