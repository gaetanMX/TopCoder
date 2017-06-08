class ABBA:

    def canObtain(self, initial, target):
        lastCharIndex = len(target)-1


        while len(initial)-1 != lastCharIndex:
            if(target[lastCharIndex]) == 'B':
                target = target[:-1]
                target = self.reverse(target)
            else:
                target = target[:-1]

            print(target)
            lastCharIndex -= 1

        if target == initial:
            return "Possible"
        else:
            return "Impossible"


    def reverse(self, s):
        return s[::-1]

if __name__ == "__main__":
        print(ABBA().canObtain("BBBBABABBBBBBA", "BBBBABABBABBBBBBABABBBBBBBBABAABBBAA"));


''' algo

start from last character  of target
if A 
    aMove
else 
    Bmove

when len(intial) == len(target)
    check if equals

'''
