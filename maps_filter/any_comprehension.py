from data import people, plants_dict, plants_list

# if all(person[1] for person in people):
#     print("Sending e-mail")
# else:
#     print("user does not have email address")

if bool(people) and all(person[1] for person in people):
    print("Sending e-mail")
else:
    print("user does not have email address")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("has grass")
else:
    print("no grass")


if any(val.plant_type == "Grass" for val in plants_dict.values()):
    print("has grass!")
else:
    print("no grass!")
