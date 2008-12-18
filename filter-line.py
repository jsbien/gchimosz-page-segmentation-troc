import sys

def abs(x):
	if x >= 0:
		return x
	else:
		return -1 * x

def left_right(line):
	left, width = line.split()[0], line.split()[2]
	return int(left), int(left) + int(width)

f = open(sys.argv[1], "r")
boxes = f.read()
f.close()

begin = 0
end = 0
begin_count = 0
end_count = 0

# perform analysis
for line in boxes.splitlines():
	left, right = left_right(line)

	begin += int(left)
	end += right
	begin_count += 1
	end_count += 1

begin /= begin_count
end /= end_count

begin_dev = 0
end_dev = 0

for line in boxes.splitlines():
	left, right = left_right(line)

	begin_dev += (left - begin) ** 2
	end_dev += (right - end) ** 2

begin_dev /= begin_count
end_dev /= end_count

# save lines
i = 1
f = open(sys.argv[1], "w")
for line in boxes.splitlines():
	left, right = left_right(line)

	if abs(left - begin) < begin_dev and abs(right - end) < end_dev:
		f.write("(maparea \"#+0\" \"line " + str(i) + "\" (rect " + line + ") (none))\n")
		i += 1

f.close()
