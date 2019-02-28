n=input("Enter a number")
if n%10==0:
  print(n)
else:
  if len(n)>1:
    slice=len(n)-1
    for i in n:
      num=int(n[:slice])
      num=num+1
    print(str(num)+'0')
  else:
    print("10")
