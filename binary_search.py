'''
Created on Mar 2, 2019

@author: Shubham
'''

# element id the value we need to find in list
import timeit
import matplotlib.pyplot as plt 

def binary_search(input_list,element):
    right_index=len(input_list)-1
    left_index=0
    def recursive(left_index,right_index,element):
        mid=left_index+(right_index-left_index)//2

        if(input_list[mid]==element):
            return mid
        elif(input_list[mid]>element):
            right_index=mid-1
            return recursive(left_index, right_index, element)
             
            
        else:
            left_index=mid+1
            return recursive(left_index, right_index, element)
    
    index=recursive(left_index, right_index, element)
    return index
element_list=[1,2,3,4,5,6,7,8,9,10]
timer_list=[]
for element in element_list:
    input_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    start = timeit.default_timer()
    element_index=binary_search(input_list,element)
    stop = timeit.default_timer()
    timer_list.append((stop-start)/60)
    print(element_index )
print(min(timer_list),timer_list.index(min(timer_list)))



  
# x axis values 
y = timer_list 
# corresponding y axis values 
x = element_list
# plotting the points  
plt.plot(x, y) 
plt.ylabel('timer') 
# naming the y axis 
plt.xlabel('element') 
  
# giving a title to my graph 
plt.title('BS') 
  
# function to show the plot 
plt.show()