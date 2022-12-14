""""
Write a program that sums each element of a list without itself

ef Input [1,2,5]

1+2,1+5, 2+1,2+5,5+1,5+2

output[ 1,2,3,5,6,7]




"""

list=[1,2,5]
new_list=[]
res=0
leftIdx=0
rightIdx= len(list)-1

while leftIdx <=rightIdx:
      for i in range(1,len(list)+1):
          if list[leftIdx] ==list[-i]:
            new_list.append(list[leftIdx])
          else:
              res = list[leftIdx] + list[-i]
              new_list.append(res)
      leftIdx+=1

#print(new_list)
print(set(new_list))