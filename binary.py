n=input()
flag=True
for i in n:
  if i!='0' and i!='1':
    flag=False
    break
if flag==False:
  print("no")
else:
  print("yes")
