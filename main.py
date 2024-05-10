import datetime

from EgyagyasSzoba import EgyagyasSzoba
from KetagyasSzoba import KetagyasSzoba
from Szalloda import Szalloda
import tkinter as tk
from tkinter import messagebox
from tkinter import Label



class SzallodasApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Helyes's Hotel & Spa")
        self.geometry("800x400")
        self.foglalasok_lista = []

        self.szalloda = Szalloda("Helyes's Hotel & Spa")
        self.szalloda.add_szoba(EgyagyasSzoba(101))
        self.szalloda.add_szoba(EgyagyasSzoba(102))
        self.szalloda.add_szoba(EgyagyasSzoba(103))
        self.szalloda.add_szoba(EgyagyasSzoba(104))
        self.szalloda.add_szoba(EgyagyasSzoba(105))
        self.szalloda.add_szoba(KetagyasSzoba(201))
        self.szalloda.add_szoba(KetagyasSzoba(202))
        self.szalloda.add_szoba(KetagyasSzoba(203))
        self.szalloda.add_szoba(KetagyasSzoba(204))
        self.szalloda.add_szoba(KetagyasSzoba(205))

        self.create_widgets()

    def create_widgets(self):
        # Gombok a bal oldalon
        gombok_frame = tk.Frame(self, padx=20, pady=20)
        gombok_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        btn_foglal = tk.Button(gombok_frame, text="Szoba foglalása", command=self.foglalas_ablak)
        btn_foglal.pack(pady=10)

        btn_lemond = tk.Button(gombok_frame, text="Foglalás lemondása", command=self.lemondas_ablak)
        btn_lemond.pack(pady=10)

        btn_kilepes = tk.Button(gombok_frame, text="Kilépés", command=self.destroy)
        btn_kilepes.pack(pady=10)

        # Visszajelzések a jobb oldalon
        self.visszajelzes_frame = tk.Frame(self, padx=20, pady=20)
        self.visszajelzes_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.visszajelzes_label = tk.Label(self.visszajelzes_frame, text=self.szalloda.lista_foglalasok(), wraplength=400, justify=tk.LEFT)
        self.visszajelzes_label.pack(fill=tk.BOTH, expand=True)

        self.foglalasok_listbox = tk.Listbox(self.visszajelzes_frame, width=40)
        self.foglalasok_listbox.pack(side=tk.LEFT, fill=tk.BOTH)


    def foglalas_ablak(self):
        foglalas_ablak = tk.Toplevel(self)
        foglalas_ablak.title("Szoba foglalása")

        ev_label = tk.Label(foglalas_ablak, text="Év:")
        ev_label.pack()
        ev_entry = tk.Entry(foglalas_ablak)
        ev_entry.pack()

        honap_label = tk.Label(foglalas_ablak, text="Hónap:")
        honap_label.pack()
        honap_entry = tk.Entry(foglalas_ablak)
        honap_entry.pack()

        nap_label = tk.Label(foglalas_ablak, text="Nap:")
        nap_label.pack()
        nap_entry = tk.Entry(foglalas_ablak)
        nap_entry.pack()

        agyak_szama_label = tk.Label(foglalas_ablak, text="Ágyas szoba:")
        agyak_szama_label.pack()

        agyak_szama_var = tk.IntVar()
        egy_agyas_radio = tk.Radiobutton(foglalas_ablak, text="Egy ágyas", variable=agyak_szama_var, value=1)
        ket_agyas_radio = tk.Radiobutton(foglalas_ablak, text="Két ágyas", variable=agyak_szama_var, value=2)
        egy_agyas_radio.pack()
        ket_agyas_radio.pack()

        def foglalas_gomb_kattintas():
            ev = int(ev_entry.get())
            honap = int(honap_entry.get())
            nap = int(nap_entry.get())
            agyak_szama = agyak_szama_var.get()
            try:
                datum = datetime.date(ev, honap, nap)
                valasz = self.szalloda.szoba_foglalasa(datum, agyak_szama)
                self.visszajelzes_label.config(text=self.szalloda.lista_foglalasok())
            except ValueError:
                self.visszajelzes_label.config(text="Érvénytelen dátum!")

        foglalas_gomb = tk.Button(foglalas_ablak, text="Foglalás", command=foglalas_gomb_kattintas)
        foglalas_gomb.pack(pady=10)


    def lemondas_ablak(self):
        lemondas_ablak = tk.Toplevel(self)
        lemondas_ablak.title("Foglalás lemondása")

        foglalasok_frame = tk.Frame(lemondas_ablak)
        foglalasok_frame.pack(pady=10)

        foglalasok_listbox = tk.Listbox(foglalasok_frame, width=40)
        foglalasok_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        for foglalas in self.szalloda.foglalasok:
            foglalasok_listbox.insert(tk.END, str(foglalas))

        def lemondas_gomb_kattintas():
            kivalasztott_index = foglalasok_listbox.curselection()
            if kivalasztott_index:
                kivalasztott_foglalas = self.szalloda.foglalasok[kivalasztott_index[0]]
                valasz = self.szalloda.foglalas_lemondasa(kivalasztott_foglalas.datum, kivalasztott_foglalas.szoba.szobaszam)
                self.visszajelzes_label.config(text=self.szalloda.lista_foglalasok())

        lemondas_gomb = tk.Button(lemondas_ablak, text="Lemondás", command=lemondas_gomb_kattintas)
        lemondas_gomb.pack(pady=10)

if __name__ == "__main__":
    app = SzallodasApp()
    app.mainloop()