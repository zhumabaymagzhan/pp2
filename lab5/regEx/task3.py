import re

def asd(s):
    if re.findall(r'[a-z]+_+[a-z]',s):
        return True
    else:
        return False
print(asd("asdasda_asdasdas"))
print(asd("asdfdsfasd"))