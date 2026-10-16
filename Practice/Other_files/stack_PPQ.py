'''
Procedural not OO
stack - pre-populated with data
insertion sort - "inserted array" - items already in it 
binary search - brute force, start to end 
'''


'''
- find first item in unsorted list
- append to sorted
- remove from unsorted
- look at first item in unsorted again
- if its less than sorted[0] then put unsorted[0] into sorted[1],  make sorted[0] sorted [1]
- if its greater than sorted[0] then put it at sorted [1]
- remove from unsorted

'''


#data items
dataItems = [6,15,100,23]
dataArray = [100,22,5,36,999,12]
sortedArray = []


for i in range(0,len(dataArray)):

    unsorted = True
    index = 0
    while unsorted and index < len(dataArray):
        sortedArray.append(dataArray[0])
        print(sortedArray)
        dataArray.remove(dataArray[0])
        print(dataArray)
        index+=1
        