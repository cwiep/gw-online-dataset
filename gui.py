#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys

def draw_trajectories(traj_list, invert_y=False):
    min_x = min(traj_list[0][:, 0]) - 20
    max_x = max(traj_list[0][:, 0]) + 20
    dpi = 50
    width = (max_x - min_x) / dpi
    fig = plt.figure(figsize=(width, 6), dpi=dpi)
    ax = fig.add_subplot(111)
    ax.hold(True)
    plt.axis("equal")
    plt.axis("off")
    # plt.axis('off')
    if invert_y:
        plt.gca().invert_yaxis()
    colormap = cm.get_cmap('jet')
    for idx, traj in enumerate(traj_list):
        color = colormap(idx / float(len(traj_list)))
        stroke_endpoints = np.where(traj[:, 2] == 1)[0]
        begin = 0
        col = 'black' if idx%2 == 0 else 'blue'
        for i, end in enumerate(stroke_endpoints):
            plt.plot(traj[:, 0], traj[:, 1], c="black", lw=5, marker=".")
            begin = end + 1
    plt.show()
    
def read_trajectory_from_file(file):
    """
    Reads points of an online trajectory from a textfile where
    each line is formatted as "x y penup". All entries have to be integers.
    penup is 0/1 depending on the state of the pen. An optional annotation of
    the presented word can be given on the first line

    :param file: Textfile containing points of a trajectory.
    :return: Numpy array with columns x, y and penup, annotation or None
    """
    points = []
    annotation = None
    with open(file, "r") as traj_file:
        for line in traj_file:
            parts = line.split(" ")
            if len(parts) != 3:
                annotation = line.strip()
                continue
            points.append([int(p.strip()) for p in parts])
    return np.array(points), annotation
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: gui.py <filename 1> <filename 2> ...")
        exit(0)
    for filename in sys.argv[1:]:
        traj, word = read_trajectory_from_file(filename)
        print("Showing plot for trajectory '{}'.".format(word))
        draw_trajectories([traj], True)
