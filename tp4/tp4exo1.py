print("veuillez choisir une table de multiplication :")
a=float(input())
m=[0,1,2,3,4,5,6,7,8,9]
for i in range ( 0 , 10 ) :
    m[i] =round(m[i]*a , 2 )
    print(a,"*",i,"=", m[i])