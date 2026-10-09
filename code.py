# Author: Salah Eddine | Python Developer (in progress)
# Stack: Python  / HTML / CSS / JS |  PHP / SQL
# Motto: I don't let AI code for me, I suffer to understand.
# 
# Dear Programmer:
# When I wrote this code, only God and I knew how it worked.
# Now, only God knows it!
#
# Therefore, if you are trying to optimize this routine
# and it fails (most surely), please increase this counter
# as a warning for the next person:
# 
# total_hours_wasted_here = 203 



taskes=[] # the most important list it has all taskes

try:
    with open("Taskes.txt", "r", encoding="utf-8") as f:
        for line in f:
            taskes.append(line.strip())

except FileNotFoundError:
    pass
  
  
while True : # main while
    # menu
  print("==================| TO==DO==LIST |=================") #hhh just semple designe
  print(" +===================|(●'◡'●)|===================+")
  print(" ||             +================+              ||")
  print(" ||             ||1  Add task   ||              ||")
  print(" ||             +================+              ||")
  print(" ||             ||2  View task  ||              ||")
  print(" ||             +================+              ||")
  print(" ||             ||3  Mark task  ||              ||")
  print(" ||             +================+              ||")
  print(" ||             ||4  Delete task||              ||")
  print(" ||             +================+              ||")
  print(" ||             ||5 Save & Exite||              ||")
  print(" ||             +================+              ||") 
  print(" ++=================|01011010|==================++")
  try: 
      chouse=(int(input("        Choose  :... "))) # input taskes
      if chouse>5 or chouse <=0 :
        print("this number is not anvariable in the above menu")
  except ValueError:
      print("enter a number not string or flout")
      continue
  match chouse:
# 1  Add task
    case 1:
          stop=False
          while True:
            print("======================================================")
            task=input("    weaite the taske : ").strip()
            if task == "":
              print("please enter a taske")
            else :
             taskes.append(task)
            while True:
              print("======================================================")
              more= input("dio need to raite anhother task y/n ; ").strip().upper()
              if more== "N" :
                stop=True
                break
              
              elif more=="Y":
                break
              else:
                print("======================================================")
                print(f"enter y/n not '{more}' ⛔")
            if stop == True:
                 break
# print all taskes
# 2  View task 
    case 2 :
        print("======================================================")
        print("======================================================")
        if not taskes:
          print("the list is empty")
                 
        else:
          print("                 =====| your taskes |====")
          print("                   ===||(～￣▽￣)～||===")
          for i , task in enumerate(taskes):
                print(f"{i+1} , {task}")
        
        
        print("======================================================")
        print("======================================================")
        
# marke task as done ✅
#3  Mark task
    case 3:
      if not taskes:
        print("======================================================")
        print("the list is empty ")
        print("======================================================")
        print("======================================================")
      else:
        while True:

            for i , task in enumerate(taskes):
              print(f"{i+1} , {task}")
            try:
              task_num=int(input("enter number by the done task : ")) -1
              if 0<= task_num <len(taskes): 
                  if "✅" in taskes[task_num]:
                    print("this taske alrady marked ?")
                  else:
                    taskes[task_num] += "✅"
                    print(f"the task {task_num +1} was done secsufuly ✅")
              else :
                  print("the number is false ")
            except ValueError:
              print("enter true number")
            print("======================================================")  
            more1= input("dio need to mark anhother task y/n ; ").upper()
            print("======================================================")
            if more1== "N":
                break
        print("==================================================")
        print("==================================================")          
# delet taskes by the index using fonction "pop"  
# 4  Delete task      
    case 4:
      if not taskes:
        print("the list is empty ")
      else:
        try:
            task_num=int(input("enter number by the task you want to delete : ")) -1
            if 0<= task_num <len(taskes): 
                deleted_task = taskes.pop(task_num)
                print(f"the task '{deleted_task}' was deleted secsufuly ✅")
            else :
                print("the number is false ")
        except ValueError:
                  print("enter true number")
# save 
# 5 Save & Exite
    case 5:
            print(taskes)
            with open ("Taskes.txt" , "w" , encoding="utf-8") as f:
                for i, task in enumerate (taskes,start=1):
                 f.write(f"{i}: {task}\n")
            print("your taskes was saved sucsifily ✅")
            print("===========Goodbye!===================")
            break
    # case _:
    #   print("this number is not anvariable in the above menu")
     

             
             