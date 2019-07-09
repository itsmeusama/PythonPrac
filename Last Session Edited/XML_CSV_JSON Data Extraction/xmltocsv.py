import pandas as pd
import itertools
from bs4 import BeautifulSoup as b

with open("file.xml", "r") as f:  # opening xml file
    content = f.read()

soup = b(content, "lxml")
pkgeid = [values.text for values in soup.findAll("pkgeid")]
pkgname = [values.text for values in soup.findAll("pkgname")]
time = [values.text for values in soup.findAll("time")]
oper = [values.text for values in soup.findAll("oper")]
# For python-3.x use `zip_longest` method
# For python-2.x use 'izip_longest method
data = [item for item in itertools.zip_longest(time, oper, pkgeid, pkgname)]
df = pd.DataFrame(data=data)
df.to_csv("sample.csv", index=False, header=None)
