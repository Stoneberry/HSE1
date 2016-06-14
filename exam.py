import re

def function0():
    f=open('C:\\Users\\Та\\Desktop\\name1.txt', 'r', encoding = 'utf-8')
    array = f.read()
    f.close()
    return array

def ages(array):
    a1=[]
    x = '[1-9][0-9]{3}'
    res = re.findall( x, array)
    for i in res:
        y=i[0:2:1]
        if y in a1:
            continue
        else:
            a1.append(y)
    return a1

def new():
    f=open('C:\\Users\\Та\\Desktop\\forprog1.txt', 'r', encoding = 'utf-8')
    array1 = f.read()
    f.close()
    return array1

def searchfor(array1, a1):
    for i in a1:
       x=' (.*?) '+i+'[0-9]{2}'
       res=re.findall( x, array1)
       print(res+i+'[0-9]{2}')
    
    

def main():
    vab1 = function0()
    vab2 = ages(vab1)
    vab3 = new()
    vab4 = searchfor(vab3, vab2)



if __name__=='__main__':
    main()
