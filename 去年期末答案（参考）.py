
# coding: utf-8

# In[8]:


def abc(a,b):
    for i in range(1,b):
        print(' '*(b-i)+i*a)
    for j in range(b,0,-1):
        print((b-j)*' '+j*a)
        
def main():
    abc(' *',5)
    
if __name__ == '__main__':
    main()


# In[2]:


"""2、用递归和非递归分别实现函数求1!+2!+3!+...+n!，主程序以n=10分别调用。（20分）"""
def asd(n):
    sum1=1
    sum2=0
    for i in range(1,n+1):
        sum1=sum1*i
        sum2=sum2+sum1
    return sum2

def main():
    print("1!+2!+3!+...+n!=",asd(10))

if __name__ == '__main__':
    main()


# In[3]:


def dfg(n):
    if n==0:
        return 1
    else:
        return n*dfg(n-1)x

def fgh(n):
    if n==0:
        return 0
    else:
        return dfg(n)+fgh(n-1)

def main():
    print("1!+2!+3!+...+n!=",fgh(10))

if __name__ == '__main__':
    main()


# In[7]:


"""3、北京车牌号的一般形式为：“京X-YYYYY”，其中X为字母，Y为字母或者数字，字母不能为I或者O，数字只能0-9之间。
请编写程序模拟选号过程：一次可以随机生成10个车牌号（不能有重复），依次将其编号为0-9，显示给用户。（20分）"""
import random
list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list2=['A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
list3=['0','1','2','3','4','5','6','7','8','9']
for i in range(1,11):
    print(i,'京',end='')
    print(random.choice(list1),end='')
    print('-',end='')
    print(random.choice(list2),end='')
    print(random.choice(list3),end='')
    print(random.choice(list3),end='')
    print(random.choice(list3),end='')
    print(random.choice(list3),end='')
    print()


# In[ ]:


a = [1,2,3,4]
b = [4,5,6,7]
c = [7,8,9,10]
import math
x = ((3-1)*(6-4)+(4-2)*(7-5))/(math.sqrt((3-1)**2+(4-2)**2)*math.sqrt((6-4)**2+(7-5)**2))
print(x)


# In[ ]:


import random
A=[]
for i in range(100000):
    a=random.randint(1,10000)
    A.append(a)
numbers = A
numbers_dict_1={}
 for num in numbers:
    if num in numbers_dict_1:
        numbers_dict_1 [num] += 1
    else:
        numbers_dict_1 [num] = 1
b = []        
for key, value in numbers_dict_1.items():  
    a = key, value
    b.append(a) 
    
fileObject = open('a.txt', 'w')  

for i in range(len(b)): 
    if i%2==0:
        fileObject.write(str(b[i])) 
        fileObject.write(',') 
    else:
        fileObject.write(str(b[i])) 
        fileObject.write('\n')  
fileObject.close() 

