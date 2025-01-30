#creation of nested dictionary of myself
person = {
    "name": "Srijita",
    "age": 18,
    "address": {
        "Home": "Adelphia Girl's hostel",
        "city": "Dehradun",
        "state": "Uttarakhand",
        
    },
    "contact": {
        "phone": "9339262802",
        "email": "srijitadebnath304@gmail.com"
    }
}

print(person["name"])  
print(person["address"]["Home"])  
print(person["contact"]["phone"])  
person["age"] = 18
person["address"]["city"] = "Dehradun"

person[" occupation"] = "Software Engineer"
person["address"]["country"] = "India"

print(person)
print(person["address"]["city"])

#nested dictionary of a employee
employee = {
    "name" :"Jako",
    "age": 25,
    "salary":"21LPA",
    "address": {
        "city": "hyderabad",
        "state":"Telangana",
        },
    "contact":{
        "phone no": "8942639239",
        "email id":"jakonicole674@yahoo.com"
        }
    }

address ={
    "work_address":{
        "city":"hyderabad",
        "state":"Telangana"
        },
    "home_address":{
    "city":"Kolkata",
    "state":"West Bengal"
    }}

    
print(employee["name"])  
print(employee["address"]["city"])
print(address["work_address"]["city"])
print(address["home_address"]["city"])      
print(employee["contact"]["phone no"])
employee["age"] = 25
employee["state"]="Telangana"

employee[" occupation"] = "Software Engineer"
employee["address"]["country"] = "India"


print(employee)

    
        
    

