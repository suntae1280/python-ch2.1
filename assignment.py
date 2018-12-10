a=1
b= a+1

print(a,b ,sep ='_____') #parameter 구분자 생성가능

print(a,b) # default parameter = " "

# 세미콜론으로 치환문 구분

e = 3.5; f =5.3
print(e,f)

#동시에 여러개 변수에 값 지정
e,f=3.5,5.3
print(e,f)

#같은값을 여러변수에 할당
x=y=z=10

print(y,x,z)


print (e,f)
e,f = f,e
print(e,f)


#동적타이핑 : 변수에 새로운 값(타입)이 할당되면 기존의 값을 버리고  새로운 값 으로 치환


a=1
print(a,type(a))
a="hello"
print(a,type(a))



#확장치환문

a=10

a+=10
print(a)