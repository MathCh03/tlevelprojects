fashiondict = {
        "Item1" : {
        "Brand" : "Moncler",
        "Type" : "Coat",
        "Colour" : "Black"
        },
        "Item2" : {
        "Brand" : "Evisu",
        "Type" : "Jeans",
        "Colour" : "Navy"
        },
        "Item3" : {
        "Brand" : "Alexander McQueen",
        "Type" : "Shoes",
        "Colour" : "White"
        }
        }

repeat=False

while True:
    welcome = (input("Hello, welcome to your fashion shopping cart! \nPlease select 1 to see your cart, or 2 to add to your cart: "))
    print(welcome)

    if welcome=="1":
        print(fashiondict)

    add1 = input("What brand is the item you wish to add: ")
    add2 = input("What type of clothing do you wish to add: ")
    add3 = input("What Colour is the type of clothing you wish to add: ")
    add4 = add1+add2+add3

    if welcome=="2":
        print(add4)
        newdict = {
            "NewItem" : {
            "Brand" : add1,
            "Type" : add2,
            "Colour" : add3
            }
            }
            #fashiondict.update(newdict)
            #fashiondict["New Item"]=NewItem
           # fashiondict["New Item"] = NewItem
    fd2dict = dict(newdict)
    fashiondict.update(fd2dict)
    print(fashiondict)
    dict.clear(newdict)
            

    again=input("Would you like to add something else to your cart? ")
    if again=="Yes" or again=="yes":
        repeat=True
            
    else:
        break;




       # fashiondict["NewItem"] =

        #    "NewItem" : {
         #   "Brand" : add1,
         #   "Type" : add2,
        #    "Colour" : add3
        #        }
            
