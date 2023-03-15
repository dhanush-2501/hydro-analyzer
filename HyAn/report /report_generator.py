from fpdf import FPDF
import pandas as pd

class PDF( FPDF ):
    def __init__ (self):
        super().__init__()

    def header(self):
        #Page border
        self.rect(5.0, 5.0, self.w - 10.0, self.h - 10.0)

        #File Header
        self.set_font('Arial', 'B', 12 )
        self.cell(0, 20, 'Hydro Analyzer Report', 1, 1, 'C')


class report():
    def __init__(self):
        super.__init__()

    def pumping_data(self):
        pass

    def pumping_test(self):
        pass


pdf = PDF()
pdf.add_page()

m = 10
pw = 210 - 2*m
ch = 10
cw = pw/6
df = pd.DataFrame(
          {'feature 1' : ['cat 1', 'cat 2', 'cat 3', 'cat 4','cat 1', 'cat 2', 'cat 3', 'cat 4','cat 1', 'cat 2', 'cat 3', 'cat 4','cat 1', 'cat 2', 'cat 3', 'cat 4','cat 1', 'cat 2', 'cat 3', 'cat 4',],
           'feature 2' : [400, 300, 200, 100,400, 300, 200, 100,400, 300, 200, 100,400, 300, 200, 100,400, 300, 200, 100]
          })

pdf.set_font('Arial', '', 12)

""""
Project Details like Project Name, Project Number, Client, Location, etc.. 
"""

pdf.cell(w=(pw), h= ch, txt= "Pumping test-water level", border =1 , ln =1)

pdf.cell(w=(pw/3), h= ch, txt= "Project: tutorial ", border =1 , ln =0 )
pdf.cell(w=(pw/3), h= ch, txt= "Project Number: ", border =1 , ln =0)
pdf.cell(w=(pw/3), h= ch, txt= "Client: ", border =1 , ln =1 )

pdf.cell(w=(pw/3), h= ch, txt= "Location: ", border =1 , ln =0 )
pdf.cell(w=(pw/3), h= ch, txt= "Pumping Test: Theis", border =1 , ln =0)
pdf.cell(w=(pw/3), h= ch, txt= "Pumping well: Pw", border =1 , ln =1 )


pdf.cell(w=(pw/3), h= ch, txt= "Test Conducted By: ", border =1 , ln =0 )
pdf.cell(w=(pw/3), h= ch, txt= "Test Date:", border =1 , ln =0)
pdf.cell(w=(pw/3), h= ch, txt= "Discharge rate: ", border =1 , ln =1 )


pdf.set_font('Arial', 'B', 17)
pdf.cell(w=pw, h=20, txt="Output:", ln=1 )

# Table Header
pdf.set_font('Arial', 'B', 16)
pdf.cell(w=cw, h=10, txt='Feature 1', border=1, ln=0, align='C')
pdf.cell(w=cw, h=10, txt='Feature 2', border=1, ln=1, align='C')
    

# Table contents
pdf.set_font('Arial', '', 14)
for i in range(0, len(df)):
    pdf.cell(w=cw, h=6, 
        txt=df['feature 1'].iloc[i], 
        border=1, ln=0, align='C')
    pdf.cell(w=cw, h=6, 
        txt=df['feature 2'].iloc[i].astype(str), 
        border=1, ln=1, align='C')
    

#Displayed Graph
pdf.image('analysis.png', x = 75, y = 100, w = 130, h = 125, type = 'PNG')

#Transmissivity and storativity Cell
pdf.ln(10)
pdf.cell(w=pw, h=ch, txt="Transmissivity: ", border=1, ln=1 )
pdf.cell(w=pw, h=ch, txt="Storativity:", border=1, ln=1)

#pdf.output(f'generate_pdf.pdf', 'F')




    