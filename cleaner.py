import makeCalendar

#Quiz number day month time
list=['quiz','quizzes','test','tests','assignment','assignments','lab','labs','exam','exams','presentation','presentations','report','reports', 'case', 'cases','due', 'submission', 'submissions', 'forms', 'form', 'plan', 'plans']
months1=['Jan.','Feb.', 'Mar.', 'Apr.', 'May.', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
months=['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months2=['January','February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days=[]
invalid='\u25aa'
dayWeek=['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
for x in range (31):
    days.append(x+1)
def cleaning (longString):
    allLines = []
    allGoodLines = []
    matrix = []
    matrix.append([])
    matrix.append([])
    #current=os.getcwd(courseName)
    f=open("wrapper.txt", "w")
    f.write(longString)
    f.close()
    path = r'C:\Users\jason\PycharmProjects\QHacks2019 2.0\wrapper.txt'
    file=open(path, encoding="utf-8")
    for line in file:
        goodLine=[]
        buzzWordName = ""
        dayOf = "0"
        monthOf = ""
        numOf = ""
        allWords=line.split()
        acc = 1
        print(line)
        for i in range (len(allWords)):
            word=allWords[i]
            for ii in range (len(list)):
                if word.lower()[len(word)-1] == ':':
                    word=word.lower()[0:len(word)-1]
                if word.lower() == list[ii].lower():
                    acc=acc*2
                    if buzzWordName == "":
                        buzzWordName=word.lower()
                        string = ""
                    try:
                        for iii in range (len(allWords[i+1][0])):
                            char = allWords[i+1][iii]
                            if char.isdigit():
                                string += char
                                numOf = string
                    except:
                        a=''
            for y in range (12):
                if word != months[y] and word != months1[y] and word != months2[y]:
                    continue
                else:
                    acc=acc*-1
                    monthOf=word
                    for z in range (30):
                        z+=1
                        if z<10 and (allWords[i+1][0:1] == str(days[z])) and allWords[i+1][1:2] not in ["0","1","2","3","4","5","6","7","8","9"]:
                            acc=acc*2
                            dayOf=(allWords[i+1][0:1])
                        elif allWords[i+1][0:2] == str(days[z]):
                            acc=acc*2
                            dayOf=(allWords[i+1][0:2])
            for zz in range (7):
                if dayWeek[zz] == word.lower():
                    acc=acc*2
                    #dayWeekOf=word.lower()
        if acc <= -2:
            buzzWordName=buzzWordName.upper()
            if numOf == "":
               goodLine.extend([buzzWordName, monthOf, dayOf])
            else:
               goodLine.extend([buzzWordName + " " + numOf, monthOf, dayOf])

            if invalid in line:
                line=line.replace(invalid, "-")
            matrix[0].append(line)
            matrix[1].append(goodLine)
    return matrix
def splittingMatrix (matrix):
    matrixGood=[]
    matrixGood.append([])
    matrixGood.append([])
    matrixMore=0
    for x in range(len(matrix[1])):
        if matrix[1][x][0] is not '':
            matrixGood[0].append(matrix[0][x])
            matrixGood[1].append(matrix[1][x])
        else:
            matrixMore=1
    return matrixGood, matrixMore

def main(longString):
    print(longString)
    #call the cleaning function
    #return good and bad values
    m=cleaning(longString)
    print(m)
    matrixG, indicator=splittingMatrix(m)
    if matrixG[0]:
        makeCalendar.main(matrixG)


'''
'''
