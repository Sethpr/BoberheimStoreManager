import time
runFlag = True

def editStore(store):
    print(store)

def listStores():
    file = open("Storelist.txt" , "r")
    stores = file.read()
    print(stores)
    file.close()
    time.sleep(2)
    return 0

def addStore(newStore):
    stores = open("Storelist.txt", "a")
    if(newStore == ""):
        newStore = input("Enter store name:")
    print(newStore)
    stores.write(newStore)
    stores.write("\n")
    editFlag = input("Add info to the store by editing it, would you like to edit this store now? (Y/N):")
    editFlag = editFlag.lower()
    if(editFlag == 'y' or editFlag == 'yes' or editFlag == 'ye'):
        editStore(newStore)
    stores.close()
    storePage = open("Stores/" + newStore + ".txt", 'w')
    storePage.write("Owner: \n#\nProducts: \n#\n")
    return 0





while(runFlag):
    print("Welcome to the Boberheim Markets")
    print("Enter what you want to do:")
    print("1: List stores")
    print("2: Go to a store")
    print("3: Add a store")
    print("4: Edit a store")
    print("Q: Quit")
    response = input(">>>")

    if(response[0] == '1'):
        listStores()

    elif(response[0] == '2'):
        print("you didn't wite this yet")

    elif(response[0] == '3'):
        if(response[0] == response):
            addStore("")
        else:
            addStore(response.split(" ", 1)[1])
    elif(response[0] == '4'):
        print("you didn't wite this yet")

    elif(response[0] == 'Q' or response[0] == 'q'):
        runFlag = False




print("Bye")