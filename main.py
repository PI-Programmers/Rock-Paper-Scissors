n=int(input("Enter the range"))
k=0
for j in range(1,n+1):
    if j>1:
        if j==2:
            print("2=1 , 2(prime)")
        else:
            for i in range(2,j):
                if j%i==0:
                    k=1
                    break
                elif j%i!=0:
                    k=2
                
        if k==1:
            print(j,"=","1 , ", end=" ")
            for i in range(2,j):
                if j%i==0:
                    print(i,end=" , ")
            print(j)
                    
        elif k==2:
            print(j,"=",1, " , ",j,"(prime)")
    elif j==1:
        print("1=1")
    
    
    
