fle= open("carac.txt", "r")
i=0
sign = ["+",'-','*','/','=','(',')', ';']
avoid = [ '#include <iostream> ']
fles = open ('test.cpp','r')
r=5 # avoid general terms used in cpp sintaxis such as #include and so on
lst =[]
for ln in fle:
    lst.append(ln)
    
while(r < len(lst)):
    for d in lst[r].split():
        if(d in sign):
            print 'sgn :', d
        else:
            print 'word:', d
        #print d
    
    r+=1

