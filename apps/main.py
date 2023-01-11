from tkinter import *
from apps.destytojas import Destytojas
from apps.igno_app import IgnoApp
from apps.giedrius import Giedrius

class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, text="Pasirinkite")
        self.b_destytojas = Button(self.f_catalog, text="Destytojas", command=self.run_destytojas)
        self.b_giedrius = Button(self.f_catalog, text="Giedrius", command=self.run_giedrius)
        self.igno_mygtukas = Button(self.f_catalog, text="Igno programa",command=self.run_igno_app)

        self.l_pasirinkimai.pack(side=TOP)
        self.b_destytojas.pack()
        self.igno_mygtukas.pack()
        self.l_pasirinkimai.pack(side=TOP)
        self.b_destytojas.pack()
        self.b_giedrius.pack()
        self.f_catalog.pack()

    def run_destytojas(self):
        self.window_destytojas = Toplevel(self.main)
        self.app = Destytojas(self.window_destytojas)
    
    def run_igno_app(self):
        self.window_my_app = Toplevel(self.main)
        self.app = IgnoApp(self.window_my_app)

    def run_giedrius(self):
        self.window_giedrius = Toplevel(self.main)
        self.app = Giedrius(self.window_giedrius)