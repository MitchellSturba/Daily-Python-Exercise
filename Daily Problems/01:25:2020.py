#There's a staircase with N steps, and you can climb 1 or 2 steps at a time.
#Given N, write a function that returns the number of unique ways you can climb the staircase.

#A recursive solution
def StairCase(N):
    if N <= 1:
        return 1
    else:
         return StairCase(N - 1) + StairCase(N - 2)

#A faster iterative approach
def StairCase2(N):
    if StairCase == 1:
        return 1
    else:
        a, b = 1, 1
        for x in range(N):
            a, b = b, a + b
        return a

if __name__ == '__main__':
    #get input
    stairs = int(input('Please etner the amount of stairs in the staircase: '))

    #Run Recursive
    uniqueCombos = StairCase(stairs)
    #Run iterative
    uniqueCombosI = StairCase2(stairs)

    #print recursive
    print('There are ' + str(uniqueCombos) + ' unique ways to climb the staircase')
    #print iterative
    print('There are ' + str(uniqueCombosI) + ' unique ways to climb the staircase')
