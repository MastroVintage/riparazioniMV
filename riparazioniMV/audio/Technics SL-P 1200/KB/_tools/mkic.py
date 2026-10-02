import json
meta=json.load(open('sheets_meta.json'))
def tile(s,ox,oy):
    W,H=meta[s]['size']; f=W/2000
    x,y=ox*f,oy*f
    t=[tt['tile'][:-4] for tt in meta[s]['tiles'] if tt['box'][0]<=x<tt['box'][2] and tt['box'][1]<=y<tt['box'][3]]
    return '%s:%s'%(s,'/'.join(t))
IC=[
('IC11','AN78M05','+5V regulator','E Regulator',('S4_sch_2',1700,255)),
('IC12','AN79N05','-5V regulator','E Regulator',('S4_sch_2',1700,280)),
('IC13','AN78N12','+12V regulator','D Main',('S4_sch_2',1500,375)),
('IC14','AN79L12','-12V regulator','D Main',('S4_sch_2',1500,395)),
('IC101','AN8370S','Optical servo control: focus/tracking error, servo, laser APC, RF amp, drop-out','D Main',('S4_sch_2',1330,330)),
('IC102','AN6554NS','Quad op-amp: tracking & focus coil drive','D Main',('S4_sch_2',770,215)),
('IC103','AN6554NS','Quad op-amp: traverse coil drive / traverse servo','D Main',('S4_sch_2',490,215)),
('IC104','AN6552S','Dual op-amp (FE amp / TE amp)','D Main',('S4_sch_2',740,340)),
('IC105','AN6914S','Dual comparator','D Main',('S4_sch_2',830,340)),
('IC106','uPD4053BC','Analog switch (CMOS triple 2ch)','D Main',('S4_sch_2',440,340)),
('IC301','EHDGA1243','Data slice and PLL (hybrid, SIL15)','D Main',('S4_sch_2',1030,265)),
('IC302','MN6617S','DSP: EFM decoder, error correction, CLV servo (84p QFP)','D Main',('S4_sch_2',1060,480)),
('IC303','MN6618A','Digital filter (42p QFP)','D Main',('S4_sch_2',1300,560)),
('IC304','MN4416S-12','16K RAM (2Kx8 SRAM) for DSP','D Main',('S4_sch_2',760,560)),
('IC331','AN6914','Dual comparator - spindle control','G Spindle control',('S5_sch_3',240,165)),
('IC351','MN74HCU04S','Hex inverter (unbuffered) - pitch control oscillator','K Pitch control',('S3_sch_1',1100,450)),
('IC352','MN74HCU04S','Hex inverter - pitch control','K Pitch control',('S3_sch_1',960,300)),
('IC353','MN74HC74S','Dual D flip-flop - pitch control','K Pitch control',('S3_sch_1',1010,270)),
('IC354','MN74HC00S','Quad NAND - pitch control','K Pitch control',('S3_sch_1',1080,280)),
('IC355','AN6564NS','Quad op-amp - pitch control VCO/PLL','K Pitch control',('S3_sch_1',1010,540)),
('IC401','MN15261PDK','System control & FL drive microcontroller (64p)','D Main',('S4_sch_2',520,520)),
('IC402','MN1550PDM','Remote control signal processing micro (18p)','D Main',('S4_sch_2',270,240)),
('IC403','MN1280-R','Reset signal generator (voltage detector)','D Main',('S4_sch_2',740,480)),
('IC501','AN8290S','Spindle motor drive, 3-phase brushless with Hall H501/H502 (24p)','C Spindle motor drive',('S3_sch_1',1225,520)),
('IC601','BX1438M (M,MC) / BX1439E (others)','IR remote receiver module','A FL',('S3_sch_1',1730,110)),
('IC801','AN78M15','+15V regulator (audio)','I Audio',('S5_sch_3',1100,140)),
('IC802','AN79N15','-15V regulator (audio)','I Audio',('S5_sch_3',1100,170)),
('IC803','AN78M15','+15V regulator (audio)','I Audio',('S5_sch_3',1100,205)),
('IC804','AN79N15','-15V regulator (audio)','I Audio',('S5_sch_3',1100,235)),
('IC805','AN78M12','+12V regulator','I Audio',('S5_sch_3',1280,130)),
('IC806','AN79N12','-12V regulator','I Audio',('S5_sch_3',1280,165)),
('IC821','MN51005PDN','Serial/parallel converter for DACs (64p)','I Audio',('S5_sch_3',720,440)),
('IC822','PCM54KP-M','16-bit parallel DAC, L ch','I Audio',('S5_sch_3',820,590)),
('IC823','PCM54KP-M','16-bit parallel DAC, R ch','I Audio',('S5_sch_3',660,590)),
('IC824','uPD4053BC','Analog switch - class-AA sample/hold (deglitch)','I Audio',('S5_sch_3',960,520)),
('IC825','uPD4053BC','Analog switch - class-AA sample/hold (deglitch)','I Audio',('S5_sch_3',960,320)),
('IC826','M5238P','Dual op-amp - sample/hold buffer','I Audio',('S5_sch_3',970,580)),
('IC827','M5238P','Dual op-amp - sample/hold buffer','I Audio',('S5_sch_3',970,385)),
('IC828','NJM5532DD','Dual op-amp - class-AA output buffer','I Audio',('S5_sch_3',1170,585)),
('IC829','NJM5532DD','Dual op-amp - class-AA output buffer','I Audio',('S5_sch_3',1160,385)),
('IC830','AL079 (SIL10 module)','LPF filter module','I Audio',('S5_sch_3',1100,500)),
('IC831','AL079 (SIL10 module)','LPF filter module','I Audio',('S5_sch_3',1100,300)),
('IC851','NJM4556SA','Headphone amplifier (SIL9)','M Headphone amp',('S5_sch_3',1520,520)),
('IC1001','MN6030','Remote control transmitter IC (handset)','Remote control unit',('S3_sch_1',690,330)),
]
with open('KB/ic_list.tsv','w') as f:
    f.write('# Fonte: parts list p.23 (m23.png) + schemi. tile = sheet:tile in KB/sheets/<sheet>/<tile>.png (300dpi). Funzioni "inferred" dove non scritte nel manuale (vedi colonna note)\n')
    f.write('ref\tpart\tfunction\tboard\tschematic_tile\tpins_file\n')
    import os
    for r,p,fn,b,(s,x,y) in IC:
        pf=[n for n in os.listdir('KB/pins') if n.startswith(r+'_')]
        f.write('\t'.join([r,p,fn,b,tile(s,x,y),pf[0] if pf else '-'])+'\n')
print(open('KB/ic_list.tsv').read())
