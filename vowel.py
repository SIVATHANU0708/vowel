a=raw_input()
b=len(a)
p=0
for i in range(0,b):
  if(a[i]=='a'or'e'or'i'or'o'or'u'):
  	p+=1
if(p>=1):
     print ("yes")
else:
     print("no")
