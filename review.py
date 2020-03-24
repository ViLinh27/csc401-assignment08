#review.py


######hw qs##########
'''
try to write each method one by one and test one by one
init first
then repr
then sets
then gets(like prices)

in the price(keep track of size and toppings).
try not to keep track of price too(because you compute it later).

orderpizza()
need while loop for user input
try not to add (accumulator)topping at end before checking the condition. protect by if statement

your pizza cost ...is a print
p = order Pizza(),,,proves it's a return
    what data type is it regturning? a Pizza class()
    don't return a string

PIZZA CLASS: __EQ__
order pizza()
problem: two pizzas but topping additions go to both and not 1.
issue is in the init
like in quieue class:
self.q = list(lst)
need constructor to contain the object into a new object.
make sure you allocate container with the constrcutor(this makes a copy of the
defualt object).
for pizza the constructor is set()

3. stack class-like a Queue
   pop from back instead of front
   add and remove from same end in a stack

4. stack is good for dealing with things enclosed within other things
you want to determine if the ()[]{} match. can they open or close
. some stuff insde other stuff complicates
things.
this is a search problem.search for something bad.
code doesn't need to be too long
::::
>>>paranthesiesMatch("([])')
True

idea:

iterate through the string of marks
    1)IF-When you see opening mark, one of ([{, push it onto stack.
    
    When you see closing mark,then

   2) ELIF-if stack is empty return false
    otherwise(not empty stack):
    pop the top of the stack (which is an opening
    mark).(check) whether it is the compliment of the
    opening mark on the top of ths stack.
    
    3)ELIF-If no match return false,

    if it is-continue
    (do nothing)
o'''

#######review midterm/final############3
'''
############final exam

see finalStudy.py for some practice problems and notes
review quizzes and notes
rework some old homework problems if needed.
you cannot get enough programming practice.

MAKE SURE TO READ QUESTIONS CAREFULLY ON EXAM!!!!!!
understand concept of q.

expect inheritance q on mult choice section, not programming section
in class= here next week, usual time, Wednesday 11/20 5:45-9pm

notes- you are allowed 2 double sided or 4 single sided pages

cummulative- covers chapter 2-8, inheritance will be on mult choice sec. only
note: chp7 is on namespacaes

same format as midterm but HARDER AND LONGER

since midterm:
while loops
, random
dictionaries, classes
container classes(and inheritance-mult choice).



'''

##########loose end: code breaking###########
'''
'''
