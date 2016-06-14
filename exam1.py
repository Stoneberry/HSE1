import re

def function0():
    f=open('C:\\Users\\Та\\Desktop\\forprog1.txt', 'r', encoding = 'utf-8')
    array = f.read()
    f.close()
    return array

def searchfor(array):
    x='([1-9][0-9]?-?[1-9]?[0-9]? ?(?:до н.э.|н.э)?) век(?:а|е|ах|у)? ?(?:до н.э.|н.э)?'
    res = re.findall( x, array)
    for i in res:
        print(i)

def main():
    vab1 = function0()
    vab2 = searchfor(vab1)


if __name__=='__main__':
    main()

        

                                        
