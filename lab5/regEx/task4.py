import re

def qwe(s):
    if re.findall(r'[A-Z]+[a-z]+',s):
        return True
    else:
        return False
print(qwe("Adsadas"))
print(qwe("adsadas"))
print(qwe("AASDASD"))
print(qwe("adsSdas"))