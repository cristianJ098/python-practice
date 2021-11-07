import os

ADD = 1
INSERT = 2
SHOW = 3
SEARCH = 4
DELETE = 5
SORT = 6
CLEAR = 7
EXIT = 8

FRUITS = []
separator = '***********'


def menu():
	
	print (f'''{separator} Fruit {separator}
{ADD} - Add
{INSERT} - Insert
{SHOW} - Show
{SEARCH} - Search
{DELETE} - Delete
{SORT} - Sort
{CLEAR} - Clear
{EXIT} - Exit
	''')

	


def add():
	print(separator,'Add Fruit',separator)
	fruit = input('Enter fruit: \t')
	FRUITS.append(fruit)
	print('Fruit added succesfully ', '**',fruit,'**')


def insert():
	print(separator,'Insert Fruit',separator)
	fruit = input('Enter fruit: \t')
	index = 0
	while index == 0:
		try:
			index = int(input('Enter the posicion you want: \t'))
		except:
			print('Pleas enter a number')
	FRUITS.insert(index,fruit)


def show():
	print(separator,'Show Fruits',separator)
	if len(FRUITS) > 0:
		num = 1
		for i in FRUITS:
			print(num, ' - ' , i)
			num += 1
	else:
		print('no fruits have been added')



def search():
	print(separator,'Search Fruit',separator)
	
	if len(FRUITS) > 0:
		search = input('Enter the name of the fruit you want to find: \n')
		if search in FRUITS:
			num=0
			cont = FRUITS.count(search)
			os.system('cls')
			print(separator * 4, '\t')
			for i in range(cont):
				index = FRUITS.index(search,num)
				print(f'The fruit {search} is in the list in the {index +1} - position\n')
				num =index + 1
			print(separator * 4, '\t')
		else:
			print('The search is empty')
	else:
		print('no fruits have been added')


def delete():
	print(separator,'Delete Fruit',separator)
	if len(FRUITS) > 0:
		num=0
		for i in FRUITS:
			print(num+1, ' - ', i)
			num +=1
		delete = 0
		while delete == 0:
			try:
				delete = int(input(f'Enter the number 1 - {len(FRUITS)} you want to remove: \n'))
			except:
				print('Please enter a number')
		if 0 < delete <= len(FRUITS):
			deleted = FRUITS.pop(delete-1)
			
		print('**',deleted,'** ',' Fruit deleted succesfully ')
	else: 
		print('no fruits have been added')


def sort():
	print(separator,'Sort Fruits',separator)
	if len(FRUITS) > 0:
		num = 0
		while num == 0:
			try:
				num = int(input('Enter 1 to sort Fruits in alphabetically o 2 to reverse alphabetically: '))
			except:
				print('Please enter a number')
		if num == 1:
			FRUITS.sort()
			show()
		else:
			FRUITS.sort(reverse=True)
			show()
	else:
		print('No fruits has been added')


def clear():
	if len(FRUITS) > 0:
		print(separator,'Clear Fruits',separator)
		option = input('Do you really want to clear the list? yes/not: \t').lower()
		if option == 'yes' or option == 'y':
			FRUITS.clear()
			print('the process is complete')
		else:
			print('aborting the process...')
	else:
		print('There are no Fruits added')




def main():
	
	continue_ = True
	while continue_:
		os.system('cls')
		menu()
		option = 0
		while option == 0:
			try:
				option = int(input('Choose a option: '))
			except:
				print('Invalid option')

		if option == ADD:
			os.system('cls')
			add()
			
		elif option == INSERT:
			os.system('cls')
			insert()
			
		elif option == SHOW:
			os.system('cls')
			show()
			
		elif option == SEARCH:
			os.system('cls')
			search()
			
		elif option == DELETE:
			os.system('cls')
			delete()
			
		elif option == SORT:
			os.system('cls')
			sort()
			
		elif option == CLEAR:
			os.system('cls')
			clear()
			
		elif option == EXIT:
			os.system('cls')
			print('See you...')
			continue_ = False
		else:
			print(separator,'Incorrect option',separator, '\t',separator, 'Choose a correct option', separator)
		input('Press a key to continue...')
		

if __name__ == '__main__':
	main()
	

	