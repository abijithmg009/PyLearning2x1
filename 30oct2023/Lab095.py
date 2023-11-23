#dict is very close to JSON, which has key and value pair


phone_book = {"Batman": 927394390, "Superman": 8772947398, "Wonder": 2784374899}

print(phone_book)
print(len(phone_book))
#index will not work with dict

print(phone_book["Batman"]) #only key is supported

phone_book2 = dict(Batman = 123, Cersi=1224, GB=213)
print(phone_book2)
print(phone_book2["GB"])
print(phone_book2.get("GB"))


new_dect = dict(name="Pramod", age = 34, isMale= True, Address = "KA")
new_dect2 = {"name":"Pramod", "age" :34, "isMale": True, "Address" : "KA"}

print(new_dect["age"])
print(new_dect["isMale"])
print(new_dect2[90])