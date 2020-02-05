import random

def getA(answerN):
    if answerN == 1:
        return 'It is c'
    elif answerN == 2:
        return 'It is d'
    elif answerN == 3:
        return 'Yes'
    elif answerN == 4:
        return 'R'

r = random.randint(1, 4)
fortune = getA(r)
print(fortune)