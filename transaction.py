import webbrowser
import os
from collections import Counter

record = open("transaction.txt", "r")
data = record.readline()
count=0


while data: 
    if count==0:
        count = 1
        title = data.split(',')
        for i in range(0,len(title)):
            title[i] = list();   # title[0] = date, title[1]=mobile, title[2]=name, title[3]=bill
    else :
        data=data.split(',')
        for i in range(0, len(data)):
            title[i].append(data[i])
    data=record.readline()     
record.close()

def CountOfCustomers():
    name = Counter(title[2])   # all customers with their frequancy
    for (key, value) in name.items():
        if value<5:
            CountList[value]+=1
        else :
            CountList[5]+=1
            
while True:
    CountList = [0,0,0,0,0,0]
    print ("------------------------*****------------------------")
    n = input("\nENTER YOUR INPUT \n1: count\n2: Total Amount\n3: single ordered customer\n4: Get a distribution of Customers\n5: Table & bar graph(Data on HTML page)\n6: Exit\n")
    if n == '1' :
        print ("NO. OF ORDER :" + str(len(title[1])))
    elif n=='2':
        total=0
        for i in range(0,len(title[3])):
            title[3][i]=int(title[3][i])
            total+=title[3][i]
        print ("TOTAL AMOUNT OF ORDER: " + str(total))
    elif n=='3':
        name = Counter(title[2])   # all customers with their frequancy
        OneTimeUser = list();
        #print(counts)
        print ("Single Ordered Customers: ")
        for (key, value) in name.items():
            if value==1:
                print(key)
                OneTimeUser.append(key)
                
    elif n=='4':
        CountOfCustomers()
        print("Orders  | Count Of Customers")
        print("----------------------------")
        for i in range(1,6):
            if i!=5:
                print(str(i)+"       |   " + str(CountList[i]))
            else :
                print(str(i)+"+      |   " + str(CountList[i]))
                

    elif n=='5':
        CountOfCustomers()
        no_Order=0
        for i in range(0,6):
            no_Order+=CountList[i]
        single=int(100*CountList[1]/no_Order)
        double=int(100*CountList[2]/no_Order)
        triple=int(100*CountList[3]/no_Order)
        four=int(100*CountList[4]/no_Order)
        fifth=int(100*CountList[5]/no_Order)
        temporary_file = open("temporary.html").read().format(CountList_1=str(CountList[1]),CountList_2=str(CountList[2]),
                                                   CountList_3=str(CountList[3]),CountList_4=str(CountList[4]),CountList_5=str(CountList[5]),
                                                   first=str(single)+'%',second=str(double)+'%',third=str(triple)+'%',forth=str(four)+'%',fifth=str(fifth)+'%')
        with open('index.html','w') as f:
            f.write(temporary_file)
            f.close()
        filename='C:/Users/Bhoopesh/Pictures/Desktop/Assinment/index.html'
        webbrowser.open_new_tab('.')   #please open index.html
        
    elif n=='6':
        break














