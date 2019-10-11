a=[1,2,3,4,5,1,2,3,4,5,6,7,8,9]
def remove_duplicates(a):
    i=0
    while i<len(a):
        j=i+1
        while j<len(a):
            if a[i]==a[j]:
                del a[j]
            else:
                j+=1
        i+=1
    print(a)
#def remove_duplicates(a):
 #   for i in range(0,len(a),1):
  #      for j in range(i+1,len(a),1):
   #         if a[i]==a[j]:
    #            del a[j]
     #           break
    #print(a)
def remove_by_appending(a):
    c=[]
    for i in a:
        if i not in c:
            c.append(i)
    return c
def remove_set(a):
    a=list(set(a))
    return a
    
