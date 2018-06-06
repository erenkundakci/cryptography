#Eren Kundakçı
#150401026

import hashlib

no = "150401026"
dizi = ""
for i in range(8):
    no = hashlib.sha512(no.encode('utf-8')).hexdigest()
    print(i+1,". hashlemede 5. karakter:",no[4])
    if(no[4]=="0" or no[4]=="1" or no[4]=="2" or no[4]=="3" or no[4]=="4"): #0. index 1. karakter olduğundan 4. index 5. karakter olacak
        dizi += "0"
    else:
        dizi += "1"
print("Elde edilen binary text:",dizi)
print("Decimal karsiligi:",int(dizi,2))



