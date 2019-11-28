
Credits=0 # Variable 01
Deffer=0 # Variable 02
Fail=0 # Variable 03

CreditsRanges=[0,20,40,60,80,100,120] # Credit Limitation List
Progress=[] # Progress Outcommers list
Trailing=[] # Module Trailing List
Reterver=[] # Module Retervers list
Exclude=[] # Excluded student List
TotalEnters =[]

def Checker(): # Progress checking Funtion

    Credits= int(input("Enter Your Credits to The System : "))
    Deffer=int(input("Enter Your Differ value to The System : "))
    Fail=int(input("Enter your Fail values to The System : "))

    Total = Credits+Deffer+Fail # Total of the Marks

    MRetriever=Deffer+Fail #Sum of Reterver's marks

    if Credits not in CreditsRanges or Deffer not in CreditsRanges or Fail not in CreditsRanges: # Figure it out the Range Error
        print("Range Error!")

    elif Total !=120: # Figure it out the credit Total
        print("Total Incorrect")

    elif Credits==120: # Progress Student
        print("Progress.")
        Progress.append(Credits)
        TotalEnters.append(Credits)

    elif Credits==100: # Find out the Module Trailing Students
        print("Progress – module trailer")
        Progress.append(Credits)
        Trailing.append(Credits)
        TotalEnters.append(Credits)

    elif Fail >=80: # Find out the Excluded Students
        print("Exclude")
        Exclude.append(Fail)
        TotalEnters.append(Fail)

    elif MRetriever>=40: # Find out the Retervers
        print("Do not progress – module retriever")
        Reterver.append(MRetriever)
        TotalEnters.append(MRetriever)

while control !="Q": # Loop for continue or Quit for Histogram
    print("\n")
    Checker()
    print("\n")
    control=str(input ("Enter C for continue / Enter Q For Histograme. "))
   
# Horizontal Histogram 

print("\n")
print("-----------------------------------------------------------------------------------------------------")
print("\n")
print("Progress ",len(Progress),":","* "*len(Progress))
print("\n")
print("Trailing ",len(Trailing),":", "* "*len(Trailing))
print("\n")
print("Retriever ",len(Reterver), ":", "* "*len(Reterver))
print("\n")
print("Excluded ",len(Exclude),":","* "*len(Exclude))
print("\n")
print(len(TotalEnters), "Outcomes in Total.")
print("\n")
print("------------------------------------------------------------------------------------------------------")