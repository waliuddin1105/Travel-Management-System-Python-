class customer:
    def __init__(self):
        next_id=1000
        self.cusId='c'+next_id
        next_id+=1
        self.name=''
        self.age=''
        self.gender=''
        self.adress=''
        self.mobile=''
        self.fileContents=''
        
    def getDetails(self):
        n=input('Enter Customer name:')
        self.name=n
        while True:
            try:
                a=input('Enter Customer age:')
                self.age=a
                break
            except ValueError as v:
                print("Please enter a number only") 

        while True:
            try:
                g=input('Enter Customer gender f/m only:')
                g=g.lower()
                if g!='f' and g!='m':
                    raise Exception
                else:
                    self.gender=g
                    break

            except Exception:
                print("Please enter f or m only!")

        adr=input('Enter Customer address:')
        self.adress=adr
        while True:
            try:
                mob=int(input('Enter Customer mobile number:'))
                self.mobile=mob
                break
            except ValueError as v:
                print("Please enter a number only")     

        with open('Old_customers.txt','w+') as f:
            f.write(f'Customer ID:{self.cusId}\nCustomer Name:{self.name}\nCustomer Age:{self.age}\nGender:{self.gender}\nMobile Number:{self.mobile}')   

    def showDetails(self):
        try:
            f=open('Old_customers.txt','r+')
            self.fileContents=f.read()
            f.close()
        except FileNotFoundError as fne:
            self.fileContents='none'
            print('File Not found')
        print(self.fileContents)

class cabs:
    def __init__(self):
        self.kilometers=''
        self.cabCost=''
        self.choice=''

    def cabDetails(self):
        print('---------------Metro Cabs---------------')
        print("1. Rent a Standard Cab- Rs.30 per KM")
        print("2. Rent a Luxury Cab- Rs.50 per KM")
        print('To calculate the total cost of your journey!')
        print('--------------------------------------------------')
        while True:
            try:
                c=int(input('Enter which type of cab do you want to use:'))
                if c!='1' and c!='2':
                    raise Exception
                else:
                    self.choice=c
                    break
            except Exception:
                print('Please enter a valid choice!')

        while True:
            try:
                km=int(input('How many kilometers do you want to travel:'))
                self.kilometers=km
                break
            except ValueError:
                print('Please enter a numeric value only!')
            
        if self.choice=='1':
            self.cabCost=self.kilometers*30
            print(f'Your tour will cost Rs.{self.cabCost} for a standard cab')

            while True:
                try:
                    hirecab=input("Press 1 to hire this cab or\nPress 2 to hire another cab")
                    if hirecab!='1' and hirecab!='2':
                        raise Exception
                    else:
                        break
                except Exception:
                    print('Please enter 1 or 2 only!')

            if hirecab==1:
                print('You have successfully hired the standard cab, go to the main menu to reciev your receipt')
            else:
                self.cabDetails()

        elif self.choice==2:
            self.cabCost=self.kilometers*50
            print(f'Your tour will cost Rs.{self.cabCost} for a standard cab')
            hirecab=input("Press 1 to hire this cab or\nPress 2 to hire another cab")

            while True:
                try:
                    if hirecab!='1' and hirecab!='2':
                        raise Exception
                    else:
                        break
                except Exception:
                    print('Please enter 1 or 2 only!')
            
            
            if hirecab==1:
                print('You have successfully hired the luxury cab, go to the main menu to reciev your receipt')
            else:
                self.cabDetails()

            k=input(('Enter any key to go to the main menu'))
            if k=='a':
                manageMenu()
            else:
                manageMenu

