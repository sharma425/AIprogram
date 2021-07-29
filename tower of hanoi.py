# IN THIS PROGRAM I HAVE WRITTEN CODE FOR TOWER OF HANOI USING RECURSIVE AND ITERATIVE AS WELL
# PROGRAM WILL ASK THE USER WHETHER HE/SHE WANT TO USE RECURSIVE OR ITERATIVE APPROACH
# PROGRAM WILL ALSO TAKE THE NUMBER OF DISKS FOR PROBLEM
# I HAVE USED SOME COMMON FUNCTIONS IN BOTH APPROACH FOR GOOD READIBILITY AND REUSABILITY
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:21:51 2021
@author: Keshav
"""''
# SETTING THE SOURCE POLE ACCORDING USING USER INPUT THE NO. OF DISKS
def initializeSource(n):
    global poleA
    for i in range(n,0,-1):
        poleA.append(i)

# FOR LEGAL MOVE BETWEEN TWO NODES 
def move1(poleX,poleY):
    if (len(poleY)==0) :    # IF SECOND POLE IS EMPTY
        x=poleX.pop()
        poleY.append(x)
    elif (len(poleX)==0):   # IF FIRST POLE IS EMPTY
        x=poleY.pop()
        poleX.append(x)
    elif poleX[-1]<poleY[-1]:  # IF FIRST POLE HAVE GREATER DISK
        x=poleX.pop()
        poleY.append(x)
    else:                      # IF SECOND POLE HAVE GREATER DISK
        x=poleY.pop()
        poleX.append(x)
    return poleX, poleY     # RETURN THE UPDATED POLES

# PRINT THE CURRENT POLES STATE 
def printPoles(poleX,poleY,poleZ,source="Source",auxillary="Auxillary",destination="Destination") :
    print(source,"Pole Content : ",end = "")    
    for i in poleX : print(i,end = "   ")
    print()
    print(auxillary,"Pole Content : ",end = "")    
    for i in poleY : print(i,end = "   ")
    print()
    print(destination,"Pole Content : ",end = "")    
    for i in poleZ : print(i,end = "   ")
    print()
     
# PROGRAM USING RECURSIVE APPROACH
def TOHrec(n,poleA,poleB,poleC,source,auxillary,destination):
    initializeSource(n)         # SETTING THE SOURCE POLE
    if n > 0:
        
         # REURING THE SAME FUNCTION TREATING n-1 DISKS BE THE NEW PROBLEM
         TOHrec(n-1, poleA, poleC, poleB,source,destination,auxillary)
         
         print("Legal move between",source,"and",destination)
         print()
         # FUNCTION CALL FOR LEGAL MOVE
         poleA, poleC = move1(poleA, poleC)
         
         # PRINTING THE UPDATED POLES
         printPoles(poleA,poleB,poleC,source,auxillary,destination)
         
         # AGAIN REURING THE SAME FUNCTION TREATING n-1 DISKS BE THE NEW PROBLEM
         TOHrec(n-1, poleB, poleA, poleC,auxillary,source,destination)
     
# PROGRAM USING ITERATIVE APPROACH
def TOH(n):
    global poleA, poleB, poleC  # DECLEARING THE LIST GLOBAL
    initializeSource(n)         # SETTING THE SOURCE POLE
    move = 2 ** n - 1           # TOTAL NUMBER OF MOVES
    printPoles(poleA,poleB,poleC)       # PRINT THE INITIAL PROBLEM
    
    # ITERATION FOR TOTAL NUMBER OF MOVES
    for i in range(1,move+1):
        if i%3==1:
            print("Legal Movement between poles : Source and Destination pole")
            poleA, poleC = move1(poleA, poleC)
        if i%3 == 2:
            print("Legal Movement between poles : Source and Auxillary pole" )
            poleA, poleB = move1(poleA, poleB)
            
        if i%3==0:
            print("Legal Movement between poles : Auxillary and Destination" )
            poleB, poleC = move1(poleB, poleC)
            
        # PRINTING THE UPDATED POLES CONSIDERING THE NUMBER OF POLES
        if n%2==0:
            printPoles(poleA,poleC,poleB)
        else:
            printPoles(poleA,poleB,poleC)
 

poleA=[]        # INITIALIZE THE LIST FOR POLE A 
poleB=[]        # INITIALIZE THE LIST FOR POLE B
poleC=[]        # INITIALIZE THE LIST FOR POLE C
 
n = input("Enter the number of discs : ")   # INPUT NO. OF DISKS FOR PROBLEM 

# ASK FOR APPROACH USER WANT TO USE
method = input("Enter 1 for recursive method & 2 for iterative : ")
if int(method) == 1:                    # IF RECURSIVE APPROACH CHOOSEN
    TOHrec(int(n), poleA, poleB, poleC,"Source","Auxillary","Destination")
else:                                   # IF ITERATIVE APPROACH CHOOSEN
    TOH(int(n))

