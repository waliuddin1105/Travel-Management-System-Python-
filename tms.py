class customer:
    def __init__(self):
        self.cusId=''
        self.name=''
        self.age=''
        self.gender=''
        self.adress=''
        self.mobile=''
        
    def getDetails(self):
        cid=input('Enter Customer ID:')
        self.cusId=cid
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

    
