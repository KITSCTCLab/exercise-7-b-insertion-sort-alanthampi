from typing import List

def insertionSort(array) -> List[int]:
    size = len(array)
    for i in range(1,size):
        key = array[i]
        j = i
        while(j>0 and array[j-1]>key):
            array[j] = array[j-1]
            j = j-1
        array[j] = key 
    return array

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
