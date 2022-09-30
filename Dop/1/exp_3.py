data = open('file.txt','w')
data.write('line 1\n')
data.write('line 2\n')
data.close()
data = open('file.txt', 'r')
for i in data:
    print(i)
while True:
    line = data.readline()
    if not line:
        break
    print(line.strip())
print(line)
data.close()