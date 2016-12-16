# Anthony Gringeri
# acgringeri
# Algorithms, Project 2
# This project involves using recursion and dynamic programming to calculate the probability of a baseball team
#   winning a series of games

import sys
import itertools
import timeit

# increase recursion limit for deep recursion
sys.setrecursionlimit(10000)

def effRecursion(n, p):
    # time algorithm and return both time elapsed and value as a tuple
    start1 = timeit.default_timer()
    prob = recursiveProbability(n, p)
    end1 = timeit.default_timer()
    return ((end1 - start1), prob)

def recursiveProbability(n, p):
    # at least 1 game should be played
    if (n <= 0):
        return False

    # call helper
    return recursiveProbabilityHelper(n, n, p)

def recursiveProbabilityHelper(i, j, p):
    # negative values should not be allowed
    if ((i < 0) or (j < 0)):
        return False

    # base cases
    elif (i == 0):
        return 1
    elif (j == 0):
        return 0

    # recursive element taken from recurrence equation
    else:
        return (((p)*(recursiveProbabilityHelper((i-1), j, p))) + ((1-p)*(recursiveProbabilityHelper(i, (j-1), p))))

def effDP(n, p):
    # time algorithm and return both time elapsed and value as a tuple
    start1 = timeit.default_timer()
    prob = dynamicProgrammingProbability(n, p)
    end1 = timeit.default_timer()
    return ((end1 - start1), prob)

def dynamicProgrammingProbability(n, p):
    # at least one game should be played
    if (n <= 0):
        return False

    # initialize our matrix for saving values
    w, h = (n+1), (n+1)
    matrix = [[0 for x in range(w)] for y in range(h)]

    # call helper
    return dynamicProgrammingProbabilityHelper(n, n, p, matrix)

def dynamicProgrammingProbabilityHelper(i, j, p, matrix):
    # negative values should not be allowed
    if ((i < 0) or (j < 0)):
        return False

    # base cases
    elif (i == 0):
        return 1
    elif (j == 0):
        return 0

    # if a value is stored in the array, then use that
    elif (matrix[i][j] != 0):
        return matrix[i][j]

    # value isn't stored in array, we need to calculate it
    else:
        # save value to matrix
        matrix[i][j] = (((p)*(dynamicProgrammingProbabilityHelper((i-1), j, p, matrix)))
                + ((1-p)*(dynamicProgrammingProbabilityHelper(i, (j-1), p, matrix))))
        # return it
        return matrix[i][j]

def main():
    # main interface for testing algorithms
    print("This program computes the odds of winning a series of n games in the series.")

    testNumber = input("To test both algorithms, enter 0.\n"
                       "To test just the recursive algorithm, enter 1.\n"
                       "To test just the dynamic programming algorithm, enter 2.\n"
                       "Enter a value: ")

    if (testNumber == "0"):
        print("Testing both algorithms...\n")

        n = int(input("Enter n, the number of games needed to win the series: "))
        p = float(input("Enter p, the probability of winning a game: "))

        recursiveTime = effRecursion(n, p)
        dynamicProgrammingTime = effDP(n, p)

        print("")

        print("Probability of winning series (recursive): ")
        print("{:8.3f}".format(recursiveTime[1]))

        print("Time elapsed for recursive algorithm: ")
        print("{:15.10f}".format(recursiveTime[0]), " seconds")

        print("")

        print("Probability of winning series (DP): ")
        print("{:8.3f}".format(dynamicProgrammingTime[1]))

        print("Time elapsed for dynamic programming algorithm: ")
        print("{:15.10f}".format(dynamicProgrammingTime[0]), " seconds")


    elif (testNumber == "1"):
        print("Testing recursive algorithm...\n")

        n = int(input("Enter n, the number of games needed to win the series: "))
        p = float(input("Enter p, the probability of winning a game: "))

        recursiveTime = effRecursion(n, p)

        print("")

        print("Probability of winning series: ")
        print("{:8.3f}".format(recursiveTime[1]))

        print("Time elapsed for recursive algorithm: ")
        print("{:15.10f}".format(recursiveTime[0]), " seconds")

    elif (testNumber == "2"):
        print("Testing dynamic programming algorithm...\n")

        n = int(input("Enter n, the number of games needed to win the series: "))
        p = float(input("Enter p, the probability of winning a game: "))

        dynamicProgrammingTime = effDP(n, p)

        print("")

        print("Probability of winning series: ")
        print("{:8.3f}".format(dynamicProgrammingTime[1]))

        print("Time elapsed for dynamic programming algorithm: ")
        print("{:15.10f}".format(dynamicProgrammingTime[0]), " seconds")

    else:
        print("Please enter a valid value and try again. Exiting...\n")

    exit(0)

# execute main method
main()