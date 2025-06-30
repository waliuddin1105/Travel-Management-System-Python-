class customer:
    def __init__(self):
        self.cusId=''
        self.name=''
        self.age=''
        self.gender=''
        self.adress=''
        self.mobile=''
        
    def getDtails():
        cid=input('Enter Customer ID:')
        n=input('Enter Customer name:')

        while True:
            try:
                a=input('Enter Customer age:')
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
                    break

            except Exception:
                print("Please enter f or m only!")

        adr=input('Enter Customer address:')

        while True:
            try:
                mob=int(input('Enter Customer mobile number:'))
                break
            except ValueError as v:
                print("Please enter a number only")        

        
