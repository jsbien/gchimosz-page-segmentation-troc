import sys
import math

def abs(x):
	if x >= 0:
		return x
	else:
		return -1 * x

def width_height(line):
	splited = line.split()
	width, height = splited[2], splited[3]
	return int(width), int(height)

f = open(sys.argv[1], "r")
boxes = f.read()
f.close()

width_avg = 0
height_avg = 0
count = 0

# perform analysis
for line in boxes.splitlines():
	width, height = width_height(line)

	width_avg += width
	height_avg += height

	count += 1

width_avg /= count
height_avg /= count

width_dev = 0
height_dev = 0

for line in boxes.splitlines():
	width, height = width_height(line)

	width_dev += (width - width_avg) ** 2
	height_dev += (height - height_avg) ** 2

width_dev = int(math.sqrt(width_dev / count))
height_dev = int(math.sqrt(height_dev / count))

#debug
print "width " + str(width_avg) + "; " + str(width_dev)
print "height " + str(height_avg) + "; " + str(height_dev)

# save lines
i = 1
f = open(sys.argv[1], "w")
for line in boxes.splitlines():
	width, height = width_height(line)

	if abs(width - width_avg) <= width_dev or abs(height - height_avg) <= height_dev:
		f.write(str(i) + " " + line + "\n")
		i += 1

f.close()
