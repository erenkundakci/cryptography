import hashlib

filename = './randomLipsum.txt'
file = open(filename)
content = file.read()
file.close()
string = ""

n = int(input("Stringin uzunlugu kac basamak olsun: "))
for i in range(n):
    content = hashlib.md5(content.encode('utf-8')).hexdigest()
    string += content[7]
print("Hex: ", string)
print("Dec:", int(string,16))
