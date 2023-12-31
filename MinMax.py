# File: MinMax.py
# Student:Alec Anaya
# UT EID:aa89468
# Course Name: CS303E
#
# Date: 2-25-2022
# Description of Program: This program is supposed to give you the maximum and minimum values out of a set of numbers that are input by
# a user. What my program does is allow for a set of numbers and then give the max and min values I set. I thought they would be place
# holders so my if satements could decipher what to do with them but i could not get my desired output. I
# im sorry i failed you i will do better next week.


def main():
    
    while(True):
        number = input("Enter an integer or 'stop' to end: ")
        maximum = 0
        minimum = 0
        if (number == "stop"):
            print("The maximum is" , maximum)
            print("The minimum is" , minimum)
            break
        
        if (number != "stop"):
            int(number)
            #maximum = int(number)
            #minimum = int(number)
            continue
        if (int(number) > maximum):
            maxmimum = number
            continue
                
        if (int(number) < minimum):
            minimum = number
            continue
            
                
            

        
                
                
            
                
                    
            #print("The maximum is" + maximum)
            #print("The minimum is" + minimum)
            #break
        #else:
        
            #print("The maximum is" + maximum)
            #print("The minimum is" + minimum)
            #break
            #int(number)
            #maximum=number
            #minimum=number
            
        
       

main()        
    
