import time
import matplotlib.pyplot as plt
import numpy as np


def linear_search(A:list, x:int)->bool:
    for i in range(len(A)):
        if A[i]==x:
            return True
    return False


def binary_search(A:list, x:int)->bool:
    left = 0
    right = len(A)-1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == x:
            return True
        elif A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return False

def test_sorted_sequences(length:list,lin:list,bi:list): #->dict:
    #runtimes = {}
    #length= []
    i:int = 1
    with open("sequences_output.txt", "a") as outfile:
        with open("sorted_sequences.txt", "r") as file:
            for line in file:
                length.append(i)
                line = [int(x) for x in line.split()]
                lin_start_time = time.time()
                lin_result = linear_search(line, 500)
                lin_end_time = time.time()
                lin.append(lin_end_time-lin_start_time)
                bin_start_time = time.time()
                bin_result = binary_search(line, 500)
                bin_end_time = time.time()
                bi.append(bin_end_time-bin_start_time)
                outfile.write( str(lin_result) + " " + str(bin_result) + "\n")
                #runtimes[len(line)] = (lin_end_time-lin_start_time, bin_end_time-bin_start_time)
                i = i+1
        #outfile.write(str(length))
    #return runtimes
    #return length
    
def plot_times():
    #lin:list
    #bi:list
    length = []
    lin = []
    bi = []
    test_sorted_sequences(length,lin,bi)
    #length = test_sorted_sequences()
    #x = np.array(runtimes.keys())
    x=[1,2,3]
    #y = np.array(runtimes.values())
    y=[1,4,9]
    with open("sequences_output.txt", "a") as outfile:
         outfile.write(str(length))
    #plt.plot(x, y)
    #plt.plot(length,lin)
    plt.plot(length,lin,'r--',length,bi,'b--')
    plt.xlabel('array length')
    plt.ylabel('time (s)')
    plt.title('Search time')
    plt.grid()
    plt.savefig("search_time.png")
    plt.show()
    
            
plot_times()


 
