import funs

# lines = funs.lines_from_file("5.intest")
lines = funs.lines_from_file("5.in")

table = {ord('F'): ord('0'), ord('B'): ord('1'), ord('L'): ord('0'), ord('R'): ord('1')}

seats = []
for l in lines:
    row = int(l[:7].translate(table), 2)
    col = int(l[7:].translate(table), 2)
    seat = row * 8 + col
    seats += [seat]

seats = sorted(seats)
print(seats[len(seats) - 1])

for i in range(len(seats) - 1):
    if seats[i] + 1 != seats[i+1]:
        print(seats[i] + 1)