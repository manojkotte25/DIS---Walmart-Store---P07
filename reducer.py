input = open("map_out.txt", "r") # open map_out.txt in read mode
lines = input.readlines() # read the data
max = lines[0].split('\t', 1)
output = open("red_out_max.txt", "w") # open red_out_max.txt in write mode
temp = max
for line in lines:
    m = line.split('\t', 1)
    if m[0].strip() == max[0].strip() :
        if float(m[1]) > float(max[1].strip()):
            max = m
    else:
        temp = max
        output.write("{0}\t{1}\n".format(max[0].strip(), max[1].strip()))
        max = m
if max[0] != temp[0]:
    output.write("{0}\t{1}\n".format(max[0].strip(), max[1].strip()))
input.close()
output.close()



input = open("map_out.txt", "r") # open map_out.txt in read mode
lines = input.readlines() # read the data
min = lines[0].split('\t', 1)
output = open("red_out_min.txt", "w") # open red_out_min.txt in write mode
temp = min
for line in lines:
    m = line.split('\t', 1)
    if m[0].strip() == min[0].strip() :
        if float(m[1]) < float(min[1].strip()):
            min = m
    else:
        temp = min
        output.write("{0}\t{1}\n".format(min[0].strip(), min[1].strip()))
        min = m
if min[0] != temp[0]:
    output.write("{0}\t{1}\n".format(min[0].strip(), min[1].strip()))
input.close()
output.close()