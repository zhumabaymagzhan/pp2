import re

def qwe(s):
    return re.split(r'(?=[A-Z])', s)

print(qwe("SzfsfsSfsdfsdCsdfsc"))