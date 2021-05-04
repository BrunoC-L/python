# problem proposed by Mathologer in this video at 16:00
# https://www.youtube.com/watch?v=iJ8pnCO0nTY&ab_channel=Mathologer

positions = [1]

def getNextPosition(previous, previousPosition):
    if previousPosition % 2:
        return previous + previousPosition + 2
    else:
        return previous + int(previousPosition / 2) + 1

for i in range(666):
    positions.append(getNextPosition(positions[-1], len(positions) - 1))

print(f'there are {len(positions)} positions')

signs = [1 if int(i / 2) % 2 == 0 else -1 for i in range(667)]
print(positions[665:667])

partitionNumbers = [1]

for i in range(1, 667):
    num = 0
    for pos, sign in zip(positions, signs):
        if len(partitionNumbers) - pos >= 0:
            delta = sign * partitionNumbers[-pos]
            num += delta

    partitionNumbers.append(num)
    print(num)