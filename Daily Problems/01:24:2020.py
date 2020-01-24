#A Bynary search using Python
import random

def BinarySearch(mylist, elemToFind, start = 0, end = None):
    print(mylist[start:end])
    #First we want to check if it's the first time we're running this search
    if end is None:
        #if it is then we want to sign the end index to the length of the list - 1
        end = len(mylist) - 1
    if start > end:
        #if the start is greateer than the end then there's no way that the element is in the list
        print("IT AIN'T IN HERE CHIEF")
        return False
    
    #If we reached this point then we can keep searching, and assign a midpoint.
    mid = (start + end) //2

    #If it find's in the hurray! it's in the list
    if mylist[mid] == elemToFind:
        print("IT'S IN HERE BOSS")
        return True
    #if not than we're gonna keep on looking
    if mylist[mid] > elemToFind:
        BinarySearch(mylist,elemToFind,start,mid-1)
    if mylist[mid] < elemToFind:
        BinarySearch(mylist,elemToFind,mid + 1, end)


#main program to run the thing and search for it
if __name__ == "__main__":
    #generate a random list of 20 numbers from 1 - 100
    a = random.sample(range(0,100), 20)
    #sort them because Binary search just NEEEEDS it to be sorted
    a.sort()
    #print the list to the user to veryify if the number is in the list
    print(a)

    #asks for number to look for
    elemFind = int(input("Choose an element: "))
    #searches
    IsInList = BinarySearch(a,elemFind)

        