#!/usr/bin/env python
# coding: utf-8

# In[10]:


#----------------Build your own implementation of Counting Sort-------#
def countingSort(listelement): #create a function fors sorting
    
    x= max(listelement)+1  #take max element of list and add 1 for creating index list
    indexList = [0 for i in range(x)] #create index list with zeros
    
    for i in range(len(listelement)): #put the elements of list into index which has same number with element
        indexList[listelement[i]] +=1 

    RunningSumList =list(indexList) #copy list
    for i in range(1,(len(RunningSumList))):  #sum i. index and (i-1). index and put new variable to i. index
        RunningSumList[i] = RunningSumList[i] + RunningSumList[i-1]

    finalList = [0 for i in range(len(listelement))] #create final list with zeros
   
    for i in range(len(listelement)): #find how many same elemnt
        finalList[ RunningSumList[listelement[i]] -1] = listelement[i]
        RunningSumList[listelement[i]] = RunningSumList[listelement[i]] -1
    print(finalList)

listelement = [1,4,1,2,7,5,2,3494,11,45] #create a random number list to try function
countingSort(listelement)


#-----------implementation of Counting Sort,that receives in input a list with all the letters of the alphabet-----#
def countingSortForAlphabet(listelement): #create a function for alphabet sorting
    ordSortedList = [] #create empty order list
    alphabet ='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz' #create an alphabet for your algorithm 
    alphabetDic = dict(enumerate(alphabet)) #create a dictionary to give a number for each alphabet
    
    for i in range(len(listelement)): #give a number for each alphabet
        for key, value in alphabetDic.items():
            if  listelement[i] == value:
                ordSortedList.append(key)
    x= max(ordSortedList)+1  #take max element of list and add 1 for creating index list
    indexList = [0 for i in range(x)] #create index list with zeros


    for i in range(len(ordSortedList)):  #put the elements of list into index which has same number with element
        indexList[ordSortedList[i]] +=1 

    RunningSumList =list(indexList) #copy list 
   
    for i in range(1,(len(RunningSumList))): #sum i. index and (i-1). index and put new variable to i. index
        RunningSumList[i] = RunningSumList[i] + RunningSumList[i-1]

    finalList = [0 for i in range(len(ordSortedList))] #create final list with zeros
   
    for i in range(len(ordSortedList)):
        finalList[ RunningSumList[ordSortedList[i]] -1] = ordSortedList[i]
        RunningSumList[ordSortedList[i]] = RunningSumList[ordSortedList[i]] -1
    
   
    for i in range(len(finalList)): #return the number to alphabet
        for key, value in alphabetDic.items():
            if  finalList[i] == key:
                finalList[i]= value
   
    return(finalList)
NameList = ['b','C','R','r','u','V','G','c','v','W','w','X','x','Y','I','g','H','h','m','S','s','y','Z','z','T','t','U','N','i','J','l','M','D','d','E','e','A','a','B','F','f','j','K','k','L','n','O','o','P','p','Q','q']
#give a random alphabet list for test function
countingSortForAlphabet(NameList)


# Time Complexity Theoretically: O()=k+n+k+n=2k+2n=2(n+k)=O(n+k)
# Time Complexity Empirically: In our example 'k' is a small value that's why we can take time complexity as O(n) empirically.

# In[ ]:


#---implementation of Counting Sort, that receives in input a list of length m #
# that contains words with maximum length equal to n, and returns the list ordered according to alphabetical order.---------- #
def countingSortForAlphabet(listelement): #same function with Q.2.2
    ordSortedList = []
    alphabet =' AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    alphabetDic = dict(enumerate(alphabet))
    
    for i in range(len(listelement)):
        for key, value in alphabetDic.items():
            if  listelement[i] == value:
                ordSortedList.append(key)
    x= max(ordSortedList)+1
    indexList = [0 for i in range(x)]


    for i in range(len(ordSortedList)):
        indexList[ordSortedList[i]] +=1 

    RunningSumList =list(indexList)
   
    for i in range(1,(len(RunningSumList))):
        RunningSumList[i] = RunningSumList[i] + RunningSumList[i-1]

    finalList = [0 for i in range(len(ordSortedList))]
   
    for i in range(len(ordSortedList)):
        finalList[ RunningSumList[ordSortedList[i]] -1] = ordSortedList[i]
        RunningSumList[ordSortedList[i]] = RunningSumList[ordSortedList[i]] -1
    
   
    for i in range(len(finalList)):
        for key, value in alphabetDic.items():
            if  finalList[i] == key:
                finalList[i]= value
   
    return(finalList)


listOfWords = ['Astronomy','Astrolabe','Baa','Astrophysics','At','Aster','Ataman'] #give a string list for test 
#Aster; Astrolabe; Astronomy; Astrophysics; At; Ataman; Attack; Baa

def count3(listOfWords, k):    
    if len(listOfWords)==1:
        return listOfWords
    else:
        firstLetters=[s[k] for s in listOfWords]  #create a list for taking first latter of strings
        set_letters=set(firstLetters)

        dict_lect={ch:[w for w in listOfWords if w[k]==ch] for ch in firstLetters} #create dic for list of words

        sort=countingSortForAlphabet(list(dict_lect.keys())) #sort them
        out=[]
        for ch in sort:
            out+=count3(dict_lect[ch], k+1)
        return out
maxlen=0
for w in listOfWords:
    if len(w)>maxlen:
        maxlen=len(w) #define max len of all strings
maxlen+=1
for i in range(len(listOfWords)):
    if len(listOfWords[i])!=maxlen:
        listOfWords[i]=listOfWords[i]+(' '*(maxlen-len(listOfWords[i]))) #if string doesnt have mex len,put ' ' until reach to max leng
final=count3(listOfWords, 0)
f=[w[:w.index(' ')] for w in final]
print(f)


# Time Complexity Theoretically: O()=k+n+k+n=2k+2n=2(n+k)=O(n+k)
# Time Complexity Empirically: It can be change with number of input strings but in our example 'k' is a small value that's why we can take time complexity as O(n) empirically.

# In[ ]:




