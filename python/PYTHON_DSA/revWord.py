# Input : str = "my name is laxmi"
# output : str= laxmi is name my 

string = "geeks quiz practice code"
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
    # appending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))



 
def rev_sentence(sentence): 
 
    # first split the string into words 
    words = sentence.split(' ') 
 
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words)) 
 
    # finally return the joined string 
    return reverse_sentence 
 
if __name__ == "__main__": 
    input = 'geeks quiz practice code'
    print (rev_sentence(input)) 
    
    
    
    
    