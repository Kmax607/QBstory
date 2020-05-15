import random

name = "Max"
number = "0"
team = "Max"
grade = "- FR -"
age = random.randint(15,16)

grades = ["- FR -","- SO -","- JR -","- SR -"]

first_name = ["Max", "Joe", "Teddy", "Xavier", "Miguel", "Anthony", "Richie", "Jeff", "Ethan", "Josh", "Noah", "Eli", "Ed", "Troy", "Dean", "Ben", "Jacob", "Kevin",  "Lou", "Mike", "Michael", "Patrick", "Len", "Paul", "CJ", "John", "Jon", "Andre", "Pierce", "Rob", "Joel", "Jacoby", "Mark", "JJ", "Zach", "Coby", "Brian", "Alfred", "Lamar", "Deshaun", "Mitch", "Chase", "Will", "Roger", "Scout", "Alex", "Gene", "Roslyn", "Austin", "Tavon", "Collin", "Jacoby", "Jonah", "Thomas", "Taylor", "James", "David", "Warren", "Joey", "Robin", "Lily", "Jim", "Pam", "Ryan", "Carson", "Kelly", "Stan", "Stanley", "Parker", "Marshall", "Brandon", "Kareem", "Jabari", "Logan", "Brittney", "Vincent", "Phil", "Brad", "Peter", "Randy", "Emmanuel", "Clark", "Scott", "Adam", "Daniel", "Hannah", "Nelson", "Rick", "Morty", "Jerry", "Homer", "Chris", "Stew", "Bob", "Bobby", "Gabe", "Evan", "Kyle", "Carmen", "Carter", "Steve", "Steven", "Aaron", "Charlie", "Morgan", "Robert", "Mack", "Jackson", "Luke", "Lucas", "Luka", "Oliver", "Harrison", "Harry", "Hugh", "Cole", "Allen", "Kenny", "Kevin", "Jeff", "Derek", "Jimmy", "Joakim", "Tyler", "Ty", "Nathan", "Nate", "Jason", "Fred", "Carrie", "Francis", "Malcolm", "Reese", "Hal", "Frank", "Brooke", "Nolan", "Niko", "Brennan", "Drew", "Dakota", "Tony", "Antonio", "Jack", "Ron", "Jude", "Howard", "Tavon", "Bruce", "Vandan", "Timothy", "John", "Michael", "Sam", "Andrew", "Dan", "John", "Kyle", "Kyler", "Bruce", "Andy", "Tanner", "Buzz", "Esteban", "Red", "Marshawn", "Darius", "Carmello"]
last_name = ["Kraus", "Chaiken", "Harris", "Smith", "Johnson", "Wufsus", "Rudd", "Kruger", "Shah", "Winger", "Malone", "Barnes", "Bryant", "Ali", "Scott", "Edwards", "Patrick", "Hershey", "Belg", "Snow", "Stark", "Fields", "Kammen", "Greenberg", "Jackson", "Carter", "McGrane", "Kornfeld", "White", "Black", "Turner", "Thomson", "Cranston", "Banks", "Watson", "Young", "Venable", "Watt", "Werth", "Hendricks", "Gilfoyle", "Woods", "Pecan", "Haut", "Hooper", "Liu", "Austin", "Price", "Williams", "Collins", "Jones", "Davis", "Green", "Robinson", "Thomas", "Wright", "Taylor", "Gabriel", "Miller", "King", "Lee", "Lew", "Walker", "Hamilton", "James", "Hill", "Gonzales", "Beasley", "Hall", "Marshall", "Hoover", "Parker", "Houston", "Granger", "Brown", "Garcia", "Sanders", "Rodriguez", "Hernandez", "Wilson", "Anderson", "Moore", "Lee", "Perez", "Clark", "King", "Scott", "Torres", "Adams", "Nelson", "Bighetti", "Baker", "Roberts", "Evans", "Diaz", "Simpson", "Blake", "Griffin", "Lewis", "Evans", "Cox", "Carter", "Tanaka", "Suzuki", "Stoker", "Morgan", "Quinn", "Mack", "Amend", "May", "Vasquez", "Stills", "Miller", "Jeffrey", "Rose", "Butler", "Noah", "Gasol", "Glasnow", "Robinson", "Fielder", "Pera", "Happ", "Souza", "Lavine", "Klein", "Armisen", "Brownstein", "Perkins", "Wilkerson", "Olson", "Franklin", "Brooks", "Nolan", "Ryan", "Shedlock", "Schwartz", "Singer", "Reed", "Richards", "Swanson", "Bush", "Morris", "Potter", "Weasley", "Law", "Luck", "Burback", "Burke", "Shanahan", "Lynch", "Walsh", "Cain", "Kane", "Lane", "Michaels", "Matthews", "Evans", "Trubisky", "Murray", "Allen", "Jobs", "Jeffrey", "Barkley", "Coulton", "Phillips", "Ray", "Durand", "Coughlin", "Davison", "Davis", "Sosa", "Johnson", "Smith", "Bernard", "Schmitt", "Agnew", "Woodley", "Fox", "Dempsey", "Wrigley", "Burrow", "Proche", "Robertson", "Robinson", "Lynch", "Wallace"]

wr1 = random.choice(first_name) + " " + random.choice(last_name)
wr1speed = random.randint(1,25)
wr1catch = random.randint(1,25)
wr1age = 0
wr1grade = random.choice(grades)
if wr1grade == "- FR -":
  wr1age = 15
if wr1grade == "- SO -":
  wr1age = 16
if wr1grade == "- JR -":
  wr1age = 17
if wr1grade == "- SR -":
  wr1age = 18

wr2 = random.choice(first_name) + " " + random.choice(last_name)
wr2speed = random.randint(1,22)
wr2catch = random.randint(1,22)
wr2age = 0
wr2grade = random.choice(grades)
if wr2grade == "- FR -":
  wr2age = 15
if wr2grade == "- SO -":
  wr2age = 16
if wr2grade == "- JR -":
  wr2age = 17
if wr2grade == "- SR -":
  wr2age = 18

te = random.choice(first_name) + " " + random.choice(last_name)
tespeed = random.randint(1,19)
tecatch = random.randint(1,30)
teage = 0
tegrade = random.choice(grades)
if tegrade == "- FR -":
  teage = 15
if tegrade == "- SO -":
  teage = 16
if tegrade == "- JR -":
  teage = 17
if tegrade == "- SR -":
  teage = 18

rb = random.choice(first_name) + " " + random.choice(last_name)
rbspeed = random.randint(1,32)
rbcatch = random.randint(1,19)
rbage = 0
rbgrade = random.choice(grades)
if rbgrade == "- FR -":
  rbage = 15
if rbgrade == "- SO -":
  rbage = 16
if rbgrade == "- JR -":
  rbage = 17
if rbgrade == "- SR -":
  rbage = 18

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

weightslvl = 0
sprintsslvl = 0
coneslvl = 0
tirelvl = 0
passlvl = 0

def get_name():
  global name
  global number
  global team
  team = random.choice(high_schools)
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
  overall = round(ovr, 2)
  print(str(overall) + " OVR - " + str(strength) + " STR - " + str(shortacc) + " SAC - " + str(longacc) + " LAC - " + str(speed) + " SPD - " + str(agility) + " AGL")

def train():
  global strength
  global shortacc
  global longacc
  global speed
  global agility
  print("BENCH | SPRINT | CONES | TARGET TOSS | LONG TOSS")
  train_type = input("How would you like to train? ").lower()
  train_effect = random.randint(1,3) 
  while train_type != "bench" and train_type != "sprint" and train_type != "cones" and train_type != "target toss" and train_type != "long toss":
    print("BENCH | SPRINT | CONES | TARGET TOSS | LONG TOSS")
    train_type = input("Enter a valid training method: ").lower()
  if train_type == "bench":
    strength += train_effect
  if train_type == "sprint":
    speed += train_effect
  if train_type == "cones":
    agility += train_effect
  if train_type == "target toss":
    shortacc += train_effect
  if train_type == "long toss":
    longacc += train_effect
  print()
  print_dash()

def print_training():
  global weightslvl
  global sprintsslvl
  global coneslvl
  global tirelvl
  global passlvl
  print("Weights - Level " + str(weightslvl))
  print("Track   - Level " + str(sprintsslvl))
  print("Cones   - Level " + str(weightslvl))
  print("Targets - Level " + str(weightslvl))
  print("Field   - Level " + str(weightslvl))

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
  print(team)
  print("#" + number + " " + name + " - QB " + grade + " " + str(age))
  print("#" + wr1_num + " " + wr1 + " - WR - " + str(wr1speed) + " SPD - " + str(wr1catch) + " CAT " + wr1grade + " " + str(wr1age))
  print("#" + wr2_num + " " + wr2 + " - WR - " + str(wr2speed) + " SPD - " + str(wr2catch) + " CAT " + wr2grade + " " + str(wr2age))
  print("#" + te_num + " " + te + " - TE - " + str(tespeed) + " SPD - " + str(tecatch) + " CAT " + tegrade + " " + str(teage))
  print("#" + rb_num + " " + rb + " - RB - " + str(rbspeed) + " SPD - " + str(rbcatch) + " CAT " + rbgrade + " " + str(rbage))
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
  print("#" + number + " " + name + " - QB - " + team + " " + grade + " " + str(age) + " - $" + str(money))
  print_stats()
  print()
  print_training()
  print()
  print("PLAY | SEE TEAM | TRAIN")
  option = input("Select an option: ").lower()
  while option != "play" and option != "see team" and option != "train":
    print("Enter a valid option:")
    print("PLAY | SEE TEAM | TRAIN")
    option = input("Select an option: ").lower()
  print()
  if option == "play":
    pass
  if option == "see team":
    print_team()
  if option == "train":
    train()

def start():
  get_name()
  get_archetype()
  get_team_numbers()
  print_dash()

start()