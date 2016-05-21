#assignment 2a Question 1 Roger Gilbertson

#Sale Price Table
def priceCalculator():
    percentages = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]
    prices      = [9.95, 14.95, 19.95, 24.95, 29.95, 34.95, 39.95, 44.95, 49.95]
    list        = []
    print('NORMAL VALUE', '\t9.95', '\t14.95', '\t19.95', '\t24.95', '\t29.95', '\t34.95', '\t39.95', '\t44.95', '\t49.95')
    print('-'*86)
    for percent in percentages:
        for price in prices:
            value = (price - (price * percent))
            value = format(value, '.2f')
            list.append(value)


    print('%off:\t5%\t', *list[0:9], sep='\t')
    print('\t\t10%\t', *list[9:18],  sep='\t')
    print('\t\t15%\t', *list[18:27], sep='\t')
    print('\t\t20%\t', *list[27:36], sep='\t')
    print('\t\t25%\t', *list[36:45], sep='\t')
    print('\t\t30%\t', *list[45:54], sep='\t')
    print('\t\t35%\t', *list[54:63], sep='\t')
    print('\t\t40%\t', *list[63:72], sep='\t')
    print('\t\t45%\t', *list[72:81], sep='\t')
    print('\t\t50%\t', *list[81:90], sep='\t')
