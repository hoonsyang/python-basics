f = open("/Users/beachmind/github/python-basics/code/새파일3.txt", 'a')
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close