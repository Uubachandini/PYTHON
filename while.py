'''
Looping statements arae also called as alternative statements

These statements are used to run a particular condition 
no of times
they are broadly divided into types 
1.while
2.for '''

# while is called as entry control loop
#while it executes when the condition is true 
'''
Syntax: while condition:
           statements
           exit condition/incrementation
           '''
#eg1:
# i=1
# while i<=10:
#     #print(i)--> in this particular line the 
#     #"1"value runs "n" times because no incrementation/exit condition specification
#     print("the value",i)
#     i+=1


 #eg2:
# while True:
#     print("the while condition")
    # Note: As default condition is true the while loop runs "infinity"times

#eg3:
# while False:
#     print("the while condition")
    #Note: as while  is also called entry control 
    #loop it just checks the condition in the entrance 
    #as default false is given as condition it won't execute

'''
    Jumping or Transfer statements:
    These statements are used to control the normal 
    execution of a program they are of"2" types
    1.Break: This statements is used to terminate/break the loop
    2.Continue:this statemets are used to skip current iteration
    and run the next iteration'''

#     i=0
#     while i<=10:
#         i+=1
#         if i==6:
#             break # a teminates/stops the program
#         print(i)

#  while i<9:
#         i+=1
#         if i==3:
#             continue# a
#         print(i) 