import pandas
df = pandas.read_csv('cvsample2.txt', 
            index_col='Employee', 
            parse_dates=['City'],
            header=0, 
            names=['name', 'City', 'Age', 'Contact'])
df.to_csv('cvsample_modified.csv')