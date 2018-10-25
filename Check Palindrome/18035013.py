#to check number palindrome
def pallindrome(n):
  tmp=n
  rev=0
  while (tmp>0):
    rev=(rev*10)+rev%2
    tmp/=10
  if (rev==n):
    print n,"is a Pallindrome."
  else:
    print n,"is not a Pallindrome."
    
