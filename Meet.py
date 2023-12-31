#  File: Meet.py

#  Description: Determine earlist meet time interval for two people

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 86610

import sys

def earliestPossibleMeeting(person1, person2, duration):
   person1.sort()
   person2.sort()
   overlap = []
   for interval in person1:
       lower1 = interval[0]
       upper1 = interval[1]
       for interval2 in person2:
           lower2 = interval2[0]
           upper2 = interval2[1]
           if lower1 >= lower2:
               new_low = lower1
           else:
               new_low = lower2
           
       
    
                                             
                
        
        
        






def main():
        #test_cases()

	# read the input data and create a list of lists for each person
	f = sys.stdin
	# read in the duration
	dur = int(f.readline().strip())
	# person 1's number of avalible slots
	num1 = int(f.readline().strip())
	p1 = []
	for x in range(num1):
		line = f.readline()
		l = line.strip().split()
		tmp = [int(l[0]), int(l[1])]
		p1.append(tmp)

	# person 2's number of avalible slots
	num2 = int(f.readline().strip())
	p2 = []
	for x in range(num2):
		line = f.readline()
		l = line.strip().split()
		tmp = [int(l[0]), int(l[1])]
		p2.append(tmp)

	print(earliestPossibleMeeting(p1,p2,dur))

if __name__ == "__main__":
  main()
