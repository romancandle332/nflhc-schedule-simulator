import math
import random
import csv

##easy index since the order will be the same
nflindex = {
    'ARI': 1,
    'ATL': 2,
    'BAL': 3,
    'BUF': 4,
    'CAR': 5,
    'CHI': 6,
    'CIN': 7,
    'CLE': 8,
    'DAL': 9,
    'DEN': 10,
    'DET': 11,
    'GB': 12,
    'HOU': 13,
    'IND': 14,
    'JAX': 15,
    'KC': 16,
    'LAC': 17,
    'LAR': 18,
    'LV': 19,
    'MIA': 20,
    'MIN': 21,
    'NE': 22,
    'NO': 23,
    'NYG': 24,
    'NYJ': 25,
    'PHI': 26,
    'PIT': 27,
    'SEA': 28,
    'SF': 29,
    'TB': 30,
    'TEN': 31,
    'WFT': 32}

##Strength of Team Value
strength = {
    'ARI': .063,
    'ATL': .500,
    'BAL': .750,
    'BUF': .688,
    'CAR': .250,
    'CHI': .563,
    'CIN': .438,
    'CLE': .250,
    'DAL': .563,
    'DEN': .563,
    'DET': .750,
    'GB': .625,
    'HOU': .188,
    'IND': .500,
    'JAX': .438,
    'KC': .688,
    'LAC': .188,
    'LAR': .500,
    'LV': .750,
    'MIA': .438,
    'MIN': .313,
    'NE': .250,
    'NO': .563,
    'NYG': .500,
    'NYJ': .438,
    'PHI': .750,
    'PIT': .750,
    'SEA': .625,
    'SF': .563,
    'TB': .063,
    'TEN': .750,
    'WFT': .750}

##for divisionalstuff
division = {
    'ARI': 'NFCW',
    'ATL': 'NFCS',
    'BAL': 'AFCN',
    'BUF': 'AFCE',
    'CAR': 'NFCS',
    'CHI': 'NFCN',
    'CIN': 'AFCN',
    'CLE': 'AFCN',
    'DAL': 'NFCE',
    'DEN': 'NFCS',
    'DET': 'NFCN',
    'GB': 'NFCN',
    'HOU': 'AFCS',
    'IND': 'AFCS',
    'JAX': 'AFCS',
    'KC': 'NFCS',
    'LAC': 'NFCS',
    'LAR': 'NFCW',
    'LV': 'NFCS',
    'MIA': 'AFCE',
    'MIN': 'NFCN',
    'NE': 'AFCE',
    'NO': 'NFCS',
    'NYG': 'NFCE',
    'NYJ': 'AFCE',
    'PHI': 'NFCE',
    'PIT': 'AFCN',
    'SEA': 'NFCW',
    'SF': 'NFCW',
    'TB': 'NFCS',
    'TEN': 'AFCS',
    'WFT': 'NFCE'}

##for conference, I should make this a loadable dictionary in its own file tbh
conference = {
    'ARI': 'NFC',
    'ATL': 'NFC',
    'BAL': 'AFC',
    'BUF': 'AFC',
    'CAR': 'NFC',
    'CHI': 'NFC',
    'CIN': 'AFC',
    'CLE': 'AFC',
    'DAL': 'NFC',
    'DEN': 'AFC',
    'DET': 'NFC',
    'GB': 'NFC',
    'HOU': 'AFC',
    'IND': 'AFC',
    'JAX': 'AFC',
    'KC': 'AFC',
    'LAC': 'AFC',
    'LAR': 'NFC',
    'LV': 'AFC',
    'MIA': 'AFC',
    'MIN': 'NFC',
    'NE': 'AFC',
    'NO': 'NFC',
    'NYG': 'NFC',
    'NYJ': 'AFC',
    'PHI': 'NFC',
    'PIT': 'AFC',
    'SEA': 'NFC',
    'SF': 'NFC',
    'TB': 'NFC',
    'TEN': 'AFC',
    'WFT': 'NFC'}

schedule = []
file = "nflhc2025.csv" ##load schedule
with open(file, newline='',encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            schedule.append(row)

##database     0      1       2         3             4                   5          6      7       8                9        10   11   12   13
database = [['Team','Wins','Losses','Opponents','Home Opponents','Away Opponents','SOS','Home SOS','Away SOS','Teams Beaten','DW','DL','CW','CL'],
            ['ARI',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['ATL',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['BAL',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['BUF',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['CAR',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['CHI',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['CIN',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['CLE',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['DAL',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['DEN',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['DET',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['GB',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['HOU',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['IND',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['JAX',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['KC',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['LAC',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['LAR',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['LV',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['MIA',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['MIN',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['NE',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['NO',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['NYG',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['NYJ',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['PHI',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['PIT',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['SEA',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['SF',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['TB',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['TEN',0,0,[],[],[],0,0,0,[],0,0,0,0],
            ['WFT',0,0,[],[],[],0,0,0,[],0,0,0,0]]
i = 1
while i < len(schedule):
    a = schedule[i][1] ##away
    b = schedule[i][2] ##home
    c = strength[a]
    d = strength[b]
    e = nflindex[a]
    f = nflindex[b]
    x = database[e][6]
    x_2 = x + d
    y = database[e][8]
    y_2 = y + d
    z = database[f][6]
    z_2 = z + c
    w = database[f][7]
    w_2 = w + c
    schedule[i].append(c)
    schedule[i].append(d)
    database[e][3].append(b)
    database[e][6] = x_2
    database[e][8] = y_2
    database[e][5].append(b)
    database[f][3].append(a)
    database[f][4].append(a)
    database[f][6] = z_2
    database[f][7] = w_2

    c -= .029
    d += .029

    home_win = (d-d*c)/(d+c-2*d*c)
    roll = random.random()
    if roll <= home_win:
        database[f][1] += 1
        database[e][2] += 1
        database[f][9].append(a)
        if conference[a] == conference[b]:
            database[f][12] += 1
            database[e][13] += 1
            if division[a] == division[b]:
                database[f][10] += 1
                database[e][11] += 1
    else:
        database[e][1] += 1
        database[f][2] += 1
        database[e][9].append(b)
        if conference[a] == conference[b]:
            database[f][13] += 1
            database[e][12] += 1
            if division[a] == division[b]:
                database[f][11] += 1
                database[e][10] += 1
    i += 1

##now we divide the SOS by games played because I'm lazy and didn't want to write a loop to do it above
value_nolossofgenerality = 1
while value_nolossofgenerality < len(database):
    a = database[value_nolossofgenerality][6]
    b = database[value_nolossofgenerality][7]
    c = database[value_nolossofgenerality][8]
    neoa = round(a/17,3)
    neob = round(b/len(database[value_nolossofgenerality][4]),3)
    neoc = round(c/len(database[value_nolossofgenerality][5]),3)
    database[value_nolossofgenerality][6] = neoa
    database[value_nolossofgenerality][7] = neob
    database[value_nolossofgenerality][8] = neoc
    value_nolossofgenerality += 1

playoffs = [['Division','Champion'],
            ['AFCN',[]],
            ['AFCE',[]],
            ['AFCS',[]],
            ['AFCW',[]],
            ['Wildcard',[]],
            ['Wildcard',[]],
            ['Wildcard',[]],
            ['NFCN',[]],
            ['NFCE',[]],
            ['NFCS',[]],
            ['NFCW',[]],
            ['Wildcard',[]],
            ['Wildcard',[]],
            ['Wildcard',[]]]
teams_in = []

##AFCN
bucket = []
team1 = 'BAL'
team2 = 'CIN'
team3 = 'CLE'
team4 = 'PIT'
bucket.append(database[nflindex[team1]][1]) 
bucket.append(database[nflindex[team2]][1]) 
bucket.append(database[nflindex[team3]][1]) 
bucket.append(database[nflindex[team4]][1])
print(bucket)
if bucket.count((max(bucket))) >= 2: ##Ties, the worst thing in sports
    print("tiebreaker")
    tiebreaker = []
    tiebreaker_division = []
    tiebreaker_conference = []
    if max(bucket) == database[nflindex[team1]][1]:
        tiebreaker.append(team1)
        tiebreaker_division.append(database[nflindex[team1]][10])
        tiebreaker_conference.append(database[nflindex[team1]][12])
    if max(bucket) == database[nflindex[team2]][1]:
        tiebreaker.append(team2)
        tiebreaker_division.append(database[nflindex[team2]][10])
        tiebreaker_conference.append(database[nflindex[team2]][12])
    if max(bucket) == database[nflindex[team3]][1]:
        tiebreaker.append(team3)
        tiebreaker_division.append(database[nflindex[team3]][10])
        tiebreaker_conference.append(database[nflindex[team3]][12])
    if max(bucket) == database[nflindex[team4]][1]:
        tiebreaker.append(team4)
        tiebreaker_division.append(database[nflindex[team4]][10])
        tiebreaker_conference.append(database[nflindex[team4]][12])
    print(tiebreaker)
    print(tiebreaker_division)
    print(tiebreaker_conference)
    if tiebreaker_division.count((max(tiebreaker_division))) >= 2: ##WHY YOU TIE SO HARD
        pick = tiebreaker[tiebreaker_conference.index(max(tiebreaker_conference))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    else:
        pick = tiebreaker[tiebreaker_division.index(max(tiebreaker_division))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    
else:
    champ = bucket.index(max(bucket))
if champ == 0:
    playoffs[1][1] = team1
    teams_in.append(team1)
elif champ == 1:
    playoffs[1][1] = team2
    teams_in.append(team2)
elif champ == 2:
    playoffs[1][1] = team3
    teams_in.append(team3)
elif champ == 3:
    playoffs[1][1] = team4
    teams_in.append(team4)

##AFCE
bucket = []
team1 = 'BUF'
team2 = 'MIA'
team3 = 'NE'
team4 = 'NYJ'
bucket.append(database[nflindex[team1]][1]) 
bucket.append(database[nflindex[team2]][1]) 
bucket.append(database[nflindex[team3]][1]) 
bucket.append(database[nflindex[team4]][1])
print(bucket)
if bucket.count((max(bucket))) >= 2: ##Ties, the worst thing in sports
    print("tiebreaker")
    tiebreaker = []
    tiebreaker_division = []
    tiebreaker_conference = []
    if max(bucket) == database[nflindex[team1]][1]:
        tiebreaker.append(team1)
        tiebreaker_division.append(database[nflindex[team1]][10])
        tiebreaker_conference.append(database[nflindex[team1]][12])
    if max(bucket) == database[nflindex[team2]][1]:
        tiebreaker.append(team2)
        tiebreaker_division.append(database[nflindex[team2]][10])
        tiebreaker_conference.append(database[nflindex[team2]][12])
    if max(bucket) == database[nflindex[team3]][1]:
        tiebreaker.append(team3)
        tiebreaker_division.append(database[nflindex[team3]][10])
        tiebreaker_conference.append(database[nflindex[team3]][12])
    if max(bucket) == database[nflindex[team4]][1]:
        tiebreaker.append(team4)
        tiebreaker_division.append(database[nflindex[team4]][10])
        tiebreaker_conference.append(database[nflindex[team4]][12])
    print(tiebreaker)
    print(tiebreaker_division)
    print(tiebreaker_conference)
    if tiebreaker_division.count((max(tiebreaker_division))) >= 2: ##WHY YOU TIE SO HARD
        pick = tiebreaker[tiebreaker_conference.index(max(tiebreaker_conference))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    else:
        pick = tiebreaker[tiebreaker_division.index(max(tiebreaker_division))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    
else:
    champ = bucket.index(max(bucket))
if champ == 0:
    playoffs[2][1] = team1
    teams_in.append(team1)
elif champ == 1:
    playoffs[2][1] = team2
    teams_in.append(team2)
elif champ == 2:
    playoffs[2][1] = team3
    teams_in.append(team3)
elif champ == 3:
    playoffs[2][1] = team4
    teams_in.append(team4)

##AFCS
bucket = []
team1 = 'IND'
team2 = 'JAX'
team3 = 'HOU'
team4 = 'TEN'
bucket.append(database[nflindex[team1]][1]) 
bucket.append(database[nflindex[team2]][1]) 
bucket.append(database[nflindex[team3]][1]) 
bucket.append(database[nflindex[team4]][1])
print(bucket)
if bucket.count((max(bucket))) >= 2: ##Ties, the worst thing in sports
    print("tiebreaker")
    tiebreaker = []
    tiebreaker_division = []
    tiebreaker_conference = []
    if max(bucket) == database[nflindex[team1]][1]:
        tiebreaker.append(team1)
        tiebreaker_division.append(database[nflindex[team1]][10])
        tiebreaker_conference.append(database[nflindex[team1]][12])
    if max(bucket) == database[nflindex[team2]][1]:
        tiebreaker.append(team2)
        tiebreaker_division.append(database[nflindex[team2]][10])
        tiebreaker_conference.append(database[nflindex[team2]][12])
    if max(bucket) == database[nflindex[team3]][1]:
        tiebreaker.append(team3)
        tiebreaker_division.append(database[nflindex[team3]][10])
        tiebreaker_conference.append(database[nflindex[team3]][12])
    if max(bucket) == database[nflindex[team4]][1]:
        tiebreaker.append(team4)
        tiebreaker_division.append(database[nflindex[team4]][10])
        tiebreaker_conference.append(database[nflindex[team4]][12])
    print(tiebreaker)
    print(tiebreaker_division)
    print(tiebreaker_conference)
    if tiebreaker_division.count((max(tiebreaker_division))) >= 2: ##WHY YOU TIE SO HARD
        pick = tiebreaker[tiebreaker_conference.index(max(tiebreaker_conference))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    else:
        pick = tiebreaker[tiebreaker_division.index(max(tiebreaker_division))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    
else:
    champ = bucket.index(max(bucket))
if champ == 0:
    playoffs[3][1] = team1
    teams_in.append(team1)
elif champ == 1:
    playoffs[3][1] = team2
    teams_in.append(team2)
elif champ == 2:
    playoffs[3][1] = team3
    teams_in.append(team3)
elif champ == 3:
    playoffs[3][1] = team4
    teams_in.append(team4)

##AFCW
bucket = []
team1 = 'DEN'
team2 = 'KC'
team3 = 'LAC'
team4 = 'LV'
bucket.append(database[nflindex[team1]][1]) 
bucket.append(database[nflindex[team2]][1]) 
bucket.append(database[nflindex[team3]][1]) 
bucket.append(database[nflindex[team4]][1])
print(bucket)
if bucket.count((max(bucket))) >= 2: ##Ties, the worst thing in sports
    print("tiebreaker")
    tiebreaker = []
    tiebreaker_division = []
    tiebreaker_conference = []
    if max(bucket) == database[nflindex[team1]][1]:
        tiebreaker.append(team1)
        tiebreaker_division.append(database[nflindex[team1]][10])
        tiebreaker_conference.append(database[nflindex[team1]][12])
    if max(bucket) == database[nflindex[team2]][1]:
        tiebreaker.append(team2)
        tiebreaker_division.append(database[nflindex[team2]][10])
        tiebreaker_conference.append(database[nflindex[team2]][12])
    if max(bucket) == database[nflindex[team3]][1]:
        tiebreaker.append(team3)
        tiebreaker_division.append(database[nflindex[team3]][10])
        tiebreaker_conference.append(database[nflindex[team3]][12])
    if max(bucket) == database[nflindex[team4]][1]:
        tiebreaker.append(team4)
        tiebreaker_division.append(database[nflindex[team4]][10])
        tiebreaker_conference.append(database[nflindex[team4]][12])
    print(tiebreaker)
    print(tiebreaker_division)
    print(tiebreaker_conference)
    if tiebreaker_division.count((max(tiebreaker_division))) >= 2: ##WHY YOU TIE SO HARD
        pick = tiebreaker[tiebreaker_conference.index(max(tiebreaker_conference))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    else:
        pick = tiebreaker[tiebreaker_division.index(max(tiebreaker_division))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    
else:
    champ = bucket.index(max(bucket))
if champ == 0:
    playoffs[4][1] = team1
    teams_in.append(team1)
elif champ == 1:
    playoffs[4][1] = team2
    teams_in.append(team2)
elif champ == 2:
    playoffs[4][1] = team3
    teams_in.append(team3)
elif champ == 3:
    playoffs[4][1] = team4
    teams_in.append(team4)

##NFCN
bucket = []
team1 = 'CHI'
team2 = 'DET'
team3 = 'GB'
team4 = 'MIN'
bucket.append(database[nflindex[team1]][1]) 
bucket.append(database[nflindex[team2]][1]) 
bucket.append(database[nflindex[team3]][1]) 
bucket.append(database[nflindex[team4]][1])
print(bucket)
if bucket.count((max(bucket))) >= 2: ##Ties, the worst thing in sports
    print("tiebreaker")
    tiebreaker = []
    tiebreaker_division = []
    tiebreaker_conference = []
    if max(bucket) == database[nflindex[team1]][1]:
        tiebreaker.append(team1)
        tiebreaker_division.append(database[nflindex[team1]][10])
        tiebreaker_conference.append(database[nflindex[team1]][12])
    if max(bucket) == database[nflindex[team2]][1]:
        tiebreaker.append(team2)
        tiebreaker_division.append(database[nflindex[team2]][10])
        tiebreaker_conference.append(database[nflindex[team2]][12])
    if max(bucket) == database[nflindex[team3]][1]:
        tiebreaker.append(team3)
        tiebreaker_division.append(database[nflindex[team3]][10])
        tiebreaker_conference.append(database[nflindex[team3]][12])
    if max(bucket) == database[nflindex[team4]][1]:
        tiebreaker.append(team4)
        tiebreaker_division.append(database[nflindex[team4]][10])
        tiebreaker_conference.append(database[nflindex[team4]][12])
    print(tiebreaker)
    print(tiebreaker_division)
    print(tiebreaker_conference)
    if tiebreaker_division.count((max(tiebreaker_division))) >= 2: ##WHY YOU TIE SO HARD
        pick = tiebreaker[tiebreaker_conference.index(max(tiebreaker_conference))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    else:
        pick = tiebreaker[tiebreaker_division.index(max(tiebreaker_division))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    
else:
    champ = bucket.index(max(bucket))
if champ == 0:
    playoffs[8][1] = team1
    teams_in.append(team1)
elif champ == 1:
    playoffs[8][1] = team2
    teams_in.append(team2)
elif champ == 2:
    playoffs[8][1] = team3
    teams_in.append(team3)
elif champ == 3:
    playoffs[8][1] = team4
    teams_in.append(team4)

##NFCE
bucket = []
team1 = 'DAL'
team2 = 'NYG'
team3 = 'PHI'
team4 = 'WFT'
bucket.append(database[nflindex[team1]][1]) 
bucket.append(database[nflindex[team2]][1]) 
bucket.append(database[nflindex[team3]][1]) 
bucket.append(database[nflindex[team4]][1])
print(bucket)
if bucket.count((max(bucket))) >= 2: ##Ties, the worst thing in sports
    print("tiebreaker")
    tiebreaker = []
    tiebreaker_division = []
    tiebreaker_conference = []
    if max(bucket) == database[nflindex[team1]][1]:
        tiebreaker.append(team1)
        tiebreaker_division.append(database[nflindex[team1]][10])
        tiebreaker_conference.append(database[nflindex[team1]][12])
    if max(bucket) == database[nflindex[team2]][1]:
        tiebreaker.append(team2)
        tiebreaker_division.append(database[nflindex[team2]][10])
        tiebreaker_conference.append(database[nflindex[team2]][12])
    if max(bucket) == database[nflindex[team3]][1]:
        tiebreaker.append(team3)
        tiebreaker_division.append(database[nflindex[team3]][10])
        tiebreaker_conference.append(database[nflindex[team3]][12])
    if max(bucket) == database[nflindex[team4]][1]:
        tiebreaker.append(team4)
        tiebreaker_division.append(database[nflindex[team4]][10])
        tiebreaker_conference.append(database[nflindex[team4]][12])
    print(tiebreaker)
    print(tiebreaker_division)
    print(tiebreaker_conference)
    if tiebreaker_division.count((max(tiebreaker_division))) >= 2: ##WHY YOU TIE SO HARD
        pick = tiebreaker[tiebreaker_conference.index(max(tiebreaker_conference))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    else:
        pick = tiebreaker[tiebreaker_division.index(max(tiebreaker_division))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    
else:
    champ = bucket.index(max(bucket))
if champ == 0:
    playoffs[9][1] = team1
    teams_in.append(team1)
elif champ == 1:
    playoffs[9][1] = team2
    teams_in.append(team2)
elif champ == 2:
    playoffs[9][1] = team3
    teams_in.append(team3)
elif champ == 3:
    playoffs[9][1] = team4
    teams_in.append(team4)

##NFCS
bucket = []
team1 = 'ATL'
team2 = 'CAR'
team3 = 'NO'
team4 = 'TB'
bucket.append(database[nflindex[team1]][1]) 
bucket.append(database[nflindex[team2]][1]) 
bucket.append(database[nflindex[team3]][1]) 
bucket.append(database[nflindex[team4]][1])
print(bucket)
if bucket.count((max(bucket))) >= 2: ##Ties, the worst thing in sports
    print("tiebreaker")
    tiebreaker = []
    tiebreaker_division = []
    tiebreaker_conference = []
    if max(bucket) == database[nflindex[team1]][1]:
        tiebreaker.append(team1)
        tiebreaker_division.append(database[nflindex[team1]][10])
        tiebreaker_conference.append(database[nflindex[team1]][12])
    if max(bucket) == database[nflindex[team2]][1]:
        tiebreaker.append(team2)
        tiebreaker_division.append(database[nflindex[team2]][10])
        tiebreaker_conference.append(database[nflindex[team2]][12])
    if max(bucket) == database[nflindex[team3]][1]:
        tiebreaker.append(team3)
        tiebreaker_division.append(database[nflindex[team3]][10])
        tiebreaker_conference.append(database[nflindex[team3]][12])
    if max(bucket) == database[nflindex[team4]][1]:
        tiebreaker.append(team4)
        tiebreaker_division.append(database[nflindex[team4]][10])
        tiebreaker_conference.append(database[nflindex[team4]][12])
    print(tiebreaker)
    print(tiebreaker_division)
    print(tiebreaker_conference)
    if tiebreaker_division.count((max(tiebreaker_division))) >= 2: ##WHY YOU TIE SO HARD
        pick = tiebreaker[tiebreaker_conference.index(max(tiebreaker_conference))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    else:
        pick = tiebreaker[tiebreaker_division.index(max(tiebreaker_division))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    
else:
    champ = bucket.index(max(bucket))
if champ == 0:
    playoffs[10][1] = team1
    teams_in.append(team1)
elif champ == 1:
    playoffs[10][1] = team2
    teams_in.append(team2)
elif champ == 2:
    playoffs[10][1] = team3
    teams_in.append(team3)
elif champ == 3:
    playoffs[10][1] = team4
    teams_in.append(team4)

##NFCW
bucket = []
team1 = 'ARI'
team2 = 'LAR'
team3 = 'SEA'
team4 = 'SF'
bucket.append(database[nflindex[team1]][1]) 
bucket.append(database[nflindex[team2]][1]) 
bucket.append(database[nflindex[team3]][1]) 
bucket.append(database[nflindex[team4]][1])
print(bucket)
if bucket.count((max(bucket))) >= 2: ##Ties, the worst thing in sports
    print("tiebreaker")
    tiebreaker = []
    tiebreaker_division = []
    tiebreaker_conference = []
    if max(bucket) == database[nflindex[team1]][1]:
        tiebreaker.append(team1)
        tiebreaker_division.append(database[nflindex[team1]][10])
        tiebreaker_conference.append(database[nflindex[team1]][12])
    if max(bucket) == database[nflindex[team2]][1]:
        tiebreaker.append(team2)
        tiebreaker_division.append(database[nflindex[team2]][10])
        tiebreaker_conference.append(database[nflindex[team2]][12])
    if max(bucket) == database[nflindex[team3]][1]:
        tiebreaker.append(team3)
        tiebreaker_division.append(database[nflindex[team3]][10])
        tiebreaker_conference.append(database[nflindex[team3]][12])
    if max(bucket) == database[nflindex[team4]][1]:
        tiebreaker.append(team4)
        tiebreaker_division.append(database[nflindex[team4]][10])
        tiebreaker_conference.append(database[nflindex[team4]][12])
    print(tiebreaker)
    print(tiebreaker_division)
    print(tiebreaker_conference)
    if tiebreaker_division.count((max(tiebreaker_division))) >= 2: ##WHY YOU TIE SO HARD
        pick = tiebreaker[tiebreaker_conference.index(max(tiebreaker_conference))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    else:
        pick = tiebreaker[tiebreaker_division.index(max(tiebreaker_division))]
        if pick == team1:
            champ = 0
        elif pick == team2:
            champ = 1
        elif pick == team3:
            champ = 2
        elif pick == team4:
            champ = 3
    
else:
    champ = bucket.index(max(bucket))
if champ == 0:
    playoffs[11][1] = team1
    teams_in.append(team1)
elif champ == 1:
    playoffs[11][1] = team2
    teams_in.append(team2)
elif champ == 2:
    playoffs[11][1] = team3
    teams_in.append(team3)
elif champ == 3:
    playoffs[11][1] = team4
    teams_in.append(team4)

##Wildcards, pray for me, I'm going in
x = 0
AFC = 0
NFC = 0
while x < 6:
    y = 1
    wildcard = []
    wildcard_wins = []
    wildcard_conference = []
    while y < len(database): ##non-divisional winners basically
        team = database[y][0]
        if team in teams_in:
            y += 1
            continue
        conf = conference[database[y][0]]
        if conf == 'NFC':
            if NFC < 3:
                wildcard.append(y)
                wildcard_wins.append(database[y][1])
                wildcard_conference.append(database[y][12])

        elif conf == 'AFC':
            if AFC < 3:
                wildcard.append(y)
                wildcard_wins.append(database[y][1])
                wildcard_conference.append(database[y][12])
        y += 1
    AFC_tiebreaker = []
    NFC_tiebreaker = []
    z = 1
    while z < len(database):
        team = database[z][0]
        if team in teams_in:
            z += 1
            continue
        if database[z][1] < max(wildcard_wins):
            z += 1
            continue
        if conference[team] == 'NFC' and NFC < 3:
            NFC_tiebreaker.append(z)
        elif conference[team] == 'AFC' and AFC < 3:
            AFC_tiebreaker.append(z)
        z += 1
    if not AFC_tiebreaker:
        pass
    elif len(AFC_tiebreaker) == 1:
        print("Solo AFC")
        if AFC == 0:
            playoffs[5][1] = database[AFC_tiebreaker[0]][0]
            AFC += 1
            x += 1
            teams_in.append(database[AFC_tiebreaker[0]][0])
        elif AFC == 1:
            playoffs[6][1] = database[AFC_tiebreaker[0]][0]
            AFC += 1
            x += 1
            teams_in.append(database[AFC_tiebreaker[0]][0])
        elif AFC == 2:
            playoffs[7][1] = database[AFC_tiebreaker[0]][0]
            AFC += 1
            x += 1
            teams_in.append(database[AFC_tiebreaker[0]][0])
    elif len(AFC_tiebreaker) == 2:
        print("Double AFC")
        if database[AFC_tiebreaker[1]][0] in database[AFC_tiebreaker[0]][9]:
            if AFC == 0:
                playoffs[5][1] = database[AFC_tiebreaker[0]][0]
                AFC += 1
                x += 1
                teams_in.append(database[AFC_tiebreaker[0]][0])
            elif AFC == 1:
                playoffs[6][1] = database[AFC_tiebreaker[0]][0]
                AFC += 1
                x += 1
                teams_in.append(database[AFC_tiebreaker[0]][0])
            elif AFC == 2:
                playoffs[7][1] = database[AFC_tiebreaker[0]][0]
                AFC += 1
                x += 1
                teams_in.append(database[AFC_tiebreaker[0]][0])
            AFC_tiebreaker.pop(0)
        elif database[AFC_tiebreaker[0]][0] in database[AFC_tiebreaker[1]][9]:
            if AFC == 0:
                playoffs[5][1] = database[AFC_tiebreaker[1]][0]
                AFC += 1
                x += 1
                teams_in.append(database[AFC_tiebreaker[1]][0])
            elif AFC == 1:
                playoffs[6][1] = database[AFC_tiebreaker[1]][0]
                AFC += 1
                x += 1
                teams_in.append(database[AFC_tiebreaker[1]][0])
            elif AFC == 2:
                playoffs[7][1] = database[AFC_tiebreaker[1]][0]
                AFC += 1
                x += 1
                teams_in.append(database[AFC_tiebreaker[1]][0])
            AFC_tiebreaker.pop(1)
        else:
            conference_bucket = []
            w = 0
            while w < len(AFC_tiebreaker):
                conference_bucket.append(database[AFC_tiebreaker[w]][12])
                w += 1
            pick = AFC_tiebreaker[conference_bucket.index(max(conference_bucket))]
            team = database[pick][0]
            if AFC == 0:
                playoffs[5][1] = database[pick][0]
                AFC += 1
                x += 1
                teams_in.append(team)
            elif AFC == 1:
                playoffs[6][1] = database[pick][0]
                AFC += 1
                x += 1
                teams_in.append(team)
            elif AFC == 2:
                playoffs[7][1] = database[pick][0]
                AFC += 1
                x += 1
                teams_in.append(team)
            AFC_tiebreaker.pop(conference_bucket.index(max(conference_bucket)))
    else:
        print("3+ AFC")
        conference_bucket = []
        w = 0
        while w < len(AFC_tiebreaker):
            conference_bucket.append(database[AFC_tiebreaker[w]][12])
            w += 1
        pick = AFC_tiebreaker[conference_bucket.index(max(conference_bucket))]
        team = database[pick][0]
        if AFC == 0:
            playoffs[5][1] = database[pick][0]
            AFC += 1
            x += 1
            teams_in.append(team)
        elif AFC == 1:
            playoffs[6][1] = database[pick][0]
            AFC += 1
            x += 1
            teams_in.append(team)
        elif AFC == 2:
            playoffs[7][1] = database[pick][0]
            AFC += 1
            x += 1
            teams_in.append(team)
        AFC_tiebreaker.pop(conference_bucket.index(max(conference_bucket)))
    if not NFC_tiebreaker:
        pass
    elif len(NFC_tiebreaker) == 1:
        print("Solo NFC")
        if NFC == 0:
            playoffs[12][1] = database[NFC_tiebreaker[0]][0]
            NFC += 1
            x += 1
            teams_in.append(database[NFC_tiebreaker[0]][0])
        elif NFC == 1:
            playoffs[13][1] = database[NFC_tiebreaker[0]][0]
            NFC += 1
            x += 1
            teams_in.append(database[NFC_tiebreaker[0]][0])
        elif NFC == 2:
            playoffs[14][1] = database[NFC_tiebreaker[0]][0]
            NFC += 1
            x += 1
            teams_in.append(database[NFC_tiebreaker[0]][0])
    elif len(NFC_tiebreaker) == 2:
        print("two NFC")
        if database[NFC_tiebreaker[1]][0] in database[NFC_tiebreaker[0]][9]:
            if NFC == 0:
                playoffs[12][1] = database[NFC_tiebreaker[0]][0]
                NFC += 1
                x += 1
                teams_in.append(database[NFC_tiebreaker[0]][0])
            elif NFC == 1:
                playoffs[13][1] = database[NFC_tiebreaker[0]][0]
                NFC += 1
                x += 1
                teams_in.append(database[NFC_tiebreaker[0]][0])
            elif NFC == 2:
                playoffs[14][1] = database[NFC_tiebreaker[0]][0]
                NFC += 1
                x += 1
                teams_in.append(database[NFC_tiebreaker[0]][0])
            NFC_tiebreaker.pop(0)
        elif database[NFC_tiebreaker[0]][0] in database[NFC_tiebreaker[1]][9]:
            if NFC == 0:
                playoffs[12][1] = database[NFC_tiebreaker[1]][0]
                NFC += 1
                x += 1
                teams_in.append(database[NFC_tiebreaker[1]][0])
            elif NFC == 1:
                playoffs[13][1] = database[NFC_tiebreaker[1]][0]
                NFC += 1
                x += 1
                teams_in.append(database[NFC_tiebreaker[1]][0])
            elif NFC == 2:
                playoffs[14][1] = database[NFC_tiebreaker[1]][0]
                NFC += 1
                x += 1
                teams_in.append(database[NFC_tiebreaker[1]][0])
            NFC_tiebreaker.pop(1)
        else:
            conference_bucket = []
            w = 0
            while w < len(NFC_tiebreaker):
                conference_bucket.append(database[NFC_tiebreaker[w]][12])
                w += 1
            pick = NFC_tiebreaker[conference_bucket.index(max(conference_bucket))]
            team = database[pick][0]
            if NFC == 0:
                playoffs[12][1] = database[pick][0]
                NFC += 1
                x += 1
                teams_in.append(team)
            elif NFC == 1:
                playoffs[13][1] = database[pick][0]
                NFC += 1
                x += 1
                teams_in.append(team)
            elif NFC == 2:
                playoffs[14][1] = database[pick][0]
                NFC += 1
                x += 1
                teams_in.append(team)
            NFC_tiebreaker.pop(conference_bucket.index(max(conference_bucket)))
    else:
        print("3+ NFC")
        conference_bucket = []
        w = 0
        while w < len(NFC_tiebreaker):
            conference_bucket.append(database[NFC_tiebreaker[w]][12])
            w += 1
        pick = NFC_tiebreaker[conference_bucket.index(max(conference_bucket))]
        team = database[pick][0]
        if NFC == 0:
            playoffs[12][1] = database[pick][0]
            NFC += 1
            x += 1
            teams_in.append(team)
        elif NFC == 1:
            playoffs[13][1] = database[pick][0]
            NFC += 1
            x += 1
            teams_in.append(team)
        elif NFC == 2:
            playoffs[14][1] = database[pick][0]
            NFC += 1
            x += 1
            teams_in.append(team)
        NFC_tiebreaker.pop(conference_bucket.index(max(conference_bucket)))

##Draft Order
t = 1
draftbook = []
while t < len(database):
    a = database[t][0]
    b = database[t][1]
    sos = 0
    r = 0
    while r < len(database[t][3]):
        c = nflindex[database[t][3][r]]
        d = database[c][1]
        sos += d
        r += 1
    e = round((sos/(17*17)),3)
    draftbook.append([a,b,e])
    t += 1

draftbook.sort(key=lambda x:x[2])
draftbook.sort(key=lambda x:x[1])
filename ="scheduleoutput.csv"
with open(filename, "w",encoding="utf8") as output:
        writer = csv.writer(output, lineterminator="\n")
        writer.writerows(database)
        writer.writerows(playoffs)
        writer.writerows(draftbook)

print(teams_in)
