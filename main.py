# python3

def parallel_processing(n, m, data):
    output = []
    
    threads=[0] * (int(n)) #what have i done....
    curentThread =int(0)
    curenttask=0
    virtsecond = 0
    flag=False
    while(not flag):
        for curentThread in range(0,int(n)):
            if int(threads[curentThread]) == 0:
                threads[curentThread]=data[curenttask]-1
                output.append((curentThread,virtsecond))
                curenttask+=1
                if curenttask==int(m):
                    flag=True
                    break
            else: threads[curentThread] =int(threads[curentThread])-1
        virtsecond+=1

    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    
    print("write n and m")
    nAndM = input().split(" ")
    n = nAndM[0]
    m = nAndM[1]
    print("write data")
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))
    

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)


if __name__ == "__main__":
    main()
