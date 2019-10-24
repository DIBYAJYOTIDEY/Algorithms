l = [2,3,4,5,6,8]
s= int(input("Enter search number:"))
n = len(l)
for i in n:
	# TODO Fill Code here
  if (n==0):
    low=0
    high=n
  mid=(low+high)/2
  if (s==mid):
    print ("No. found")
    break
  elif (s>mid):
    low=mid+1
  elif:
    high=mid-1
