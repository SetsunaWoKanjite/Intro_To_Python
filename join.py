base = "Cynthia"

list_names=["Cynthia", "cYnthia", "cyNthia", "cynThia", "cyntHia", "cynthIa", "fkjdbjdgjdgdjdjngdjidnjsnjdndgjfhufdbhgdfkbfbkfjb"]
for name in list_names:
    print (name)
    if name.casefold() == base.casefold():
        print ("True")
        print (name.title())
    else:
        print ("False")
    print ("------------")