import pygame
import sys
import subprocess
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
ekran = pygame.display.set_mode((1050, 400), 0, 32)
czcionka = pygame.font.Font('freesansbold.ttf', 16)
def rysuj_tekst(tekst, czcionka, kolor, powierzchnia, x, y):
    tekstobj = czcionka.render(tekst, 1, kolor)
    tekstrect = tekstobj.get_rect()
    tekstrect.topleft = (x, y)
    powierzchnia.blit(tekstobj, tekstrect)
click = False
def main_menu():
    while True:
        ekran.fill((34, 140, 34))
        rysuj_tekst('Kości - menu główne', czcionka, (255, 255, 255), ekran, 65, 40)
        pozycja_x, pozycja_y = pygame.mouse.get_pos()
        przycisk_1 = pygame.Rect(50, 100, 200, 50)
        przycisk_2 = pygame.Rect(50, 200, 200, 50)
        przycisk_3 = pygame.Rect(50, 300, 200, 50)
        if przycisk_1.collidepoint((pozycja_x, pozycja_y)):
            if click:
                rozpocznij_gre()
        if przycisk_2.collidepoint((pozycja_x, pozycja_y)):
            if click:
                instrukcja()
        if przycisk_3.collidepoint((pozycja_x, pozycja_y)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(ekran, (148, 11, 6), przycisk_1)
        pygame.draw.rect(ekran, (148, 11, 6), przycisk_2)
        pygame.draw.rect(ekran, (148, 11, 6), przycisk_3)
        rysuj_tekst('Rozpocznij grę', czcionka, (255, 255, 255), ekran, 90, 115)
        rysuj_tekst('Zasady gry', czcionka, (255, 255, 255), ekran, 105, 215)
        rysuj_tekst('Wyjdź z menu', czcionka, (255, 255, 255), ekran, 95, 315)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
def rozpocznij_gre():
    subprocess.call([sys.executable, "gra.py"])
def instrukcja():
    running = True
    while running:
        ekran.fill((34, 140, 34))
        rysuj_tekst('Zasady gry:', czcionka, (255, 255, 255), ekran, 20, 20)
        rysuj_tekst('Używa się pięciu klasycznych kości do gry o kształcie sześcianu z liczbą punktów 1, 2, 3, 4, 5 i 6 na poszczególnych ściankach.', czcionka, (255, 255, 255), ekran, 20, 50)
        rysuj_tekst('W każdej kolejce gracz ma do dyspozycji trzy rzuty kostkami. Pierwszy rzut odbywa się zawsze wszystkimi pięcioma kostkami.', czcionka, (255, 255, 255), ekran, 20, 70)
        rysuj_tekst('Przy następnych dwóch nieobowiązkowych rzutach gracz może wybrać ze wszystkich kostki zatrzymane, a niezatrzymanymi', czcionka, (255, 255, 255), ekran, 20, 90)
        rysuj_tekst('wykonuje rzut. Celem rzutów w kolejce jest uzyskanie odpowiedniej kombinacji. Po wykonaniu rzutów układ oczek uzyskany na', czcionka, (255, 255, 255), ekran, 20, 110)
        rysuj_tekst('kostkach musi zostać zapisany przez gracza w tabeli punktacji do jednej z kategorii.', czcionka, (255, 255, 255), ekran, 20, 130)
        rysuj_tekst('Za wybraną kategorię otrzymuje się odpowiednią liczbę punktów. Raz wybrana kategoria nie może zostać użyta ponownie.', czcionka, (255, 255, 255), ekran, 20, 150)
        rysuj_tekst('Koniec gry następuje z chwilą użycia ostatniej kategorii w tabelce. Wygrywa gracz z największą liczbą punktów.', czcionka, (255, 255, 255), ekran, 20, 170)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)
main_menu()