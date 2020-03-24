#midterm problems
1#d)error, because compare string to int

2.A, about strings being immutable
s.replace returns because it makes a copy
s. replace has nothing assigned so ignore it.(wasted line of code

7.a, 

#9.
def classify(precipLst):
    avg = sum(precipLst)/len(precipLst)
        if avg>=50:
            return 'wet'
        elif avg >=20:
            return 'normal'
        else:
            return 'dry'


#10
def firstLetter(letter, phrase):
#start with empty list
    ans = []
    #get rid of punctiation
    for punct in ",.!?":
        phrase = phrase.replace(punct, "")
    #split into words
     #iterate over them                                          
    for word in phrase.split():
        if word[0].upper() ==letter.upper():
            ans.append(word)
        #if word starts iwth code
        #save letter
    #return accummulated list
    return word


#11
#2d accumlator
                                              

def oddCount(1st2d):
   count = 0                                           
   for row in lst2d:
       for num in row:
           if num% 2!=0:
             count+=1
    return count




#12
#indexed accumulator
def findAll(target, lst):
   indices =[]
   #indxed iteration
   for i in range(len(lst)):
       if lst[i]==target:
          indices.append(i)
    return indices



#13.
 #indexed search for pair
  # with different differences
  def isArithmmetic (numLst):
     #compute initinal difference
    delta = numLst[1]-numLst[0]
      #iterate through pairs
      for i in range(len(numLst)-1):                                        
        #if pair difference not same as intial-false
        #all apirs have same diff-true
        if numLst[i+1] - numLst[i] !=delta:
            return Flase
    return True





