"""Organizza le pagine pulite in SERVICE_BULLETINS/<doc>/KB/{pages,ocr,scan_map.tsv} + DATA/<doc>_pulito.pdf"""
import os, shutil, subprocess, img2pdf, sys
SB=sys.argv[1]; CL=sys.argv[2]
SRC={'s00':'scan.pdf','s73':'scan0073.pdf','s74':'scan0074.pdf','s75':'scan0075.pdf'}
DOCS=[ # cartella, [(tag, scan, nota)]
 ('SB_A6-87-17_spindle_AN8290S',[('p01','s00-000','Service Bulletin A6-87-17 p.1'),('p02','s00-001','retro (OVER), non numerato')]),
 ('SB_A6-88-11_massa_switch_RF',[('p01','s00-002','1 of 4'),('p02','s00-003','2 of 4'),('p03','s00-004','3 of 4'),('p04','s00-005','4 of 4')]),
 ('SB_A6-89-1_gommino_disc_magnet',[('p01','s00-000'.replace('s00-000','s74-000'),'pagina unica')]),
 ('TI_HAD8607677T0_FPC_jig',[('p01','s74-002','pagina unica')]),
 ('SUP_AD8908221S1_SL-P1200X_balance_out',[('p01','s73-000','copertina = p.1 (non numerata)'),('p02','s73-001','-2-'),('p03','s73-002','-3-'),('p04','s73-003','-4- Printed in Japan K891002480YY'),('p05','s73-004','foglio allegato non numerato: IMPORTANT!!! Grounding the unit')]),
 ('TI_UK_1987-05_SL-P520_P720_spindle',[('p01','s75-000','pagina unica (scansione migliore; s75-002 e s75-004 sono copie identiche)')]),
]
for d,pages in DOCS:
    kb=os.path.join(SB,d,'KB'); os.makedirs(kb+'/pages',exist_ok=True); os.makedirs(kb+'/ocr',exist_ok=True); os.makedirs(os.path.join(SB,d,'DATA'),exist_ok=True)
    with open(kb+'/scan_map.tsv','w',encoding='utf-8') as f:
        f.write('page_tag\tsource_pdf\tpdf_page\tnota\n')
        for t,s,n in pages:
            f.write(f'{t}\t{SRC[s[:3]]}\t{int(s[4:])+1}\t{n}\n')
            shutil.copy(f'{CL}/{s}.png',f'{kb}/pages/{t}.png')
            txt=subprocess.run(['tesseract',f'{kb}/pages/{t}.png','-','--psm','4'],capture_output=True,text=True).stdout
            open(f'{kb}/ocr/{t}.txt','w',encoding='utf-8').write(txt)
    with open(os.path.join(SB,d,'DATA',d+'_pulito.pdf'),'wb') as f:
        f.write(img2pdf.convert([f'{kb}/pages/{t}.png' for t,_,_ in pages],layout_fun=img2pdf.get_fixed_dpi_layout_fun((300,300))))
    print(d,len(pages))
