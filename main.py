import random

name = "Max"
number = "0"
team = "Max"
grade = "- FR -"
age = random.randint(14,15)
energy = 10

league = "high school"

grades = ["- FR -","- SO -","- JR -","- SR -"]

wins = 0
losses = 0

first_name = ["Max", "Joe", "Teddy", "Xavier", "Miguel", "Anthony", "Richie", "Jeff", "Ethan", "Josh", "Noah", "Eli", "Ed", "Troy", "Dean", "Ben", "Jacob", "Kevin",  "Lou", "Mike", "Michael", "Patrick", "Len", "Paul", "CJ", "John", "Jon", "Andre", "Pierce", "Rob", "Joel", "Jacoby", "Mark", "JJ", "Zach", "Coby", "Brian", "Alfred", "Lamar", "Deshaun", "Mitch", "Chase", "Will", "Roger", "Scout", "Alex", "Gene", "Roslyn", "Austin", "Tavon", "Collin", "Jacoby", "Jonah", "Thomas", "Taylor", "James", "David", "Warren", "Joey", "Robin", "Lily", "Jim", "Pam", "Ryan", "Carson", "Kelly", "Stan", "Stanley", "Parker", "Marshall", "Brandon", "Kareem", "Jabari", "Logan", "Brittney", "Vincent", "Phil", "Brad", "Peter", "Randy", "Emmanuel", "Clark", "Scott", "Adam", "Daniel", "Hannah", "Nelson", "Rick", "Morty", "Jerry", "Homer", "Chris", "Stew", "Bob", "Bobby", "Gabe", "Evan", "Kyle", "Carmen", "Carter", "Steve", "Steven", "Aaron", "Charlie", "Morgan", "Robert", "Mack", "Jackson", "Luke", "Lucas", "Luka", "Oliver", "Harrison", "Harry", "Hugh", "Cole", "Allen", "Kenny", "Kevin", "Jeff", "Derek", "Jimmy", "Joakim", "Tyler", "Ty", "Nathan", "Nate", "Jason", "Fred", "Carrie", "Francis", "Malcolm", "Reese", "Hal", "Frank", "Brooke", "Nolan", "Niko", "Brennan", "Drew", "Dakota", "Tony", "Antonio", "Jack", "Ron", "Jude", "Howard", "Tavon", "Bruce", "Vandan", "Timothy", "John", "Michael", "Sam", "Andrew", "Dan", "John", "Kyle", "Kyler", "Bruce", "Andy", "Tanner", "Buzz", "Esteban", "Red", "Marshawn", "Darius", "Carmello"]
last_name = ["Kraus", "Chaiken", "Harris", "Smith", "Johnson", "Wufsus", "Rudd", "Kruger", "Shah", "Winger", "Malone", "Barnes", "Bryant", "Ali", "Scott", "Edwards", "Patrick", "Hershey", "Belg", "Snow", "Stark", "Fields", "Kammen", "Greenberg", "Jackson", "Carter", "McGrane", "Kornfeld", "White", "Black", "Turner", "Thomson", "Cranston", "Banks", "Watson", "Young", "Venable", "Watt", "Werth", "Hendricks", "Gilfoyle", "Woods", "Pecan", "Haut", "Hooper", "Liu", "Austin", "Price", "Williams", "Collins", "Jones", "Davis", "Green", "Robinson", "Thomas", "Wright", "Taylor", "Gabriel", "Miller", "King", "Lee", "Lew", "Walker", "Hamilton", "James", "Hill", "Gonzales", "Beasley", "Hall", "Marshall", "Hoover", "Parker", "Houston", "Granger", "Brown", "Garcia", "Sanders", "Rodriguez", "Hernandez", "Wilson", "Anderson", "Moore", "Lee", "Perez", "Clark", "King", "Scott", "Torres", "Adams", "Nelson", "Bighetti", "Baker", "Roberts", "Evans", "Diaz", "Simpson", "Blake", "Griffin", "Lewis", "Evans", "Cox", "Carter", "Tanaka", "Suzuki", "Stoker", "Morgan", "Quinn", "Mack", "Amend", "May", "Vasquez", "Stills", "Miller", "Jeffrey", "Rose", "Butler", "Noah", "Gasol", "Glasnow", "Robinson", "Fielder", "Pera", "Happ", "Souza", "Lavine", "Klein", "Armisen", "Brownstein", "Perkins", "Wilkerson", "Olson", "Franklin", "Brooks", "Nolan", "Ryan", "Shedlock", "Schwartz", "Singer", "Reed", "Richards", "Swanson", "Bush", "Morris", "Potter", "Weasley", "Law", "Luck", "Burback", "Burke", "Shanahan", "Lynch", "Walsh", "Cain", "Kane", "Lane", "Michaels", "Matthews", "Evans", "Trubisky", "Murray", "Allen", "Jobs", "Jeffrey", "Barkley", "Coulton", "Phillips", "Ray", "Durand", "Coughlin", "Davison", "Davis", "Sosa", "Johnson", "Smith", "Bernard", "Schmitt", "Agnew", "Woodley", "Fox", "Dempsey", "Wrigley", "Burrow", "Proche", "Robertson", "Robinson", "Lynch", "Wallace"]

wr1 = random.choice(first_name) + " " + random.choice(last_name)
wr1speed = random.randint(1,25)
wr1catch = random.randint(1,25)
wr1age = 0
wr1grade = random.choice(grades)
if wr1grade == "- FR -":
  wr1age = 14
if wr1grade == "- SO -":
  wr1age = 15
if wr1grade == "- JR -":
  wr1age = 16
if wr1grade == "- SR -":
  wr1age = 17

wr2 = random.choice(first_name) + " " + random.choice(last_name)
wr2speed = random.randint(1,22)
wr2catch = random.randint(1,22)
wr2age = 0
wr2grade = random.choice(grades)
if wr2grade == "- FR -":
  wr2age = 14
if wr2grade == "- SO -":
  wr2age = 15
if wr2grade == "- JR -":
  wr2age = 16
if wr2grade == "- SR -":
  wr2age = 17

te = random.choice(first_name) + " " + random.choice(last_name)
tespeed = random.randint(1,19)
tecatch = random.randint(1,30)
teage = 0
tegrade = random.choice(grades)
if tegrade == "- FR -":
  teage = 14
if tegrade == "- SO -":
  teage = 15
if tegrade == "- JR -":
  teage = 16
if tegrade == "- SR -":
  teage = 17

rb = random.choice(first_name) + " " + random.choice(last_name)
rbspeed = random.randint(1,32)
rbcatch = random.randint(1,19)
rbage = 0
rbgrade = random.choice(grades)
if rbgrade == "- FR -":
  rbage = 14
if rbgrade == "- SO -":
  rbage = 15
if rbgrade == "- JR -":
  rbage = 16
if rbgrade == "- SR -":
  rbage = 17

olovr = random.randint(2,30)
dl = random.randint(2,30)
lb = random.randint(2,30)
db = random.randint(2,30)

acceptable_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]
wr_numbers = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89"]
te_numbers = ["40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89"]
rb_numbers = ["20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30" "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49"]

high_schools = ["Grandview Academy", "Clearwater High", "Oakwood High", "Lincoln Prep", "Riverbank High", "Central Valley Academy"]

money = 0

strength = 0
shortacc = 0
longacc = 0
speed = 0
agility = 0

weightslvl = 1
tracklvl = 1
coneslvl = 1
targetslvl = 1
fieldlvl = 1

def get_name():
  global name
  global number
  global team
  team = random.choice(high_schools)
  high_schools.remove(team)
  name = input("Enter your name: ")
  number_req = input("Enter your number request: ")
  while number_req not in acceptable_numbers:
    number_req = input("Enter a number from 1-19: ")
  get_request = random.randint(1,3)
  if get_request == 1:
    number = random.choice(acceptable_numbers)
  else:
    number = number_req
  print()

def get_archetype():
  global strength
  global shortacc
  global longacc
  global speed
  global agility
  print("Strong - 6 STR - 2 SAC - 3 LAC - 1 SPD - 1 AGL")
  print("Accurate - 2 STR - 5 SAC - 4 LAC - 1 SPD - 1 AGL")
  print("Mobile - 1 STR - 3 SAC - 1 LAC - 6 SPD - 5 AGL")
  arch = input("Choose your archetype: ").lower()
  while arch != "strong" and arch != "accurate" and arch != "mobile":
    arch = input("Enter a valid archtype: ").lower()
  if arch == "strong":
    strength = 6
    shortacc = 2
    longacc = 3
    speed = 1
    agility = 1
  if arch == "accurate":
    strength = 2
    shortacc = 5
    longacc = 4
    speed = 1
    agility = 1
  if arch == "mobile":
    strength = 1
    shortacc = 3
    longacc = 1
    speed = 6
    agility = 5
  print()

def print_stats():
  global strength
  global shortacc
  global longacc
  global speed
  global agility
  ovr = (strength + shortacc + longacc + speed + agility) / 5
  overall = round(ovr, 1)
  rstrength = round(strength,1)
  rshortacc = round(shortacc,1)
  rlongacc = round(longacc,1)
  rspeed = round(speed,1)
  ragility = round(agility,1)
  print(str(overall) + " OVR - " + str(rstrength) + " STR - " + str(rshortacc) + " SAC - " + str(rlongacc) + " LAC - " + str(rspeed) + " SPD - " + str(ragility) + " AGL")

def train():
  global strength
  global shortacc
  global longacc
  global speed
  global agility
  global weightslvl
  global tracklvl
  global coneslvl
  global targetslvl
  global fieldlvl
  global energy
  energycost = random.randint(1,2)
  if energy < energycost:
    print("You're too tired to train. Come back with more energy")
  else:
    print("LIFT | SPRINT | CONES | TARGET TOSS | LONG TOSS")
    train_type = input("How would you like to train? ").lower()
    train_effect = (0.1 * random.randint(1,3))
    while train_type != "lift" and train_type != "sprint" and train_type != "cones" and train_type != "target toss" and train_type != "long toss":
      print("LIFT | SPRINT | CONES | TARGET TOSS | LONG TOSS")
      train_type = input("Enter a valid training method: ").lower()
    if train_type == "lift":
      strength += (train_effect * weightslvl)
    if train_type == "sprint":
      speed += (train_effect * tracklvl)
    if train_type == "cones":
      agility += (train_effect * coneslvl)
    if train_type == "target toss":
      shortacc += (train_effect * targetslvl)
    if train_type == "long toss":
      longacc += (train_effect * fieldlvl)
    energy -= energycost
  print()
  print_dash()

def print_training():
  global weightslvl
  global tracklvl
  global coneslvl
  global targetslvl
  global fieldlvl
  print("Weights - Level " + str(weightslvl))
  print("Track   - Level " + str(tracklvl))
  print("Cones   - Level " + str(coneslvl))
  print("Targets - Level " + str(targetslvl))
  print("Field   - Level " + str(fieldlvl))

def get_team_numbers():
  global wr1_num
  global wr2_num
  global te_num
  global rb_num
  global number
  if number in wr_numbers:
    wr_numbers.remove(number)
  wr1_num = random.choice(wr_numbers)
  wr_numbers.remove(wr1_num)
  if wr1_num in te_numbers:
    te_numbers.remove(wr1_num)
  wr2_num = random.choice(wr_numbers)
  if wr2_num in te_numbers:
    te_numbers.remove(wr2_num)
  te_num = random.choice(te_numbers)
  if te_num in rb_numbers:
    rb_numbers.remove(te_num)
  rb_num = random.choice(rb_numbers)

def print_team():
  global wr1
  global wr1speed
  global wr1catch
  global wr1age
  global wr1grade
  global wr2
  global wr2speed
  global wr2catch
  global wr2age
  global wr2grade
  global te
  global tespeed
  global tecatch
  global teage
  global tegrade
  global wr1_num
  global wr2_num
  global te_num
  global rb_num
  global grade
  global age
  global team
  global name
  global wins
  global losses
  global olovr
  global dl
  global db
  global lb
  print(team + " " + str(wins) + "-" + str(losses))
  print("#" + number + " " + name + " - QB " + grade + " " + str(age))
  print("#" + wr1_num + " " + wr1 + " - WR - " + str(wr1speed) + " SPD - " + str(wr1catch) + " CAT " + wr1grade + " " + str(wr1age))
  print("#" + wr2_num + " " + wr2 + " - WR - " + str(wr2speed) + " SPD - " + str(wr2catch) + " CAT " + wr2grade + " " + str(wr2age))
  print("#" + te_num + " " + te + " - TE - " + str(tespeed) + " SPD - " + str(tecatch) + " CAT " + tegrade + " " + str(teage))
  print("#" + rb_num + " " + rb + " - RB - " + str(rbspeed) + " SPD - " + str(rbcatch) + " CAT " + rbgrade + " " + str(rbage))
  print("OL - " + str(olovr))
  print("DL - " + str(dl))
  print("LB - " + str(lb))
  print("DB - " + str(db))  
  print()
  input("Press Enter to Continue ")
  print()
  print_dash()

def print_dash():
  global name
  global money
  global number
  global team
  global grade
  global age
  global energy
  print("#" + number + " " + name + " - QB - " + team + " " + grade + " " + str(age) + " - $" + str(money) + " - " + str(energy) + " Energy")
  print_stats()
  print()
  print_training()
  print()
  print("PLAY | SEE TEAM | TRAIN | SHOP")
  option = input("Select an option: ").lower()
  while option != "play" and option != "see team" and option != "train" and option != "shop":
    print("Enter a valid option:")
    print("PLAY | SEE TEAM | TRAIN | SHOP")
    option = input("Select an option: ").lower()
  print()
  if option == "play":
    season()
  if option == "see team":
    print_team()
  if option == "train":
    train()
  if option == "shop":
    shop()

def season():
  league
  if league == "high school":
    opponents = high_schools
    season_length = 8
  if wins + losses < season_length:
    play(random.choice(opponents))
  print_dash()

def play(opponent):
  global team
  high_schools.remove(opponent)
  home_or_away = random.randint(1,2)
  if home_or_away == 1:
    print(team + " at " + opponent)
  else:
    print(opponent + " at " + team)
  input("Press enter to continue")

pos = "OFF"

def possession():
  global pos
  time = 60
  if time > 45:
    quarter == 1
  elif time < 45 and time > 30:
    quarter == 2
  elif time == 30:
    print("Halftime")
  elif time < 45 and time < 15:
    quarter == 3
  elif time < 15:
    quarter == 4
  elif time == 0:
    print("Game over")
  if pos == "OFF":
    pos = "DEF"
    time
  else:
    pos = "OFF"

weights_price = 5
track_price = 5
cones_price = 5
targets_price = 5
field_price = 5

def shop():
  global money
  global weights_price
  global track_price
  global cones_price
  global targets_price
  global field_price
  global weightslvl
  global tracklvl
  global coneslvl
  global targetslvl
  global fieldlvl
  global money
  print("UPGRADE WEIGHTS - $" + str(weights_price) + " | UPGRADE TRACK - $" + str(track_price) + " | UPGRADE CONES  - $" + str(cones_price) + " | UPGRADE TARGETS  - $" + str(targets_price) + " | UPGRADE FIELD $- " + str(field_price))
  purchase = input("What would you like to buy? ").lower()
  while "weights" not in purchase and "track" not in purchase and "cones" not in purchase and "targets" not in purchase and "field" not in purchase:
    purchase = input("Enter a valid item ").lower()
  if "weights" in purchase:
    weightslvl += 1
    money -= weights_price
    weights_price += 5
  if "track" in purchase:
    tracklvl += 1
    money -= track_price
    track_price += 5
  if "cones" in purchase:
    coneslvl += 1
    money -= cones_price
    cones_price += 5
  if "targets" in purchase:
    targetslvl += 1
    money -= targets_price
    targets_price += 5
  if "field" in purchase:
    fieldlvl += 1
    money -= field_price
    field_price += 5
  else:
    print_dash()

def start():
  get_name()
  get_archetype()
  get_team_numbers()
  print_dash()

start()