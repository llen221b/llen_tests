# Program to generate a random number between 1 and 15; 1 and 40
import cmd
import random
import time

class MojaKonsola(cmd.Cmd):
    prompt = 'MojaKonsola> '  # Prompt, który będzie wyświetlany w konsoli

    def do_start(self, arg):
        """Polecenie start: rozpoczyna generowanie losowych numerów"""
        self.generuj_losowy_numer(1, 15)
        time.sleep(240)  # Czekaj 4 minuty
        self.generuj_losowy_numer(1, 40)
        time.sleep(240)  # Czekaj 4 minuty
        return True

    def generuj_losowy_numer(self, min, max):
        liczba = random.randint(min, max)
        print("Wylosowano numer:", liczba)

    def do_quit(self, arg):
        """Polecenie quit: zamyka konsolę"""
        print("Zamykanie konsoli...")
        return True

    def default(self, line):
        print("Nieznane polecenie:", line)

    def emptyline(self):
        pass

if __name__ == '__main__':
    konsola = MojaKonsola()
    konsola.cmdloop()
