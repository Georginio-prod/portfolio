"""Build the bilingual CV assets served by the portfolio.

The French document is kept byte-for-byte from the CV supplied by Komla.  The
English document is a faithful translation of the same information, redrawn in
the same one-page, two-column style so it remains easy to scan internationally.
"""

from pathlib import Path
from shutil import copy2

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parents[1]
SOURCE_FR = Path(r"C:\Users\ger\Documents\Perso\Nouveau dossier\CV_2026-09-07_Komla Etonam Georges_EKLOU.pdf")
OUTPUT_DIR = ROOT / "public" / "cv"
OUTPUT_FR = OUTPUT_DIR / "CV_Komla_Etonam_Georges_EKLOU_FR.pdf"
OUTPUT_EN = OUTPUT_DIR / "CV_Komla_Etonam_Georges_EKLOU_EN.pdf"

SLATE = HexColor("#4B6173")
INK = HexColor("#15191E")
MUTED = HexColor("#4B535B")
RULE = HexColor("#D8DDE1")


def paragraph(c: canvas.Canvas, text: str, x: float, y: float, width: float, style: ParagraphStyle) -> float:
    """Draw a ReportLab paragraph and return the next y coordinate."""
    block = Paragraph(text, style)
    _, height = block.wrap(width, y)
    block.drawOn(c, x, y - height)
    return y - height


def rule(c: canvas.Canvas, y: float, x: float, width: float) -> float:
    c.setStrokeColor(RULE)
    c.setLineWidth(0.65)
    c.line(x, y, x + width, y)
    return y - 15


def heading(c: canvas.Canvas, text: str, x: float, y: float, width: float) -> float:
    c.setFillColor(SLATE)
    c.setFont("Helvetica", 15)
    c.drawString(x, y, text)
    return y - 14


def tag(c: canvas.Canvas, text: str, x: float, y: float) -> float:
    c.setFont("Helvetica", 7.9)
    text_width = stringWidth(text, "Helvetica", 7.9) + 16
    c.setFillColor(SLATE)
    c.roundRect(x, y - 12, text_width, 17, 1.5, fill=1, stroke=0)
    c.setFillColor(white)
    c.drawCentredString(x + text_width / 2, y - 6.3, text)
    return text_width


def experience(
    c: canvas.Canvas,
    y: float,
    period: str,
    company: str,
    location: str,
    role: str,
    bullets: list[str],
    x: float,
    width: float,
    body: ParagraphStyle,
) -> float:
    date_width = tag(c, period, x + 18, y)
    c.setFillColor(INK)
    c.setFont("Helvetica", 8.2)
    c.drawString(x + 18 + date_width + 10, y - 1, company)
    c.setFillColor(MUTED)
    c.drawString(x + 18 + date_width + 10, y - 11, location)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 9.1)
    y -= 29
    c.drawString(x + 18, y, role)
    y -= 6
    for bullet in bullets:
        y = paragraph(c, f"-&nbsp;&nbsp;{bullet}", x + 18, y, width - 18, body) - 2
    return y - 26


def generate_english_cv() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    copy2(SOURCE_FR, OUTPUT_FR)

    c = canvas.Canvas(str(OUTPUT_EN), pagesize=A4, pageCompression=1)
    c.setTitle("Komla Etonam Georges EKLOU - CV (English)")
    c.setAuthor("Komla Etonam Georges EKLOU")
    page_width, page_height = A4
    sidebar = 183
    margin = 23
    content_x = sidebar + 22
    content_width = page_width - content_x - 25

    c.setFillColor(SLATE)
    c.rect(0, 0, sidebar, page_height, fill=1, stroke=0)

    side_title = ParagraphStyle(
        "side-title", fontName="Helvetica", fontSize=12, leading=15, textColor=white, alignment=TA_LEFT
    )
    side_body = ParagraphStyle(
        "side-body", fontName="Helvetica", fontSize=8.4, leading=11, textColor=white
    )
    side_body_bold = ParagraphStyle(
        "side-body-bold", fontName="Helvetica-Bold", fontSize=8.4, leading=11, textColor=white
    )
    profile = ParagraphStyle(
        "profile", fontName="Helvetica", fontSize=8.7, leading=11.3, textColor=INK
    )
    body = ParagraphStyle(
        "body", fontName="Helvetica", fontSize=7.8, leading=10.1, textColor=MUTED
    )

    y = page_height - 32
    for line in [
        "Email - etonameklou19@gmail.com",
        "Phone - +228 98 93 85 55",
        "Location - Zanguera, Lome, Togo",
        "Nationality - Togolese",
    ]:
        y = paragraph(c, line, 24, y, sidebar - 40, side_body) - 6

    y -= 20
    y = paragraph(c, "Languages", 23, y, sidebar - 42, side_title) - 10
    y = paragraph(c, "<b>French</b><br/>Native", 23, y, sidebar - 42, side_body) - 8
    y = paragraph(c, "<b>English</b><br/>B1 - Intermediate", 23, y, sidebar - 42, side_body) - 22

    y = paragraph(c, "Interests", 23, y, sidebar - 42, side_title) - 10
    y = paragraph(c, "<b>Sport &amp; leisure</b>", 23, y, sidebar - 42, side_body_bold) - 6
    y = paragraph(c, "<b>Travel &amp; tourism</b>", 23, y, sidebar - 42, side_body_bold) - 6
    y = paragraph(c, "<b>Reading &amp; music</b>", 23, y, sidebar - 42, side_body_bold) - 22

    y = paragraph(c, "Strengths", 23, y, sidebar - 42, side_title) - 10
    for item in [
        "Research-minded and eager to learn",
        "Curious",
        "Active listener",
        "Team player",
        "Rigorous and reliable",
    ]:
        y = paragraph(c, f"<b>{item}</b>", 23, y, sidebar - 42, side_body_bold) - 6

    y -= 10
    y = paragraph(c, "Additional skills", 23, y, sidebar - 42, side_title) - 10
    y = paragraph(
        c,
        "Linux<br/>Git / Git flow<br/>Docker<br/>Node.js<br/>Figma, UI/UX<br/>React, Java, Python<br/>WordPress<br/>MySQL Workbench, WAMP, Firebase, MongoDB<br/>Scrum<br/>Excel, Word, PowerPoint",
        23,
        y,
        sidebar - 42,
        side_body,
    ) - 18

    y = paragraph(c, "Online", 23, y, sidebar - 42, side_title) - 10
    y = paragraph(c, "LinkedIn: Komla Etonam Georges EKLOU<br/>GitHub: Georginio-Prod<br/>georginio.w3frame.com", 23, y, sidebar - 42, side_body)

    y = page_height - 35
    c.setFillColor(INK)
    c.setFont("Helvetica", 17)
    c.drawString(content_x, y, "Komla Etonam Georges EKLOU")
    y -= 22
    c.setFillColor(SLATE)
    c.setFont("Helvetica", 15)
    c.drawString(content_x, y, "Full Stack & Web3 Developer")
    y = rule(c, y - 13, content_x, content_width)

    y = paragraph(
        c,
        "Computer Science graduate with experience in web and Web3 application development. Passionate about designing reliable, high-performing solutions, I work across front-end and back-end development with JavaScript, TypeScript, Vue.js, Nuxt.js, React and APIs. Rigorous, autonomous and analytical, I am looking to contribute to dependable products as a Full Stack Developer.",
        content_x,
        y,
        content_width,
        profile,
    )
    y = rule(c, y - 15, content_x, content_width)

    y = heading(c, "Professional experience", content_x, y, content_width)
    timeline_x = content_x + 4
    c.setStrokeColor(INK)
    c.setLineWidth(1)
    c.line(timeline_x, y - 4, timeline_x, 260)

    y = experience(c, y, "May 2025 - Present", "Globe & Citizen", "Canada", "Full Stack Developer - Smart Contract Integrator", ["Integrated smart contracts.", "Delivered back-end and front-end features.", "Created tests."], content_x, content_width, body)
    y = experience(c, y, "Mar 2025 - Present", "W3 Frame", "Lome, Avedji", "Web Developer", ["Built WordPress websites.", "Delivered web-development training."], content_x, content_width, body)
    y = experience(c, y, "Dec 2024 - Mar 2025", "Prodicom Inter Togo", "Tsevie, Togo", "Customer Service Intern & Sales Analyst", ["Analysed customer data to identify purchasing trends and growth opportunities.", "Produced detailed reports on product and sales performance."], content_x, content_width, body)
    y = experience(c, y, "Aug 2024 - Oct 2024", "W3 Frame", "Lome, Togo", "UI Integration", ["Created and integrated pixel-perfect visual mockups for websites.", "Developed web applications."], content_x, content_width, body)
    y = experience(c, y, "May 2024 - Aug 2024", "New Brain Factory", "Klikame, Lome, Togo", "Web Developer Intern", ["Designed an e-commerce web application with React / Next.js for my final-year project."], content_x, content_width, body)

    y = heading(c, "Education", content_x, y - 2, content_width)
    y = experience(c, y, "Nov 2021 - Jul 2024", "UCAO UUT", "Lome, Togo", "Bachelor's in Engineering Sciences - Computer Science", ["Application Development specialisation.", "Honours: Assez bien (Good).", "Three-year degree in technological sciences."], content_x, content_width, body)

    y = heading(c, "Core skills", content_x, y - 2, content_width)
    y = paragraph(c, "<b>Vue.js, Nuxt.js</b><br/><b>Blockchain / Solidity</b><br/><b>JavaScript, TypeScript</b><br/><b>Tailwind CSS, DaisyUI</b><br/><b>HTML &amp; CSS</b>", content_x + 18, y, content_width - 18, body)

    c.save()


if __name__ == "__main__":
    generate_english_cv()
