import sys
read = sys.stdin.readline

N = int(read().rstrip())
SWITCH = list(map(int, read().rstrip().split(' ')))
STUDENT_LEN = int(read().rstrip())
STUDENTS = [[*map(int, read().rstrip().split(' '))] for _ in range(STUDENT_LEN)]


def toggleSwitch(num):
  if num == 1:
    return 0
  return 1

def studentOfBoy(num):
  step = 1
  while True:
    if (num*step) > len(SWITCH):
      break

    SWITCH[(num*step)-1] = toggleSwitch(SWITCH[(num*step)-1])
    step += 1

def studentOfGirl(num):
  SWITCH[num-1] = toggleSwitch(SWITCH[num-1])
  step = 1
  while True:
    if (num-step) <= 0 or (num+step) > len(SWITCH):
      break

    left = SWITCH[num-1-step]
    right = SWITCH[num-1+step]
    if left == right:
      SWITCH[num-1-step] = toggleSwitch(SWITCH[num-1-step])
      SWITCH[num-1+step] = toggleSwitch(SWITCH[num-1+step])
      step += 1
      continue
    break

for gen, num in STUDENTS:
  if gen == 1:
    studentOfBoy(num)
  if gen == 2:
    studentOfGirl(num)

start = 0
end = 20
while start < len(SWITCH):
  print(*SWITCH[start:end])
  start += 20
  end += 20