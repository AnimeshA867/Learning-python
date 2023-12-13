data=[]

for i in range (0,5):
    dataValue={"Country":"","Capital":""}
    dataValue["Country"]=str(input("Enter the country Name:"))
    dataValue["Capital"]=str(input("Enter the Capital Name:"))
    data.append(dataValue)
search=str(input("Enter the country name to find the capital:"))
found=0;
index=0;
for i in data:
    if(i["Country"]==search):
        found=1
        index=data.index(i);

if(found):

    print("Country: %s\nCapital: %s "%(data[index]["Country"], data[index]["Capital"]))

else:
    print("Country name doesn't match with one entered above.");