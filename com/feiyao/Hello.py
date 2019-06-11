#!/usr/bin/python3

import re
import sys


if len(sys.argv) > 1:
    tdmfilename = sys.argv[1]
else: 
    tdmfilename = r"tdm.log"
    
print("parsing log file %s" %(tdmfilename))
wiresharkName = r"wireshark_load_by_hex"

headlistR = ['00', '80', '9F', 'EC', 'B5', 'F4', 'E8', 'E7', '32', '0E', '0A', '12', '08', '00', '45', '00', 
            '01', '7A', '00', '00', '40', '00', '3E', '11', '0B', '4B',  '0A', '0A', '06', '86', '1E', '01', 
            '01', '98', '1E', '5F', '13', '89', '01', '66', '00', '00', '07', '00', '17', '00', '6B' ]

headlistS = ['00', '80', '9F', 'EC', 'B5', 'F4', 'E8', 'E7', '32', '0E', '0A', '12', '08', '00', '45', '00', 
            '01', '7A', '00', '00', '40', '00', '3E', '11', '0B', '4B', '1E', '01', '01', '98', '0A', '0A', 
            '06', '86', '1E', '5F', '13', '89', '01', '66', '00', '00', '07', '00', '17', '00', '6B' ]
tdmfile = open(tdmfilename, "r")

phoneSend = r'ua3 : R'
phoneReceived = r'ua3 : S'
count = 0

def getStart(start):
    startTemp = ''
    if (len(str(hex(start))) == 4) :
        startTemp = str(hex(start)).replace('0x', '00', 1)
    elif (len(str(hex(start))) == 5) :
        startTemp = str(hex(start)).replace('0x', '0', 1)
    elif (len(str(hex(start))) == 3) :
        startTemp = str(hex(start)).replace('0x', '000', 1)
    else:
        startTemp = str(hex(start)).replace('0x', '', 1)
    
    return startTemp

wireshark2 = open(wiresharkName, "w")

for line2 in tdmfile:
    if(re.match(phoneSend, line2) or re.match(phoneReceived, line2)):
        start = 0          
               
        line2Temp = line2[8:]  
        if line2.find(phoneSend)>-1 :     
            line2TempSplit = headlistS + line2Temp.split() 
        else:
            line2TempSplit = headlistR + line2Temp.split()
                
        
        line2TempSplitCopy = line2TempSplit.copy()
                
        i = 0
        while i < (1 + len(line2TempSplit) // 16) :
            
            i += 1   
            startTemp = getStart(start)  
            start += 16
            wireshark2.write(startTemp + r"   ")
            
            if len(line2TempSplitCopy) < 16:
                for line2TempSpliter in line2TempSplitCopy: 
                    wireshark2.write(line2TempSpliter + r" ")
            else:             
                for line2TempSpliter in line2TempSplitCopy[0:16]: 
                    wireshark2.write(line2TempSpliter + r" ")
                line2TempSplitCopy =  line2TempSplitCopy[16:]  
                
                         
            wireshark2.write('\n') 
 
        
        count += 1
print("total UAUDP count = %d " %(count)) 

tdmfile.close()

if __name__ == 'main':
    print('hello')

