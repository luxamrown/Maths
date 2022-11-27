import operator

eqForm = "ax + b = c"
operators = ["+", "-", "/", "."]
ops = { "+": operator.add, "-": operator.sub, "/":operator.truediv, ".":operator.mul }

linearEquation = input(str("Enter equation 1 var: "))

def joinOpWithInt(list):
    res = []
    # print(list[0] == str(operators[1]))
    # print("initt", list)
    if list[0] != str(operators[1]) and list[0] != str(operators[0]):
        list.insert(0, "+")

    # print("liss",list)
    for idx in range(len(list)):
        if idx % 2 != 0:
            res.append(list[idx-1:idx+1])
        for idxRes in range(len(res)):
            res[idxRes] = "".join(res[idxRes])
    return res

# print(joinOpWithInt(['+', '2', '-', '5']))

def extractOpWithInt(list):
    extractRes = []

    for idx in range(len(list)):
        extractRes.append(list[idx][0])
        extractRes.append(list[idx][1:])

    return extractRes


def getKoef(eq, var):
    splitedEq = eq.split()
    return splitedEq[0][0:splitedEq[0].index(var)]

def getVar(var):
    return var[-1]

def getRightSection(splitedEq):
    return splitedEq[splitedEq.index("=")+1:]

def getLeftSectionWithoutVar(splitedEq):
    return splitedEq[1:splitedEq.index("=")]

def getInitVar(eq):
    splitedEq = eq.split()
    var = splitedEq[0]

    konsts = getLeftSectionWithoutVar(splitedEq)
    rightSec = getRightSection(splitedEq)
    
    print("{} {} = {}".format(var, " ".join(konsts), " ".join(rightSec)))

    return var, joinOpWithInt(konsts), joinOpWithInt(rightSec)



def doAddSubbRightSec(list):
    result = 0
    dividedListInt = len(list) // 4
    remainInt = []
    listIteration = 0
    selectedRangeList = []


    if len(list) % 4 != 0:
        remainInt.append(list[-2:])
        
    while listIteration != dividedListInt:
        for idxL in range(1, len(list)+1):
            if idxL % 4 == 0:
                selectedRangeList.append(list[idxL-4:idxL])
                listIteration += 1

    for idxL in range(len(selectedRangeList)):
        for idxI in range(len(selectedRangeList[idxL])):
            if idxI > 0:
                if selectedRangeList[idxL][idxI] in operators:
                    # print("{} {} {}".format(int(selectedRangeList[idxL][idxI-1]) * (-1 if selectedRangeList[idxL][idxI-2] == "-" else 1),ops[selectedRangeList[idxL][idxI]],int(selectedRangeList[idxL][idxI+1]) * (-1 if selectedRangeList[idxL][idxI] == "-" else 1)))
                    # print(ops[selectedRangeList[idxL][idxI]](int(selectedRangeList[idxL][idxI-1]) * (-1 if selectedRangeList[idxL][idxI-2] == "-" else 1),  int(selectedRangeList[idxL][idxI+1])))
                    result = result + (ops[selectedRangeList[idxL][idxI]](int(selectedRangeList[idxL][idxI-1]) * (-1 if selectedRangeList[idxL][idxI-2] == "-" else 1),  int(selectedRangeList[idxL][idxI+1])))
    if len(remainInt) > 0:
        for idxR in range(len(remainInt[0])):
            if remainInt[0][idxR] in operators:
                result = (ops[remainInt[0][idxR]](result, int(remainInt[0][idxR+1])))
                        
    return result

def mergeRightSect(list):
    mergedRight = []
    for idxRs in range(len(list)):
        for idxRi in range(len(list[idxRs])):
            mergedRight.append(list[idxRs][idxRi])
    return mergedRight
            
def solveAddSubRight(rightSect):
    result = 0
    if len(extractOpWithInt(rightSect)) > 2:
        result = doAddSubbRightSec(extractOpWithInt(rightSect))
    else:
        result = joinOpWithInt(rightSect)
    return result

def changeOpToChangeSect(list):
    list = extractOpWithInt(list)

    for idx in range(len(list)):
        if list[idx] == "+":
            list[idx] = "-"
        elif list[idx] == "-":
            list[idx] = "+"

    return joinOpWithInt(list)

    
def solve(eq):
    var, leftKonst, rightSect = getInitVar(eq)
    
    koeff = getKoef(var, getVar(var))
    eq = [var, leftKonst, "=", rightSect]

    eq.remove(leftKonst)
    eq.insert(len(eq), changeOpToChangeSect(leftKonst))

    leftKonst, rightSect = getLeftSectionWithoutVar(eq), getRightSection(eq)

    rightSect = mergeRightSect(rightSect)
    print("{} = {}".format(var, ' '.join(extractOpWithInt(rightSect))))

    rightSect = solveAddSubRight(rightSect)
    print("{} = {}".format(var, rightSect))

    result = rightSect / int(koeff)
    print("{} = {}/{}".format(getVar(var), rightSect, koeff))
    print("{} = {}".format(getVar(var), result))


    print("the result is {}".format(result))

solve(linearEquation)
