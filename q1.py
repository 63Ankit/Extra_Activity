# ====================Advance Python=================
#================== Comprehension Question===========
'''
1. List Comprehension
2. Set Comprehension
3. dictionary comprehension

Question Based on the list Comprehension

Question Based on the Dictionary Comprehension
'''
# OOPS Concept here. 
'''
Class
(Inbuilt class, User Define Class)
Access the properties of the class:= using the class name and using the object name 
Object
Object Properties 
Class properties
Class method 
object method 
static method

Piller of the OOPS:
1 Inheritance:-
2 Encapsulation:-
3 Polymorphism 
4 Abstraction

# find even and odd without using the modulus operator 
num = int(input("Enter a number: "))

last_digit = num - (num // 10) * 10  # Extract last digit

if last_digit in [0, 2, 4, 6, 8]:
    print("Even")
else:
    print("Odd")

# Using the Bitwise Operator
num = int(input("Enter a number: "))

if (num & 1) == 0:
    print("Even")
else:
    print("Odd")
 # Using a simple method
 num = int(input("Enter a number: "))
n = num

while n > 1:
    n = n - 2

if n == 0:
    print("Even")
else:
    print("Odd")




n1=int(input("Enter a number: "))
if n1%2==0:
    print(n1**3)


#WAP to print last value from the list it should be string and is length should be more than 3
l1=["Ankit","AJva","ujhdd"]
if type(l1[2])==str and len(l1[2])>3:
    print(l1[2])

# use of isinstance
l1=["Ankit","AJva","ujhdd"]
print(isinstance(l1,list))


# WAP to check character is in upperCase
A="Ankit"
if "A"<=A[0]<="Z":
    print(A[0])

# WAP to check character is in Special Char
A=input("Enter a Char: ")
if not "A"<=A<="Z" and not "a"<=A<="z" and  not "0"<=A[0]<="9":
    print(A)

#WAP to chaeck the character is vovwl or consonent 
a=input("ENter a Char: ")
if a in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonent")

#WAP to check the data is single valued data or multivalued data 
data=eval(input("Enter something"))
if type(data) is (int or float or complex or bool) :
    print("Singal valued ")
else:
    print("Multi valued ")
    
# WAP to print cube of even number and square of odd number
n=int(input("Enter a number: "))
if n%2==0:
    print(n**3)
else:
    print(n**2)



# 
a=input("Enter a char")
if "A"<=a<="Z":
    print("Upper Case")
elif "a"<=a<="z":
    print("Lower Case")
elif "0"<=a<="9":
    print("Number ")
else:
    print("Sp. Character ")

# WAP to create a marksheet to respective grades
marks=int(input("Enter your marks here: "))
if 90<=marks<=98:
    print("Grade A")
elif 70<=marks<=89:
    print("Grade A")
elif 45<=marks<=69:
    print("Grade C")
else:
    print("Grade D") 

# WAP to program to check if a number is divisible by 3 "FIZZ" 5 "BUZZ" 3&5 "FIZZBUZZ"
n=int(input("ENter a number: "))
if  n%5==0 and n%3==0:
    print("FIZZBUZZ")
elif n%5==0:
    print("BUZZ")
elif n%3==0:
    print("FIZZ")

    
n1=int(input("Enter the number 1"))
n2=int(input("Enter the number 2"))
n3=int(input("Enter the number 3"))
n4=int(input("Enter the number 4"))

if n1>n2 and n2>n3 and n3>n4:
    print(n1)
elif n2>n3 and n3>n4:
    print(n2)
elif n3>n4:
    print(n3)
else:
    print(n4)
    

#  WAP to check the number is divisible by 5 and even number
n=int(input("Enter a number: "))
if n%5==0:
    if n%2==0:
        print("Divisible by 5 and also even ")
    else:
        print("divisible by 5 but not even")
else:
    print("not divisible 5 ")



# WAP to check the char is vowel or cons using nested if
n=input("Enter a char: ")
if "A"<=n<="z":
    if n in "AEIOUaeiou":
        print("Vowel")
    else:
        print("Not vowel")
else:
    print("Not a char")


# WAP to find the greatest number among three nummbers using nested if
n1=10
n2=20
n3=30
if n1>n2:
    if n1>n3:
        print(n1)
    else:
        print(n3)
else:
    if n2>n3:
        print(n2)
    else:
        print(n3)+


# WAP to create a email cridential
n1=input("Enter here Email: ")
n2=input("Enter here  Password: ")
if n1=="A@gmail.com":
    if n2=="Ankit@123":
        print("Login Sucessful")
    else:
        print("Password is Wrong:")
else:
    print("Wrong email")


# 
#==================================================================================================
# ======================================== While Loop===========================================
# WAP to print hello world 10 times
i=1
while i<=10:
    print("Hello World")
    i+=1

    
# WAP to print first 10 natural number
i=1
while i<=10:
    print(i)
    i+=1



# 
# WAP to print first 10 natural number
i=1
while i<=10:
    print(i,end=' ')
    i+=1

# Wap to print alll even numbers between 1 to 15
i=1
while i<51:
    if i%2==0:
        print(i)
    i+=1


# WAP to check is the number even print cube of it if number in odd print square of it 
i=1
while i<=50:
    if i%2==0:
        print(i**3)
    else:
        print(i**2)
    i+=1


# WAP to print number divisible by 5 between m to n
m=int(input("ENter a number"))
n=int(input("ENter a number"))
while m<=n:
    if i%5==0:
        print(i)
    i+=1

#WAP to print sum of first 10 natural number
i=1
sum=0
while i<=10:
    sum=sum+i
    i+=1
print(sum)


#WAP to print product of first 10 natural number
i=1
Product=1
while i<=10:
    Product=Product*i
    i+=1
print(Product)


# reverse a number whithout using slicing
a=345
sum=0
while a!=0:
    sum=sum*10+a%10
    
    a=a//10
    i+=1
print(sum)



# WAP to print all the upper case alphabet for the given string
a="AnkitS"
i=0
while i<len(a):
    if "A"<=a[i]<="Z":
        print(a[i])
    i+=1

# WAP to print all the upper case alphabet for the given string
a="DAtaSCiENce"
add=''
i=0
while i<len(a):
    if "A"<=a[i]<="Z":
        add+=a[i]
    i+=1
add1=add+str(len(add))
print(add1)

# WAP to print all the integers present inside the list.
A=["Ankikt",10,20]
i=0
while i<len(A):
    if type(A[i])==int:
        print(A[i])
    i+=1

#==================================================================
a='ababccad'
d={}
i=0
while i<len(a):
    d[a[i]]=a.count(a[i])

    i+=1
print(d)


#==============================================================
a='Python is very easy'
a1=a.split()
i=0
d={}
while i<len(a1):
    d[a1[i]]=a1[i][::-1]
    i+=1
print(d)

#=================================================
a='Python is very easy'
a1=a.split()
i=0
d={}
while i<len(a1):
    if i%2==0:  
        d[a1[i]]=a1[i][::-1]
    else:
        d[a1[i]]=a1[i][::-1]+str(len(a1[i])*2)                         
    i+=1
print(d)

#==================================================
i=1
n=int(input("Enter a number here: "))
while i<=10:
    print(f"{n}*{i}={n*i}")
    i+=1

    
#==================================================
a=512
sum=0
while a>0:
    sum=sum+a%10
    a=a//10
print(sum)   


# 
a='Hello'
b='bye'
c=a+b
i=0
i1=len(a)
s=''
while i<len(a):
    s=s+c[i]
    s=s+c[i1]
    i+=1
    i1+=+i1
print(s)


a='Hello'
b='bye'
i=0
out=''
while i<len(a) or i<len(b):
    if i<len(a):
        out+=a[i]
        
    if i<len(b):
        out+=b[i]
    i+=1
print(out)


a='ababccad'
d={}
i=0
while i<len(a):
    d[a[i]]=a.count(a[i])

    i+=1
print(d)
#=============================================================
a='aaabcbbc'
i=0
out=''
c=1
while i<len(a)-1:
    if a[i]==a[i+1]:
        c+=1
    else:
        out+=a[i]+str(c)
        c=1
    i+=1
out+=a[-1]+str(c)
print(out)
#====================================================

a=['Hai',10,'Hai',3+5j,35,10,[1,2,3]]
out=[]
i=0
while i<len(a):
    if a[i] not in out:
        if a.count(a[i])>1:
         out+=[a[i]]
    i+=1
    
print(out)
  

a=[777,'hello',121,12,3+5j,99,123]
output=[777,121,99]
i=0
out=[]
while i<len(a):
    if type(a[i]==int) and str(a[i])==str(a[i])[::-1]:
        out+=[a[i]]
    i+=1
print(out)


#==================================
a=['Hello',10,'Python','star',[1,2,3],'ab']
i=0
out={}
while i<len(a):
    if type(a[i])==str:
        if i%2==0:
            out[a[i]]=a[i][::-1]+str(len(a[i])*2)
        else:
            out[a[i]]=len(a[i])*2
    i+=1

print(out)


#================================================================

a='((()))('
i=0
count=0
while i<len(a):
    if a[i]=='(':
        count+=1
    elif a[i]==')':
        count-=1
        
print(count)


#====================================================
a='((()))('
i=0
count=0
count1=0
while i<len(a):
    if a[i]=='(':
        count+=1
    elif a[i]==')':
        count1+=1
        
print(abs(count-count1))



#===================================================
n1=int(input("Enter a number here: "))
count=0
i=1
while i<n1:
    if n1%i==0:
        count+=i
    
    i+=1
print(count)
if count==n1:
    print("perfect number ")
else:
    print("not a perfect")

#===================================================


# Print natural number
for i in range(1,11):
    print(i,end=' ')

# WAP to print all the even numbers between 1 to 15
for i in range(1,16):
    if i%2==0:
        print(i)

# WAP to print the length of the collection without len()
count=0
for i in "Ankit":
    count+=1
print(count)




d=[10,20,30,40]
count=0
for i in d:
    count+=1
print(count)


d={'name':'Ankit','age':12}
for i in d:
    print(d[i])
print(d.keys())
print(d.values())
print(d.items())


d={'name':'Ankit','age':12}
for i in d.values():
    print(i)


# WAP to extract all the upper case alphabet from the given string.
a='AnKitA'
for i in a:
    if 'A'<=i<='Z':
        print(i)



#============================================================
a='AnKitA'
for i in range(len(a)):
    if 'A'<=a[i]<='Z' and i%2==0:
        print(a[i])


#============================================================
# WAP to extract all the integers from a list using isInstanse
l1=[10,20,30,40,50,'Ankit',87]
l2=[]
for i in l1:
    if isinstance(i,int):
        l2.append(i)
print(l2)



# WAP to check number of upper case with number of lower case present insside a string if number of upper cases a  more then number of lowercase then concat uppercase alphabet with lower case alphabet if not print the p[rodunct ] length of uppercase with lower case alphabet

A='AnkitAag'
upper=''
lower=''
for i in A:
    if "A"<=i<"Z":
        upper+=i
    elif 'a'<=i<'z':
        lower+=i
if len(upper)>len(lower):
    print(upper+lower)
else:
    print(len(upper)*lower)




# WAP to print factorial of a number
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)



# WAP 
str1='nitin how is ava'
l1=[]
for i in str.split(' '):
    if str(i)==str(i)[::-1]:
        l1.append(i)
print(l1)


# WAP 
a=['hai',3,3.3,[1,3,3],'hello']
for i in a:
    if type(i)==int or type(i)==complex or type(i)==float:
        print(i)
    
'''
a=['hai',3,3.3,[1,2,3],'Hello']
a1=[]
for i in a:
    if type(i)==int or type(i)==complex or type(i)==float:
        a1.append(1)
    else:
        a1.append(len(i))
print(a1)
