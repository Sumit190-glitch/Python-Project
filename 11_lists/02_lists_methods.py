advance = [45 , 78, 90, 100]
advanced = [45, 45, 45, 45, 45]
advance.append(20)
advance.extend(advanced)
advance.insert(2, 50)
advance.remove(78)
advance.pop(3)
advance.sort()
advance.reverse()
advance.__add__(advanced)
print(advance)