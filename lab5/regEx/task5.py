import re

def qwe(s):
    if re.fullmatch(r'a.*b',s):
        return True
    else:
        return False
print(qwe("adsfkmsasadf"))
print(qwe("asdfsdkljmlb"))
print(qwe("asasdfsd asdfasdfb"))