from collections import defaultdict 
  
# Function for min operation  
def minOperation(arr, n):  
  
    # Insert all elements in hash.  
    Hash = defaultdict(lambda:0)  
    for i in range(0, n):  
        Hash[arr[i]] += 1
  
    # find the max frequency  
    max_count = 0
    for i in Hash:  
        if max_count < Hash[i]:  
            max_count = Hash[i]  
  
    # return result  
    return n - max_count  
  
# Driver Code 
if __name__ == "__main__":  
  
    arr = [1, 1, 1, 1, 2, 2, 2] 
    n = len(arr)  
    print(minOperation(arr, n)) 
      