room1 = {
    "room1": {
        "name": "name",
        "description": "description",
        "loot": [],
        "actions": [],
        "enemy": "enemy name"
    }



while True:
    print("Room name?")

    name = input()

    if name in room1:
        print(room1[name] + " is the name of the " + name)

    else:

        print("room" + name + "doesn't exist, enter another" )

        room = input()

        room1[name] = room


        print("updated")






 
















"""# one level access
for room in rooms:
    print(room.get("room1", "that room does not exist"))"""


"""class DictQuery(dict):
    def get(self,path, default=None):
        keys = path.split("/")
        val = None

        for key in keys:
            if val:
                if isinstance(val,list):
                    val = [v.get(key, default) if v else None for v in val]
                else:
                    val = val.get(key, default)
            else:
                val = dict.get(self,key,default)

            if not val:
                break

        return val"""












#for r_id,r_info in rooms.items():
 #   print("\nKey:", r_id)

  #  for key in r_info:
   #     print(key + ":", r_info[key])

#print(rooms["room1"]["name"])
#print(list(rooms.keys()))
#print("Value: %s" % rooms.get("room1"))
