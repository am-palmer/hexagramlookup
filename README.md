# hexagramlookup

command line python tool

reverse hexagram lookup - used to find the name and description of a hexagram
hexagrams are represented as 6 digit binary strings. 0 corresponds to yin (broken) and 1 corresponds to yang (unbroken)
hexagrams are typed from bottom to top, as they are read (so 100000 is yang in the first place, followed by 5 yins ascending)

so 111111 is hexagram 1, the creative

useage:
-hx [6 digit permutation of 1s and 0s]
prints the hexagram as well as the name and descriptions from the james legge i ching.

i.e. -hx 101010

can also do -hx [1-64] for simple lookup i.e. -hx 33 will bring up the 33rd hexagram

-r 
generates a random hexagram. could be used for divination

to do: 
make output prettier
more options 
