
import string

filepath= "hwtext.txt"
charcount={}
digrams={}
trigrams={}

def solvechars(word):
    
    for c in word:
        if c in charcount:
            charcount[c]+=1
        else:
            charcount[c]=1


def solvedigrams(word):
    
    for c in range(len(word)-1):
        kelime=word[c:c+2]
        if kelime in digrams:
            digrams[kelime]+=1
        else:
            digrams[kelime]=1



def solvetrigrams(word):
    
    for c in range(len(word)-2):
        kelime=word[c:c+3]
        if kelime in trigrams:
            trigrams[kelime]+=1
        else:
            trigrams[kelime]=1


def punctuations(line):
    for c in string.punctuation:
        line=line.replace(c," ")
    return line
with open(filepath,"r",encoding='utf-8') as filep:
    for line in filep:
        line = punctuations(line)
        line=line.lower()
        line= line.rstrip("\n")
        txtsplitted=line.split(" ")
        
        for w in txtsplitted:
            solvechars(w)
        for w in txtsplitted:
            solvedigrams(w)
        for w in txtsplitted:
            solvetrigrams(w)

#print(charcount)
#print(digrams)
#print(trigrams)

#a)
#Five most common characters
rvssortedcharcounts=sorted(charcount.items(), key=lambda x: x[1], reverse=True)#Decreasing Order
print("Five most common characters-->")
print(rvssortedcharcounts[:5])
#Five least common characters
sortedcharcounts=sorted(charcount.items(), key=lambda x: x[1])#Increasing Order
print("Five least common characters -->")
print(sortedcharcounts[:5])
#b)
#Five most common Digrams
rvssorteddigramcounts=sorted(digrams.items(),key=lambda x: x[1],reverse=True)#Decreasing Order
print("Five most common Digrams -->")
print(rvssorteddigramcounts[:5])
#c)
#Five most common Trigrams
rvssortedtrigramcounts=sorted(trigrams.items(),key=lambda x: x[1],reverse=True)#Decreasing Order
print("Five most common Trigrams -->")
print(rvssortedtrigramcounts[:5])
        





















