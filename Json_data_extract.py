#Data Extracting From Json
import json
from pprint import pprint

data = json.load(open('samplej.json'))


pprint(data)
