# 1)Function named ds
def ds(roll_no,name):
    global List 
    global Tuple
    global Set
    global Dictionary
    #2)Add parameters
    List=[roll_no,name]
    Tuple=(roll_no,name)
    Set={roll_no,name}
    Dictionary={"Roll no.": roll_no , "Name":name}


def printds():
   
    print("\nList       : ",List,"\n")
    print("Tuple      : ",Tuple,"\n")
    print("Set        : ",Set,"\n")
    print("Dictionary : ",Dictionary,"\n")

#3)After adding values change the values during runtime
def dsUpdate():
   print("Updating Data Structures :-\n")
   rn=int(input("Enter the roll no : "))
   nm=input("Enter the name    : ")
   ds(rn,nm)
   List.append("CO-Batch-3)
   Set.add("SYCO-B")
   Dictionary["Language"]="Python"           
   Dictionary.update({"Class":"SYCO-B"})

ds(130,"Moin Qureshi")
printds()
dsUpdate()
printds()

#5)Delete these data structures
del List
del Tuple
del Set
del Dictionary
