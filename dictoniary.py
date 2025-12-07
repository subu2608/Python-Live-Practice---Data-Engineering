'''
trip={ "Id":"45678",
      "Name":"Subu",
      "pickup point":"tirunelveli",
      "drop point":"UK or Germany",
      "cost":"Hardwork",
      "approx travel time":"83 days",
    "Money making":["Entreprenur","Share Market","Forex Market"]
}


print(trip.get("airport")) #get display as none, even though the key is not available in dictionary
print(trip.keys())
print(trip.values())
'''

#item is method
'''
for key,value in trip.items():
    print(key,":",value)
'''

#update
'''
trip.update({"Money making":["Entreprenur"]})
print(trip)
'''


#pop
'''
trip.pop("Money making")
print(trip)
'''

#filter from list of the values
'''
print(trip["Money making"][2])
'''

'''
for m in trip["Money making"]:
    print(m)
'''

trip={ "45678": {"Id":"45678", "Name":"Subu", "pickup point":"tirunelveli","drop point":"UK or Germany",
      "cost":"Hardwork", "approx travel time":"83 days", "Money making":["Entreprenur","Share Market","Forex Market"]},

        "45679": {"Id":"45679", "Name":"aaru", "pickup point":"chennai", "drop point":"USA","cost":"smart work",
         "approx travel time":"83 days","Money making":["Photography"]}
}
for t, value in trip.items():
    print(t)
    print(value["Name"],"-->", value["drop point"], "-->", value["Money making"])



