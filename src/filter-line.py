#
# DjVu line numerator box filter (c) Grzegorz Chimosz 2008-2009
# released under GNU GPL with ABSOLUTELY NO WARRANTY
#

import sys
import math

#
# auxiliary functions
#

def abs(x):
	if x >= 0:
		return x
	else:
		return -1 * x

def boxcmp((l1, b1, w1, h1), (l2, b2, w2, h2)):
	if (b2 - b1) == 0:
		return l2 - l1
	else:
		return b2 - b1

#
# read and parse file
#

f = open(sys.argv[1], "r")
boxes = []

for line in f:
	[left, bottom, width, height] = line.split()

	# cast to integers
	left = int(left)
	bottom = int(bottom)
	width = int(width)
	height = int(height)

	# add tuple to list
	boxes.append((left, bottom, width, height))

f.close()

boxes.sort(cmp=boxcmp)


#
# perform analysis
#

count = 0 # number of boxes

width_avg = 0
height_avg = 0

for box in boxes:
	_, _, width, height = box

	width_avg += width
	height_avg += height

	count += 1

if count == 0:
	exit()

width_avg /= count
height_avg /= count

width_dev = 0
height_dev = 0

for box in boxes:
	_, _, width, height = box

	width_dev += (width - width_avg) ** 2
	height_dev += (height - height_avg) ** 2

width_dev = int(math.sqrt(width_dev / count))
height_dev = int(math.sqrt(height_dev / count))

#debug
print "width (avg:)" + str(width_avg) + "; (dev:)" + str(width_dev)
print "height (avg:)" + str(height_avg) + "; (dev:)" + str(height_dev)


#
# save result
#

i = 1
f = open(sys.argv[1], "w")
r = open(sys.argv[1] + "-rejected", "w")

for box in boxes:
	left, bottom, width, height = box
	line = str(left) + " " + str(bottom) + " " + str(width) + " " + str(height) + "\n"

	if abs(width - width_avg) <= width_dev or abs(height - height_avg) <= height_dev:
		f.write(str(i) + " " + line)
		i += 1
	else:
		r.write(line)

f.close()
