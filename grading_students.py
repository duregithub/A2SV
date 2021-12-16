#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    output = []
    for i in range(len(grades)):
        if grades[i] < 38 or grades[i] == 100:
            output.append(grades[i])
        else:
            
            if (grades[i] % 10) <= 5:
                if (grades[i] - (grades[i] % 10) + 5) - grades[i] < 3:
                    output.append((grades[i] - (grades[i] % 10)) + 5)
                    
                else:
                    output.append(grades[i])
            else:
                
                if (grades[i] - (grades[i] % 10) + 10) - grades[i] < 3:
                    print(grades[i])
                    output.append((grades[i] - (grades[i] % 10)) + 10)
                else:
                    output.append(grades[i])
    return output
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
