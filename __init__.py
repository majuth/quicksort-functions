import random
import matplotlib.pyplot as plt
import numpy as np
import timeit

#Median of three quicksort function
def mo3_quickSort(alist):
   mo3_quickSortHelper(alist,0,len(alist)-1)

def mo3_quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = mo3_partition(alist,first,last)

       mo3_quickSortHelper(alist,first,splitpoint-1)
       mo3_quickSortHelper(alist,splitpoint+1,last)


def mo3_partition(alist,first,last):
   middle = ((int) ((last + first) / 2))

   firstValue = alist[first]
   middleValue = alist[middle]
   lastValue = alist[last]

   v = [firstValue, middleValue, lastValue]
   v.sort()
   pivotvalue = v[1]
   values = {firstValue: first, middleValue: middle, lastValue: last}
   pivot = values.get(pivotvalue)

   alist[pivot] = alist[first]
   alist[first] = pivotvalue

   i = first + 1
   for j in range(first + 1, last+1):
        if alist[j] < pivotvalue:
            temp = alist[j]
            alist[j] = alist[i]
            alist[i] = temp
            i += 1

   leftVal = alist[first]
   alist[first] = alist[i-1]
   alist[i-1] = leftVal
   return i - 1



#Normal quicksort function
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

#Testing and graphs
#Testing quicksort
def testQuicksort(arraySize):
    array = []
    for i in range(arraySize):
        array += [random.randint(0,100)]
    quickSort(array)

sizesQuickSort = []
timesQuickSort = []

for i in range(0, 30001, 2311):
    sizesQuickSort.append(i)
    timesQuickSort.append(timeit.Timer(lambda: testQuicksort(i)).timeit(number=(1)))

#Testing median of three sort
def testmo3sort(arraySize):
    array = []
    for i in range(arraySize):
        array += [random.randint(0,100)]
    mo3_quickSort(array)

sizesmo3Sort = []
timesmo3Sort = []


for i in range(0, 30001, 2311):
    sizesmo3Sort.append(i)
    timesmo3Sort.append(timeit.Timer(lambda: testmo3sort(i)).timeit(number=(1)))

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(sizesQuickSort, timesQuickSort, s=10, c='b', marker=".", label='Quick Sort')
ax1.scatter(sizesmo3Sort, timesmo3Sort, s=10, c='r', marker=".", label='MO3 Quick Sort')
plt.xlabel('Array size')
plt.ylabel('Time')
plt.legend(loc='upper left')
plt.title('Time for Quick sort vs MO3 Quick Sort')
plt.show()
