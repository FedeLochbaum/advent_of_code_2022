input_path = 'advent_of_code_2022/challenges/Day 6: Tuning Trouble/input'

packet_window = 4
message_window = 14

with open(input_path) as f:
  for line in f:
    for i in range(line[:-1].__len__()):
      if (i >= packet_window - 1):
        if (set(line[i - packet_window:i]).__len__() == packet_window): print('Part 1: ', i); break
      if (i >= message_window - 1):
        if (set(line[i - message_window:i]).__len__() == message_window): print('Part 2: ', i); break