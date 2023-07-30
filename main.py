#importing a text file (https://www.youtube.com/watch?v=0EgSo7hsRWM):
file = open("zein text.txt", "r")

f = file.readlines(
)  # change file into list to better extract from it (every line)


list = []
for line in f:
  list.append(line.strip())  # to remove(/n)


def printFile():  # to print the data in a readable way
  for x in f:
    print(x)


#importing a text file (https://www.youtube.com/watch?v=0EgSo7hsRWM):
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
      

  print("this is the event with the highest count of tickets",maxevent)

def main():
  username = input("Hello please enter a username:")
  password = input("Please enter your password:")

  while username == "admin":  
    counter = 0
    if password == "admin123123":
      print("welcome admin")
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
main()  