#hw8.py
#1)
class Pizza:
    def __init__(self, size='M',tp = set()):
        self.size = size
        self.toppings = set(tp)
        self.setsize(size)
        
    def __repr__(self):
        return 'Pizza(\'{}\',{})'.format(self.size,self.toppings)
    def setsize(self,nsize):
        #size choices are 'S', 'M', 'L'
        if nsize=='S':
            self.size='S'
        elif nsize=='M':
            self.size= 'M'
        elif nsize=='L':
            self.size= 'L'
    def getsize(self):
        return self.size
    def addTopping(self,item):
        self.toppings.add(item)
    def removeTopping(self,item):
        self.toppings.discard(item)
    def price(self,tprice,ttoppings):
        #code
        if self.size=='S':
            ttoppings=0.70*len(self.toppings)
            tprice= 6.25+ ttoppings
        elif self.size=='M':
            ttoppings= 1.45* len(self.toppings)
            tprice= 9.95+ttoppings
        elif self.size=='L':
            ttoppings = 1.85* len(self.toppings)
            tprice= 12.95+ttopings
        return tprice
    def __eq__(self,other):
        if self.size==other.size:
            for t in self.toppings:
                for t2 in other.toppings:
                    return True
                    
        else:
            return False

#2)
def orderPizza(self,usize,utop):
    #code
    ptop = {}
    usize = input('Welcome to Python Pizza!\nWhat size pizza would you like (S,M,L): ')
    utop = input('Type topping to add(or Enter to quit): ')#fix repeat if possible
    while utop != '':
        utop = input('Type topping to add(or Enter to quit): ')
        ptop = ptop.add(utop)
    print( 'Your pizza costs $'+price)
    return(Pizza())

#3)
class Stack(list):
##    def __str__(self):
##        return 'Stack({})'.format(repr(self))
    def push(self,item):
        self.append(item)

    def isEmpty():
        if self==[]:
            return True
        else:
            return False

    
#4)
#reference: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
def parenthesesMatch(ustr):
    stk = []
    op=['(','[','{']
    cl=[')',']','}']
    for s in ustr:
        if s in op:
            stk.append(s)
        elif stk==[]:
            return False
        elif s in cl:
            i = cl.index(s)
            if op[i]!=stk.pop():
                return False
            else:
                pass
    return True
      

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw8TEST.py'))


    
