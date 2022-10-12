from typing import List

def insertionSort(array,size) -> List[int]:
  for i in range(size-1):
      key = array[i]
      j = size-1
      while(j>=0 and a[j]>key):
          list[j+1] = list[j]
          j = j-1
          list[j+1] = key

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
