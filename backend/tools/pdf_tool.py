from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import re


def clean_text(text):
    text = str(text)

    text = text.replace("₹", "Rs.")
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")

    # Remove emojis / unsupported characters
    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    # Remove markdown symbols
    text = text.replace("**", "")
    text = text.replace("__", "")
    text = text.replace("###", "")
    text = text.replace("##", "")
    text = text.replace("#", "")

    return text


def create_trip_pdf(plan_text, filename="tripmate_plan.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    normal_style = styles["BodyText"]
    normal_style.fontName = "Helvetica"
    normal_style.fontSize = 10
    normal_style.leading = 14

    story = []

    story.append(Paragraph("TripMate AI Travel Plan", title_style))
    story.append(Spacer(1, 16))

    cleaned_text = clean_text(plan_text)

    for line in cleaned_text.split("\n"):
        line = line.strip()

        if line:
            story.append(Paragraph(line, normal_style))
            story.append(Spacer(1, 6))
        else:
            story.append(Spacer(1, 8))

    doc.build(story)

    return filename