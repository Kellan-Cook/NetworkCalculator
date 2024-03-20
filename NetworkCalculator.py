import math
import sys

print("enter ip and submask in format ***.***.***.***/**")

a = input()

print("enter number of subnets to split into")

b = input()

a = a.split("/")
mask = a[1]

if(a[0].count(".") > 3):
    print("INVALID IP OR SUBNET MASK")
else:

    fullip = a[0].split(".")
    maskoctet = math.floor(int(mask) / 8)
    maskoctetpos = int(mask) % 8

    #this is trigerd if the mask is a multiple of 8
    x = 0
    submask = 0
    while(submask < int(b)):
        submask = math.pow(2, x)
        submaskpos = x
        x = x + 1
        
        
    print(str(submask) + " - " + str(submaskpos))

    bitpos = 7 - maskoctetpos
    x = submaskpos
    subnet = 0
    while(x > 0):
         subnet = subnet + math.pow(2, int(8 - x))
         print(str(x) + ' - ' + str(bitpos) + " - " + str(subnet))
         x = x - 1
         if(x < 0):
            sys.exit("[Program Error] - stuck in loop")

    #checks for possible errors should never happen
    if(subnet - int(subnet) != 0):
            sys.exit("[Program Error] - non whole value detected")
    
    subnet = int(subnet) + int(fullip[maskoctet])
    x = 0
    finalanswer = str()
    while(maskoctet != x):
         finalanswer = finalanswer + "." + str(fullip[x])
         x = x + 1
    finalanswer = finalanswer + "." + str(subnet)
    
    while(x < 3):
         finalanswer = finalanswer + ".0"
         x = x + 1
    
    finalanswer = finalanswer[1:]
    newsubmask = int(mask) + int(submaskpos)
    print("===================================================")
    print("first network of new subnets = " + finalanswer + "/" + str(newsubmask))
    print("===================================================")
    



    
