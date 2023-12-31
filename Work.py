
#  File: Work.py
#  Description: Program uses methods of binary search and linear search to find minimum lines of code written by a student
# one function creates the total number of written lines and the other ones solve the problem using the total
#  Student Name: Alec Anaya
#  Student UT EID: aa89468
#  Partner Name: Alyssa Wu Zhang
#  Partner UT EID: awz227
#  Course Name: CS 313E
#  Unique Number: 52525
#  Date Created: 9/30/2022
#  Date Last Modified: 10/1/2022


import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    # Create series to find total number of line written
    series = 0
    count = 0
    term = v
  
    while term > 0:
        term = v // (k ** count)
        series += term
        count += 1
        print(series)
    return series

    
        
            



# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    #uses linear search to find when the first number of lines written will equal the total used in the series
    i=0
    for i in range(n):
        i += 1
        
        if n == sum_series(i,k) or n-1<sum_series(i,k)<=n+1:
            return i
        else:
            continue
        
    #return i
    
            


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    #uses binary search to find when a value will equal the sum of the series which is the total number of lines n
    bottom = 0
    top = n
    while(top >= bottom):
        mid = (top + bottom)//2
        if sum_series(mid,k) < n:
            bottom = mid + 1
        elif n == sum_series(mid,k):
            return mid
        else:
            top = mid -1 
            
    return (bottom)
    



def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
