
def find_max_min(l):
    mimx = []
    l.sort()

    if l[0] == l[len(l) - 1]:
        mimx.append(len(l))
    else:
        mimx.append(l[0])
        mimx.append(l[len(l)-1])

    return mimx
