#!/usr/bin/env python

#todo: code support for changing lines, make output prettier (line wrap, colors)
#todo: code less flimsy failsafes

import argparse
import random
import unicodedata

parser = argparse.ArgumentParser(description='Simple hexagram lookup using 6-character binary values.')

# can split the hexagram parser argument into 2 arguments - lookup for 1-64, hexagram for binary search
#parser.add_argument('-l', '--lookup', action =)
parser.add_argument('-hx', '--hexagram', default = '000000', help = 'Takes a six-digit combination of 1s (yang, unbroken) and 0s (yin, broken) corresponding to a hexagram. For example: 010111 (hexagrams are read from bottom to top). Alternatively enter a value from 1-64 to get the corresponding hexagram.')
parser.add_argument('-r', "--random", action = 'store_true', help = 'Generates a random hexagram.')
args = parser.parse_args()

    
class HexagramDictionary(object):
    ichingtuple = []
    
    def __init__(self):
        self.BuildHexTuple()

     
    def SimplePrintHexagram(self, hexstr):
        univalue = "\u00a2"
        uniblock = unicodedata.lookup('BLACK SQUARE')
        for letter in hexstr[::-1]:
            if letter == '0':
                print ""+ uniblock + uniblock + uniblock + "   " + uniblock + uniblock + uniblock + "   0"
            else:
                print "" + uniblock + uniblock + uniblock + uniblock + uniblock + uniblock + uniblock + uniblock + uniblock + "   1"

    def RandomHexagram(self):
        randnum = random.randint(0, 63)
        randhex = self.ichingtuple[randnum]
        self.SimplePrintHexagram(randhex[0])
        print randhex[1]
        print randhex[2]
    
    # retrieves hexagram information and zips as tuples
    def BuildHexTuple(self):
        HexNumList = []
        HexNameListEng = []
        LeggesDescList = []
        
        num = open('hexcodes.txt')
        for line in num:
            HexNumList.append(str(line.strip()))

        name = open('hexnames.txt')
        for line in name:
            HexNameListEng.append(str(line.strip()))
        
        desc = open('jamesleggedesc.txt')
        for line in desc:
            LeggesDescList.append(str(line.strip()))
        
        
        HexagramDictionary.ichingtuple = list(zip(HexNumList, HexNameListEng, LeggesDescList))
        
hexa = HexagramDictionary()

if (args.random):
    hexa.RandomHexagram()    

elif (args.hexagram):
    #lookup argument logic
    if (len(args.hexagram) < 3 and int(args.hexagram) > 0 and int(args.hexagram) < 65):
        hextuple = hexa.ichingtuple[int(args.hexagram) -1]
        hexa.SimplePrintHexagram(hextuple[0])
        print hextuple[1]
        #print "\n"
        print hextuple[2]
    elif (len(args.hexagram) == 6):
        for tuple in hexa.ichingtuple:
            if str(tuple[0]) == args.hexagram:
                hexa.SimplePrintHexagram(tuple[0])
                print tuple[1]
                #print "\n"
                print tuple[2]
