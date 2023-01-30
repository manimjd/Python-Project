#MOHIT VA MASAHAT
choose1 = input("Mohit or Masahat: ")


#MASAHAT
if choose1.lower() == "masahat":
    choose = input("Enter a shape: ")
    #LOZI
    def lozi():
        if choose.lower() == "lozi":
            GH_koochack = int(input("Enter Ghotr koochack:"))
            GH_bozorg = int(input("Enter Ghotr bozorg:"))
            print((GH_bozorg*GH_koochack)/2)
        else:
            pass
    if choose.lower() == "lozi":
        lozi()
    else:
        pass

    #SQUARE
    def square():
        if choose.lower() == "square":
            z = int(input("Enter zel:"))
            print((z*z))
        else:
            pass
    if choose.lower() == "square":
        square()
    else:
        pass

    #MOSTATIL
    def mostatil():
        if choose.lower() == "mostatil":
            tool = int(input("Enter tool:"))
            arz = int(input("Enter arz:"))
            print((tool*arz))
        else:
            pass
    if choose.lower() == "mostatil":
        mostatil()
    else:
        pass

    #MOSALAS
    def mosalas():
        if choose.lower() == "mosalas":
            ghaede = int(input("Enter Ghaede:"))
            ertefa = int(input("Enter ertefa:"))
            print((ghaede*ertefa)/2)
        else:
            pass
    if choose.lower() == "mosalas":
        mosalas()
    else:
        pass

    #CIRCLE
    def circle():
        if choose.lower() == "circle":
            sh = int(input("Enter shoaa:"))
            print((sh*sh)*3.14)
        else:
            pass
    if choose.lower() == "circle":
        circle()
    else:
        pass

    #MOTAVAZI AL AZLA
    def mot():
        if choose.lower() == "motavazi al azla":
            Ghaede = int(input("Enter Ghaede:"))
            ertefa = int(input("Enter ertefa:"))
            print((Ghaede*ertefa)/2)
        else:
            pass
    if choose.lower() == "motavazi al azla":
        mot()
    else:
        pass

#MOHIT
elif choose1.lower() == "mohit":
    choose = input("Enter a shape: ")
    #LOZI
    def lozi():
        if choose.lower() == "lozi":
            zelb = int(input("Enter zel bozorg:"))
            zelk = int(input("Enter zel koochak:"))
            print((zelb*2)+(zelk*2))
        else:
            pass
    if choose.lower() == "lozi":
        lozi()
    else:
        pass

    #SQUARE
    def square():
        if choose.lower() == "square":
            z = int(input("Enter zel:"))
            print((z*4))
        else:
            pass
    if choose.lower() == "square":
        square()
    else:
        pass

    #MOSTATIL
    def mostatil():
        if choose.lower() == "mostatil":
            zelb = int(input("Enter zelb:"))
            zelk = int(input("Enter zelk:"))
            print(((zelb*2)+(zelk*2)))
        else:
            pass
    if choose.lower() == "mostatil":
        mostatil()
    else:
        pass

    #MOSALAS
    def mosalas():
        if choose.lower() == "mosalas":
            zel = int(input("Enter zel:"))
            print(zel*3)
        else:
            pass
    if choose.lower() == "mosalas":
        mosalas()
    else:
        pass

    #CIRCLE
    def circle():
        if choose.lower() == "circle":
            gh = int(input("Enter ghotr:"))
            print(gh*3.14)
        else:
            pass
    if choose.lower() == "circle":
        circle()
    else:
        pass

    #MOTAVAZI AL AZLA  
    def mot():
        if choose.lower() == "motavazi al azla":
            zelb = int(input("Enter zelb:"))
            zelk = int(input("Enter zelk:"))
            print(((zelb*2)+(zelk*2)))
        else:
            pass
    if choose.lower() == "motavazi al azla":
        mot()
    else:
        pass