from datetime import date# this is to import today's date
#importing a text file (https://www.youtube.com/watch?v=0EgSo7hsRWM)
file = open("zein text.txt", "r")
f = file.readlines()  # change file into list to better extract from it (every line)

keys = ["tick", "event", "username", "date", "priority"]
list = []



for line in f:
  
  dict = {}
  values=line.split(",")#turning the line into list of values
  for i in range(len(keys)):
    dict[keys[i]]=values[i]
  list.append(dict)



  


#defining 2 functions for user and admin menus
def displayAdminMenu():
  print("________________")
  print("kindly choose from 1 to 7 \n1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket's Priority\n5. Disable Ticket\n6. Run Events\n7. Exit\n")
  

  
def displayUserMenu():
  print("kindly choose between the 2 options\n1. Book a ticket\n2. Exit\n")  


#defining a fuction to show the event ID with the highest number of tickets.
def displayStatistics():
  

  list1 = []
  for record in list: # to create list1 which only has events in it
    event = record["event"]
    list1.append(event)
  def checkCount(item): #  a function which raises a count every time it finds a specific event
    counter=0
    for record in list1:
      if item==record:
        counter+=1
    return counter  

    
  maxcount=0
  maxevent=list1[0]
  for ev in list1: # to check the event with the highest count
    if checkCount(ev)>maxcount:
      maxcount= checkCount(ev)
      maxevent=ev
      

  print("this is the event with the highest count of tickets:",maxevent)

def bookTicket():
    new_tick=int(list[-1]['tick'][4:])+1 # to get ticket number +1
    new_ticket_String = "tick" + str(new_tick) # to add "tick" to the previous number
    new_event=input("please enter an event number:")
    new_username=input("please enter a name:")
    new_date=input("please enter date:")
    new_priority=input("please enter priority number:")
    new_ticket={} #creating a dictionary
    values=[new_ticket_String,new_event,new_username,new_date,new_priority]
    for i in range(len(values)):
      new_ticket[keys[i]]=values[i]
    list.append(new_ticket)    #appending to the privous list from file
      
    print("New list containing the new ticket is:\n",list)  

 
def changePriority():
  old_tick_num=input("Please enter the number of ticket in list:")
  old_tick= "tick"+old_tick_num
  found=False

  for dict in list:
    if old_tick==dict['tick']: # checking if ticket is inside list
      new_priority=input("please type new priority:")
      found=True
      dict['priority']=new_priority
      
      
  if(found == False): print("This ticket was not found")

  else:
    print(list)
   

def disableTicket():
  old_tick_num=input("Please enter the ticket ID that you want to delete in list:")
  old_tick= "tick"+old_tick_num
  found=False


  for index in range(len(list)-1):# 0 , 1, 2 ,  3 
    dict=list[index]
    if old_tick == dict['tick']:
      print ("found")
      del list[index]
      found = True
      

      

  if(found == False): print("This ticket was not found")
  else: print(list)

def bookUserTicket(username):
  new_tick=int(list[-1]['tick'][4:])+1 # to get ticket number +1
  new_ticket_String = "tick" + str(new_tick) # to add "tick" to the previous number
  new_event="ev"+input("please enter an event number:")
  new_date=input("please enter date:")
  priority="0"
  new_ticket={} 
  values=[new_ticket_String,new_event,username,new_date,priority]
  for i in range(len(values)):
    new_ticket[keys[i]]=values[i]
  list.append(new_ticket) 
  print(list) 
  list22=[]
  
  s= "\n"+(",".join(values))
  list22.append(s)
  with open('zein text.txt', 'a') as f:#https://www.pythontutorial.net/python-basics/python-write-text-file/
    f.write("".join(list22))

def merge_priority(key, left, right):  
  # empty list for the resulting list
  sorted_list = []
    # while neither of the lists is empty
  while left != [] and right != []:
      if int(left[0][key]) > int(right[0][key]):
        sorted_list.append(left.pop(0))
        # the pop function remove an item by specifing the index and returns its value
      else:
        sorted_list.append(right.pop(0))
  if left == []:
    sorted_list += right

  elif right == []:
    sorted_list += left

  return sorted_list

def displayAllTickets(): 
  sorted_list = mergeSort(list,"date")
 
  


  for event in sorted_list: 
    print(",".join(event.values()))#.values takes all values inside a dictionary, .join concatenates(joins) the values with an indicated string

def mergeSort(unsorted_list,kaey):
  if len(unsorted_list) <= 1:
    return unsorted_list
    # returning any list that contains one element or it's empty
  else:
    mid = len(unsorted_list) // 2
    left = mergeSort(unsorted_list[:mid], key)
    right = mergeSort(unsorted_list[mid:],  key)
    return (merge_priority(key, left, right,))

def runEvents(): 
  list_today=[]
  for i in list:
    if i['date']==str(date.today()).replace("-",""):#date.today.replace is to get todays date in this format(yyyymmdd)c
      list_today.append(i)
      
  
  sorted_list = mergeSort(list_today,"priority")

  print("these are today's events: \n")
  for event in sorted_list: 
    print(",".join(event.values()))#.values takes all values inside a dictionary, .join concatenates(joins) the values with an indicated string
  
  #deleting todays events
  for i in sorted_list:
    for j in list:
      if i['tick']==j['tick']:
        list.remove(j)
      

  print(list)   


def main():
  username = input("Hello please enter a username:")
  password = input("Please enter your password:")

  while username == "admin":  
    counter = 0
    if password == "admin123123":
      print("welcome admin")
      displayAdminMenu()
      choice=int(input()) 
      while choice != 7:
        if choice == 1:
          displayStatistics()
        elif choice == 2:
          bookTicket()
        elif choice == 3:
          displayAllTickets()  
        elif choice == 4:
          changePriority()    
        elif choice == 5:
          disableTicket()  
        elif choice == 6:
          runEvents()  
        else:
          print("!!!invaild input!!!") 
        displayAdminMenu()
        choice=int(input())   
      print("You have exited the program")  

      
      break
    else:
      while password != "admin123123":# to not allow the admin to try more than 5 times with wrong password
        counter += 1
        if counter < 5:
          print("Incorrect Username and/or Password")
          username = input("please enter a username:")
          password = input("enter your password:")
  
        elif counter >= 5:
          print(
              "program will terminate because you have entered the wrong password 5 times"
          )
          exit()
        else:
          print("welcome admin")
          break
  
  if username != "admin":
    print("Hello", username)
    displayUserMenu()
    choice=int(input("please enter a number:"))
    while choice!=2:
      if choice == 1:
        bookUserTicket(username)
        #https://www.pythontutorial.net/python-basics/python-write-text-file/ (to write in a textfile)
      else:
          print("!!!invaild input!!!")
      displayUserMenu()  
      choice=int(input("please enter a number:"))
      
        
        
main()  