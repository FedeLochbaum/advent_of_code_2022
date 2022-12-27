input_path = 'advent_of_code_2022/challenges/Day 25: Full of Hot Air/input'
import math

SNAFU_DIGIT_TO_DECIMAL_DIGIT = { '-': -1, '=': -2, '0': 0, '1': 1, '2': 2 }
DECIMAL_DIGIT_TO_SNAFU_DIGIT = { -1: '-', -2: '=', 0: '0', 1: '1', 2: '2' }
DIGITS = [-2, -1, 0, 1, 2]
def decimal(snafu_number):
  dec = 0
  length = len(snafu_number)
  for i in range(length):
    dec += SNAFU_DIGIT_TO_DECIMAL_DIGIT[snafu_number[i]] * math.pow(5, abs(i - length))
  return dec

def value_of_power(power):
  res = 0
  while(power > 1): res += power * 2; power //= 5
  return res + 2

def snafu(dec, power):
  if dec in DIGITS: return DECIMAL_DIGIT_TO_SNAFU_DIGIT[dec]
  next_power_val = int(power / 5)
  for digit in DIGITS:
    mul = power * digit
    if abs(dec - mul) <= value_of_power(next_power_val):
      return DECIMAL_DIGIT_TO_SNAFU_DIGIT[digit] + snafu(dec - mul, next_power_val)

count = 0
power = 1
with open(input_path) as f:
  for line in f: count += decimal(line[:-1])

while count > value_of_power(power): power *= 5
print('Part 1: ', snafu(count, power))