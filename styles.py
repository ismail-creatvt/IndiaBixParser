from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_COLOR_INDEX
from docx.shared import Pt, RGBColor

document = Document()

HEADING_1 = 'Head 1'
HEADING_2 = 'Head 2'
HEADING_3 = 'Head 3'
MONTSERRAT_REGULAR = 'Montserrat'
CODE_BLUE = 'Code Blue'
CAUTION_CODE = 'Caution Code'
CONSOLAS = 'Consolas'
CAUTION_STYLE = 'Caution Style'
CAUTION_BOLD = 'Caution Bold'
NOTE_STYLE = 'Note Style'
NOTE_BOLD = 'Note Bold'
NOTE_CODE = 'Note Code'

styles = document.styles

#changing the page margins
sections = document.sections
for section in sections:
    section.top_margin = Pt(35)
    section.bottom_margin = Pt(35)
    section.left_margin = Pt(30)
    section.right_margin = Pt(30)

list_bullet = document.styles['List Bullet']
list_bullet.font.name = MONTSERRAT_REGULAR
list_bullet.font.size = Pt(12)

heading_1 = styles.add_style(HEADING_1, WD_STYLE_TYPE.PARAGRAPH)
heading_1.font.name = MONTSERRAT_REGULAR
heading_1.font.size = Pt(18)

heading_2 = styles.add_style(HEADING_2, WD_STYLE_TYPE.PARAGRAPH)
heading_2.font.name = MONTSERRAT_REGULAR
heading_2.font.size = Pt(16)

heading_2 = styles.add_style(HEADING_3, WD_STYLE_TYPE.PARAGRAPH)
heading_2.font.name = MONTSERRAT_REGULAR
heading_2.font.size = Pt(14)


montserrat_regular = styles.add_style(MONTSERRAT_REGULAR, WD_STYLE_TYPE.PARAGRAPH)
montserrat_regular.font.name = MONTSERRAT_REGULAR
montserrat_regular.font.size = Pt(12)

code_style = styles.add_style(CODE_BLUE, WD_STYLE_TYPE.CHARACTER)
code_style.font.name = CONSOLAS
code_style.font.size = Pt(12)
code_style.font.color.rgb = RGBColor(0x36, 0xb5, 0xe1)
code_style.font.highlight_color = WD_COLOR_INDEX.GRAY_25
code_style.font.bold = True

caution_style = styles.add_style(CAUTION_STYLE, WD_STYLE_TYPE.PARAGRAPH)
caution_style.font.color.rgb = RGBColor(0xc9, 0x52, 0x2d)
caution_style.font.size = Pt(11)
caution_style.font.name = MONTSERRAT_REGULAR

caution_text_bold = styles.add_style(CAUTION_BOLD, WD_STYLE_TYPE.CHARACTER)
caution_style.font.color.rgb = RGBColor(0Xc9, 0x52, 0x2d)
caution_text_bold.font.size = Pt(11)
caution_text_bold.font.bold = True
caution_text_bold.font.name = MONTSERRAT_REGULAR

caution_text_code = styles.add_style(CAUTION_CODE, WD_STYLE_TYPE.CHARACTER)
caution_style.font.color.rgb = RGBColor(0Xc9, 0x52, 0x2d)
caution_text_code.font.size = Pt(11)
caution_text_code.font.bold = True
caution_text_code.font.name = CONSOLAS

note_style = styles.add_style(NOTE_STYLE, WD_STYLE_TYPE.PARAGRAPH)
note_style.font.color.rgb = RGBColor(0X01, 0x57, 0xb5)
note_style.font.size = Pt(11)
note_style.font.name = MONTSERRAT_REGULAR

note_text_bold = styles.add_style(NOTE_BOLD, WD_STYLE_TYPE.CHARACTER)
note_style.font.color.rgb = RGBColor(0X01, 0x57, 0xb5)
note_text_bold.font.size = Pt(11)
note_text_bold.font.bold = True
note_text_bold.font.name = MONTSERRAT_REGULAR

note_text_code = styles.add_style(NOTE_CODE, WD_STYLE_TYPE.CHARACTER)
note_style.font.color.rgb = RGBColor(0X01, 0x57, 0xb5)
note_text_code.font.size = Pt(11)
note_text_code.font.bold = True
note_text_code.font.name = CONSOLAS

