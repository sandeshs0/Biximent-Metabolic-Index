
print("---Welcome. Let's know something about you.---")
weight = (input("Enter your weight in Kilograms: "))
age = (input("Enter your Age in Solar Cycles: "))
gender = input("What gender are you? (R,S or T): ")
bixiLev = (input("What is your Biximent Level?: "))

# Calculation of Biximent Metabolic Index (BMI)
# Gender Factors:

if (gender == "R" or gender == "r"):
    gf = 8.46
    valid_gen = True
elif (gender == "S" or gender == "s"):
    gf = 4.23
    valid_gen = True
elif (gender == "T" or gender == "t"):
    gf = 6.35
    valid_gen = True
else:
    print("Wrong Input for Gender")


while (float(weight) > 28 and (float(age) > 16 and float(age) < 96) and float(bixiLev) >= 30):
    # BMI
    bmi = 2.56*float(age)+((float(bixiLev)*467)/(float(weight)*float(gf)))

    # Recommendation:
    if (bmi < 80):
        recTreat = "Mild case, no treatment required"
    elif (bmi >= 80 and bmi < 120):
        recTreat = "Serious case, Medication treatment"
    elif (bmi >= 120 and bmi < 200):
        recTreat = "Acute case, Ultravoilet treatment"
    elif (bmi >= 200 and bmi < 360):
        recTreat = "Severe case, Replacement therapy \n Inhabitant is Highly Contagious"
    elif (bmi >= 360):
        recTreat = "Extreme case, Hospitalization \n Inhabitant is Highly Contagious"

    # Printing the OutPut:->
    print("\n---Biximent Metabolic Index Report---")
    print("Gender: ", gender)
    print("Age: ", age, " cycles")
    print("Weight: ", weight, "kilograms")
    print("Biximent Level: ", bixiLev)
    print("BMI: ", bmi)
    print("Recommended treatment: ", recTreat)
    break
else:
    print("Wrong Input")
