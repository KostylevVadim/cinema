from random import randint
from datetime import date, timedelta




def person(cursor, n1, n2):
    names = ['Jacob','Jordan','David','Kenneth',
            'Joseph','Donald','Daniel','Gary',
            'Brian','William','Edward','Sandra',
            'Maria','Diane','Carol','Betty',
            'Lisa','Brenda','Michelle']
    surnames = ['Howard','Cox','Webster','Ortiz',
            'Rosales','Sims','Lucas','Eaton','Green',
            'Livingston','Stokes','Pittman','Ashley',
            'Arnold','Foley','Allen','Ferguson','Duke',
            'Hanson','Archer','Beard','Drake']
    bio = ['good person','bad person','strange person','greate person', 'best person', 'love food', 'not popular', 'love scating', 'well known', 
           'not proffesional',
        'loves games', 'has youtube channel', 'very rich', 'was a prisoner', ' loves music', 'musician', 'loves money', 'has a plane',
          'health problems',
        'no parents', 'lives on lighthouse']
    if n1 and n2:
        names = n1
        surnames = n2
    for i in range(40):
        fullname = names[randint(0,len(names)-1)] + ' ' + surnames[randint(0,len(surnames)-1)]
        ful_bio = bio[randint(0,int(len(bio)/2)-1)] + ' ' + bio[randint(int(len(bio)/2),int(len(bio))-1)]
        test_date1, test_date2 = date(1900, 6, 3), date(2020, 7, 1)
        born_delta = randint(0,40000)
        born_date = test_date1 + timedelta(days=born_delta)
        death_date = 0
        if(randint(0,1) == 0):
            death_delta =randint(0,2720)
            death_date = test_date2 - timedelta(days = death_delta)
        if death_date ==0:
            cursor.execute("INSERT INTO person (per_name, birth_date, bio) VALUES(%s,%s,%s)",
            (fullname,born_date,ful_bio))
        else :
            cursor.execute("INSERT INTO person (per_name, birth_date, death_date, bio) VALUES(%s,%s,%s,%s)",
            (fullname,born_date, death_date,ful_bio))
        