import customtkinter as ctk
from ..shared import ImageDisplay
from qualitag import CodingProject


class DashboardScreen(ctk.CTkFrame):

    def __init__(self, *args, project: CodingProject, **kwargs):
        super().__init__(*args, **kwargs)

        ImageDisplay(
            self,
            image=project.generate_most_common_tags_chart(),
            title="Tags mais comuns",
        ).pack(fill="both", expand=True)

    def __change_tag_view(self, tag: str):
        pass
