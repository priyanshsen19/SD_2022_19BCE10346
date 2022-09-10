p2=list()
position=list()

matrix = [] 
R=5
C=5
flag=0
p1=list(input("Player1 Input:").split(', '))
while(flag!=len(p1)):
    flag=0
    for I in p1:
        no=int(I[-1])
        if no>5 or no<1:
            print("Character going out of grid bounds!Retry")
            p1=list(input("Player1 Input:").split(', '))
            flag=0
        else:
            flag+=1
            continue
    
for i in range(R):
    c="A-"
    c+=p1[i]
    p1[i],c=c,p1[i]
for i in range(R):          
    a=[]
    for j in range(C):       
        if i!=4:
            a.append("-   ")
        else:
            matrix.append(p1)
            break
    matrix.append(a) 
for i in range(R): 
    for j in range(C):
        print(matrix[i][j], end = " ") 
    print()
p2=list(input("Player2 Input:").split(', '))
while(flag!=len(p2)):
    flag=0
    for I in p2:
        no=int(I[-1])
        if no>5 or no<1:
            print("Character going out of grid bounds!Retry")
            p2=list(input("Player2 Input:").split(', '))
            flag=0
        else:
            flag+=1
            continue   
for i in range(R):
    c="B-"
    c+=p2[i]
    p2[i],c=c,p2[i]
for i in range(R):
    for j in range(C):
        if i==0:
            matrix[i][j]=p2[i]       
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ") 
    print()


 
