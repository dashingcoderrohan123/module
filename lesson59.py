#write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.

def match_words(words):
    ctr=0
    empty_list=[]
    for x in words:
        if len(x)>1 and x[0]==x[-1]:
            ctr += 1
            empty_list.append(x)
    print("list of words with first and last charecters\n",empty_list)
    return ctr            
            
count=match_words(["fruit","education","list","name","age"])
print(count)            