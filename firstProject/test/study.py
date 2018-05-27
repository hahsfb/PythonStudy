from socket import *

tcpid = socket(AF_INET, SOCK_STREAM)

tcpid.accept()










for i in [1, 2]:
    for j in [1, 2, 3]:
        print (i, j)
        break
    else:
        print ("for - j")
else:
    print("for - i")


def myfn():
    def myfn2():
        return "My Python"
    return myfn2()


print(myfn())
