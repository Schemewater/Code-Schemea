# File: Anagrams.py

# Description: A program to group strings into anagram families

# Student Name: Alec Anaya

# Student UT EID: AA89468

# Course Name: CS 313E

# Unique Number:

# Output: True or False
def are_anagrams(str1, str2):
    #if str1!= int() and str2 != int:
    newstr1 = list(str1)
    newstr2 = list(str2)
    newstr1.sort()
    newstr2.sort()
    if (newstr1 == newstr2):
        return True
    
    else:
        return False


# Input: lst is a list of strings comprised of lowercase letters only
# Output: the number of anagram families formed by lst
def anagram_families(lst):
    newlst = []
    if len(lst) == 1:
        return 1
    else:
       # for i in lst:
            #for j in lst:
                #if are_anagrams(i,j)==True:
                    #newlst.append(i)
        scheme =[]
        for i in lst:
            scheme.append(sorted(i))
        print(scheme)
        new = set(scheme)
        print(new)
        return len(new)
            
    
        
        #return le"n(tuple(newlst))
 
anagram_families(['ate','bat','cat','eat','rat','tab','tea'])
            


"""def main():
    # read the number of strings in the list
    num_strs = int(input())

    # add the input strings into a list
    lst = []
    for i in range(num_strs):
        lst += [input()]

    # compute the number of anagram families
    num_families = anagram_families(lst)

    # print the number of anagram families
    print(num_families)

if __name__ == "__main__":
    main()
"""