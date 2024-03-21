import math
import sys


def ipOctets(a: str):
     
    a = a.split("/")

    if(a[0].count(".") != 3):
        sys.stderr("[Input Error] - Invalid IP adresse\n")
        sys.exit(1)

    b = a[0].split(".")

    return b

def ipMask(a: str):
    print(a)
    print("mask count: " + str(a.count("/")))
    if(a.count("/") != 1):
        sys.stderr("[Input Error] - Invalid IP MASK\n")
        sys.exit(1)
    a = a.split("/")
    b = a[1]
    print(b)

    return b


def subMaskSplit(a: str):
    print("enter number of subnets to split into")

    b = input()


    mask = ipMask(a)
    fullip = ipOctets(a)
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
            sys.stderr("[Program Error] - non whole value detected\n")
            sys.exit(1)

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
    

def submaskSize(a: str):
     
    a = a.split("/")    
    mask = a[1]
    b = input("how many hosts per network do you need (put ',' between values for more then one): ")

    b = b.split(",")
    b = sorted(b, reverse=True)
    subnetsize = []
    for hostCount in b:
        bitsize = 0
        hostsize = 0
        while(hostsize + 2 < int(hostCount)):
            hostsize = math.pow(2, bitsize)
            bitsize = bitsize + 1
            decnum = math.pow(2, bitsize)
            print(str(bitsize) + ' - ' + str(int(hostsize)))
            

        if(bitsize > int(mask)):
             sys.stderr("[Process Error] host size to large for given network\n")
             sys.exit(1)
        x = 0
        subnetsize.append(bitsize)
    x = 0
    print("===================")
    while(len(b) > x):


         print(str(b[x]) + " - " + str(subnetsize[x]))
         x = x + 1

             
          
          

    





print("enter current ip and submask in format ***.***.***.***/**")

a = input("ip: ")

print("choose wich function you would like to perform")
print("1 - subnet start calculator")
print("2 - get size of subnets for given host count")
function = input()

if(function == "1"):
     subMaskSplit(str(a))
elif(function == "2"):
     submaskSize(str(a))