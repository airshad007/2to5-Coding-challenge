import math
import itertools


triangle_lst = []
square_lst = []
pentagonal_lst = []
hexagonal_lst = []
heptagonal_lst = []
octagonal_lst = []

#range 1000-9999

def getTriangle():
  #Store all 4 digit Triangle numbers using n(n+1)/2 
  for i in range(1000,9999):
    num = math.floor(math.sqrt(2*i))
    if(num*num + num)/2 == i:
      triangle_lst.append(i)

def getSquare():
  #Store all 4 digit Square numbers using n*n
  for i in range(1000,9999):
    num = math.sqrt(i)
    if num % 1 == 0 and int((i%100)/10) != 0:
      square_lst.append(i)

def getpentagonal():
  #Store all 4 digit Pentagonal numbers using n*(3n-1)/2
  for i in range(1000,9999):
    num = math.floor(math.sqrt(i))
    while (3*num*num - num)/2 > i:
      num = num -1
      if (3*num*num - num)/2 == i:      
        pentagonal_lst.append(i)
        break

        

#Store all 4 digit Hexagonal numbers using n(2n-1)
def getHexagonal():
  for i in range(1000,9999):
    num = math.ceil(math.sqrt(i))
    while (2*num*num - num) > i:
      num = num -1
      if (2*num*num - num) == i:      
        hexagonal_lst.append(i)
        break
    

#Store all 4 digit Heptagonal numbers using n(5n-3)/2
def getHeptagonal():
  for i in range(1000,9999):
    num = math.ceil(math.sqrt(2*i))
    while (5*num*num - 3*num)/2 > i:
      num = num -1
      if (5*num*num - 3*num)/2 == i:      
        heptagonal_lst.append(i)
        break
        
#Store all 4 digit Octagonal numbers using n(3n-2)
def getOctagonal():
  for i in range(1000,9999):
    num = math.ceil(math.sqrt(i))
    while (3*num*num - 2*num) > i:
      num = num -1
      if (3*num*num - 2*num) == i:      
        octagonal_lst.append(i)
        break

getTriangle()
getSquare()        
getpentagonal()
getHexagonal()
getHeptagonal()
getOctagonal()

chain = []

for triangle_num in triangle_lst:
  chain.append(triangle_num)
  for pentagonal_num in pentagonal_lst:
    if triangle_num % 100 == int(pentagonal_num / 100) and pentagonal_num not in chain:
      chain.append(pentagonal_num)
      for hexagonal_num in hexagonal_lst:
        if triangle_num % 100 == int(pentagonal_num / 100) and hexagonal_num not in chain:
          chain.append(pentagonal_num)
      

#print "triangle_dict"
#print triangle_dict
#print "square_dict"
#print square_dict
#print "pentagonal_dict"
#print pentagonal_dict
#print "hexagonal_dict"
#print hexagonal_dict
#print "heptagonal_dict"
#print heptagonal_dict
#print "octagonal_dict"
#print octagonal_dict

#print "triangle_lst"
#print triangle_lst
#print "square_lst"
#print square_lst
#print "pentagonal_lst"
#print pentagonal_lst
#print "hexagonal_lst"
#print hexagonal_lst
#print "heptagonal_lst"
#print heptagonal_lst
#print "octagonal_lst"
#print octagonal_lst    

triangle_lst = [1234,1345]
square_lst = [3478,7894]
pentagonal_lst = [7895,8800]
hexagonal_lst = [7878,9536]
heptagonal_lst = [3656,3994]
octagonal_lst = [9834,5612]

#all_permutations = [x for x in itertools.permutations([triangle_lst,square_lst,pentagonal_lst,hexagonal_lst,heptagonal_lst,octagonal_lst],2)]
#print all_permutations

#new_list = [[i,j,k,l,m,n] for i in triangle_lst for j in square_lst for k in pentagonal_lst for l in hexagonal_lst for m in heptagonal_lst for n in octagonal_lst]
#file_name = ''
#print new_list
#print len(new_list)

#for octagonal_num in octagonal_lst:
#  #print "octagonal_num"+str(octagonal_num)
#  for triangle_num in triangle_lst:
#    #print "triangle_num"+str(triangle_num)
#    if octagonal_num % 100 == int(triangle_num / 100):
#      for square_num in square_lst:
#        #print "square_num"+str(square_num)
#        if triangle_num % 100 == int(square_num / 100):
#          for pentagonal_num in pentagonal_lst:
#            #print "pentagonal_num"+str(pentagonal_num)
#            if square_num % 100 == int(pentagonal_num / 100):
#              for hexagonal_num in hexagonal_lst:
#                #print "hexagonal_num"+str(hexagonal_num)
#                if pentagonal_num % 100 == int(hexagonal_num / 100):
#                  for heptagonal_num in heptagonal_lst:
#                    #print "heptagonal_num"+str(heptagonal_num)
#                    if hexagonal_num % 100 == int(heptagonal_num / 100):
#                      for octagonal_num in octagonal_lst:
#                        #print "octagonal_num"+str(octagonal_num)
#                        if heptagonal_num % 100 == int(octagonal_num / 100):
#                          print triangle_num,square_num,pentagonal_num,hexagonal_num,heptagonal_num,octagonal_num


#for key in triangle_dict:
#  if square_dict.contains_key(triangle_dict[key]):
#  
#  if pentagonal_dict.contains_key(triangle_dict[key]):
#  
#  if   
                          
#Build 6 4-digit numbers picking one from each list                        
                          
#print "After removal"      
#print "triangle_lst"
#print triangle_lst
#print "square_lst"
#print square_lst
#print "pentagonal_lst"
#print pentagonal_lst
#print "hexagonal_lst"
#print hexagonal_lst
#print "heptagonal_lst"
#print heptagonal_lst
#print "octagonal_lst"
#print octagonal_lst

numbers = [ [ 0 for i in range(6) ] for j in range(6) ]
numbers[0] = list(triangle_lst)
numbers[1] = list(square_lst)
numbers[2] = list(pentagonal_lst)
numbers[3] = list(hexagonal_lst)
numbers[4] = list(heptagonal_lst)
numbers[5] = list(octagonal_lst)
solution = [ 0 for i in range(6) ]

def FindNext(last, length):
  print "last: "+str(last)
  print "length: "+str(length)
  for i in range(0, len(solution)):
    print "i: "+str(i)
    print " solution["+str(i)+"]:" +str(solution[i])
    if solution[i] != 0:
      continue                
    for j in range(0, len(numbers[i])):
      print "j: "+str(j)
      print "Number[i][j]: "+ str(numbers[i][j])
      print "Solution[last]: "+str(solution[last])
      unique = True;                                                       
      for k in range(0, len(solution)):
        if numbers[i][j] == solution[k]:
          unique = False;
          print "Breaking out since unique is False"
          break;
         
      if unique and ((numbers[i][j] / 100) == (solution[last] % 100)):                    
        solution[i] = numbers[i][j]
        print "Setting solution["+str(i)+"]= "+str(numbers[i][j])
        if (length == 5):
          if solution[5] / 100 == solution[i] % 100:
            print "Returning true for length 5"
            return True
        print "calling findnext for last = "+str(i)+" and length = "+str(length+ 1)
        if FindNext(i, length + 1):
          print "Returning from recursive function"
          return True                       
        
    print "Setting solution["+str(i)+"]"+"= 0"
    solution[i] = 0
  print "returning false for last :  "+str(last)+" length: "+str(length)
  return False

for i in range(0,len(numbers[5])):
  solution[5] = numbers[5][i]
  if FindNext(5, 1):
    break 

print solution


