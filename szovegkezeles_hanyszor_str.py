def szovegek1():
    szoveg = input("Kérem, adjon meg egy szöveget: \n\t").lower()
    keresettSz = input("Kérem, adja meg a keresett szöveget: \n\t").lower()
    talaltDb = 0
    keresettHossza = len(keresettSz)
    print(len(szoveg))
    if szoveg.__contains__(keresettSz):
        for i in range(0, len(szoveg)):
            # print(szoveg[i], end=" ")
            if szoveg[i] == keresettSz[0]:
                j = 0
                n = i
                talalt = False
                while szoveg[n] == keresettSz[j] and not talalt:
                    if j+1 == keresettHossza:
                        talaltDb += 1
                        talalt = True
                    else:
                        j += 1
                        n += 1
                    # print(j, end=" ")

    return f"\n'{keresettSz}' {talaltDb} alkalommal jelenik meg a szövegben."


print(szovegek1())
