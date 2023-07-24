arr = [1,2,1,3,5,6,4]

length = len(arr);
max = arr[0];
index = 0;

for x in range(length):
    
    if arr[x] > max :
        max = arr[x]
        index = x

print(index);
