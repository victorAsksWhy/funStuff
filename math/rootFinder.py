def rootFinder(minimum, maximum, root):
    found = []
    for x in range(minimum, maximum + 1):
        answer = pow(minimum, 1.0/root)
        if answer % 1 == 1:
            found.append(answer)
        minimum = minimum + 1
        return found
    
print(rootFinder(1,99999,3))