
def three_point_mid(f,a,index,h):
    val = (f[a+index]-f[a-index])/(2*h) 
    return val

def three_point_end(f,a,index,h) :

    val = (-3*f[a]+4*f[a+index]-f[a+2*index])/(2*h)
    return val



h= 0.1
x = [1.1,1.2,1.3,1.4]
f=[9.025013,11.02318,13.46374,16.44465]
index = 1

count = 0
for i in range(4) : 
 if count == 0 :
    print(three_point_end(f,i,index,h))
 elif count== len(f)-1 :
    print(three_point_end(f,i,-index,-h))   
 else :
    print(three_point_mid(f,i,index,h))   
 count += 1    


