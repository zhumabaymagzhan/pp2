import re

def qwe(s):
    replace= re.sub(r'[ .,]',':',s)
    return replace
print(qwe("asfdas dfsdafsdaf sdaf adsf"))