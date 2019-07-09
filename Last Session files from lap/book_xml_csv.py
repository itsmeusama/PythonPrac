import xml.etree.ElementTree as ET
import csv
# Parse XML doc and get root
tree = ET.parse("new_book.xml")
root = tree.getroot()

# open a file for writing
book_data = open('book_extr.csv', 'w')

# create the csv writer object
# Create list that contain header
csvwriter = csv.writer(book_data)
book_head = []

count = 0
for element in root.findall('Book'):
    book_nodes = []
    publisher_list = []
    if count == 0:
        Title = element.find('Title').tag
        book_head.append(Title)
        Author = element.find('Author').tag
        book_head.append(Author)
        Genre = element.find('Genre').tag
        book_head.append(Genre)
        Price = element.find('Price').tag
        book_head.append(Price)
        csvwriter.writerow(book_head)
        count = count + 1

    # Get Child Node
    Title = element.find('Title').text
    book_nodes.append(Title)
    Author = element.find('Author').text
    book_nodes.append(Author)
    Genre = element.find('Genre').text
    book_nodes.append(Genre)
    Price = element.find('Price').text
    book_nodes.append(Price)

    Publisher = element[1].tag
    publisher_list.append(Publisher)
    Company = element[1][0].text
    publisher_list.append(Company)
    Address = element[1][1].text
    publisher_list.append(Address)
    book_nodes.append(publisher_list)

    # Write resident to csv
    csvwriter.writerow(book_nodes)

# close csv file
book_data.close()
