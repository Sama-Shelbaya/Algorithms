def Insertion_Sort(array):

    for i in range(1 , len(array)):
        
        key = array[i]
        j = i - 1
              
        while j >= 0 and key < array[j]:
            
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key


nums = [5,9,3,10,1,2]
Insertion_Sort(nums)
print("The Ascending Order of the array =")
print(nums)
