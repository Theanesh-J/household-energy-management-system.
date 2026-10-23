import numpy as n
import matplotlib.pyplot as plt
from datetime import datetime
company_id_list=["1","2","3","4","5","6","7","8"]
house_data={
    1: {
        "house_id":11,
        "source_type": "solar",
        "energy_generated": 250,
        "energy_consumed": 180,
        "energy_saved": 0
    },
    2: {
        "house_id":12,
        "source_type": "wind",
        "energy_generated": 150,
        "energy_consumed": 150,
        "energy_saved": 5
    },
    3: {
        "house_id":13,
        "source_type": "solar",
        "energy_generated": 400,
        "energy_consumed": 320,
        "energy_saved": 80
    },
    4: {
        "house_id":14,
        "source_type": "solar",
        "energy_generated": 500,
        "energy_consumed": 420,
        "energy_saved": 31
    }
}
#--------------------------------------------------------------------------------------------
#                              FUNCTIONS
#--------------------------------------------------------------------------------------------
def header():#to print report column headings
    print(f'{"House id":<24}{"Source type":<24}{"energy generated(kWh)":<24}\
{"energy consumed(kWh)":<24}{"energy saved(kWh)":<24}')
def report(y,x): #prints report content y is the dictionary name,x is the index
    print(f'{y[x]["house_id"]:<24}{y[x]["source_type"]:<24}\
{y[x]["energy_generated"]:<24}{y[x]["energy_consumed"]:<24}\
{y[x]["energy_saved"]:<24}')
def total_energy_saved():
    total=0
    for x,obj in house_data.items():
       total+=(obj["energy_saved"])
    return(total)
def average_energy_saved():
    average=format(total_energy_saved()/len(house_data),".2f")
    return average
def sort_house_energy():
    sorted_house_data=house_data.copy()#make acopy of the dictionary of data
    n=len(sorted_house_data)
    for i in range (n):
        for j in range(1,n):
            if sorted_house_data[j]["energy_saved"]<sorted_house_data[j+1]["energy_saved"]:#bubble sort logic with nested dictionary indexing.
                temp=sorted_house_data[j]
                sorted_house_data[j]=sorted_house_data[j+1]
                sorted_house_data[j+1]=temp
    return sorted_house_data
def find_bonus():#returns a list of houses for bonus and finds bonus amount
    global bonus
    sorted_house_data=sort_house_energy()
    n= len(sorted_house_data)
    count=0#number of houses tied at top.
    houses_for_bonus=[]#list---------------------------------------------------------------------------------
    bonus=sorted_house_data[1]["energy_saved"]*1.25
    if bonus!=0:#incase all houses have 0 energy saved.
      for i in range(1,n):#to get indexing from 1 to length of data
          if sorted_house_data[i]["energy_saved"]!=sorted_house_data[i+1]["energy_saved"] and count==0:#checks if the first and second highest saved energies are different
              houses_for_bonus.append(sorted_house_data[1]["house_id"])
              break
          elif sorted_house_data[1]["energy_saved"]==sorted_house_data[i+1]["energy_saved"]:#counts all tied houses at top
              count+=1
      if count>0:
          for j in range(1,count+2):#if count=1 two houses are tied hence limit must be 3 for this for loop hence count+2
              houses_for_bonus.append(sorted_house_data[j]["house_id"])#using count for indexing limit,adds all tied houses to bonus house list
    return(houses_for_bonus)
def obtain(value):#input data name and returns list of that e.g list of house ids.
    data_list=[]
    for x,y in house_data.items():
        data_list.append(y[value])
    return(data_list)
def input_valid(input_type):#--------------------------------------------------input validation for expected positive integers
  while True:
    if(input_type == "household_id"):
      value = input("Enter Household ID\n")
    elif(input_type== "energy_consumed"):
      value = input("Enter the energy consumed\n")
    elif(input_type=="energy_generated"):
      value=input("Enter the energy generated\n")
    try:
      value=int(value)
      if value<0:
        print("invalid input enter a positive value")
      else:
        break
    except:
      print("Invalid Input retry")
  return(value)
def enter_source_type():#--------------------------------------input validation for wind or solar.
  while True:
    e_source=input("Enter Energy souce type\n").lower()
    if e_source == "wind" or e_source=="solar":
      break
    else:
      print("invalid input please enter wind or solar")
  return e_source
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#                          PROGRAM STARTS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    user_type=(input("Welcome to the company name \
energy system.\nType A if you are a company member\n\
Type B if you are a household owner\n")).upper()
    if user_type=="A":
        company_id=input("Enter company member ID\n")
        if company_id in company_id_list:
            task=input("Type A to enter new household data\nType B to \
view house hold data\nType C to edit existing household data\nType D to \
view weekly report\nType E for numerical analysis and graphs.\n").upper()
            hid_list=obtain("house_id")#creates a list of house ids from the main nested dictionary
            if task=="A":
                while task=="A": #------------------------------------------------------------------------enter new house data---------------------------------
                    hhold_id=input_valid("household_id")
                    if hhold_id not in hid_list:
                        e_source=enter_source_type()
                        e_gen=input_valid("energy_generated")
                        e_con=input_valid("energy_consumed")
                        if e_gen>e_con:
                            e_save=e_gen-e_con
                        elif e_gen<=e_con:
                            e_save=0
                        house_data[len(house_data)+1]={
                            "house_id":hhold_id,
                            "source_type":e_source,
                            "energy_generated":e_gen,
                            "energy_consumed":e_con,
                            "energy_saved":e_save
                        }
                        task=input("type 'A' to add data for another house, type 'x' to \
exit\n").upper()
                    else:
                      print("This house ID already exists, enter new house ID or use function C to edit existing household data\n")   #user interface improvement
            elif task=="B":#-------------------------------------------------------view house data for specific house---------------------------------------------------
                header()
                for i in range(1,len(house_data)+1):
                    report(house_data,i)
            elif task =="C":#------------------------------------------------------edit data for a specific house-------------------------------------------------------
                edit_house_id= int(input("enter required house hold ID"))
                hid_list=obtain("house_id")
                if edit_house_id in hid_list:
                  e_source=enter_source_type()
                  e_gen=input_valid("energy_generated")
                  e_con=input_valid("energy_consumed")
                  if e_gen>e_con:
                      e_save=e_gen-e_con
                  elif e_gen<=e_con:
                      e_save=0
                  house_data[hid_list.index(edit_house_id)+1]={
                          "house_id":edit_house_id,
                          "source_type":e_source,
                          "energy_generated":e_gen,
                          "energy_consumed":e_con,
                          "energy_saved":e_save,
                    }
            elif task=="D":# --------------------------------------------------------print weekly report-----------------------------------------------------------
                header()
                for i in range(1,len(house_data)+1):
                    report(house_data,i)
                print("\n\nSORTED HOUSE DATA BY ENERGY SAVED")
                sorted_house_data=sort_house_energy()
                header()
                for i in range(1,len(house_data)+1):
                    report(sorted_house_data,i)
                print("SUMMARY STATISTICS")
                print("Total",total_energy_saved(),"kWh")
                print("Average", average_energy_saved(),"kWh")
                houses_for_bonus=find_bonus()
                if not houses_for_bonus:
                  print("No eligible houses for bonus")
                else:
                  print("House(s) for bonus")
                  header()
                  for k in houses_for_bonus:
                      report(sorted_house_data,houses_for_bonus.index(k)+1)
                  print("bonus\n",bonus,"£")
                print("This report was generated on",datetime.now(),"\n\n")
             #------------------------------------------------------------------------------------------------
             #                                     NUMERICAL ANALYSIS AND CHART.
             #--------------------------------------------------------------------------------------------------
            elif task=="E":
              #-------------------------------Task 6 Evaluation.
              data = n.loadtxt('dataset_file.txt',dtype=str)
              house_id=data[:,0]
              source_type=data[:,1]
              energy_generated=(data[:,2]).astype(int)
              energy_consumed=(data[:,3]).astype(int)
              energy_saved=(data[:,4]).astype(int)
              print("\n\nNumerical analysis")
              print("Total energy saved:", n.sum(energy_saved))
              print("Average energy saved:", n.mean(energy_saved))
              print("Minimum energy saved:", n.min(energy_saved))
              print("Maximum energy saved:",n.max(energy_saved))
              print("Median:",n.median(energy_saved))
              print("Standard deviation:",round(n.std(energy_saved),2))
              print("Variance:",n.var(energy_saved))
              #Bar chart of energy saved by every household.
              xlabels=[]
              for i in range(len(house_id)): #creates a list of x labels with house ids and source type
                xlabels.append(f"({house_id[i]}),({source_type[i]})")
              #bar graph
              plt.figure(figsize=(24,6))#widen the graph
              x=n.arange(len(xlabels))
              width=0.3
              plt.bar(x-width, energy_generated, width, label="Energy generated",color="blue")
              plt.bar(x,energy_consumed,width,label="Energy consumed", color="red")
              plt.bar(x+width,energy_saved,width,label="Energy saved",color="green")
              #labels and title
              plt.xlabel("household(Energy source)")
              plt.ylabel("energy(kWh)")
              plt.title("household energy produced, consumed and saved")
              plt.xticks(x, xlabels, rotation=60,fontsize=8)
              plt.legend()
              plt.subplots_adjust(bottom=0.2) #add more bottom space for long labels.
              plt.savefig("bar_chart.png")
              print("bar chart saved as bar_chart.png\n\n")
              plt.close()
        else:
          print("Invalid company member ID entered heading back to main menu\n") #user interface improvement
    elif user_type=="B":
        houses_for_bonus=find_bonus()
        hid_list=obtain("house_id")
        owner_id=input_valid("household_id")
        if owner_id in hid_list and owner_id not in houses_for_bonus:
            header()
            report(house_data,hid_list.index(owner_id)+1)
        elif owner_id in hid_list and owner_id in houses_for_bonus:
            header()
            report(house_data,hid_list.index(owner_id)+1)
            print("congratulations, you saved the most energy your bonus is ",bonus,"£")
        else:
          print("invalid house_id returning to main menu")
    else:
      print("Invalid user type entered try again\n")#user interface improvement
