f = open("/Users/beachmind/github/python-basics/code/새파일3.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()