## Calculate the supossed score if you follow the input strategy
input_path = 'advent_of_code_2022/challenges/Day 2: Rock Paper Scissors/input'

# Part 1
score = 0

shape_score = { 'A': 1, 'B': 2, 'C': 3 }

input_to_play = { 'X': 'A', 'Y': 'B', 'Z': 'C' }

round_score = { 'A': { 'A': 3, 'B': 6, 'C': 0 }, 'B': { 'A': 0, 'B': 3, 'C': 6 }, 'C': { 'A': 6, 'B': 0, 'C': 3 } }

with open(input_path) as f:
  for line in f:
    oponent_play, play = line[:-1].split(' ')
    my_play = input_to_play[play]
    score += shape_score[my_play] + round_score[oponent_play][my_play]

print('Part1: ', score)

# Part 2
score = 0

score_by_expected = { 'X': 0, 'Y': 3, 'Z': 6 }

play_by_result = { 'A': { 'X': 'C', 'Y': 'A', 'Z': 'B' }, 'B': { 'X': 'A', 'Y': 'B', 'Z': 'C' }, 'C': { 'X': 'B', 'Y': 'C', 'Z': 'A' } }

with open(input_path) as f:
  for line in f:
    oponent_play, expected_result = line[:-1].split(' ')
    my_play = play_by_result[oponent_play][expected_result]
    score += shape_score[my_play] + score_by_expected[expected_result]

print('Part2: ', score)