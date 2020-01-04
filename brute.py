import time
import array
def calcdiff(i,j,arr):
	return abs(arr[i]-arr[j])+abs(i-j)
def maxdistance(arr,n):
	result=0
	start_time=time.time()
	for i in range(0,n):
		for j in range(i,n):
			if(calcdiff(i,j,arr)>result):
				result=calcdiff(i,j,arr)
	return result
end_time=time.time()
arr = [ -2, 11, -4, 13, -5, -2 ] 
n=len(arr)
print(maxdistance(arr,n))
print(end_time-start_time)
