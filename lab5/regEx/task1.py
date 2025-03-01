import re

def match_pattern(s):
    pattern = r"ab*" 
    if re.fullmatch(pattern, s):
        return True
    return False

s = int(input())
arr = []
for i in range(s):
    us_input = input()
    arr.append(us_input)
for s in arr:
    print(f"{s}: {match_pattern(s)}")
