curYear = input()
curYear = str(int(curYear) + 1)

def by(curYear):
        if curYear[0] != curYear[1] and curYear[0] != curYear[2] and curYear[0] != curYear[3] and curYear[1] != curYear[2] and curYear[1] != curYear[3] and curYear[2] != curYear[3]:
            print(curYear)
        else:
            curYear = str(int(curYear) + 1)
            by(curYear)

by(curYear)
