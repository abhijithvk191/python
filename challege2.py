a = list("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
leng = len(a)
for x in range(0,leng):
   asci = ord(a[x])
   if (asci >= 97 and asci <= 122):
       new_asci = asci + 2
       if (new_asci > 122):
           new_asci = new_asci - 26
       a[x] = chr(new_asci)
result = ''.join(a)
print (result)
