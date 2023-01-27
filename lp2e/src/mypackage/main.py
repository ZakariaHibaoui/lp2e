#import webbrowser


#webbrowser.open("https://github.com/ZakariaHibaoui/lp2e/issues")

#frame for documentation
def docu(self,F):
    F.destroy()
    docu_f2=Frame(root)
    docu_f2.grid()
    button_back = Button(docu_f2, text='Cancel', command=lambda : IMG_Stegno.back(self,docu_f2))
    button_back.config(font=('Helvetica',18),bg='#e8c1c7')
    button_back.grid(pady=15)
    button_back.grid()    