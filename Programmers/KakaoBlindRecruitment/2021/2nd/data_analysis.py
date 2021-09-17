import json
from collections import defaultdict
from matplotlib import pyplot as plt
import numpy as np

rent_dict = defaultdict(list)
return_dict = defaultdict(list)

with open("dataset/problem2_day-1.json") as json_file:
    json_data = json.load(json_file)
    for time in json_data:
        for data in json_data[time]:
            rent_dict[data[0]].append(int(time))
            return_dict[data[1]].append(int(time) + data[2])


def draw():
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Horizontally stacked subplots')
    ax1.bar(rent_dict.keys(), [len(rent_dict[x]) for x in rent_dict])
    ax1.set_title('rent')
    ax2.bar(return_dict.keys(), [len(return_dict[x]) for x in return_dict])
    ax2.set_title('return')
    plt.show()