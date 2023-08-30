import string
import random

len_input = int(input("Enter the length of password:"))
sp_char = input("Do you want special Character?")
l1=list(string.ascii_lowercase)
l2=list(string.ascii_uppercase)
l3=list(string.digits)

while(True):

    if len_input<8:
        print("Minimum length of password is 8\n")
        len_input = int(input("Enter the length of password:"))
    else:
        break

if sp_char=='yes' or sp_char=='Yes' or sp_char=='y' or sp_char=='Y':
        l4=list(string.punctuation)
        random.shuffle(l1)
        random.shuffle(l2)
        random.shuffle(l3)
        random.shuffle(l4)

        part1 = round(len_input * (30/100))
        part2 = round(len_input * (20/100))
        print(part1,part2)

        result=[]

        for x in range(part1):
            result.append(l1[x])
            result.append(l2[x])
        for x in range(part2):
            result.append(l3[x])
            result.append(l4[x])

        while True:
            if len_input%2!=0:
                result.pop()
                break  
            else:
                break

        
        random.shuffle(result)
        password="".join(result)
        print(password)
else:
        random.shuffle(l1)
        random.shuffle(l2)
        random.shuffle(l3)
        

        part1 = round(len_input * (30/100))
        part2 = round(len_input * (20/100))
        
        result=[]

        for x in range(part1):
            result.append(l1[x])
            result.append(l2[x])
        for x in range(part2):
            result.append(l3[x])
            result.append(l2[x])

        while True:
            if len_input%2!=0:
                result.pop()
                break  
            else:
                break
        random.shuffle(result)
        password="".join(result)
        print(password)  