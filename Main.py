# coding=utf-8
from kivy.uix.screenmanager import ScreenManager,Screen
from ScreenObjects.TablaVacia import TablaVacia
from kivy.properties import ObjectProperty
from ScreenObjects.Tabla import Tabla
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from Algoritmos.MMSK import mmsk
from Algoritmos.MM1 import mm1
from Algoritmos.MMS import mms
from Algoritmos.MG1 import mg1
from kivy.lang import Builder
from kivy.app import App

Builder.load_file('Kivy_Files/InitialScreen.kv')
Builder.load_file('Kivy_Files/ErrorPopup.kv')
Builder.load_file('Kivy_Files/MM1Screen.kv')
Builder.load_file('Kivy_Files/MMSScreen.kv')

class ErrorPopup(Popup):
    errores = []
    def on_open(self):
        for e in self.errores:
            self.ids['errord'].add_widget(Label(text=e))


class MMSScreen(Screen):
    #Inputs
    lmd = ObjectProperty()
    mu = ObjectProperty()
    s = ObjectProperty()
    n = ObjectProperty()
    #Outputs
    lsr = ObjectProperty()
    lqr = ObjectProperty()
    wsr = ObjectProperty()
    wqr = ObjectProperty()
    pr = ObjectProperty()

    def on_pre_enter(self, *args):
        self.lmd.text = ''
        self.mu.text = ''
        self.s.text = ''
        self.n.text = ''
        self.lsr.text = ''
        self.lqr.text = ''
        self.wsr.text = ''
        self.wqr.text = ''
        self.pr.text = ''
        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(TablaVacia())

    def return_to_menu(self):
        screen_manager.transition.duration = 1.5
        screen_manager.transition.direction = "right"
        screen_manager.current = 'initial_screen'

    def mms(self):
        errores = []
        if self.lmd.text == "":
            errores.append("Lambda no puede estar vació")
        if self.mu.text == "":
            errores.append("Mu no puede estar vació")
        if self.s.text == "":
            errores.append("S no puede estar vació")

        if len(errores)==0:
            l = float(self.lmd.text)
            m = float(self.mu.text)
            s = int(self.s.text)
            if self.n.text != "":
                aux = int(self.n.text)
                ls,lq,ws,wq,p,pn = mms(l,m,s,aux)
                self.lsr.text = str(ls)
                self.lqr.text = str(lq)
                self.wsr.text = str(ws)
                self.wqr.text = str(wq)
                self.pr.text = str(p)
                self.ids['drawing_box'].clear_widgets()
                self.ids['drawing_box'].add_widget(Tabla(pn))
            else:
                ls,lq,ws,wq,p,pn = mms(l,m,s)
                self.lsr.text = str(ls)
                self.lqr.text = str(lq)
                self.wsr.text = str(ws)
                self.wqr.text = str(wq)
                self.pr.text = str(p)
                self.ids['drawing_box'].clear_widgets()
                self.ids['drawing_box'].add_widget(Tabla(pn))
        else:
            the_popup = ErrorPopup()
            the_popup.errores = errores
            the_popup.open()






class MM1Screen(Screen):

    #Inputs
    lmd = ObjectProperty()
    mu = ObjectProperty()
    n = ObjectProperty()

    #Outputs
    lr = ObjectProperty()
    lqr = ObjectProperty()
    wr = ObjectProperty()
    wqr = ObjectProperty()
    pr = ObjectProperty()


    def on_pre_enter(self, *args):

        self.lmd.text = ''
        self.mu.text = ''
        self.n.text = ''
        self.lr.text = ''
        self.lqr.text = ''
        self.wr.text = ''
        self.wqr.text = ''
        self.pr.text = ''

        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(TablaVacia())

    def return_to_menu(self):
        screen_manager.transition.duration = 1.5
        screen_manager.transition.direction = "right"
        screen_manager.current = 'initial_screen'

    def mm1(self):
        errores = []
        #print(self.lmd.text+" - "+self.mu.text+" - "+self.n.text)
        if self.lmd.text == "":
            errores.append("Lambda no puede estar vació")
        if self.mu.text == "":
            errores.append("Mu no puede estar vació")

        if len(errores)==0:
            l = float(self.lmd.text)
            m = float(self.mu.text)
            if self.n.text != "":
                aux = int(self.n.text)
                ls,ws,lq,wq,p,pnl = mm1(l,m,aux)
                self.lr.text = str(ls)
                self.lqr.text = str(lq)
                self.wr.text = str(ws)
                self.wqr.text = str(wq)
                self.pr.text = str(p)
                self.ids['drawing_box'].clear_widgets()
                self.ids['drawing_box'].add_widget(Tabla(pnl))
            else:
                ls, ws, lq, wq, p, pnl = mm1(l,m)
                self.lr.text = str(ls)
                self.lqr.text = str(lq)
                self.wr.text = str(ws)
                self.wqr.text = str(wq)
                self.pr.text = str(p)
                self.ids['drawing_box'].clear_widgets()
                self.ids['drawing_box'].add_widget(Tabla(pnl))
        else:
            the_popup = ErrorPopup()
            the_popup.errores = errores
            the_popup.open()


class InitialScreen(Screen):
    def go_to_screen(self,screen_name):
        screen_manager.transition.duration = 1.5
        screen_manager.transition.direction = "left"
        screen_manager.current = screen_name
    def close_app(self):
        App.get_running_app().stop()


screen_manager = ScreenManager()
screen_manager.add_widget(InitialScreen(name="initial_screen"))
screen_manager.add_widget(MM1Screen(name="mm1_screen"))
screen_manager.add_widget(MMSScreen(name="mms_screen"))

class App(App):
    def build(self):
        self.title = 'Simulador de modelos de filas de espera'
        return screen_manager

sample = App()
sample.run()