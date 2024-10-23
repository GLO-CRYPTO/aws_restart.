#importing modules
import csv
import copy
#defining the dictionary
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
#iterating my dictionary
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
#defining a list of my car inventory
    
myInventoryList = []

with open('car_fleet.csv') as csvFile:#open csv file for reading
    csvReader = csv.reader(csvFile, delimiter=',')  
    #create csv reader object to read file
    lineCount = 0  
    
    
    for row in csvReader:#iterate each row in csv file
        if lineCount == 0:#check if it is the first row header
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
           #create a deep copy dic
            currentVehicle = copy.deepcopy(myVehicle) 
            #assign values from csv row to corresponding keys in dictionary
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            #add populated dictionary to inventory list
            lineCount += 1  
    print(f'Processed {lineCount} lines.')#read and copy data from csv file

    currentVehicle = copy.deepcopy(myVehicle)
   
   
    for myCarProperties in myInventoryList:#iterate over each car in the inventory list
             for key, value in myCarProperties.items():#iterate over each key-value pair in the dictionary
                    print("{} : {}".format(key,value))#print each key and its corresponding value
             print("-----")#prints a separator between cars
                                     
                                     
                                     
    
    
