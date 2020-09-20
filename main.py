SCU Systeme de Chiffement Univrsel(c) copyright 2020 
#Every tool you need in 1.5 kilooctets (ko)
from time import *
cst=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def crypt():
  dec = input("message a chiffrer : ");
  decl = [];
  key=int(input("cle de chiffement : "));
  enc=[];
  lo=len(dec);
  out=str()
  for i in range(lo):
    decl.append(dec[i])
  for i in range(lo):
    if decl[i] in cst:
      tmp=cst.index(decl[i]);
      enc.append(cst[tmp+key])
  for i in range(lo):
    out=out + enc[i]
  print(out.upper())
def decrypt():
  dec = input("message a dechiffrer : ");
  decl = [];
  key=int(input("cle de chiffement : "));
  enc=[];
  lo=len(dec);
  out=str()
  for i in range(lo):
    decl.append(dec[i])
  for i in range(lo):
    if decl[i] in cst:
      tmp=cst.index(decl[i]);
      enc.append(cst[tmp-key])
  for i in range(lo):
    out=out + enc[i]
  print(out.upper())
def lte(key,dec):
  decl = [];
  enc=[];
  lo=len(dec);
  out=str()
  for i in range(lo):
    decl.append(dec[i])
  for i in range(lo):
    if decl[i] in cst:
      tmp=cst.index(decl[i]);
      enc.append(cst[tmp-key])
  for i in range(lo):
    out=out + enc[i]
  print(out.upper())
def bruteforce():
  ttt=input("message a dechiffrer : ")  
  for h in range(26):
    lte(h,ttt)