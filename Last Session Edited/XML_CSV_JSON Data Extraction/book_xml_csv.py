import xml.etree.ElementTree as ET
import csv
# Parse XML doc and get root
tree = ET.parse("new_book.xml")
#tree = ET.parse("C:\Users\uiqbal\Desktop\Attempted Py scripts\XML_CSV_JSON Data Extraction\new_book.xml")
root = tree.getroot()

# open a file for writing
book_data = open('book_extr.csv', 'w')

# create the csv writer object
# Create list that contain header
csvwriter = csv.writer(book_data)
book_head = []   # To get the Titles

count = 0
for element in root.findall('Book'):
    book_nodes = []  # To get the child Values
    publisher_list = []  # To get the child values of Publisher
    if (count == 0):
        Title = element.find('Title').tag
        book_head.append(Title)
        Author = element.find('Author').tag
        book_head.append(Author)
        Genre = element.find('Genre').tag
        book_head.append(Genre)
        Price = element.find('Price').tag
        book_head.append(Price)
        #Publisher = element.find('Publisher').tag
        Publisher = element[5].tag
        book_head.append(Publisher)  #Book_head Printing all the titles/Headings
        #print ('Element Titles: ')
        csvwriter.writerow(book_head)
        count = count + 1
    
    # Get Child Nodes of Book elem
    Title = element.find('Title').text
    book_nodes.append(Title)
    Author = element.find('Author').text
    book_nodes.append(Author)
    Genre = element.find('Genre').text
    book_nodes.append(Genre)
    Price = element.find('Price').text
    book_nodes.append(Price)

    Publisher = element[5][0].text
    #Publisher = element.find('Publisher').getchilderen()
    publisher_list.append(Publisher)
    Company = element[5][1].text
    publisher_list.append(Company)
    Address = element[5][2].text
    publisher_list.append(Address)
    RegNo = element[5][3].text
    publisher_list.append(RegNo)
    book_nodes.append(publisher_list)

    # Write book details to csv
    csvwriter.writerow(book_nodes)


# close csv file
book_data.close()
