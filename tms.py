import os as o

class ManageMenu:
        def __init__(self):
            pass
        def manageMenu(self):
            inp=input('\n\n\n\n\n\n\n\n\n\t\t\t\tEnter your name to progress further:')
            o.system('cls')
            m=menus()
            m.menu()

class customer:
    next_id=1000
    def __init__(self):
        self.cusId='c'+str(customer.next_id)
        customer.next_id+=1
        self.name=''
        self.age=''
        self.gender=''
        self.address=''
        self.mobile=''
        self.fileContents=''
        
    def getDetails(self):
        n=input('Enter Customer name:')
        self.name=n
        while True:
            try:
                a=int(input('Enter Customer age:'))
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
        self.address=adr
        while True:
            try:
                mob=int(input('Enter Customer mobile number:'))
                self.mobile=mob
                break
            except ValueError as v:
                print("Please enter a number only")     

        with open('Old_customers.txt','a+') as f:
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
        me=menus()
        print('---------------Metro Cabs---------------')
        print("1. Rent a Standard Cab- Rs.30 per KM")
        print("2. Rent a Luxury Cab- Rs.50 per KM")
        print('To calculate the total cost of your journey!')
        print('--------------------------------------------------')
        while True:
            try:
                c=int(input('Enter which type of cab do you want to use: '))
                if c!=1 and c!=2:
                    raise Exception
                else:
                    self.choice=c
                    break
            except Exception:
                print('Please enter a valid choice!')

        while True:
            try:
                km=int(input('How many kilometers do you want to travel: '))
                self.kilometers=km
                break
            except ValueError:
                print('Please enter a numeric value only!')
            
        if self.choice==1:
            self.cabCost=self.kilometers*30
            print(f'Your tour will cost Rs.{self.cabCost} for a standard cab')

            while True:
                try:
                    hirecab=input("Press 1 to hire this cab or\nPress 2 to hire another cab:\n")
                    if hirecab!='1' and hirecab!='2':
                        raise Exception
                    else:
                        break
                except Exception:
                    print('Please enter 1 or 2 only!')

            if hirecab=='1':
                print('You have successfully hired the standard cab, go to the main menu to recieve your receipt')
            else:
                self.cabDetails()

        elif self.choice==2:
            self.cabCost=self.kilometers*50
            print(f'Your tour will cost Rs.{self.cabCost} for a standard cab')
            hirecab=input("Press 1 to hire this cab or\nPress 2 to hire another cab:\n")

            while True:
                try:
                    if hirecab!='1' and hirecab!='2':
                        raise Exception
                    else:
                        break
                except Exception:
                    print('Please enter 1 or 2 only!')
            
            
            if hirecab=='1':
                print('You have successfully hired the luxury cab, go to the main menu to recieve your receipt')
            else:
                self.cabDetails()

            k=input(('Enter any key to go to the main menu:'))
            if k=='a':
                o.system('cls')
                me.menu()
            else:
                o.system('cls')
                me.menu()

class booking:
    def __init__(self):
        self.hotelChoice=''
        self.pack=''
        self.hotelCost=''
        
    
    def hotels(self):
        hotels=['Avari Towers','Pearl Continental','Beach Luxury Hotel']
        i=1
        for h in hotels:
            print(str(i)+'.'+h)
            i+=1
        c=input('Select which hotel do you wanna book or check details of\nOr press any other key to go back to the main menu: ')
        self.hotelChoice=c
        me=menus()

        if(self.hotelChoice=='1'):
            print("\t\t\t\tWELCOME TO AVARI TOWERS!\nThe highest rated 5 star hotel in Karachi!\nEnjoy the food, the gym, the pool, the garden, luxury suites and much more with Avari Towers")
            print('Packages offered by Avari Towers:\n')
            print("1.Standard Pack")
            print("All the basic facilities you need\nPrice:Rs 50,000.00 per night")
            print("2.Premium Pack")
            print("Enjoy the Premium lifestyle!\nPrice:Rs 100,000.00 per night")
            print("3.Luxury Pack")
            print("Enjoy the Luxury at Avari Towers:\nPrice:Rs 160,000.00 per night")

            p=input("\nEnter which pack you want to avail\nOr press any other key to go back:\n")
            self.pack=p

            if(self.pack=='1'):
                self.hotelCost=50000.00
                print("You have succesfully availed the Standard package at the Avari Towers!")
                print("You can get your receipt from the main menu:")
            elif(self.pack=='2'):
                self.hotelCost=100000.00
                print("You have succesfully availed the Premium package at the Avari Towers!")
                print("You can get your receipt from the main menu:")
            elif(self.pack=='3'):
                self.hotelCost=160000.00
                print("You have succesfully availed the Luxury package at the Avari Towers!")
                print("You can get your receipt from the main menu:")
            else:
                o.system('cls')
                self.hotels()
            
            k=input('Press any key to return to the main menu:')
            if k=='a':
                o.system('cls')
                me.menu()
            else:
                o.system('cls')
                me.menu()

        elif(self.hotelChoice=='2'):
            print("\t\t\t\tWELCOME TO PEARL CONTINENTAL!\nThe HIGHEST rated Luxury and event hotel in Karachi!\nEnjoy the ambiance, the feel, the restaurants, the pools , fitness centers, Family rooms and much more with Pearl Continental")
            print('Packages offered by Pearl Continental:\n')
            print("1.Vacation Pack")
            print("Get the full vacation experience\nPrice:Rs 40,000.00 per night")
            print("2.Family Pack")
            print("The total family package\nPrice:Rs 60,000.00 per night")
            print("3.Event Pack")
            print("The package for the best event experience!\nPrice:Rs 140,000.00 per night")

            p=input("\nEnter which pack you want to avail\nOr press any other key to go back:\n")
            self.pack=p

            if(self.pack=='1'):
                self.hotelCost=40000.00
                print("You have succesfully availed the Vacation package at Pearl continental!")
                print("You can get your receipt from the main menu:")
            elif(self.pack=='2'):
                self.hotelCost=60000.00
                print("You have succesfully availed the Family package at Pearl continental!")
                print("You can get your receipt from the main menu:")
            elif(self.pack=='3'):
                self.hotelCost=140000.00
                print("You have succesfully availed the Event package at Pearl continental!")
                print("You can get your receipt from the main menu:")
            else:
                o.system('cls')
                self.hotels()
            
            k=input('Press any key to return to the main menu:')
            if k=='a':
                o.system('cls')
                me.menu()
            else:
                o.system('cls')
                me.menu()

        elif(self.hotelChoice=='3'):
            print('\t\t\t\tWELCOME TO Beach Luxury Hotel!\nSet near the mangroves at the coast of the Arabian Sea, get ready for an adventure like never before at the Beach Luxury Hotel!')
            print('Packages offered by Beach Luxury Hotel:\n')
            print("1.Beach Pack")
            print("Book your own hut at the beach and enjoy the wonders\nPrice:Rs 55,000.00 per day")
            print("2.Special Pack")
            print("Get the full access to all the facilities\nPrice:Rs 90,000.00 per day")

            p=input("\nEnter which pack you want to avail\nOr press any other key to go back:\n")
            self.pack=p

            if(self.pack=='1'):
                self.hotelCost=55000.00
                print("You have succesfully availed the Vacation package at the Beach Luxury Hotel")
                print("You can get your receipt from the main menu:")
            elif(self.pack=='2'):
                self.hotelCost=90000.00
                print("You have succesfully availed the Special Package at the Beach Luxury Hotel!")
                print("You can get your receipt from the main menu:")
            else:
                o.system('cls')
                self.hotels()
            
            k=input('Press any key to return to the main menu:')
            if k=='a':
                o.system('cls')
                me.menu()
            else:
                o.system('cls')
                me.menu()
            
        else:
            o.system('cls')
            me.menu()
            


class charges(customer,cabs,booking):
    def __init__(self):
            customer.__init__(self)
            cabs.__init__(self)
            booking.__init__(self)
    
    def printBill(self):
        with open('receipt.txt','a+') as f:
            f.write("\t\t\t\tPak Travelers")
            f.write("--------------------------RECEIPT-------------------------------")
            f.write("-----------------------------------------------------------------")
            
            f.write(f'Customer ID: {self.cusId}\n')
            f.write(f'DESCRIPTION\t\tTOTAL\n')
            f.write(f'Hotel Cost\t\t{self.hotelCost}\n')
            f.write(f'Cab travel cost\t\t{self.cabCost}\n')
            f.write('-------------------------------------------------------------\n')
            f.write(f'Total Expenses\t\t{self.hotelCost + self.cabCost}\n')

        
    def displayBill(self):
        try:
            f=open('receipt.txt','r+')
            contents=f.read()
            f.close()
        except FileNotFoundError:
            print('Error file not found')
            contents='none'
        print(contents)

class menus():
    def menu(self):
        ret=''

        ch=charges()
        c=cabs()
        b=booking()
        cust=customer()

        print('\t\t\t\t\t* Pak Travels By Wali And Umer *')
        print("--------------------------------------------------Main Menu---------------------------------------------------")
        print('\t\t\t\t    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
        print('\t\t\t\t   |\t\t\t\t\t   |')
        print('\t\t\t\t   |\tCustomer Management -> 1\t   |')
        print('\t\t\t\t   |\tCabs Management     -> 2\t   |')
        print('\t\t\t\t   |\tBookings Management -> 3\t   |')
        print('\t\t\t\t   |\tCharges & Bill      -> 4\t   |')
        print('\t\t\t\t   |\tExit                -> 5\t   |')
        print('\t\t\t\t   |\t\t\t\t\t   |')
        print('\t\t\t\t   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|')
        while True:
            try:
                mainChoice=input('Enter your choice:')
                if mainChoice not in ['1','2','3','4','5']:
                    raise Exception
                else:
                    break
            except Exception:
                print('Please enter a valid option!')
        
        if mainChoice=='1':
            print('----------------------------------Customers----------------------------------')
            print('1. Enter a new Customer')
            print('2. See previous customers:')
            print('Enter your choice\nOR press any key to return to main menu: ')
            inChoice=input()

            if inChoice=='1':
                cust.getDetails()
                ret=input('press any key to return back to main menu: ')
                if ret=='a':
                    o.system('cls')
                    self.menu()
                else:
                    o.system('cls')
                    self.menu()
            elif inChoice=='2':
                cust.showDetails()
                ret=input('press any key to return back to main menu: ')
                if ret=='a':
                    o.system('cls')
                    self.menu()
                else:
                    o.system('cls')
                    self.menu()
            else:
                o.system('cls')
                self.menu()
            
        elif mainChoice=='2':
            c.cabDetails()
            ret=input('press any key to return back to main menu: ')
            if ret=='a':
                o.system('cls')
                self.menu()
            else:
                o.system('cls')
                self.menu()

        elif mainChoice=='3':
            b.hotels()
            ret=input('press any key to return back to main menu: ')
            if ret=='a':
                o.system('cls')
                self.menu()
            else:
                o.system('cls')
                self.menu()
        
        elif mainChoice=='4':
            print('------------------GET YOUR RECEIPT------------------')
            ch.printBill()
            print('Your receipt has already been printed, it can be accessed from the file path')
            print('To display the receipt here press 1 or press any other key to go back to the main menu:')
            inchoice=input()
            
            if inchoice=='1':
                ch.displayBill()
                ret=input('press any key to return back to main menu: ')
                if ret=='a':
                    o.system('cls')
                    self.menu()
                else:
                    o.system('cls')
                    self.menu()
            else:
                self.menu()
        else:
            o.system('cls')
            mm=ManageMenu()
            mm.manageMenu()

#main
mm=ManageMenu()
mm.manageMenu()