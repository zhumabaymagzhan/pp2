import re
def qwe(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)
print(qwe("DsdlfkpsdlKdlskflBdskfjs"))