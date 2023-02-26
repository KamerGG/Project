
tahta = [[" "," "," "],[" "," "," "],[" "," "," "]]
sıra = 0

def tahta_yazdır():
    print(f" {tahta[0][0]} | {tahta[0][1]} | {tahta[0][2]} ")
    print("--------------")
    print(f" {tahta[1][0]} | {tahta[1][1]} | {tahta[1][2]} ")
    print("--------------")
    print(f" {tahta[2][0]} | {tahta[2][1]} | {tahta[2][2]} ")
    print("--------------")
def halme_al():

    global sıra
    satır = int(input("Satır Numarası"))
    sutun = int(input("Sutun Numarası"))
    if tahta[satır][sutun] != " ":
        print("Bu kutu dolu lütfen başka bir kutu seçin")
        return halme_al()
    if sıra == 0:
        tahta[satır][sutun] = "X"
        sıra = 1
    else:
        tahta[satır][sutun] = "O"
        sıra = 0
def oyun():
    tahta_yazdır()
    halme_al()
    if tahta[0][0] and tahta[0][1] and tahta[0][2] == "X" :
        if sıra == 0:
            print("Kazanan 1. Oyuncu")
            tahta_yazdır()
            return 0
        else:
            print("Kazanan 2. Oyuncu")
            tahta_yazdır()
            return 0
    if tahta[1][0] and tahta[1][1] and tahta[1][2] == "X" :
        if sıra == 0:
            print("Kazanan 1. Oyuncu")
            tahta_yazdır()
            return 0
        else:
            print("Kazanan 2. Oyuncu")
            tahta_yazdır()
            return 0
    if tahta[2][0] and tahta[2][1] and tahta[2][2] == "X" :
        if sıra == 0:
            print("Kazanan 1. Oyuncu")
            tahta_yazdır()
            return 0
        else:
            print("Kazanan 2. Oyuncu")
            tahta_yazdır()
            return 0
    if tahta[0][0] and tahta[1][1] and tahta[2][2] == "X" :
        if sıra == 0:
            print("Kazanan 1. Oyuncu")
            tahta_yazdır()
            return 0
        else:
            print("Kazanan 2. Oyuncu")
            tahta_yazdır()
            return 0 
    if tahta[0][2] and tahta[1][1] and tahta[2][0] == "X" :
        if sıra == 0:
            print("Kazanan 1. Oyuncu")
            tahta_yazdır()
            return 0
        else:
            print("Kazanan 2. Oyuncu")
            tahta_yazdır()
            return 0
    return oyun()
print(oyun())