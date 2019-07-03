from bs4 import BeautifulSoup
infile = open("note.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents,'xml')
to = soup.find_all('to')
sentto = soup.find_all('from')
heading = soup.find_all('heading')
body = soup.find_all('body')
for i in range(0, len(to)):
    print('\n')
    print("From :" + sentto[i].get_text(),", to :",end=' ')
    
    print(to[i].get_text(),end=' ')
    print('\n')
    print("message :" + body[i].get_text())