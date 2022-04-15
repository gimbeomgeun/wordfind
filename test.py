with open("word.txt", "r") as f:
           data = f.read()
           
lines=data.split("\n")
print(lines)

for y in range(len(lines)):
           for x in range(len(lines[y])):
                          if lines[y][x] == "a":
                                     print(x,y)
