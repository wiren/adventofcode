# pk = [5764801, 17807724]
pk = [2084668, 3704642]
loops = [1, 1]

for i in range(2):
    while pow(7, loops[i], 20201227) != pk[i]:
        loops[i] += 1

key = pow(pk[0], loops[1], 20201227)
print('Res:', key)
