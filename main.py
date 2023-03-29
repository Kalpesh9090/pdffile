from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image('logo_the_avengers.png',10,8,25)
        self.set_font('times','B',20)
        self.cell(0,10,'Title',align='C')
        self.ln(20)

pdf = FPDF('P','mm','A4',)

pdf.add_page()
pdf.set_auto_page_break(auto=True,margin=16)
pdf.set_font('times','',16)
pdf.cell(8, 5,'''Python is a high-level, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of significant indentation.[33]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, 
including structured (particularly procedural), object-oriented and functional programming. 
It is often described as a "batteries included" language due to its comprehensive standard library.
[34][35]

Guido van Rossum began working on Python in the late 1980s as a successor 
to the ABC programming language and first released it in 1991 as Python 0.9.0.[36] 
Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not 
completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, 
was the last release of Python 2.[37]

Python consistently ranks as one of the most popular programming languages''', ln=True)
pdf.output('pdf2.pdf')