def canObtain(initial, target):
    listTocheck = [initial]
    for x in listTocheck:
        targetA = aMove(x)
        targetB = bMove(x)
        if targetA == target:
            print(targetA)
            return "Possible"
        elif targetB == target:
            print(targetB)
            return "Possible"
        else:
            listTocheck.extend([targetA,targetB])
            if len(targetA) > len(target):
                return "Impossible"

    return "Impossible"

def aMove(s):
    s += 'A'
    return s

def bMove(s):
    s = s[::-1]
    s += 'B'
    return s

print(canObtain("BBBBABABBBBBBA", "BBBBABABBABBBBBBABABBBBBBBBABAABBBAA"));

