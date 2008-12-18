import sys
import math

def abs(x):
	if x >= 0:
		return x
	else:
		return -1 * x

def left_right_height(line):
	left, width, height = line.split()[0], line.split()[2], line.split()[3]
	return int(left), int(left) + int(width), int(height)

f = open(sys.argv[1], "r")
boxes = f.read()
f.close()

left_avg = 0
right_avg = 0
height_avg = 0
count = 0

# perform analysis
for line in boxes.splitlines():
	left, right, height = left_right_height(line)

	left_avg += left
	right_avg += right
	height_avg += height

	count += 1

left_avg /= count
right_avg /= count
height_avg /= count

left_dev = 0
right_dev = 0
height_dev = 0

for line in boxes.splitlines():
	left, right, height = left_right_height(line)

	left_dev += (left - left_avg) ** 2
	right_dev += (right - right_avg) ** 2
	height_dev += (height - height_avg) ** 2

left_dev = int(math.sqrt(left_dev / count))
right_dev = int(math.sqrt(right_dev / count))
height_dev = int(math.sqrt(height_dev / count))

#debug
print "left " + str(left_avg) + "; " + str(left_dev)
print "right " + str(right_avg) + "; " + str(right_dev)
print "height " + str(height_avg) + "; " + str(height_dev)

# save lines
i = 1
f = open(sys.argv[1], "w")
for line in boxes.splitlines():
	left, right, height = left_right_height(line)

	if abs(left - left_avg) <= left_dev and abs(right - right_avg) <= right_dev and abs(height - height_avg) <= height_dev:
		f.write("(maparea \"#+0\" \"line " + str(i) + "\" (rect " + line + ") (none))\n")
		i += 1

f.close()
