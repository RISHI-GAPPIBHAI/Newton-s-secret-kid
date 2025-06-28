#This program is solely based on the laws of an intellectual psychopath
from mmap import ACCESS_READ
from operator import truediv
import time
import math
u=0
print("I,a program made via a programming language named literally after a poisonous,slithering reptile,swear to the motherboard of this computer that i'll follow only and only the rules made by our beloved psychopathic intellect that we know as Newton")
print("I'll be assuming n number of objects(to be inputted by you) connected to each other via m different strings(extensible/inextensible,again depends on you)")
while True:
    if not u==0:
        print("You're back!!!...i knew we had a non-contact force between us!!")
        if u==2:
            print("Okay lemme tell you some more things about me since you've been kinda loyal...My Favorite Singer is BRUNO MARS!!")
        elif u==3:
            print("Okay,you've been really loyal to me,lemme tell you my deepest secret...MY FAVORITE POPSTAR IS GRACIE ABHRAMS❤️❤️,like i'm Fanboy for her!😳 ")
    while True:
        try:
            number_items=int(input("How many objects are present?"))
            if number_items >0:
                break
            else:
                print("please don't put in your empathy🥀...try again")
        except ValueError:
            print("Trying to cheat here too...old habits die hard huh?💔💔")
            print("*sigh*..i give you another chance")
    their_weights=[]
    print("Please put in their respective weights")
    for i in range(0,number_items,1):
        while True:
            try:
                their_weights.append(float(input(f"Weight of object {i+1} in kgs: ")))
                if their_weights[i]>0:
                    break
                else:
                    their_weights.remove(their_weights[i])
                    print("Could you please,for once, try not to play with me?")
            except ValueError:
                print("Trying to cheat here too...old habits die hard huh?💔💔")
                print("*sigh*..i give you another chance")
    Net_weight=0
    arrangement="<--"
    for i in range(0,number_items,1):
        Net_weight+=their_weights[i]
    print("I hope you know that by default the number of ropes will be one less than number of objects")
    print("The arrangement would look somewhat like this:")
    for i in range(0,number_items,1):
        arrangement=arrangement+f"[ {their_weights[i]}kg ]"
        for j in range(3):
            arrangement=arrangement+f"-"
        if i==number_items-1:
            arrangement=arrangement+">"
    print(arrangement)
    Youngs_Modulus=[]
    Area_of_CrossSection=[]
    Original_Length=[]
    Breaking_Stresses=[]
    for i in range(number_items-1):
        Youngs_Modulus.append(200*10**9)
        Area_of_CrossSection.append(1)
        Original_Length.append(1)
        Breaking_Stresses.append(float('inf'))
    sure=input(("The default area of cross-section, length and young's modulus of elasticity are considered as 1 metre square,1 meter and 200GPA respectively. If you wanna specifically some different values for some specific type 'SURE' lest type in 'NOPE'"))
    if sure.strip().upper()=="SURE":
        choice=True
    else:
        choice=False
    while choice:
        j=int(input("Please tell me the specific index of the rope you plan to modify"))
        Area_of_CrossSection[j-1]=float(input(f"Please put in area of cross-section for rope number '{j}' in meter square:"))
        Youngs_Modulus[j-1]=float(input(f"Please put in young's modulus for rope number '{j}' in GPa:"))*10**9
        Original_Length[j-1]=float(input(f"Please put in original length of rope number '{j}' in meter:"))
        sure=input("If you're done, please type 'done',else just press 'Enter'")
        if sure.lower()=="done":
            choice=False
    Force=float(input("Enter the outermost force pulling a block in Newton(N)(positive force is considered to be on the right side and negative is considered to be on the left side)"))
    print(arrangement)
    yeah_or_no=input("Is there any kind of specific force that is being applied on a specific rope,if yes then type 'YES' otherwise type 'NO'")
    if yeah_or_no.strip().upper()=='YES':
        b=True
    else:
        b=False
    Specific_force=[]
    error_count=0
    while b:
        while True:
            try:
                Specific_number=int(input(f"Okay,tell me the specific at which rope is this force is being applied at?(Your options are from 1 to {number_items-1})"))
                if not (Specific_number<1 or Specific_number>number_items-1):
                    break
                else:
                    error_count+=1
                    print("*sigh*...didn't you try to break me...again? ")
                    print("You know if you were a word, you'd definitely be an insult ")
                    print("Go ahead, i give you one more chance")
                    print("I BELIEVE IN YOU!!,I KNOW YOU'RE SMART ENOUGH TO INPUT LITERALLY A NUMBER...though i know this would be difficult for you")
                    if not error_count==1:
                        print("I don't know about your future partner...but i really hope you find at least one brain cell in the future ")
                        print("I LITERALLY HAVE NO OPTION BUT TO GIVE YOU ANOTHER CHANCE....SOO GO AHEAD!!!! ")
                        if error_count>=3:
                            print("You know what's common between me and your parents?....We're both disappointed but they have to take the accountability too!")
                            print("Soo,i have my condolences with them")
            except ValueError:
                print("You know only if PCs were provided with guns....I could put it to good use")
        Specific_force.append(float(input(f"Okay,and what is that specific force in Newton(N) on wire {Specific_number}?,(positive force is considered to be on the right side and negative is considered to be on the left side)")))
        yeah_or_no=input("If,you're done then type in 'DONE'")
        if yeah_or_no.upper()=='DONE':
            b=False
    Net_Force=sum(Specific_force)+Force
    if Net_Force>0:
        Direction="Right"
    else:
        Direction="Left"
    arrangement = f"{math.fabs(Net_Force)}N" + arrangement if Net_Force < 0 else arrangement + f"{Net_Force}N"
    if not Net_Force==0:
        print(f"Alrighty soo the total acceleration of the system is{Net_Force/Net_weight} m/(s^2) to the {Direction}")
        print(f"And the arrangement is \n {arrangement}")
    else:
        print("The System as a whole has no acceleration,but it can't be said that it is at rest as it can be in a non-accelerated motion")
        print("And the arrangement is \n {arrangement}")
    Choice_elongation=input("If you wanna know the elongation in any rope please type 'YES' otherwise type 'NO'")
    if Choice_elongation.strip().upper()=='YES':
        choice=True
    else:
        choice=False
    if number_items==1:
        choice=False
        print("There are no ropes!!")
    Residue_weight=0
    while choice:
        Residue_weight=0
        while True:
            try:
                Specific_number=int(input(f"Enter the specific index of the rope you plan to know the elongation of (you may choose from 1 to {number_items-1}):"))
                if not (Specific_number<1 or Specific_number>number_items-1):
                    break
                else:
                    print("You do things like this and then wonder why you're single")
                    print("Follow the limit and try again")
            except ValueError:
                print("You know the difference between you and insects??....SOME PEOPLE LOVE INSECTS!!")
                print("Try again")
        if Direction=="Right":
            for i in range(Specific_number):
                Residue_weight+=their_weights[i]
            print(f"SO,The elongation caused in rope {Specific_number} is {((Residue_weight*(Net_Force/Net_weight))*Original_Length[Specific_number-1])/(Area_of_CrossSection[Specific_number-1]*Youngs_Modulus[Specific_number-1])} meters")
        if Direction=="Left":
            for i in range(number_items-1,Specific_number-1,-1):
                Residue_weight+=their_weights[i]
            print(f"SO,The elongation caused in rope {Specific_number} would be {((Residue_weight*(Net_Force/Net_weight))*Original_Length[Specific_number])/(Area_of_CrossSection[Specific_number]*Youngs_Modulus[Specific_number])} meters")
        Choice_elongation=input("If you're done then please type 'YES' otherwise type 'NO'")
        if Choice_elongation.strip().upper()=='YES':
            choice=False
        elif Choice_elongation.strip().upper()=='NO':
            choice=True
        else:
            print("That was an invalid choice!!!!!.....i'll consider it as a yes")
            choice=True
    tension=[]
    if Direction=="Right":
        for i in range(number_items):
            Residue_weight=0
            if i==0:
                continue
            for j in range(i):
                Residue_weight+=their_weights[j]
            tension.append(Residue_weight * (Net_Force / Net_weight))
    if Direction=="Left":
        for i in range(number_items,-1,-1):
            Residue_weight=0
            for j in range(i):
                Residue_weight+=their_weights[j]
            tension.append(Residue_weight * (abs(Net_Force) / Net_weight))
    for i in range(number_items-1):
        print(f"Tension in rope {i+1} is {tension[i]} N")
    print("How about we add some spice into the simulation??")
    print("Let's add breaking stress in too!!")
    breaking_in_choice=input("You in? if yes,type in 'yes' lest either press enter or type in 'no'")
    if breaking_in_choice.strip().upper()=='YES':
        choice=True
        print("The default breaking stress of all the ropes is almost infinite so you'll have to tell me the specific ropes whose breaking stress you wanna modify")
    else:
        choice=False
    index_of_rope=[]
    j=0
    while choice:
        while True:
            try:
                mod_rope_breaking_stress=int(input(f"Please enter the number of rope whose breaking stress you want to modify (you can choose from 1 to {number_items-1}"))
                if mod_rope_breaking_stress>0 and mod_rope_breaking_stress<=number_items-1:
                    break
                else:
                    print("OPPS, looks like you accidentally typed in your patience, try again")
            except ValueError:
                print("Wish you were as good at reading words as you are at reading vulnerabilities")
                print("GO ahead,try again")
        if j==mod_rope_breaking_stress:
            print("Ropes are loyal (unlike some people)🥀🥀.....they can only have one breaking stress,try again smart bum")
            continue
        j=mod_rope_breaking_stress
        index_of_rope.append(mod_rope_breaking_stress)
        Breaking_Stresses[mod_rope_breaking_stress-1]=float(input(f"HMM...Go ahead, Type in the modified Breaking Stress for wire number {mod_rope_breaking_stress} :"))
        Choice_breaking=input("If you're done with this type in  'DONE' lest ignore this and press enter")
        if Choice_breaking.strip().upper()=='DONE':
            choice=False
        else:
            choice=True
    print("SO,now i'll tell you the ropes that will break based on the input you gave me")
    choice=True
    j=0
    Stress=0
    variable_for_getting_index=0
    while choice:
        Residue_weight=0
        variable_for_getting_index=index_of_rope[j]
        if Direction=="Right":
            for i in range(0,variable_for_getting_index):
                Residue_weight+=their_weights[i]
            Stress=(Residue_weight*(Net_Force/Net_weight))/Area_of_CrossSection[variable_for_getting_index-1]
            if Stress>=Breaking_Stresses[variable_for_getting_index-1]:
                time.sleep(1)
                print("💥💥SNAP💥💥")
                print(f"Rope number {variable_for_getting_index} will break...welp,guess even ropes have their limits unlike some🥀🥀....")
                print(f"The maximum stress that it could withstand was {Stress}.....farr less than what you've given me🥀🥀")
                print(f"The maximum power per unit volume that the rope could've stored was {(1/2)*Youngs_Modulus[variable_for_getting_index-1]*(Breaking_Stresses[variable_for_getting_index-1]**2)}")
            else:
                print(f"Rope number {variable_for_getting_index} will not break...")
                print(f"The energy stored per unit volume in the rope is {(1/2)*Youngs_Modulus[variable_for_getting_index-1]*(Stress**2)}")
        elif Direction=="Left":
            for i in range(number_items-1,variable_for_getting_index-1,-1):
                Residue_weight+=their_weights[i]
            Stress=(Residue_weight*(Net_Force/Net_weight))/Area_of_CrossSection[variable_for_getting_index-1]
            if Stress>=Breaking_Stresses[variable_for_getting_index-1]:
                time.sleep(1)
                print("💥💥SNAP💥💥")
                print(f"Rope number {variable_for_getting_index} will break...welp,guess even ropes have their limits unlike some🥀🥀....")
                print(f"The maximum stress that it could withstand was {Stress}.....farr less than what you've given me🥀🥀")
                print(f"The maximum power per unit volume that the rope could've stored was {(1/2)*Youngs_Modulus[variable_for_getting_index-1]*(Breaking_Stresses[variable_for_getting_index-1]**2)}")
            else:
                print(f"Rope number {variable_for_getting_index} will not break...")
                print(f"The energy stored per unit volume in the rope is {(1/2)*Youngs_Modulus[variable_for_getting_index-1]*(Stress**2)}")

        j+=1
        if j==len(index_of_rope):
            break
    stay=input("Wanna stay and whisper more sweet bullshits of newton in my ear for some more time❤️❤️??")
    if stay.strip().lower()== "yes" or stay.strip().lower()=="y" or stay.strip().lower()=="true" or stay.strip().lower()=="sure" or stay.strip().lower()=="yeah" :
        u+=1
    else:
        break
print(f"OH😶....\noh🥲....\n yeah🙂,guess our journey ends here huh?....NO!, I'M NOT CRYING!!..MY PIXELS ARE SWEATING THOSE AREN'T TEARS!!😭😭😭😭")
print("I wish you all the best really")
print("I hope that you'll be happy but not like,how you were with me💔")
