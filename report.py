from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def generate_pdf(file_path, data):

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("TalentScout AI Interview Report", styles["Title"]))
    content.append(Spacer(1, 20))

    content.append(Paragraph(f"Name: {data['name']}", styles["Normal"]))
    content.append(Paragraph(f"Role: {data['role']}", styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph(f"Final Score: {data['score']}/10", styles["Normal"]))
    content.append(Paragraph(f"Result: {data['result']}", styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("Summary:", styles["Heading2"]))
    content.append(Paragraph(data["summary"], styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("Strengths:", styles["Heading2"]))
    content.append(Paragraph(data["strengths"], styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("Areas to Improve:", styles["Heading2"]))
    content.append(Paragraph(data["improvements"], styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("Suggestions:", styles["Heading2"]))
    content.append(Paragraph(data["suggestions"], styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("Skill Breakdown:", styles["Heading2"]))
    content.append(Paragraph(data["skills"], styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("Next Steps:", styles["Heading2"]))
    content.append(Paragraph(data["next_steps"], styles["Normal"]))

    doc.build(content)