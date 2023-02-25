def capitalize(s, ind):
    NewStr = ''
    for i in range(len(s)):
        if i in ind:
            NewStr += str. upper(s[i])
        else:
            NewStr += s[i]
    return NewStr
print(capitalize('aderty', [1, 2, 5]))