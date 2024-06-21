ROWS, COLUMNS=6,7

pop=[[106,107,111,133,221,767,1766],[502,635,809,947,1402,3634,5268],[2,2,2,6,13,30,46],[163,203,276,408,547,729,628],[2,7,26,82,172,307,392],[16,24,38,74,167,511,809]]
continents=['Africa','Asia','Australia','Europe','North America','South America']

y_total=[]
i=0
while i <COLUMNS:
    y_total.append(0)
    i=i+1
print('%48s' %('year 1750 1800 1850 1900 1950 2000 2050'))

i=0
while i < ROWS:
    print('%13s' % continents[i], end='')
    j=0
    while j < COLUMNS:
        print('%5d' %pop[i][j],end='')
        y_total[j]+=pop[i][j]
        j=j+1
    print()
    i=i+1

print('%13s' %('World'),end='')
j=0
while j < COLUMNS:
    print('%5d' % y_total[j] , end='')
    j=j+1
print()