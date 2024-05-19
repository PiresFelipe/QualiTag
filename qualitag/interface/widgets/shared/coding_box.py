import customtkinter as ctk
from tkinter import TclError


class CodingBox(ctk.CTkTextbox):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.__build()
        
        # Binding selection events
        self.bind("<B1-Motion> <ButtonRelease-1>", self.on_select)
        self.bind("<Double-Button-1>", self.on_select)

    def __build(self):
        pass

    def on_select(self, event):
        
        def get_selection():
            try:
                selection = self.index("sel.first")
                print("on_select ", event, selection)
            except TclError:
                return
            
        self.after(3, get_selection)

    def add_tag(self, event):
        print(event)   
