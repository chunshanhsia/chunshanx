import array
### Question 1

### use an extry array to hold the last shift.  For each step, copy and insert it into X, then update it, and then copy and insert it into Y
### pros: simple logic, easy to understanding, easy to maintain
### cons: used extra moemory to hold the last shift tempary array. And the copy operation may consume more cpu time.
### time complexity: n*(n+1)/2 ==> O(n*n)
### space complexity: n + 2* n*n ==>  O(n*n)
def foo_1(xs, start_token=-1, placeholder=-3):
    size = len(xs)
    T = [placeholder for r in range(size)]
    T[size-1] = start_token
    X = [[]]
    Y = [[]]
    r = 0
    for c in range(size, 0, -1):
        X.insert(r, T.copy())

        for j in range(c-1, size):
            if j > 0:
                T[j-1] = T[j]
                
        T[size-1]= xs[r]
        Y.insert(r, T.copy())
        r +=1
        
    print("X is:")
    for r in X:
        for c in r:
            print(c,end = " ")
        print()
 
    print("Y is:")
    for r in Y:
        for c in r:
            print(c,end = " ")
        print()



### initilize 2 2-dimention array X and Y, then update each one step by step.
### comaring with solution 1 (foo_1)
### pros: no extra memory used, and avoid arry copy operation to have beter performance
### cons:  code logic become little more complex than solution 1.
### time complexity: n*(n+1)/2 ==> O(n*n)
### space complexity: 2* n*n ==>  O(n*n)
def foo_2(xs, start_token=-1, placeholder=-3):
    size = len(xs)
    X = [[placeholder for r in range(size)] for c in range(size)]
    Y = [[placeholder for r in range(size)] for c in range(size)]
    
    Y[0][size-2] = start_token;
    Y[0][size-1] = xs[0];
    X[0][size-1] = start_token;
    
    for r in range(1, size):
        for c in range(size-r-1, size):
            X[r][c] = Y[r-1][c];
            if(c > 0):
                Y[r][c-1] = Y[r-1][c];

        Y[r][size-1] = xs[r];
        
    print("X is:")        
    for r in X:
        for c in r:
            print(c,end = " ")
        print()
    
    print()
    print("Y is:")    
    for r in Y:
        for c in r:
            print(c,end = " ")
        print()
    print()    


### Since Y holds all of the data  X has except X[0], they same portion could be shared 
### pros: reduced memory space from 2*n*n into n*(n+1), as well as good performance as solution 2 does
### cons: programmer needs to know how the array memeory is managed
### time complexity: n*(n+1)/2 ==> O(n*n)
### space complexity: n*(n+1) ==>  O(n*n)
def foo_3(xs, start_token=-1, placeholder=-3):
    size = len(xs)
    X = [[]]
    Y = [[placeholder for r in range(size)] for c in range(size)]
    
    X.insert(0, Y[0].copy())
    X[0][size-1] = start_token;
    Y[0][size-2] = start_token;
    Y[0][size-1] = xs[0];
    
    for r in range(1, size):
        X.insert(r, Y[r-1])
        for c in range(size-r-1, size):
            if(c > 0):
                Y[r][c-1] = Y[r-1][c];

        Y[r][size-1] = xs[r];
    
    print("X is:")     
    for r in X:
        for c in r:
            print(c,end = " ")
        print()
    
    print("Y is:") 
    for r in Y:
        for c in r:
            print(c,end = " ")
        print()

# Test above functions */ 
arr = [1,2, 3, 4, 5, 6]
foo_1(arr)
foo_2(arr)
foo_3(arr)


### Question 2

### use an extry array to map the times of each element appears in the arry 
### pros: simple logic, good performance
### cons: used extra moemory to count each element.
### time complexity: 3*n ==> O(n*n)
### space complexity: n ==>  O(n)
def find_missing_dup_1(arr): 
    size = len(arr)       
    min = arr[0]
    max = arr[0] 
    for i in range(size):
        if arr[i] < min:
            min = arr[i]
        else:
            if arr[i] > max: 
                max = arr[i]
                
    if min + size -1 != max:
        raise Exception(' Invalid input array : {}', arr)   
        
    flag = array.array('i',(0 for i in range(0,size)))   
    for i in range(size): 
        flag[arr[i]-min] +=1
        
    r = 0
    m = 0
    found = 0
    for i in range(size): 
        if flag[i] == 0:
            m = i+min        
            print("The missing element is", m)
            found +=1
            if found == 2:
                break;    
        else:
            if flag[i] == 2:
                r = i+min
                print("The repeating element is", r)
                found +=1
                if found == 2:
                    break;
                    
    if found < 2:
        raise Exception(' Invalid input array : {}', arr)
        
    return ["The missing element is", m, "The repeating element is", r]  


### sorting the array first 
### pros: simple
### cons: used extra for sorting
### time complexity: n*Log(n) + n/2  ==> O(n*Log(n))
### space complexity: no extra space needed
def find_missing_dup_2(arr): 
    size = len(arr)   
    arr.sort();        
    r = 0
    m = 0
    found = 0
    for i in range(1, size): 
        if arr[i] == arr[i-1] +2:
            m = arr[i] - 1       
            print("The missing element is", m) 
            found +=1
            if found == 2:
                break;
        else:
            if arr[i] == arr[i-1]:
                r = arr[i]
                print("The repeating element is", r) 
                found +=1
                if found == 2:
                    break;
 
    if found < 2:
        raise Exception('Invalid input array : {}', arr)
        
    return ["The missing element is", m, "The repeating element is", r] 

### XOR  
### 1. Let x and y be the desired output elements.
### 2. Calculate XOR of all the array elements. xorResult = arr[0]^arr[1]^arr[2]…..arr[n-1]
### 3. XOR the result (xorResult) with all numbers from min to max
### 4. In the result (xorResult), all elements would be nullified by itself except x and y. All the bits that are set in xorResult will be set in either x or y. 
### So if we take any set bit (I have chosen the rightmost set bit in code) of xorResult and then divide the elements of the array in two sets – 
### one set of elements with same bit set and other set with same bit not set. By doing so, we will get x in one set and y in another set. 
### Now if we do XOR of all the elements in first set, we will get x, and by doing same in other set we will get y, then idenfy which is exits in the array or not

### pros: no extra memory, bitwise operation is fast good performance. 
### cons: logic seems complex without in-depth knowledge of bitwise operation
### time complexity: 3*n  ==> O(n)
### space complexity: no extra space needed
def find_missing_dup_3(arr): 
    size = len(arr)
    min = arr[0]
    max = arr[0] 
    for i in range(size):
        if arr[i] < min:
            min = arr[i]
        else:
            if arr[i] > max: 
                max = arr[i]
    
    xorResult = arr[0]
    for i in range(1, size):
        xorResult ^= arr[i]
     
     
    for i in range(min, max+1):
        xorResult ^= i

#Get the rightmost set bit in set_bit_no 
    set_bit_no = xorResult & ~(xorResult - 1); 
    x =0
    y =0
    for i in range(size):
        if(arr[i] & set_bit_no == 1):
            x ^= arr[i]        
        else:
            y ^=  arr[i]
    
    for i in range(min, max+1):
        if(i & set_bit_no == 1):
            x ^= i       
        else:
            y ^= i
            
    xIsDup = False
    yIsDup = False
    for i in range(size):
        if arr[i] == x: 
            xIsDup = True
        else:
            if arr[i] == x: 
                yIsDup = True
    
    if xIsDup == True and yIsDup == False:
        print("The missing element is", y)
        print("The repeating element is", x)      
        return ["The missing element is", y, "The repeating element is", x]
    else:
        if xIsDup == False and yIsDup == True:
            print("The missing element is", x)
            print("The repeating element is", y)      
            return ["The missing element is", x, "The repeating element is", y]
    
    raise Exception('Invalid input array : {}', arr)   
    
    
# Driver program to test above functions */ 
arr = [7,  3, 5, 5, 6, 2]
arr1 = [7,  3, 5, 5, 6, 2, 0,-1,1,-2] 
arr2=[1,1, 3]
arr3=[1,2, 3]
arr4=[1,2, 4]
arr5=[1,2]
arr6=[]
find_missing_dup_1(arr)
print(find_missing_dup_1(arr1))
#find_missing_dup_1(arr2)
#find_missing_dup_1(arr3)
#find_missing_dup_1(arr4)
#find_missing_dup_1(arr5)
#find_missing_dup_1(arr6)

find_missing_dup_2(arr)
print(find_missing_dup_2(arr1))
#find_missing_dup_2(arr2)
#find_missing_dup_2(arr3)
#find_missing_dup_2(arr4)
#find_missing_dup_2(arr5)
#find_missing_dup_2(arr6)

find_missing_dup_3(arr)
print(find_missing_dup_3(arr1))
#find_missing_dup_3(arr2)
#find_missing_dup_3(arr3)
#find_missing_dup_3(arr4)
#find_missing_dup_3(arr5)
#find_missing_dup_3(arr6)
