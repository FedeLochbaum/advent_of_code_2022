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
