import xml.etree.ElementTree as ET
import csv
# Parse XML doc and get root
tree = ET.parse("new_book.xml")
#tree = ET.parse("C:\Users\uiqbal\Desktop\Attempted Py scripts\XML_CSV_JSON Data Extraction\new_book.xml")
root = tree.getroot()

#print(root)
#print("root subelements: ", root.getchildren())
#DeprecationWarning(for below code) use list (elam)
#root.getchildren()[0]
#root.getchildren()[0].getchildren()
dir(root)