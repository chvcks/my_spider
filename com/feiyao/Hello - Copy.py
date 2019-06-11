#!/usr/bin/python3

import re

headfilename = r"D:\Users\shilongh\Desktop\head"
tdmfilename = r"D:\Users\shilongh\Desktop\tdm.log"
wiresharkName = r"D:\Users\shilongh\Desktop\wireshark"

headfile = open(headfilename, "r")
tdmfile = open(tdmfilename, "r")

phoneSend = r'ua3 : R'
phoneReceived = r'ua3 : S'
count = 0


for line2 in tdmfile:
    if(re.match(phoneSend, line2) or re.match(phoneReceived, line2)):
        start = 32
        print(line2[6])
        wiresharkNameTemp = wiresharkName + str(count) + line2[6]
        print(wiresharkNameTemp)
        wireshark2 = open(wiresharkNameTemp, "w")        
        for headline in headfile:
            wireshark2.write(headline)                         
        wireshark2.close()    
        headfile.seek(0, 0) 
        
        line2Temp = line2[8:]  
        line2TempSplit = line2Temp.split() 
        
        wireshark3 = open(wiresharkNameTemp, "a")
        wireshark3.write(line2TempSplit[0])
        
        print(line2TempSplit)
        line2TempSplit = line2TempSplit[1:]
        line2TempSplitCopy = line2TempSplit.copy()
        
        print(len(line2TempSplit) % 16)
        print(len(line2TempSplit) // 16)
        
        i = 0
        while i < (1 + len(line2TempSplit) // 16) :
            start += 16
            i += 1    
            if (len(str(hex(start))) == 4) :
                startTemp = str(hex(start)).replace('0x', '00', 1)
            elif (len(str(hex(start))) == 5) :
                startTemp = str(hex(start)).replace('0x', '0', 1)
            else:
                startTemp = str(hex(start)).replace('0x', '', 1)  
            
            wireshark3.write("\n" + startTemp + r"   ")
            
            if len(line2TempSplitCopy) < 16:
                for line2TempSpliter in line2TempSplitCopy: 
                    wireshark3.write(line2TempSpliter + r" ")
            else:             
                for line2TempSpliter in line2TempSplitCopy[0:16]: 
                    wireshark3.write(line2TempSpliter + r" ")
                line2TempSplitCopy =  line2TempSplitCopy[16:]   
              
 
        
        count += 1
print("count = %d " %(count)) 
headfile.close()
tdmfile.close()



