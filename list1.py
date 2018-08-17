print("program of list")
all_list=[]
for i in range(1,10):
    all_list.append(i)  
   
   
print(all_list)
even=[]
odd=[]
for j in all_list:
    if(j%2==0):
       even.append(j)

    else:
        odd.append(j)

print('even list are: ',even)
print('odd list are: ',odd)

