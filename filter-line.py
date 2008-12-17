import sys

OFFSET = 700

def abs(x):
	if x >= 0:
		return x
	else:
		return -1 * x

f = open(sys.argv[1], "r")
boxes = f.read()
f.close()

begin = 0
end = 0
begin_count = 0
end_count = 0

# perform analysis
for line in boxes.splitlines():
	left, width = line.split()[1], line.split()[3]
	right = int(left) + int(width)

	begin += int(left)
	end += right
	begin_count += 1
	end_count += 1

begin /= begin_count
end /= end_count

# save lines
i = 1
f = open(sys.argv[1], "w")
for line in boxes.splitlines():
	left, width = line.split()[1], line.split()[3]
	right = int(left) + int(width)
	if abs(int(left) - begin) < OFFSET and abs(right - end) < OFFSET:
		f.write("(maparea \"#+0\" \"line " + str(i) + "\" (rect " + line + ") (none))\n")
		i += 1

f.close()
