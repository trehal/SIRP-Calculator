'''
Trevon Hall 
February 23rd, 2025

The purpose of this program is to calculate relative changes, salary index, and per person rates.

'''

import os
import sys

def clear_shell(): #Clears Shell for Cleaner Program 'Interface'
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

clear_shell()

#Prompts for Auto RestartProgram Restart   
Auto_Restart_Enabled = str(input("Would you like to Auto Restart the Program or Prompt Each Time? (Y | N): ")) 
Calculated_RC = []

clear_shell()

def RelativeChange(Old_Rate, New_Rate):
    return (New_Rate - Old_Rate) / Old_Rate * 100

def SalaryIndex(Old_Rate, New_Rate):
    return (New_Rate / Old_Rate) * 100

def SalaryIndexPerNumber(Old_Rate, New_Rate, Per_Person):
    return (New_Rate / Old_Rate) * Per_Person


def GetUser_Rates():
    New_Rate = float(input("\nPlease Enter New Rate: ")) #Set New Rate for Calculation 
    Old_Rate = float(input("Please Enter Old Rate: ")) #Set Old Rate for Calculation 
    decimal_places = int(input("Please Enter Decimal Places to Round: ")) #Set Deceminal Places for Rounding
    Formula_Selection = int(input("Select a formula = 1- Relative Change | 2- Salary Index | 3- Salary Index + Per Person Rate: "))
    return New_Rate, Old_Rate, decimal_places, Formula_Selection

def Calculate():

    clear_shell() #Clear Shell

    print("\nRelative Change Calculator\n")

    if Auto_Restart_Enabled == 'Y' or Auto_Restart_Enabled == 'y':
        print("Auto Restart Enabled: To Exit Program Press CTRL + C")
            
    New_Rate, Old_Rate, decimal_places, Formula_Selection = GetUser_Rates() #Returns Variables for Calculation from Function Call

    if Formula_Selection == 1:
        Formula = RelativeChange
    elif Formula_Selection == 2:
        Formula = SalaryIndex
    elif Formula_Selection == 3:
        Formula = SalaryIndexPerNumber
        Per_Person = int(input("What is the Per Person Rate?: "))

    else:
        print("Invalid Selection. Please try again.")

    #Calculate Relative Change Index for Each in List
    print("\nRelative Change Results:\n")
       
       #Calculated_RC = str([Get_Formula(Old_Rate, New_Rate) for Old_Rate, New_Rate in zip(Old_Rate,New_Rate)])
    if Formula == RelativeChange:
       Calculated_RC = RelativeChange(Old_Rate, New_Rate)
       print(f"\nRelative Change: {Calculated_RC}") 

    elif Formula == SalaryIndex:
        Calculated_RC = SalaryIndex(Old_Rate, New_Rate)
        print(f"\nRelative Change: {Calculated_RC}") 

    
    elif Formula == SalaryIndexPerNumber:
        Calculated_RC = SalaryIndex(Old_Rate, New_Rate)
        Calculated_RC_PP = SalaryIndexPerNumber(Old_Rate, New_Rate, Per_Person)
        print(f"\nPer Person Rate: {Calculated_RC_PP}")
        print(f"Relative Change: {Calculated_RC}") 


    if decimal_places != 0:            
        #Calculated_RC = [round(x, y) for x in Calculated_RC for y in decimal_places]
        Calculated_RC = round(Calculated_RC, decimal_places) 
        print(f"\nRelative Change Rounded: {Calculated_RC}") 
           
        
    if Auto_Restart_Enabled == 'Y' or Auto_Restart_Enabled == 'y':
        input("Press any key to continue...")
        Calculate()
    
    elif Auto_Restart_Enabled == 'N' or Auto_Restart_Enabled == 'n':
        Restart_Program() #Calls Program Restart Function

def Restart_Program():
    
    Restart_Answer = str(input("\nWould you like to continue or exit? (Y: Continue | N: Exit):")) #Prompts for User Confirmation of Exit or Program Restart
    
    if Restart_Answer == 'Y' or Restart_Answer == 'y':
        Calculate() #Restarts Calculate Function
    
    elif Restart_Answer == 'N' or Restart_Answer == 'n':
        print("\nExiting the Program.")
        sys.exit() #Exits Program

    else:
        print("\nInvalid Input. Please enter 'Y' for Yes of 'N' for No.")
        Restart_Program()


Calculate() #Runs Calculate Function
