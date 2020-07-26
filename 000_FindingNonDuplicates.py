###############################################################################################################
#SUMMARY: The aim of this function is to find any number that doesn't appear twice.
#Date: 26/07/2020
#Environment: Python 3 Jupyter
###############################################################################################################

#7. Given the following array [5,1,5,1,2,3,3,4,4], create a function called "find_non_duplicate_in_arr(array)"
#That will return the element that is not duplicated i.e: '2'
#[5,1,5,1,2,3,3,4,4]

################################################################################################################
#SUMMARY: This function will populate a dictionary with the amount of times each number in an  array appears.
#It will then check the values are not 2. If they are not equal to 2, then they count them as non duplicates.
#Parameters: An array named "arrayc" - (can have any numbers inside)
#Returned Output: Returns the key that is not equal to 2. Could be multiple keys.
#If it comes back with an error, it will return -1. An error means there are only duplicates, or nothing at all.
################################################################################################################
def find_non_duplicates(arrayc):
    #phase 0
    dictcount={}
    #phase 1
    for element in arrayc:
        if element in dictcount:
            dictcount[element]=dictcount[element]+1
        else:
            dictcount[element]=1
        #print(element, "comes up", dictcount[element], "time(s)")
    #print(dictcount)
    #phase 2
    for key in dictcount:
        if dictcount[key]!=2:
            #print(key)
            return(key)
    return(-1)
################
#Main Function
################

ar=[5,1,5,1,2,3,3,4,4]
ar2=[2,4,12,5,23,5,23,6,2,3,6,1,2,61,2,6,1,2,6,23,6,23,47,2,346,23,5,2,4,2,24,2,4,24,2,424,2,42,4,2]

print(find_non_duplicates([5,1,5,1,2,3,3,4,4])==2)
print(find_non_duplicates([1,1,6,6,7,7,5,8,8])==5)
print(find_non_duplicates([1,1,2,2,3,3])==-1)
print(find_non_duplicates([])==-1)
print(find_non_duplicates(ar2)==2)

#############
#End of File
#############
