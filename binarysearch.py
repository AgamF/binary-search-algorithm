import time

array = []
item = 0

for x in range(1000):
  item += 1
  array.append(item)
print(array)

def binary_search(arr, n):
  mid_point = len(arr) // 2
  if arr[mid_point] == n:
    return n
  elif arr[mid_point] < n:
    return binary_search(arr[mid_point:len(arr)], n)
  else:
    return binary_search(arr[0:mid_point], n)

def iterative_search(arr, n):
  for item in arr:
    if item == n:
      return n

def main():
  start = time.time()
  print("binary", binary_search(array, 200))
  end = time.time()
  print(f"Operation took {end - start} seconds")
  start = time.time()
  print("iterative", iterative_search(array, 200))
  end = time.time()
  print(f"Operation took {end - start} seconds")

main()
