# I used this to process it into json
# C++ is my main language but I decided that python would be easier
mapping = {}
with open("supp/codes.txt") as codes:
    while True:
        num = codes.readline()
        if (not num):
            break
        while (True):
            try:
                num = int(num)
                break
            except:
                num = codes.readline()
        key = codes.readline().rstrip()
        if (not key):
            break
        while (key == "\n"):
            key = codes.readline().rstrip()
        mapping[key] = num
print(mapping)