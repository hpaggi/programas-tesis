def main():
    import numpy
    import random
    for i in (10,20,30,50,100,200,300,600):
        s="H"+str(i)
        f= open(s, 'w', encoding='ascii', errors='ignore')
        H=numpy.zeros((i+1,73), dtype =float)
        for k in range(0,i+1):
            for j in range(0,73):  # 73 es el numero de campos +1
                H[k,j]=max(1-random.random()-0.5,0.01)
        for k in range(0,i+1):
            for j in range(0,73):                
                f.write(str(H[k,j])+"\n")
        f.close()
        
        
main()