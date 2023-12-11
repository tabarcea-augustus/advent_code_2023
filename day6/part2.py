'''
d - distance achieved
T - race time
h - hold time
D - minimum distance (target distance)
d = (T - h) * h
d = -h^2 + Th => parabola de la 0 la T pe x; de la 0 la max_distance in a race pe y
shift the quadratic eq by D, because that is the minimum distance we want
d = -h^2 + Th + D
'''
import math
import re


def solve_milisecond_interval(T, D):
    sol = (math.sqrt(T**2 - 4 * (D+0.01)) + T ) / 2
    sol2 = (-math.sqrt(T**2 - 4 * (D+0.01)) + T ) / 2

    sol = math.floor(sol)
    sol2 = math.ceil(sol2)

    return max(sol, sol2) - min(sol, sol2) + 1

with open('input.txt', 'r') as fd:


    lines = fd.readlines()
    times = lines[0].replace('Time:', '')
    times = re.sub(' +', ' ', times)
    times = times.replace('  ', ' ').replace('\n', '').split(' ')
    times = list(filter(lambda x: x, times))
    distances = lines[1].replace('Distance:', '')
    distances = re.sub(' +', ' ', distances)
    distances = distances.replace('  ', ' ').replace('\n', '').split(' ')
    distances = list(filter(lambda x: x, distances))

    print(times, distances)
    # times = list(map(lambda x: int(x), times))
    # distances = list(map(lambda x: int(x), distances))
    times = [int(''.join(times))]
    distances = [int(''.join(distances))]
    races = zip(times, distances)


prod = 1
for race in races:
    race_time = race[0]
    race_distance = race[1]
    print(race_time, race_distance)
    aux_ways = solve_milisecond_interval(race_time, race_distance)
    prod *= aux_ways
    print(aux_ways)

print(prod)