from io import open

# file_text = open('new.txt',"w")# open file if no exist create

phrase  ="Beatiful day for study python \n miercoles"

#file_text.write(phrase)#write In the file



# file_text.close()#close file 
#----------------------------------read


# file_text = open('new.txt',"r")#open for read

# # text = file_text.read()#read all
# text =file_text.readlines()#read all for lines and save inside a list
# print(text)

# file_text.close()#close file 

#--------------------------------- append
# file_txt = open("new.txt","a")#for open file with for append
# file_txt.write("Always is good learn more")
# file_txt.close()

#--------------------------------- move the position cursor
file_txt = open("new.txt","r")
print(file_txt.read())
file_txt.seek(0)#move the cursor
print(file_txt.read(20))#read hasta the position indicated


