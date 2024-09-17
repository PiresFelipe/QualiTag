from __future__ import annotations
from .exporter_base import ExporterBase
from typing import TYPE_CHECKING

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm

from wordcloud import get_single_color_func

if TYPE_CHECKING:
    from qualitag.src import CodingProject


class PDFExporter(ExporterBase):

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def export(self, project: CodingProject):

        doc = SimpleDocTemplate(self.filepath, pagesize=A4)
        elements = []
        styles = getSampleStyleSheet()

        # Seção: Questões
        elements.append(Paragraph("Questões", styles["Title"]))
        for i, question in enumerate(project.questions):
            _text = question.question
            if len(_text) < 3:
                _text = "Não foi informado"
            question_text = f"<b>Questão {i+1:03d}:</b> <i>{question.question}</i>; <b>Respostas:</b> {len(question.answers)}"
            elements.append(Paragraph(question_text, styles["Normal"]))
            elements.append(Spacer(1, 12))

        # Seção: tags
        elements.append(Paragraph("Tags", styles["Title"]))
        img = project.generate_most_common_tags_chart(as_buffer=True)
        img = Image(img, width=160 * mm, height=120 * mm)
        elements.append(img)
        elements.append(Spacer(1, 24))

        for tag in project.tags_manager.get_all_tags(sort=True):
            elements.append(
                Paragraph(
                    f"{tag.name}: {project.tags_manager.counter[tag.name.lower()]}",
                    styles["Heading2"],
                )
            )
            _description = tag.description
            if not _description or len(_description) < 3:
                _description = "Não há descrição para essa tag"
            elements.append(Paragraph(_description, styles["Normal"]))
            elements.append(Spacer(1, 24))

            if project.tags_manager.counter[tag.name.lower()] > 3:
                # Cria nuvem de palavras
                img = project.generate_wordcloud(
                    tag.name,
                    as_buffer=True,
                    width=int(160 * mm),
                    height=int(80 * mm),
                    color_func=get_single_color_func(tag.color),
                )
                img = Image(img, width=160 * mm, height=80 * mm)
                elements.append(img)
                elements.append(Spacer(1, 24))

        # Criar o PDF
        doc.build(elements)
