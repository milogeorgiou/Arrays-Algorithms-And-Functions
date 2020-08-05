###############################################################################################################
#SUMMARY: This function should find the single character out of a longer string that isn't a duplicate
#Date: 01/08/2020
#Environment: Python 3 Jupyter
###############################################################################################################

#8. Given the following string "aabbccedd"
#create a function called "find_non_duplicate_in_str(string)" that will return the element that is not duplicated i.e: 'e'

################################################################################################################
#SUMMARY: Fairly Similar to the first function to find Duplicates
#However some variables are changed
#The function should find similar letters in the dictionary, counting each time a unique letter appears.
#Parameters: str, or any string.
#Returned Output: 
#True
#True
#True
#True
#True
################################################################################################################

def find_non_duplicatesstr(str):
    #phase 0
    dictcountstr={}
    #phase 1
    for element in str:
        if element in dictcountstr:
            dictcountstr[element]=dictcountstr[element]+1
        else:
            dictcountstr[element]=1
        #print(element, "comes up", dictcount[element], "time(s)")
    #print(dictcount)
    #phase 2
    for key in dictcountstr:
        if dictcountstr[key]!=2:
            #print(key)
            return(key)
    return(-1)
################
#Main Function
################

str="aabbccedd"
str2="aannmmkklljjhhggyyttrruuiioppccxx"

print(find_non_duplicatesstr("aabbccedd")=="e")
print(find_non_duplicatesstr("hhggjjyyuuiivvx")=="x")
print(find_non_duplicatesstr("aabbccddeff")!="v")
print(find_non_duplicatesstr("")==-1)
print(find_non_duplicatesstr(str2)=="o")

#############
#End of File
#############
