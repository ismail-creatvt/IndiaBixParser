from docx.oxml.shared import OxmlElement, qn
from docx.shared import Pt

from styles import MONTSERRAT_REGULAR, CAUTION_STYLE, CAUTION_CODE, \
    HEADING_1, HEADING_2, HEADING_3, NOTE_STYLE, NOTE_CODE, CODE_BLUE


def shade_cells(cells, shade):
    for cell in cells:
        tcPr = cell._tc.get_or_add_tcPr()
        tcVAlign = OxmlElement("w:shd")
        tcVAlign.set(qn("w:fill"), shade)
        tcPr.append(tcVAlign)


def set_cell_margins(cell, **kwargs):
    """
    cell:  actual cell instance you want to modify

    usage:

        set_cell_margins(cell, top=50, start=50, bottom=50, end=50)

    provided values are in twentieths of a point (1/1440 of an inch).
    read more here: http://officeopenxml.com/WPtableCellMargins.php
    """
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')

    for m in [
        "top",
        "start",
        "bottom",
        "end",
    ]:
        if m in kwargs:
            node = OxmlElement("w:{}".format(m))
            node.set(qn('w:w'), str(kwargs.get(m)))
            node.set(qn('w:type'), 'dxa')
            tcMar.append(node)

    tcPr.append(tcMar)


def unordered_list(document, el):
    for c in el.findAll('li'):
        p = paragraph(document, c, True)
        p.style = 'List Bullet'


def paragraph(document, el, indent=False):
    p = document.add_paragraph()
    if indent:
        p.paragraph_format.left_indent = Pt(40)
    p.style = MONTSERRAT_REGULAR
    for c in el.contents:
        if isinstance(c, str):
            p.add_run(c.replace('\n', ' '))
        elif c.name == 'b' or c.name == 'strong':
            bold(p, c.text)
        elif c.name == 'i' or c.name == 'em':
            italic(p, c.text)
        elif c.name == 'code':
            code(p, c.text)
        elif c.name == 'ul':
            unordered_list(document, c)
        elif c.name == 'p':
            if c.has_attr('class'):
                if c['class'] == 'note':
                    note(document, c)
                elif c['class'] == 'caution':
                    caution(document, c)
            else:
                p = paragraph(document, c, indent)
    return p


def data_dictionary(document, el):
    for e in el.findAll(['dt', 'dd', 'p']):
        if e.name == 'dt':
            paragraph(document, e)
        elif e.name == 'dd':
            paragraph(document, e, True)


def note(document, el):
    table = document.add_table(rows=1, cols=1)
    cell = table.cell(0, 0)
    shade_cells([cell], "#E1F5FE")
    set_cell_margins(cell, top=40, bottom=5, start=15, end=15)
    p = cell.paragraphs[0]
    p.style = NOTE_STYLE
    pf = p.paragraph_format
    pf.space_before = Pt(15)
    pf.space_after = Pt(15)
    pf.left_indent = Pt(20)
    pf.right_indent = Pt(15)

    for c in el.contents:
        if isinstance(c, str):
            p.add_run(c.replace('\n', ''))
        elif c.name == 'b' or c.name == 'strong':
            bold(p, c.text)
        elif c.name == 'italic' or c.name == 'em':
            italic(p, c.text)
        elif c.name == 'code':
            note_code(p, c.text)
    document.add_paragraph()


def caution(document, el):
    table = document.add_table(rows=1, cols=1)
    cell = table.cell(0, 0)
    shade_cells([cell], "#feefe3")
    set_cell_margins(cell, top=40, bottom=5, start=15, end=15)
    p = cell.paragraphs[0]
    p.style = CAUTION_STYLE
    pf = p.paragraph_format
    pf.space_before = Pt(15)
    pf.space_after = Pt(15)
    pf.left_indent = Pt(20)
    pf.right_indent = Pt(15)

    for c in el.contents:
        if isinstance(c, str):
            p.add_run(c.replace('\n', ' '))
        elif c.name == 'b' or c.name == 'strong':
            bold(p, c.text)
        elif c.name == 'italic' or c.name == 'em':
            italic(p, c.text)
        elif c.name == 'code':
            caution_code(p, c.text)
    document.add_paragraph()


def h1(document, text):
    p = document.add_paragraph(text)
    p.style = HEADING_1


def h2(document, text):
    p = document.add_paragraph(text)
    p.style = HEADING_2


def h3(document, text):
    p = document.add_paragraph(text)
    p.style = HEADING_3


def devsite_code(document, el):
    pass


def bold(p, text):
    p.add_run(text.replace('\n', ' ')).bold = True


def italic(p, text):
    p.add_run(text.replace('\n', ' ')).italic = True


def caution_code(p, text):
    p.add_run(text.replace('\n', ' ') + ' ').style = CAUTION_CODE


def note_code(p, text):
    p.add_run(text.replace('\n', ' ') + ' ').style = NOTE_CODE


def code(p, text):
    p.add_run(text.replace('\n', ' ') + ' ').style = CODE_BLUE

