file = open("Data1.txt", "r")
m, n = map(int,file.readline().strip().split())
c = list(map(float,("0 "*m).split()))
c.extend(list(map(float,file.readline().strip().split())))
c.append(0)
A = []
for i in range(m):
    constrain = list(map(float,("0.0 "*i + "1.0 "+ "0.0 "*(m-1-i)).split()))
    constrain.extend(list(map(float,file.readline().strip().split())))
    A.append(constrain)
"""print("Inıtial")
for i in A:
    print(i)
print("__________________________________________________")
print(c)
print("\n \n \n")"""

basic_variables = [i for i in range(m)]

a = 0
is_feasible = True
while(all(n>=0 for n in c[:n+m])==False):
                
    ind_list = c.copy()
    ind_list = sorted(ind_list)
    min_index = ind_list[0]
    basic_line_index = -1
    new_basic_cons = 100000

    for j in ind_list:
        min_index = c.index(j)
        if j >= 0:
            break
        is_break = False
        for i in range(m):
            if (A[i][min_index] > 0 and (A[i][-1]/A[i][min_index]) < new_basic_cons and A[i][-1] > 0):
                new_basic_cons = A[i][-1]/A[i][min_index]
                basic_line_index=i
                is_break = True
        if is_break:
            break
    
    basic_variables[basic_line_index] = min_index

    if basic_line_index==-1:
        print("Unbounded")
        is_feasible = False
        break
    
    multiplier=1/A[basic_line_index][min_index]
    A[basic_line_index] = [x * multiplier for x in A[basic_line_index]]
    for i in range(m):
        if i != basic_line_index:
            variable2 = A[i][min_index]   #variable2 seçilen line min indexindeki eleman 
            for num in range(len(A[i])):
                A[i][num]= A[i][num]-A[basic_line_index][num]*variable2

    variable2 = c[min_index]               #variable2 seçilen line min indexindeki eleman 
    products=[] 
    for num in range(len(c)):
        c[num]= c[num]-A[basic_line_index][num]*variable2
    
    a+= 1
    """print("Iteration : ",a)
    for i in A:
        print([round(x ,3) for x in i])
    print("__________________________________________________")
    print([round(x ,3) for x in c])
    print("\n \n")"""


output = [0 for i in range(m+n)]

index= 0
for i in basic_variables:
    output[i] = A[index][-1]
    index +=1

if is_feasible:
    print("Optimal variable vector:")
    print([round(x ,3) for x in output[m:]])
    print()
    print("Optimal result:")
    print("z: ", -round(c[-1],3))