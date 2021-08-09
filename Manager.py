runFlag = True

def editStore(store):
    print(store)

def listStores():
    stores = open("/Storelist.txt" , "r")
    print(str(stores))
    stores.close()
    return 0

def addStore(newStore):
    stores = open("/Storelist.txt", "a")
    if(newStore == ""):
        newStore = input("Enter store name:")
    stores.write(newStore)
    stores.write("\n")
    editFlag = input("Add info to the store by editing it, would you like to edit this store now? (Y/N):")
    editFlag = editFlag.lower()
    if(editFlag == 'y' or editFlag == 'yes' or editFlag == 'ye'):
        editStore(newStore)
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
