import pandas as pd

def get_fromcsv():
    print('Getting data from credits.csv')
    df = pd.read_csv('credits.csv',',')
    names = []
    surnames = []
    arr = df['cast'].to_list()
    print(len(arr))
    for elem in arr:
        list = elem.split(',')
        name = ''
        for list_elem in list:
            if 'name' in list_elem:
                st = list_elem.replace(" 'name': '","").replace("'","").split(' ')
                if len(st)==2:
                    if st[0] not in names:
                        names.append(st[0])
                    if st[1] not in surnames:
                        surnames.append(st[1])
    return names, surnames

