input_path = 'advent_of_code_2022/challenges/Day 15: Beacon Exclusion Zone/input'

sensors = {} # sensor_point => [becon_point, distance]
beacons = {} # x: { y: true | Nothinng }
min_x = float('inf'); max_x = 0

# |y1 - y2| + |x1 - x2|
def manhattan_distance(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

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

    sensor_point = [y_sensor, x_sensor]

    # Beacon
    beacons_parts = parts[1].split(', ')
    x_beacon_str = beacons_parts[0].split('=')
    y_beacon_str = beacons_parts[1].split('=')
    x_beacon = int(x_beacon_str[-1])
    y_beacon = int(y_beacon_str[-1])

    min_x = min(min_x, x_beacon)
    max_x = max(max_x, x_beacon)

    beacon_point = [y_beacon, x_beacon]

    if (y_beacon_str[-1] not in beacons): beacons[y_beacon_str[-1]] = {}
    beacons[y_beacon_str[-1]][x_beacon_str[-1]] = True

    sensors[''.join([y_sensor_srt[-1], ',', x_sensor_srt[-1]])] = [beacon_point, manhattan_distance(sensor_point, beacon_point)]

count = 0
row_to_check = 2000000 # how many positions cannot contain a beacon?
for c in range(min_x, max_x + 1):
  point_to_check = [row_to_check, c]
  if (str(row_to_check) in beacons and str(c) in beacons[str(row_to_check)]): continue # There is already a bacon here
  if (''.join([str(row_to_check), ',', str(c)]) in sensors): continue

  # Check with the rest of sensors
  for sensor in sensors.keys():
    sensor_point = sensor.split(',')
    dist = manhattan_distance(list(map(int, sensor_point)), point_to_check)
    if (dist <= sensors[sensor][1]): count += 1; break
  
print('Part 1: ', count)

# 4234241 too low
# 4271259 too low
# 4271260 too low