Str1 = "EXAM -T20EJICS116"
Str2 = ""
I=0
while I<len(Str1):
 if Str1[I]>="A" and Str1[I]<="M":
  Str2=Str2+Str1[I+1]
 elif Str1[I]>="0" and Str1[I]<="9":
  Str2=Str2+ (Str1[I-1])
 else:
  Str2=Str2+"*"
I=I+1
print("string is ",Str2)