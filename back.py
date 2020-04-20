from datetime import timezone
import datetime
import csv



def TimeConverter(csv_file, newfile, keyfile):

    DictionaryCountry = []
    DictionaryState = []
    Dateindex = " "
    Countryindex = " "
    Provinceindex = " "
    firstrows = True

    with open(csv_file, 'r') as t:
        stuff = csv.reader(t)
        with open(newfile, 'w', newline='') as f:
            new = csv.writer(f)
            with open(keyfile, 'w') as key:
                for row in stuff:
                    if firstrows:
                        firstrows = False
                        for n in range (0, len(row)):
                            if row[n] == 'Date':
                                Dateindex = n
                            if row[n] == 'Country_Region':
                                Countryindex = n
                            if row[n] == 'Province_State':
                                Provinceindex = n

                    elif firstrows == False:
                        t = row[Dateindex].split("-")
                        k = 0
                        for m in t:

                            if k == 0:
                                k += 1
                                Year = m
                            elif k == 1:
                                k += 1
                                Month = m
                            elif k == 2:
                                Day = m
                                dt =datetime.datetime(int(Year), int(Month), int(Day))
                                timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
                                row[Dateindex] = timestamp
                        if row[Countryindex] not in DictionaryCountry:
                            DictionaryCountry.append(row[Countryindex])
                            row[Countryindex] = DictionaryCountry.index(row[Countryindex])
                        else:
                            row[Countryindex] = DictionaryCountry.index(row[Countryindex])

                        if row[Provinceindex] not in DictionaryState:
                            DictionaryState.append(row[Provinceindex])
                            row[Provinceindex] = DictionaryState.index(row[Provinceindex])
                        else:
                            row[Provinceindex] = DictionaryState.index(row[Provinceindex])

                    new.writerow(row)
                key.write('Country = ' + str(DictionaryCountry) + '\n' + 'State = ' + str(DictionaryState))


TimeConverter('train.csv', 'train2.csv', 'keytrain2.txt')