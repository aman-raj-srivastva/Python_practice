#                                                   <-----Read operations----->

with open('assets/tst.txt','r') as f:
    # f.read() --> will print the content in single string, newline as \n; (although not working here)
    # file_content=f.read()
    # print(file_content)
    
    # file_lines=f.readlines() 
    # print(file_lines)         # prints all lines in txt file in list form
    
    # file_line=f.readline()      # only reads one line at a time 
    # print(file_line)            #-> prints 1st line in txt file
    # file_line=f.readline()
    # print(file_line)            #-> prints 2nd line in txt file
    # file_line=f.readline()
    # print(file_line)            #-> prints 3rd line in txt file
    
    # file_line=f.readline()      # only reads one line at a time 
    # print(file_line, end='')            #-> prints 1st line in txt file with ending 
    # file_line=f.readline()
    # print(file_line, end='3rd line: ')            #-> prints 2nd line in txt file
    # file_line=f.readline()
    # print(file_line, end='-----***-----')            #-> prints 3rd line in txt file
    
    # # also you can do the following for printing line by line of the txt file
    # for line in f:
    #     print(line, end='') # *** new line will not be printed if it was printed earlier
        
    # file_limit=f.read(8) #in chunks like division with specific size value
    # print(file_limit, end='*')
    # file_limit=f.read(9)
    # print(file_limit, end='*')
    # file_limit=f.read(9)
    # print(file_limit, end='*')
    # file_limit=f.read(7)
    # print(file_limit, end='*')
    # file_limit=f.read(7)
    # print(file_limit, end='*')
    # file_limit=f.read(7)
    # print(file_limit, end='*') # and so on ...
    ## or to do in whole file use the following code:
    # f_limit=f.read(7)
    # while len(f_limit) > 0:
    #     print(f_limit, end='*')
    #     f_limit=f.read(7)
    
    # f_content=f.read(10)
    # f_content=f.read(10)
    # print(f.tell()) # f.tell() will tell the position of pointer (the point from which the next operation will take place)
    
    f.seek(17) # pointer/cursor moves to position/index 17 of txt file from start (give error for -ve value)
    f_content=f.read(8)
    print(f_content)
    print('Now pointer at',f.tell())
    
#                                                    <-----Write Operations----->
 
# with open('assets/tst2.txt','w') as f: # as tst2.txt is not available thus this will create that file
#     f.write("TEST") # CAUTION: this will erase all the data in file and rewrite it with TEST
#     f.seek(0)
#     f.write('R')
    
# # copying a file from one to another
# with open('tst.txt','r') as rf:
#     with open('tstcpy.txt','w') as wf:
#         for line in rf:
#             wf.write(line)
# with open('world.jpeg','rb') as rf: # in rb and wb b refers to bytes
#     with open('globe.jpeg','wb') as wf:
#         for line in rf:
#             wf.write(line)

# profit=[] # for list
profit={} # for dictionary
with open('assets/profit.csv','r') as f:
    for line in f:
        tokens=line.split(',')
        day=tokens[0]
        price=float(tokens[1])
        # profit.append([day,price]) # as a list
        profit[day]=price # as a dictinary
print(profit)