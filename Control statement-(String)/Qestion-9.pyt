T = int(input("Enter number of strings:"))
for i in range(T):
    s = input("Enter string:")
    vowels = 0
    consonents = 0
    for char in s:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowels += 1
            else:
                consonents += 1
    print("Vowels:", vowels)
    print("Consonants:", consonents)
    # second method
# v=0
# c=0
# T=int(input())
# for i in range(T):
#     s=input()
#     for i in s:
#         if(i=='A' or i=='E'):
#             v+=1
#         else:
#             c+=1
# print("vowel",v)
# print("consonant",c)