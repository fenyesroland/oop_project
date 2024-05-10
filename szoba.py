
class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    def __str__(self):
        return f"Szoba {self.szobaszam} - Ár: {self.ar} Ft/Éjszaka"