input_path = 'advent_of_code_2022/challenges/Day 15: Beacon Exclusion Zone/input'

sensors = {} # sensor_point => [becon_point, distance]
beacons = {} # x: { y: true | Nothinng }
min_x = float('inf'); max_x = 0

# |x1 - x2| + |y1 - y2|
def manhattan_distance(p1, p2): return abs(p1[1] - p2[1]) + abs(p1[0] - p2[0])

with open(input_path) as f:
  for line in f:
    parts = line[:-1].split(': closest beacon is at ')

    # Sensor
    sensor_data = parts[0].split(' ')
    x_sensor_srt = sensor_data[-2][:-1].split('=')
    y_sensor_srt = sensor_data[-1].split('=')
    x_sensor = int(x_sensor_srt[-1])
    y_sensor = int(y_sensor_srt[-1])

    min_x = min(min_x, x_sensor)
    max_x = max(max_x, x_sensor)

    # Beacon
    beacons_parts = parts[1].split(', ')
    x_beacon_str = beacons_parts[0].split('=')
    y_beacon_str = beacons_parts[1].split('=')
    x_beacon = int(x_beacon_str[-1])
    y_beacon = int(y_beacon_str[-1])

    min_x = min(min_x, x_beacon)
    max_x = max(max_x, x_beacon)

    # Points
    sensor_point = [x_sensor, y_sensor] # (x, y)
    beacon_point = [x_beacon, y_beacon] # (x, y)

    if (x_beacon_str[-1] not in beacons): beacons[x_beacon_str[-1]] = {}

    beacons[x_beacon_str[-1]][y_beacon_str[-1]] = True

    sensors[''.join([x_sensor_srt[-1], ',', y_sensor_srt[-1]])] = [beacon_point, manhattan_distance(sensor_point, beacon_point)]

# Part 1
def part_1():
  counter = {}
  y = 2000000 # how many positions cannot contain a beacon?

  for sensor in sensors.keys():
    sensor_point = sensor.split(',')
    xp = int(sensor_point[0])
    yp = int(sensor_point[1])
    partial_distance = abs(yp - y)
    missing = sensors[sensor][1] - partial_distance
    if (missing > 0):
      for x in range(xp - missing, xp + missing):
        point_key = ''.join([str(x), ',', str(y)])
        if (point_key in sensors): continue
        counter[point_key] = True

  print('Part 1: ', counter.__len__())

def possible_points_to_distance(center, radius, max_val, min_val, how_far = 1):
  vals = []
  exceeded = radius + how_far
  for y in range(max(center[1] - exceeded, min_val), min(center[1] + exceeded + 1, max_val)):
    if (y >= min_val and y <= max_val):
      missing =  abs(center[1] - y)
      x_1 = center[0] - exceeded + missing
      x_2 = center[0] + exceeded - missing
      if (x_1 >= min_val and x_1 <= max_val): vals.append([x_1, y])
      if (x_2 >= min_val and x_2 <= max_val): vals.append([x_2, y])
  return vals

def is_contained(point, _from):
  for k in list(sensors.keys())[_from:]:
    sensor_point = k.split(',')
    d = manhattan_distance([int(sensor_point[0]), int(sensor_point[1])], point)
    if (d <= sensors[k][1]): return True
  
  return False

# Part 2
_max = 4000000; _min = 0; i = 0;
key = list(sensors.keys())[2]
_, distance = sensors[key]
points = possible_points_to_distance(list(map(int, key.split(','))), distance, _max, _min, 1)

for point in points:
  if (not is_contained(point, 0)): print('Part 2: ', (point[0] * _max) + point[1]); break