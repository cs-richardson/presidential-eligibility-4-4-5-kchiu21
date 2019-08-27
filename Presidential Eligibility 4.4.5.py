"""
This code ask for three inputs from user for age, if they are born in the U.S.
and how long have they been living in the US. If they meet all three
requirments below they are eligible to run for president. If the user does
not meet the requirment
"""
ageUser = int(input("Age: "))
citizenOfuser = bool(input("Born in the U.S.? (Yes/No): "))
residentTime = int(input("Years of Residency: "))
if (ageUser >= 35 and citizenOfuser==True and residentTime>=14):
    print ("You are eligible to run for president!")
else: 
    print ("You are not eligible to run for president.")