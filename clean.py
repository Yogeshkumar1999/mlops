f = open("req.txt")
f1 = open("requirment.txt", "w")
for line in f:
    line = line.strip()
    data = line.split("=")[0]
    f1.write(data)
    f1.write("\n")

f1.close()

