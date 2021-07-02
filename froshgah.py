mojodi_kala = ["kabl", "fiuz"]
gaymat_cala = {"kabl": 55000, "fiuz": 150000}
tedad_kala = {"kabl": 1000, "fiuz": 500}
vahed_andaze_giri_cala = {"kabl": "matri", "fiuz": "addai"}
vahed_andaze_giri_cala__1 = {"kabl": "matr kabl", "fiuz": "add fiuz"}
bale_khayr = ["bale", "khayr"]

while True:
    print("list kala hay mojod: kabl, fiuz")
    kala = input("Be Froshgah alactronik khosh amadid . mahsol khod ra antakhab knid: ").lower()
    if kala in mojodi_kala:
        if kala in "kabl":
            print(f"{tedad_kala[kala]} matr mojod ast")
        elif kala in "fiuz":
            print(f"{tedad_kala[kala]} add mojod ast")
        while True:
            gaymat = input("gaymat ra mikhahid bale / khayr?: ").lower()
            if gaymat in bale_khayr[0]:
                print(f"gaymat kala {vahed_andaze_giri_cala[kala]} {gaymat_cala[kala]} toman")
                while True:
                    kharid_kala = input("aya mahsol ra kharid mikonid bale / khayr?: ").lower()
                    if kharid_kala in bale_khayr[0]:
                        tedad = int(input(f"chand {vahed_andaze_giri_cala__1[kala]} mikhahid?: "))
                        tedad_kharid = tedad * gaymat_cala[kala]
                        print(f"sorat hesab shoma mishavad {tedad_kharid}")
                        while True:
                            shomare_kart = str(int(input("shomare cart ra vard knid: ")))
                            tedad_shomare_cart = 0
                            for tedad_shomare_cart__1 in shomare_kart:
                                tedad_shomare_cart = tedad_shomare_cart + 1
                            if tedad_shomare_cart == 16:
                                adres = input("adres ra vard knid: ")
                                print(f"mahsol shoma be adres {adres} frestade shod")
                                print("az kharid shoma mamnonim")
                                break
                            elif tedad_shomare_cart > 16:
                                print("shomare cart bishtar az 16 ast!.lotfan dobare amthan knid!!!")
                            elif tedad_shomare_cart < 16:
                                print("shomare cart kamtar az 16 ast!.lotfan dobare amthan knid!!!")
                        break
                    elif kharid_kala in bale_khayr[1]:
                        print("salamati ra baraytan arzo miknim")
                        break
                    else:
                        print("lotfan bale ya khayr ra antekhab knid")
                break
            elif gaymat in bale_khayr[1]:
                print("salamati ra baraytan arzo miknim")
                break
            else:
                print("lotfan bale ya khayr ra antekhab knid")
        break
    else:
        print("lotoan kalay dr lest ra antekhab knid")



