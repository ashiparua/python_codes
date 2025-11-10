# check if given to string are anagram or not anargram are thje word that contain the same charactor but in diffrent order 
s1="slient"
s2="listen"
if sorted(s1)==sorted(s2):
    print("anagram")
else:
    print("not anagram")