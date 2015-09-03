ROUND_SUFFIX = ".rnd"
STANDINGS_SUFFIX = ".slp"

WHITE_ID = 2
BLACK_ID = 3
SCORE_ID = 4
SCORE_CODES = {"1":"1", "0.5": "3", "0": "2"}

######
# parse 
def parse(location):

    data = []
    
    rounds = []
    end = False;
    i = 1 ;
    while not end:
        try:
            file_name = location + "." + str(i) + ROUND_SUFFIX
            f = open(file_name)
            rounds.append(f.read())
            i += 1
        except FileNotFoundError:
            end = True

    num_rounds = len(rounds)
    num_players = getNumberOfPlayers(location);

    data.append([num_rounds, num_players])

    for round in rounds:
        data.append(parseDataFromRound(round, num_players))

    return data

def parseDataFromRound(round, num_players):
    games = []

    tables = round.split("\n")[1:-1];
    for table in tables:
        table_data = table.split("|")

        ## Turn auto-wins against "bye" into last player
        if (int(table_data[BLACK_ID]) == 0):
            table_data[BLACK_ID] = str(num_players + 1)
        if (int(table_data[WHITE_ID]) == 0):
            table_data[WHITE_ID] = str(num_players + 1)

        games.append([table_data[WHITE_ID],
                table_data[BLACK_ID],
                SCORE_CODES[table_data[SCORE_ID]]])

    return games

def getNumberOfPlayers(location):
    try:
        file_name = open(location + STANDINGS_SUFFIX)
        data = file_name.read().split("\n")
    except FileNotFoundError:
        print("Invalid file name")
        exit()

    return int(data[-2].split("|")[0])
