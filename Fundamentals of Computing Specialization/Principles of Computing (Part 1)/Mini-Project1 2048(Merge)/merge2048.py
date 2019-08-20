"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # create an empty list
    mergelst = []
    
    # put all non-zero values from the list line to begining of mergelst
    for val in list(line):
        if (val != 0):
            mergelst.append(val)
    
    # replace same pairs values with twice it's value
    mergelst2 = [];
    idx = 0
    while idx < (len(mergelst)):
        if (idx < len(mergelst)-1 and mergelst[idx] == mergelst[idx+1]):
            mergelst2.append(2*mergelst[idx])
            idx += 1
        else:
            mergelst2.append(mergelst[idx])
            
        idx +=1
    
    # add zeros at the end of merged list to make the size same as list line         
    mergelst2.extend([0]*(len(line)-len(mergelst2)))
    
    return mergelst2

## uncomment the tests below 
## 1- test an empty list. Expected output : Result = []
#lst = merge([])
#print "Result = ", lst
## 2- test a list of 1 element. Expected output: Result = [4]
#lst = merge([4])
#print "Result = ", lst
## 3- test lst of size 2 with no pairs.
## Input : [8,4]. Expected output: Result = [8,4]
#lst = merge([8,4])
#print "Result = ", lst
## 4- test lst of size 2 with 1 pair.
## Input : [8,8]. Expected output: Result = [16,0]
#lst = merge([8,8])
#print "Result = ", lst
## 5- test some combination of lst of size greater than 2 but even size.
## Input : [2,2,0,0]. Expected output: Result = [4,0,0,0]
#lst = merge([2,2,0,0])
#print "Result = ", lst
## 6- test some combination of lst of size greater than 2 but odd.
## Input : [2,2,2]. Expected output: Result = [4,2,0]
#lst = merge([2,2,2])
#print "Result = ", lst
## 7- test some combination of lst of odd size with set of pairs.
## Input : [2,2,0,2,2]. Expected output: Result = [4,4,0,0,0]
#lst = merge([2,2,0,2,2])
#print "Result = ", lst
## 8- test some combination of lst of odd size with no pairs.
## Input : [2,4,0,2,8]. Expected output: Result = [2,4,2,8,0]
#lst = merge([2,4,0,2,8])
#print "Result = ", lst



