s = 'aviv423ADSD-'
flag = True
for c in s:
    if not c.isalpha() and not c.isdigit():
        flag = False
        break
print(flag)
