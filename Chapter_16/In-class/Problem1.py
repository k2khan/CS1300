firstLine = True

with open('raceByState.csv') as inputFile:
    for line in inputFile:
        linelist = line.split(',')
        """ First Line """ 
        if firstLine:
            header0 = linelist[0]
            header1 = linelist[1]
            header2 = linelist[2]
            header3 = linelist[3]
            header4 = linelist[4]
            header5 = linelist[5]
            header6 = linelist[6]
            header7 = linelist[7]
            print( f'{header0:<20}  {header1:>9}  {header2:>9}  {header3:>9}  {header4:>9} {header5:>9}  {header6:>9}  {header7:>9}')
            firstLine = False
            continue 

        """ 7 Columns """
        state = linelist.pop(0)
        total = linelist[0]
        white = linelist[1]
        black = linelist[2]
        native = linelist[3]
        asian = linelist[4]
        pacific = linelist[5]
        multirace = linelist[6]

        percentage0 = int(linelist[1]) / int(linelist[0]) * 100
        percentage1 = int(linelist[2]) / int(linelist[0]) * 100
        percentage2 = int(linelist[3]) / int(linelist[0]) * 100
        percentage3 = int(linelist[4]) / int(linelist[0]) * 100
        percentage4 = int(linelist[5]) / int(linelist[0]) * 100
        percentage5 = int(linelist[6]) / int(linelist[0]) * 100

        print( f'{state:<20}  {total:>9}  {white:>9} ({percentage0:>4.1f}%)  {black:>9} ({percentage1:>4.1f}%)  {native:>9} ({percentage2:>4.1f}%)  {asian:>9} ({percentage3:>4.1f}%)  {pacific:>9} ({percentage4:>4.1f}%)  {multirace:>9} ({percentage5:>4.1f}%)')
