#!/usr/bin/python
#File Name: IncomeTax.py
#Author: Luis Navarro

#Header
print("\n         Personal Income Tax Calculator      ")
print("\nValid Filing Statuses:                       ")
print("\n0 = Unmarried Filer                          ")
print("1 = Married Filing Jointly                     ")
print("2 = Head of Household                          ")

#Prompts
filingStatus = int(input("\nEnter the filing status: "))
taxableIncome = float(input("Enter your taxabale income: "))

#Decison tree
if filingStatus == 0:

    #print("\nfilingStatus: " + str(filingStatus)) #Debug

    #Determinig Tax Rate
    if (taxableIncome >= 0 and  taxableIncome <= 9951):
        taxRate = .10
        #print("Tax rate: " + str(taxRate)) #Debug

        #Determining Income Tax
        incomeTax = taxableIncome * taxRate
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))
        
    elif (taxableIncome >= 9952  and  taxableIncome <= 40526):
        taxRate = .12
        #print("Tax rate: " + str(taxRate)) #Debug

        #Determining Income Tax
        taxBasket1 = 9951 * .10
        taxBasket2 = (taxableIncome - 9951) * taxRate
        incomeTax = taxBasket1 + taxBasket2
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))
        
    elif (taxableIncome >= 40527  and  taxableIncome <= 86376):
        taxRate = .22
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 9951 * .10
        taxBasket2 = (40526 - 9951) * 0.12
        taxBasket3 = (taxableIncome - 40526) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))

    elif (taxableIncome >= 86377  and  taxableIncome <= 164926):
        taxRate = .24
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 9951 * .10
        taxBasket2 = (40526 - 9951) * 0.12
        taxBasket3 = (86376 - 40526) * 0.22
        taxBasket4 = (taxableIncome - 86376) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3 + taxBasket4
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))
        
    elif (taxableIncome >= 164927  and  taxableIncome <= 209426):
        taxRate = .32
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 9951 * .10
        taxBasket2 = (40526 - 9951) * 0.12
        taxBasket3 = (86376 - 40526) * 0.22
        taxBasket4 = (164926 - 86376) * 0.24
        taxBasket5 = (taxableIncome - 164926) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3 + taxBasket4 + taxBasket5
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))

    elif (taxableIncome >= 209427  and  taxableIncome <= 523601):
        taxRate = .35
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 9951 * .10
        taxBasket2 = (40526 - 9951) * 0.12
        taxBasket3 = (86376 - 40526) * 0.22
        taxBasket4 = (164926 - 86376) * 0.24
        taxBasket5 = (209426 - 164926) * 0.32
        taxBasket6 = (taxableIncome - 209426) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3 + taxBasket4 + taxBasket5 + taxBasket6
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))

    elif (taxableIncome >= 523602):
        taxRate = .37
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 9951 * .10
        taxBasket2 = (40526 - 9951) * 0.12
        taxBasket3 = (86376 - 40526) * 0.22
        taxBasket4 = (164926 - 86376) * 0.24
        taxBasket5 = (209426 - 164926) * 0.32
        taxBasket6 = (523601 - 209426) * 0.35
        taxBasket7 = (taxableIncome - 523601) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3 + taxBasket4 + taxBasket5 + taxBasket6 + taxBasket7
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))  


elif filingStatus == 1:

    #print("\nfilingStatus: " + str(filingStatus)) #Debug

    #Determinig Tax Rate
    if (taxableIncome >= 0 and  taxableIncome <= 19901):
        taxRate = .10
        #print("Tax rate: " + str(taxRate)) #Debug

        #Determining Income Tax
        incomeTax = taxableIncome * taxRate
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))
        
    elif (taxableIncome >= 19902  and  taxableIncome <= 81501):
        taxRate = .12
        #print("Tax rate: " + str(taxRate)) #Debug

        #Determining Income Tax
        taxBasket1 = 19901 * .10
        taxBasket2 = (taxableIncome - 19901) * taxRate
        incomeTax = taxBasket1 + taxBasket2
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))
        
    elif (taxableIncome >= 81502  and  taxableIncome <= 172751):
        taxRate = .22
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 19901 * .10
        taxBasket2 = (81501 - 19901) * 0.12
        taxBasket3 = (taxableIncome - 81501) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))

    elif (taxableIncome >= 172752  and  taxableIncome <= 329851):
        taxRate = .24
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 19901 * .10
        taxBasket2 = (81501 - 19901) * 0.12
        taxBasket3 = (172751 - 81501) * 0.22
        taxBasket4 = (taxableIncome - 172751) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3 + taxBasket4
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))
        
    elif (taxableIncome >= 329852  and  taxableIncome <= 418851):
        taxRate = .32
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 19901 * .10
        taxBasket2 = (81501 - 19901) * 0.12
        taxBasket3 = (172751 - 81501) * 0.22
        taxBasket4 = (329851 - 172751) * 0.24
        taxBasket5 = (taxableIncome - 329851) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3 + taxBasket4 + taxBasket5
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))

    elif (taxableIncome >= 418852  and  taxableIncome <= 628301):
        taxRate = .35
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 19901 * .10
        taxBasket2 = (81501 - 19901) * 0.12
        taxBasket3 = (172751 - 81501) * 0.22
        taxBasket4 = (329851 - 172751) * 0.24
        taxBasket5 = (418851 - 329851) * 0.32
        taxBasket6 = (taxableIncome - 418851) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3 + taxBasket4 + taxBasket5 + taxBasket6
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))

    elif (taxableIncome >= 628302):
        taxRate = .37
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 19901 * .10
        taxBasket2 = (81501 - 19901) * 0.12
        taxBasket3 = (172751 - 81501) * 0.22
        taxBasket4 = (329851 - 172751) * 0.24
        taxBasket5 = (418851 - 329851) * 0.32
        taxBasket6 = (628301 - 418851) * 0.35
        taxBasket7 = (taxableIncome - 628301) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3 + taxBasket4 + taxBasket5 + taxBasket6 + taxBasket7
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))


elif filingStatus == 2:

    #print("\nfilingStatus: " + str(filingStatus)) #Debug

    #Determinig Tax Rate
    if (taxableIncome >= 0 and  taxableIncome <= 14201):
        taxRate = .10
        #print("Tax rate: " + str(taxRate)) #Debug

        #Determining Income Tax
        incomeTax = taxableIncome * taxRate
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))
        
    elif (taxableIncome >= 14202  and  taxableIncome <= 54201):
        taxRate = .12
        #print("Tax rate: " + str(taxRate)) #Debug

        #Determining Income Tax
        taxBasket1 = 14201 * .10
        taxBasket2 = (taxableIncome - 14201) * taxRate
        incomeTax = taxBasket1 + taxBasket2
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))
        
    elif (taxableIncome >= 54202  and  taxableIncome <= 86351):
        taxRate = .22
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 14201 * .10
        taxBasket2 = (54201 - 14201) * 0.12
        taxBasket3 = (taxableIncome - 54201) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))

    elif (taxableIncome >= 86352  and  taxableIncome <= 164901):
        taxRate = .24
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 14201 * .10
        taxBasket2 = (54201 - 14201) * 0.12
        taxBasket3 = (86351 - 54201) * 0.22
        taxBasket4 = (taxableIncome - 86351) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3 + taxBasket4
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))
        
    elif (taxableIncome >= 164902  and  taxableIncome <= 209401):
        taxRate = .32
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 14201 * .10
        taxBasket2 = (54201 - 14201) * 0.12
        taxBasket3 = (86351 - 54201) * 0.22
        taxBasket4 = (164901 - 86351) * 0.24
        taxBasket5 = (taxableIncome - 164901) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3 + taxBasket4 + taxBasket5
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))

    elif (taxableIncome >= 209402  and  taxableIncome <= 523601):
        taxRate = .35
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 14201 * .10
        taxBasket2 = (54201 - 14201) * 0.12
        taxBasket3 = (86351 - 54201) * 0.22
        taxBasket4 = (164901 - 86351) * 0.24
        taxBasket5 = (209401 - 164901) * 0.32
        taxBasket6 = (taxableIncome - 209401) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3 + taxBasket4 + taxBasket5 + taxBasket6
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))

    elif (taxableIncome >= 523602):
        taxRate = .37
        #print("Tax rate: " + str(taxRate)) #Debug
        
        #Determining Income Tax
        taxBasket1 = 14201 * .10
        taxBasket2 = (54201 - 14201) * 0.12
        taxBasket3 = (86351 - 54201) * 0.22
        taxBasket4 = (164901 - 86351) * 0.24
        taxBasket5 = (209401 - 164901) * 0.32
        taxBasket6 = (523601 - 209401) * 0.35
        taxBasket7 = (taxableIncome - 523601) * taxRate
        incomeTax = taxBasket1 + taxBasket2 + taxBasket3 + taxBasket4 + taxBasket5 + taxBasket6 + taxBasket7
        print("%s %.2f" % ("Your income tax for 2021 will be: $", float(incomeTax)))


else:
    print("Input error in filing status or income. Processing stopped")
