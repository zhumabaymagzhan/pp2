import re

def qwe(s):
    camelCase = re.sub(r'_(.)', lambda x: x.group(1).upper(), s)
    return camelCase[0].lower() + camelCase[1:]


print(qwe("qwefdsfqa_afsdfasf_asafasd"))