from bs4 import BeautifulSoup as bs

import requests

list=['quiz','quizzes','test','tests','assignment','assignments','lab','labs','exam','exams',\
      'presentation','presentations','report','reports']
s='quiz'
#for s in range (len(list)):
website='https://www.thesaurus.com/browse/{}?s=t'.format(s)
page=requests.get(website)
soup = bs(page.content, 'html.parser')
test=[]
testArray=soup.find_all('a', {'data-linkid': 'nn1ov4'})
for x in range (len(testArray)):
    test.append(testArray[x].decode_contents(formatter="html"))
print (test)
