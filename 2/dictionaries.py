houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}

houses["Hermione"] = "Gryffindor"

print(houses["Harry"])

if houses["Harry"] == houses["Hermione"]:
    print(f"Both in {houses["Harry"]}")
else:
    print("Different houses")