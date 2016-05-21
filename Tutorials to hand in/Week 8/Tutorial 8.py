# Tutorial 8 - Roger Gilbertson


def filecopy(sourcefile, destinationfile):
    try:
        sfile = open(sourcefile, 'r')                                                                                               #SOURCEFILE
        dfile = open(destinationfile, 'w')                                                                                          #DESTINATION FILE / COPIED FILE
        count = len(open(sourcefile).readlines(   ))
        omitStartCount = int(input('Omit how many lines from the start? '))                                                         #LINES TO BE OMMITTED
        omitEndCount   = int(input('Omit how many lines from the end? '))
        omitCountTotal = omitStartCount + omitEndCount                                                                              #TOTAL COUNT OF OMITS FOR ERROR CHECKING
        if omitCountTotal >= count:                                                                                                 #IF OMIT COUNT GREATER THEN SOURCEFILE LINES. ERROR MESSAGE
            print('The total omit count you selected, {} lines.  It is greater than {} lines in txt file.'.format(omitEndCount, count))
        else:                                                                                                                       #CODE FOR GOING THRU SOURCEFILE TO DEST FILE
            counter = 0
            for line in sfile :
                counter += 1
                if (counter > omitStartCount) and (count - counter >= omitEndCount):
                    dfile.write(line)
            sfile.close()
            dfile.close()
    except:                                                                                                                         #ERROR MESSAGE IF FILE SOURCEFILE NOT FOUND
        print('Could not open the file ()'.format(sourcefile))
        print('Output file not WRITTEN')

def main():                                                                                                                         #MAIN USING FILECOPY FUNCTION
    filecopy(input('Enter the source file'), input('Enter the desination file'))                                                    #FUNCTION CALL WITH USER INPUT
    count = len(open('test.txt').readlines(   ))
    print('There are a total of {} lines in this txt file.'.format(count))

main()