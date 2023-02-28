import sys

# Read the input from standard input
s = sys.stdin.read()
#  Makes a copy of s
s_copy = s
# Converts the message to all uppercase
s = s.upper()
s = s.replace(" ","")
s = s.replace(",","")
s = s.replace(";","")
s = s.replace(".","")
# Converts message to mutable datatype 
s = list(s)
# Transforms message characters into code
for i in range(len(s)):
    s[i] = ord(s[i]) + int(sys.argv[1])
    s[i] = chr(s[i])
s = "".join(s)
# Print out the code in blocks of 5.
count = 0
for i in range(len(s)):
    print(s[i], end = "")
    count+=1
    if count >= 5:
        count = 0
        print(" ", end = "")



