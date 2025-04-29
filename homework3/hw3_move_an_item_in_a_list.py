l = [12, 3, 4, 10, 8]

if len(l) >= 2:
    last_element = l.pop()
    l.insert(0, last_element)
    print(l)
else:
    print(l)
