import random

lista_hasel = ["CYBERPRZESTRZEŃ", "KAKTUS", "GŁOŚNIK", "BATON", "HERBATA", "MALINY", "PODUSZKA"]
haslo = list(random.choice(lista_hasel))  # list rozbija string na literki
# print(haslo) #sprawdzenie
ilosc_liter = len(haslo)
ilosc_prob = 10

print(f'Hasło ma {ilosc_liter} liter.')
print(f'Masz {ilosc_prob} prób. Powodzenia :)')
haslo_teraz = list('_' * ilosc_liter)  # miejsca na literki hasła
print('HASŁO: ', haslo_teraz)

while ilosc_prob > 0:
    print('*' * 60)
    if ilosc_prob != 10: print('Pozostało prób:', ilosc_prob)
    odp_litera = input("Podaj literę: ").upper()  # zamiana małej litery na dużą (bo takie są w hasłach)
    if not odp_litera: continue  # jeśli był pusty znak - idź do kolejnej iteracji
    ile_razy = 0  # ile razy podana litera występuje w haśle
    miejsce = 0  # numerator miejsca literki w hasle
    if odp_litera not in haslo_teraz:  # jeśli użytkownik jeszcze nie odgadł tej litery
        for litera in haslo:
            if litera == odp_litera:
                haslo_teraz[miejsce] = odp_litera
                ile_razy += 1
            miejsce += 1
        if ile_razy == 0:
            print('Tej litery nie ma w haśle :(')
            ilosc_prob -= 1
        else:
            print(f'Ta litera występuje w haśle {ile_razy} raz(y) ;)')
    else:
        print('Ta litera występuje już w haśle!')
    print('HASŁO:', haslo_teraz)
    if haslo_teraz != haslo:
        czy_zgaduje = input('Czy chcesz spróbować odgadnąć hasło? T/N: ').upper()
        if czy_zgaduje == 'N':
            continue
        elif czy_zgaduje == 'T':
            odp_haslo = input('Podaj hasło: ')
            if odp_haslo.upper() == ''.join(haslo):
                print('*' * 60)
                print(f'Brawo! Hasło to {odp_haslo.upper()}. Gratuluję wygranej!')
                break
            else:
                print('Hasło jest niepoprawne! Straciłeś jedną szansę :(')
                ilosc_prob -= 1
        else:
            print('Nie rozumiem, przechodzę dalej!')
            continue
    else:
        print('*' * 60)
        print('Brawo! Hasło to {}. Gratuluję wygranej!'.format(''.join(haslo_teraz)))
        break

if ilosc_prob == 0 and haslo_teraz != haslo:
    print('*' * 100)
    print('Przykro mi, przegrałeś grę :(')
    print('Haslo to',haslo)
