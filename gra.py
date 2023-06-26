import random
import pygame


#Konfiguracja
pygame.init()
ekran = pygame.display.set_mode([600, 800])
pygame.display.set_caption("Kośći - Rozgrywka")
czcionka = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()
fps = 60

#Dane początkowe
rzut = False
liczby = [0, 0, 0, 0, 0]
wybrane = [False, False, False, False, False]
naciśnięto = False
rysuj_naciśnięte = 30
count = 110
pozostało_rzutów = 3
wyniki = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
wybór = [False, False, False, False, False, False, False, False, False, False, False, False, False]
wykonano = [False, False, False, False, False, False, False, False, False, False, False, False, False]
możliwe = [False, False, False, False, False, False, False, False, False, False, False, False, False]
suma = [0, 0, 0, 0, 0, 0, 0]
coś_wybranego = False
dodatkowy_czas = False
koniec_gry = False
największy_wynik = 0
wynik = 0
restart = ''

#klasy
class Wybór:
    def __init__(self, pozycja_x, pozycja_y, text, select, możliwości, wykonane, mój_wynik):
        self.pozycja_x = pozycja_x
        self.pozycja_y = pozycja_y
        self.text = text
        self.wybrane = select
        self.możliwe = możliwości
        self.wykonano = wykonane
        self.wynik = mój_wynik

    def rysuj(self):
        pygame.draw.line(ekran, (0, 0, 0), (self.pozycja_x, self.pozycja_y + 31), (self.pozycja_x + 225, self.pozycja_y + 31), 2)
        name_tekst = ''
        if not self.wykonano:
            if self.możliwe:
                name_tekst = czcionka.render(self.text, True, (34, 140, 34))
            elif not self.możliwe:
                name_tekst = czcionka.render(self.text, True, (255, 0, 0))
        else:
            name_tekst = czcionka.render(self.text, True, (0, 0, 0))
        if self.wybrane:
            pygame.draw.rect(ekran, (20, 35, 30), [self.pozycja_x, self.pozycja_y + 2, 155, 30])
        ekran.blit(name_tekst, (self.pozycja_x + 5, self.pozycja_y + 10))
        wynik_tekst = czcionka.render(str(self.wynik), True, (0, 0, 255))
        ekran.blit(wynik_tekst, (self.pozycja_x + 165, self.pozycja_y + 10))


class Kosci:
    def __init__(self, pozycja_x, pozycja_y, num, key):
        self.pozycja_x = pozycja_x
        self.pozycja_y = pozycja_y
        self.numer = num
        global wybrane
        self.key = key
        self.active = wybrane[self.key]
        self.kość = ''

    def rysuj(self):
        self.kość = pygame.draw.rect(ekran, (148, 11, 6), [self.pozycja_x, self.pozycja_y, 100, 100], 0, 5)
        if self.numer == 1:
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 50, self.pozycja_y + 50), 10)
        if self.numer == 2:
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 20, self.pozycja_y + 20), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 80, self.pozycja_y + 80), 10)
        if self.numer == 3:
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 50, self.pozycja_y + 50), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 20, self.pozycja_y + 20), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 80, self.pozycja_y + 80), 10)
        if self.numer == 4:
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 20, self.pozycja_y + 20), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 80, self.pozycja_y + 80), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 20, self.pozycja_y + 80), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 80, self.pozycja_y + 20), 10)
        if self.numer == 5:
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 50, self.pozycja_y + 50), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 20, self.pozycja_y + 20), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 80, self.pozycja_y + 80), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 20, self.pozycja_y + 80), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 80, self.pozycja_y + 20), 10)
        if self.numer == 6:
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 20, self.pozycja_y + 50), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 80, self.pozycja_y + 50), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 20, self.pozycja_y + 20), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 80, self.pozycja_y + 80), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 20, self.pozycja_y + 80), 10)
            pygame.draw.circle(ekran, (255, 255, 255), (self.pozycja_x + 80, self.pozycja_y + 20), 10)
        if self.active:
            pygame.draw.rect(ekran, (255, 0, 0), [self.pozycja_x, self.pozycja_y, 100, 100], 4, 5)

    def sprawdź_naciśnięcie(self, coordinates):
        if self.kość.collidepoint(coordinates):
            if wybrane[self.key]:
                wybrane[self.key] = False
            elif not wybrane[self.key]:
                wybrane[self.key] = True


def od_nowa():
    global rzut
    global liczby
    global wybrane
    global naciśnięto
    global pozostało_rzutów
    global wyniki
    global wybór
    global wykonano
    global możliwe
    global suma
    global coś_wybranego
    global wynik
    rzut = False
    liczby = [0, 0, 0, 0, 0]
    wybrane = [False, False, False, False, False]
    naciśnięto = False
    pozostało_rzutów = 3
    wyniki = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    wybór = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    wykonano = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    możliwe = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    suma = [0, 0, 0, 0, 0, 0, 0]
    coś_wybranego = False
    wynik = 0



def dokonaj_wyboru(num, moja_lista, wykonano_list):
    for index in range(len(moja_lista)):
        moja_lista[index] = False
    if not wykonano_list[num]:
        moja_lista[num] = True
    return moja_lista


def rysowanie_elementów():
    global koniec_gry
    global wynik_gry
    rzut_tekst = czcionka.render('Rzut kośćmi', True, (255, 255, 255))
    ekran.blit(rzut_tekst, (80, 165))
    accept_tekst = czcionka.render('Zakończ rundę', True, (255, 255, 255))
    ekran.blit(accept_tekst, (390, 165))
    turns_tekst = czcionka.render('Dostępne rzuty kośćmi: ' + str(pozostało_rzutów), True, (255, 255, 255))
    ekran.blit(turns_tekst, (15, 15))
    but_tekst = czcionka.render('Wybrane kości nie są przerzucane', True, (255, 255, 255))
    ekran.blit(but_tekst, (280, 15))
    pygame.draw.rect(ekran, (255, 255, 255), [0, 200, 225, 800 - 200])
    pygame.draw.line(ekran, (0, 0, 0), (0, 40), (600, 40), 3)
    pygame.draw.line(ekran, (0, 0, 0), (0, 200), (600, 200), 3)
    pygame.draw.line(ekran, (0, 0, 0), (600, 0), (600, 200), 3)
    pygame.draw.line(ekran, (0, 0, 0), (250, 0), (250, 40), 3)
    pygame.draw.line(ekran, (0, 0, 0), (155, 200), (155, 800), 3)
    pygame.draw.line(ekran, (0, 0, 0), (225, 200), (225, 800), 3)
    if koniec_gry:
        over_tekst = czcionka.render('Koniec gry', True, (255, 255, 255))
        ekran.blit(over_tekst, (280, 280))
    wynik_tekst = czcionka.render('Aktualny wynik: ' + str(wynik_gry), True, (255, 255, 255))
    ekran.blit(wynik_tekst, (280, 340))
    największy_wynik_tekst = czcionka.render('Największy Wynik: ' + str(największy_wynik), True, (255, 255, 255))
    ekran.blit(największy_wynik_tekst, (280, 370))


def rysuj_kości():
    kość1.rysuj()
    kość2.rysuj()
    kość3.rysuj()
    kość4.rysuj()
    kość5.rysuj()


def rysuj_konfiguracje():
    jedynki.rysuj()
    dwójki.rysuj()
    trójki.rysuj()
    czwórki.rysuj()
    piątki.rysuj()
    szóstki.rysuj()
    trzy_j.rysuj()
    cztery_j.rysuj()
    full.rysuj()
    m_strit.rysuj()
    d_strit.rysuj()
    generał.rysuj()
    szansa.rysuj()
    łączny_wynik1.rysuj()
    bonus_jeden_sześć.rysuj()
    łączny_wynik2.rysuj()
    łączny_wynik.rysuj()
    łącznie_jeden_sześć.rysuj()
    całkowity_wynik.rysuj()
    bonus.rysuj()


def sprawdź_możliwośći(lista_pozycji, nums):
    lista_pozycji[0] = True
    lista_pozycji[1] = True
    lista_pozycji[2] = True
    lista_pozycji[3] = True
    lista_pozycji[4] = True
    lista_pozycji[5] = True
    lista_pozycji[12] = True
    max_count = 0

    for index in range(1, 7):
        if nums.count(index + 1) > max_count:
            max_count = nums.count(index + 1)
    if max_count >= 3:
        lista_pozycji[6] = True
        if max_count >= 4:
            lista_pozycji[7] = True
            if max_count >= 5:
                lista_pozycji[11] = True
    if max_count < 3:
        lista_pozycji[6] = False
        lista_pozycji[7] = False
        lista_pozycji[8] = False
        lista_pozycji[11] = False
    elif max_count == 3:
        lista_pozycji[7] = False
        lista_pozycji[11] = False
        sprawdzanie = False
        for index in range(len(nums)):
            if nums.count(nums[index]) == 2:
                lista_pozycji[8] = True
                sprawdzanie = True
        if not sprawdzanie:
            lista_pozycji[8] = False
    elif max_count == 4:
        lista_pozycji[11] = False

    lowest = 10
    highest = 0
    for index in range(len(nums)):
        if nums[index] < lowest:
            lowest = nums[index]
        if nums[index] > highest:
            highest = nums[index]

    if lowest + 1 in nums and lowest + 2 in nums and lowest + 3 in nums and lowest + 4 in nums:
        lista_pozycji[10] = True
    else:
        lista_pozycji[10] = False
    if (lowest + 1 in nums and lowest + 2 in nums and lowest + 3 in nums) or (
            highest - 1 in nums and highest - 2 in nums and highest - 3 in nums):
        lista_pozycji[9] = True
    else:
        lista_pozycji[9] = False
    return lista_pozycji


def sprawdź_wyniki(lista_wybranych, lista_numerów, lista_możliwości, punkty):
    active = 0
    for index in range(len(lista_wybranych)):
        if lista_wybranych[index]:
            active = index
    if active == 0:
        punkty = lista_numerów.count(1)
    elif active == 1:
        punkty = lista_numerów.count(2) * 2
    elif active == 2:
        punkty = lista_numerów.count(3) * 3
    elif active == 3:
        punkty = lista_numerów.count(4) * 4
    elif active == 4:
        punkty = lista_numerów.count(5) * 5
    elif active == 5:
        punkty = lista_numerów.count(6) * 6
    elif active == 6 or active == 7:
        if lista_możliwości[active]:
            punkty = sum(lista_numerów)
        else:
            punkty = 0
    elif active == 8:
        if lista_możliwości[active]:
            punkty = 25
        else:
            punkty = 0
    elif active == 9:
        if lista_możliwości[active]:
            punkty = 30
        else:
            punkty = 0
    elif active == 10:
        if lista_możliwości[active]:
            punkty = 40
        else:
            punkty = 0
    elif active == 11:
        if lista_możliwości[active]:
            punkty = 50
        else:
            punkty = 0
    elif active == 12:
        punkty = sum(lista_numerów)
    return punkty


def sprawdź_sumę(suma_łącznie, lista_wyników, mój_bonus):
    suma_łącznie[0] = lista_wyników[0] + lista_wyników[1] + lista_wyników[2] + lista_wyników[3] + lista_wyników[4] + lista_wyników[5]
    if suma_łącznie[0] >= 63:
        suma_łącznie[1] = 35
    else:
        suma_łącznie[1] = 0
    suma_łącznie[2] = suma_łącznie[0] + suma_łącznie[1]

    suma_łącznie[4] = lista_wyników[6] + lista_wyników[7] + lista_wyników[8] + lista_wyników[9] + lista_wyników[10] + \
        lista_wyników[11] + lista_wyników[12]
    suma_łącznie[5] = suma_łącznie[2]
    suma_łącznie[6] = suma_łącznie[4] + suma_łącznie[5]
    if mój_bonus:
        suma_łącznie[3] += 100
        mój_bonus = False
    return suma_łącznie, mój_bonus

#Rozgrywka
rozgrywka = True
while rozgrywka:
    timer.tick(fps)
    ekran.fill((0, 105, 3))
    przycisk1 = pygame.draw.rect(ekran, (148, 11, 6), [10, 160, 280, 30])
    przycisk2 = pygame.draw.rect(ekran, (148, 11, 6), [310, 160, 280, 30])
    if koniec_gry:
        restart = pygame.draw.rect(ekran, (0, 0, 0), [277, 272, 300, 30])
    kość1 = Kosci(10, 50, liczby[0], 0)
    kość2 = Kosci(130, 50, liczby[1], 1)
    kość3 = Kosci(250, 50, liczby[2], 2)
    kość4 = Kosci(370, 50, liczby[3], 3)
    kość5 = Kosci(490, 50, liczby[4], 4)
    jedynki = Wybór(0, 200, 'Jedynki', wybór[0], możliwe[0], wykonano[0], wyniki[0])
    dwójki = Wybór(0, 230, 'Dwójki', wybór[1], możliwe[1], wykonano[1], wyniki[1])
    trójki = Wybór(0, 260, 'Trójki', wybór[2], możliwe[2], wykonano[2], wyniki[2])
    czwórki = Wybór(0, 290, 'Czwórki', wybór[3], możliwe[3], wykonano[3], wyniki[3])
    piątki = Wybór(0, 320, 'Piątki', wybór[4], możliwe[4], wykonano[4], wyniki[4])
    szóstki = Wybór(0, 350, 'Szóstki', wybór[5], możliwe[5], wykonano[5], wyniki[5])
    łączny_wynik1 = Wybór(0, 380, '1 - 6 Łącznie', False, False, True, suma[0])
    bonus_jeden_sześć = Wybór(0, 410, 'Bonus', False, False, True, suma[1])
    łączny_wynik2 = Wybór(0, 440, '1 - 6 + bonus', False, False, True, suma[2])
    trzy_j = Wybór(0, 470, '3 jednakowe', wybór[6], możliwe[6], wykonano[6], wyniki[6])
    cztery_j = Wybór(0, 500, '4 jednakowe', wybór[7], możliwe[7], wykonano[7], wyniki[7])
    full = Wybór(00, 530, 'Full (3 na 2)', wybór[8], możliwe[8], wykonano[8], wyniki[8])
    m_strit = Wybór(0, 560, 'Mały strit', wybór[9], możliwe[9], wykonano[9], wyniki[9])
    d_strit = Wybór(0, 590, 'Duży strit', wybór[10], możliwe[10], wykonano[10], wyniki[10])
    generał = Wybór(0, 620, 'Generał', wybór[11], możliwe[11], wykonano[11], wyniki[11])
    szansa = Wybór(0, 650, 'Szansa', wybór[12], możliwe[12], wykonano[12], wyniki[12])
    bonus = Wybór(0, 680, 'Bonus', False, False, True, suma[3])
    łączny_wynik = Wybór(0, 710, 'Suma: specjalne', False, False, True, suma[4])
    łącznie_jeden_sześć = Wybór(0, 740, 'Suma: 1 - 6', False, False, True, suma[5])
    całkowity_wynik = Wybór(0, 770, 'Całkowity wynik', False, False, True, suma[6])
    wynik_gry = suma[6]
    rysowanie_elementów()
    rysuj_kości()
    rysuj_konfiguracje()
    możliwe = sprawdź_możliwośći(możliwe, liczby)
    wynik = sprawdź_wyniki(wybór, liczby, możliwe, wynik)
    suma, dodatkowy_czas = sprawdź_sumę(suma, wyniki, dodatkowy_czas)

    if rysuj_naciśnięte < 30:
        obrys_przycisku = pygame.draw.rect(ekran, (0, 0, 0), [10, 160, 280, 30], 4)
        rysuj_naciśnięte += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rozgrywka = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if koniec_gry and restart.collidepoint(event.pos):
                od_nowa()
                koniec_gry = False
            kość1.sprawdź_naciśnięcie(event.pos)
            kość2.sprawdź_naciśnięcie(event.pos)
            kość3.sprawdź_naciśnięcie(event.pos)
            kość4.sprawdź_naciśnięcie(event.pos)
            kość5.sprawdź_naciśnięcie(event.pos)
            if przycisk1.collidepoint(event.pos) and pozostało_rzutów > 0:
                rzut = True
                pozostało_rzutów -= 1
                rysuj_naciśnięte = 0
            if przycisk2.collidepoint(event.pos) and coś_wybranego and pozostało_rzutów < 3:
                if wyniki[11] == 50 and wykonano[11] and możliwe[11]:
                    dodatkowy_czas = True
                for i in range(len(wybór)):
                    if wybór[i]:
                        wykonano[i] = True
                        wyniki[i] = wynik
                        wybór[i] = False
                for i in range(len(wybrane)):
                    wybrane[i] = False
                pozostało_rzutów = 3
                liczby = [0, 0, 0, 0, 0]
                coś_wybranego = False
            if 0 <= event.pos[0] <= 155:
                if 200 < event.pos[1] < 381 or 470 < event.pos[1] < 681:
                    if 200 < event.pos[1] < 230:
                        naciśnięto = 0
                    elif 230 < event.pos[1] < 260:
                        naciśnięto = 1
                    elif 260 < event.pos[1] < 290:
                        naciśnięto = 2
                    elif 290 < event.pos[1] < 320:
                        naciśnięto = 3
                    elif 320 < event.pos[1] < 350:
                        naciśnięto = 4
                    elif 350 < event.pos[1] < 380:
                        naciśnięto = 5
                    elif 470 < event.pos[1] < 500:
                        naciśnięto = 6
                    elif 500 < event.pos[1] < 530:
                        naciśnięto = 7
                    elif 530 < event.pos[1] < 560:
                        naciśnięto = 8
                    elif 560 < event.pos[1] < 590:
                        naciśnięto = 9
                    elif 590 < event.pos[1] < 620:
                        naciśnięto = 10
                    elif 620 < event.pos[1] < 650:
                        naciśnięto = 11
                    elif 650 < event.pos[1] < 680:
                        naciśnięto = 12
                    wybór = dokonaj_wyboru(naciśnięto, wybór, wykonano)

    if rzut:
        for numer in range(len(liczby)):
            if not wybrane[numer]:
                liczby[numer] = random.randint(1, 6)
        rzut = False

    for i in range(len(możliwe)):
        if wybór[i] and not możliwe[i]:
            click_tekst = czcionka.render('Niedozwolony wybór - 0 punktów.', True, (255, 255, 255))
            ekran.blit(click_tekst, (230, 205))
        if wybór[i]:
            coś_wybranego = True

    if koniec_gry:
        if wynik_gry > największy_wynik:
            największy_wynik = wynik_gry

    if False not in wykonano:
        koniec_gry = True

    pygame.display.flip()
pygame.quit()