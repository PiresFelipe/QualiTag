from tkinter import filedialog, messagebox

import customtkinter as ctk

from ...utils import fonts


class FileMenu(ctk.CTkFrame):

    def __init__(self, *args, project, **kwargs):
        super().__init__(*args, **kwargs)

        self.__project = project
        _font = ctk.CTkFont(size=12)
        ctk.CTkButton(
            self,
            text="Salvar projeto",
            command=self.save_project,
            font=_font,
            width=_font.measure("Salvar projeto"),
            fg_color="transparent",
            hover_color=("#DCDCDC", "#898989"),
            text_color=("black", "white"),
        ).pack(side="left", padx=5, anchor="w")

        ctk.CTkButton(
            self,
            text="Exportar Excel",
            command=self.export_excel,
            font=_font,
            width=_font.measure("Exportar Excel"),
            fg_color="transparent",
            hover_color=("#DCDCDC", "#898989"),
            text_color=("black", "white"),
        ).pack(side="left", padx=5, anchor="w")

        ctk.CTkButton(
            self,
            text="Exportar PDF",
            command=self.export_pdf,
            font=_font,
            width=_font.measure("Exportar PDF"),
            fg_color="transparent",
            hover_color=("#DCDCDC", "#898989"),
            text_color=("black", "white"),
        ).pack(side="left", padx=5, anchor="w")

    def save_project(self):

        _file = filedialog.asksaveasfilename(
            filetypes=[("QualiTag project", "*.pkl")],
            confirmoverwrite=True,
            defaultextension=".pkl",
            initialfile="qualitag_project.pkl",
        )

        try:
            self.__project.save(_file)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

    def export_excel(self):

        file = filedialog.asksaveasfilename(
            title="Exportar codificação",
            filetypes=[("Excel files", "*.xlsx")],
            initialfile="codificação.xlsx",
            defaultextension=".xlsx",
            confirmoverwrite=True,
        )

        self.__project.export_data(file)

    def export_pdf(self):

        file = filedialog.asksaveasfilename(
            title="Exportar codificação",
            filetypes=[("PDF files", "*.pdf")],
            initialfile="relatório_qualitag.pdf",
            defaultextension=".pdf",
            confirmoverwrite=True,
        )

        self.__project.export_data(file)
