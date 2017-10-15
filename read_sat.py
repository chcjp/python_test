#!python3

import xlrd

data = xlrd.open_workbook('Strong Satellite Transponders Lists 11-10-2017.xlsx')
f = open('sat.txt', 'w')

for num in range(21):
    table = data.sheets()[num]
    title = table.cell(rowx=5,colx=0).value
    angle = table.cell(rowx=2,colx=0).value
    str = '%d, %s,    %s\n' % (num, title,angle)
    print(str)
    nrows = table.nrows
    #ncols = table.ncols
    f.write(str)
    for rx in range(5,nrows):
        cell_freq = table.cell(rowx=rx,colx=2).value
        cell_pol = table.cell(rowx=rx,colx=3).value
        cell_sym = table.cell(rowx=rx,colx=4).value
        pol = 0
        if cell_pol == 'H':
            pol = 1
        else:
            pol = 0
        str = "    {  %.0f,       %.0f     %d} ,\n" % (cell_freq, cell_sym, pol)
        f.write(str)
    f.write('\n')
    pass

f.close()    
