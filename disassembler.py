import string
import os
from bitstring import Bits

def bintodec(str):
	a=Bits(bin=str)
	b=a.int
	return b


  
output = ""
flag=0
address = 492
    
with open('fib_bin.txt','r') as f:
	for line in f:
		
		for word in line.split():
			#print (word)
			 
			address = address + 4
			ad = str (address) 
			         #display the text file as a whole
			#print (word[:6])
			opcode=word[:6]   	#extracting first 6 characters
			funct=word[26:]		#extracting last 6 characters
			rd =word[16:21]		#extracting characters from 16-21
			#print rd
			rs =word[6:11]		#extracting characters from 6-11
			#print rs
			rt =word[11:16]		 #extracting characters from 11-16
			#print rt
			sa=word[21:26]		 #extracting characters from 21-26
			immediate = word[16:]	#extracting first 16 characters
			RD=bintodec(rd)
			RS =bintodec(rs)
			RT =bintodec(rt)
			SA=bintodec(sa)
			R1 = str(RD)
			R2 = str(RS)
			R3 = str(RT)
			R4 = str(SA)
			imm = bintodec(immediate)
			Im = str (imm)
			#print (opcode)			
			if (flag == 1):
				twocom = bintodec(word)   #binary to decimal converter
				two = str (twocom)		  # twos complement
				#print two
				print(opcode+ rs + rt + rd +sa+" \t"+ad+"\t" +two)
				output = opcode+ rs + rt + rd +sa+" \t"+ad+"\t" +two
				
			elif word =="00000000000000000000000000000000":   #NOP
				print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +"NOP")
				output = opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +"NOP"
			elif opcode == "000000" : #rtype
				opcode1=""
				#print funct
				if funct == "100100" :   
					opcode1="AND"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3)
					output = opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3
				elif funct=="100101":
					opcode1="OR"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3)
					output = opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3
				elif funct=="100000":
					opcode1="ADD"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3
				elif funct=="100001":
					opcode1="ADDU"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3
				elif funct=="100010":
					opcode1="SUB"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3
				elif funct=="100011":
					opcode1="SUBU"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3
				elif funct=="100110":
					opcode1="XOR"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3
				elif funct=="100111":
					opcode1="NOR"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3
				elif funct=="101010":
					opcode1="SLT"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R2+ ", R" +R3
				elif funct=="001101":
					opcode1="BREAK"
					flag=1
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1
					#print(flag)
				elif funct=="001000":
					opcode1="JR"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R2)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R2
				elif funct=="000000":
					opcode1 = "SLL"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R3+ ", R" +R4)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R3+ ", R" +R4
				elif funct == "000010":
					opcode1 = "SRL"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R3+ ", R" +R4)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R3+ ", R" +R4
				elif funct == "000011":
					opcode1 = "SRA"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R1+ ", R"+ R3+ ", R" +R4)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R1+ ", R"+ R3+ ", R" +R4
				else:
					print("Error")
				#print (opcode1)
				#print (flag)
				
			
			elif opcode == "000010":		#  jump type
				opcode1 = "J"
				target = word[6:]
				Tr = bintodec(target) * 4
				tr = str(Tr)
				print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + "   #" +tr)
				output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  "+ ad + "\t" +opcode1 + "   #" +tr
				
			elif opcode =="001000":			#  Immediate
				opcode1 = "ADDI"
				print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R3+ ", R"+ R2+ ", #" +Im)
				output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R3+ ", R"+ R2+ ", #" +Im
				
			elif opcode =="001001":
				opcode1 = "ADDIU"
				print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R3+ ", R"+ R2+ ", #" +Im)
				output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R3+ ", R"+ R2+ ", #" +Im
				
			elif opcode =="000100":
				opcode1 = "BEQ"
				print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R2+ ", R"+ R3+ ", #" +Im)
				output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R2+ ", R"+ R3+ ", #" +Im
				
			elif opcode =="000101":
				opcode1 = "BNE"
				print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R2+ ", R"+ R3+ ", #" +Im)
				output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R2+ ", R"+ R3+ ", #" +Im
				
			elif opcode =="000111":
				opcode1 = "BGTZ"
				print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R2+ ", #" +Im)
				output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R2+ ", #" +Im
				
			elif opcode =="000110":
				opcode1 = "BLEZ"
				print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R2+ ", #" +Im)
				output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R2+ ", #" +Im
				
			elif opcode =="000001":
				if rs == "00000":
					opcode1 = "BLTZ"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R2+ ", #" +Im)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R2+ ", #" +Im
					
				elif rs == "00001":
					opcode1 = "BGEZ"
					print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R2+ ", #" +Im)
					output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " + ad + "\t" +opcode1 + " R" +R2+ ", #" +Im
					
								
			elif opcode =="101011":
				opcode1 = "SW"
				print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R3+ ","+ Im+ "(" +"R"+R2+")")
				output=(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R3+ ","+ Im+ "(" +"R"+R2+")")
				
				
			elif opcode =="100011":
				opcode1 = "LW"
				print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R3+ ","+ Im+ "(" +"R"+R2+")")
				output=(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R3+ ","+ Im+ "(" +"R"+R2+")")
				
			elif opcode =="001010":
				opcode1 = "SLTI"
				print(opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R3+", R" +R2+", #" +Im)
				output=opcode+ " " + rs + " " + rt + " " + rd +" "+sa+"  " +ad + "\t" +opcode1 + " R" +R3+", R" +R2+", #" +Im
			
			else :			                             #different opcode
				
				print('No')
				
			f = open("fib_out.txt", "a") 
			                  #opens a file for writing
			f.write(output + "\n")
			
			
			f.close()
				
					

