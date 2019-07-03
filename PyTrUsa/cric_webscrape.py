from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable

def TeamOrPlayer():
	choice=input('Enter your choice:')
	tp={'1':'team-rankings','2':'player-rankings'}
	
	if choice in tp:
		return tp[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return TeamOrPlayer()


def Value():
	choice=input('Enter your choice:')
	val={'1':'batting','2':'bowling','3':'all-rounder'}
	
	if choice in val:
		return val[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return Value()


def URL():
	#val=Menu()
	url='https://www.icc-cricket.com/rankings/+val
    #https://www.icc-cricket.com/rankings/mens/team-rankings/odi
	header=gen.upper() +' ' +mode[1:].upper() + ' ' + val.upper()
	print('\n{:<15}  {:<30}\n{:<15}  {:<30}'.format('',tp.upper(),'',header))
	return url,tp


def SOUP(url,tp):
	try:
		res=requests.get(url)
		soup=BeautifulSoup(res.text,'lxml')
		a= soup.find_all('tr',{'class':'table-body'})
		data={}
			
		for i in a :
			team=[]
			name=''
			rating=''

			try:
				rank=int(i.contents[1].text)
			except:
				pass
			
			try:	
				name=i.contents[3].text.replace('\n','')
				name=" ".join(name.split())
				if rank==1 and tp=='player-rankings':
					name=name[0:-3]
			except:
				pass

			try:
				rating=i.contents[9].text
			except:
				if rank==1 :
					rating=i.contents[5].text
				else:
					rating=i.contents[7].text
			
			team.extend([name,rating])
			data[rank]=team
		
		return data

	except:
		return SOUP(url,tp)


def Print(data):
	print('\nRANKING \t)
	for i in sorted(data):
		print('{:<10}'.format(i),end='')
		for j in range(len(data[i])):
			print('{:<26}'.format(data[i][j]),end='     ')
		print()


def main():
	
	url,tp=URL()
	data=SOUP(url,tp)
	Print(data)	


if __name__=='__main__':
	main()