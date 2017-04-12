f = open("Walmart_Features.txt","r")  # open file, read-only raw data
o = open("map_out.txt", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split("		") 
    if len(data) == 4:
        store, date, temp, price = data
        o.write("{0}\t{1}\n".format(store, price))
f.close()
o.close()






