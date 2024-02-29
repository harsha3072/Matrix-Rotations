def ReadMatrix():
  matrix = []
  for i in range(int(input())):
    row = [int(j) for j in input().split()]
    matrix.append(row) 
  return matrix


def Rotate(a = []):
    a1 = [[] for i in range(len(a))]
    for i in range(len(a)):
        for j in a[i]:
            a1[i].append(j)
    for x in range(len(a)):
        for y in range(len(a[x])):
            a1[y][len(a) - x - 1] = a[x][y]
    return a1

matrix = ReadMatrix()
matrix1 = [[] for i in range(len(matrix))]
for i in range(len(matrix)):
    for j in matrix[i]:
        matrix1[i].append(j)
rotation = 0
while True:
  line = input().split()
  if line[0] == "-1":
    break

  elif line[0] == "R":
    rotation += int(line[1])
    for i in range((int(line[1]) // 90) % 4):
        matrix = Rotate(matrix)

  elif line[0] == "U":
     matrix1[int(line[1])][int(line[2])] = int(line[3])
     matrix = matrix1.copy()
     for i in range((rotation // 90) % 4):
        matrix = Rotate(matrix)

  elif line[0] == "Q":
    print(matrix[int(line[1])][int(line[2])])

  else:
    print("Error: unexpected command '" + line[0] + "'")
    exit(1)
