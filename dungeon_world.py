import random
import time
import sys

magic = [{"name": "Firebolt", "cost": 5, "dmg": 30},
         {"name": "Spirit Bomb", "cost": 10, "dmg": 40},
         {"name": "Stupefy", "cost": 15, "dmg": 50}]

choice_magic = '''1. Firebolt
2. Spirit Bomb
3. Stupefy'''
class player:
    def __init__(self, name, hp, mp, atk, df, magic, spatk):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk = atk
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.actions = ["Attack", "Magic"]
        self.magic = magic
        self.spatk = spatk

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
    def generate_sp_damage(self):
        return self.spatk
    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)
    def take_damage(self):
        self.hp = self.hp - en_dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    def get_hp(self):
        return self.hp
    def get_maxhp(self):
        return self.maxhp
    def get_mp(self):
        return self.mp
    def get_maxmp(self):
        return self.maxmp
    def get_atk(self):
        return self.atk
    def get_spell_name(self, i):
        return self.magic[i]["name"]
    def get_spell_mp_cost(self, i):
        self.mp = self.mp - self.magic[i]["cost"]
        if self.mp < 0:
            self.mp = 0
            print("No more magic points left!")
        return self.mp
    def choose_action(self):
        i = 1
        for  item in self.actions:
            print(i, item)
            i = i + 1

class enemy:
    def __init__(self, name, hp, atk, df):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
    def take_damage(self):
        self.hp = self.hp - pl_dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    def take_team_damage(self):
        self.hp = self.hp - team_dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    def take_total_damage(self):
        self.hp = self.hp - (team_dmg + pl_dmg)
        if self.hp < 0:
            self.hp = 0
        return self.hp
    def take_sp_damage(self):
        self.hp = self.hp - sp_dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    def get_hp(self):
        return self.hp
    def get_df(self):
        return self.df
    def get_atk(self):
        return self.atk

class team:
    def __init__(self, hp, thp, atk):
        self.hp = hp
        self.atk = atk
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.thp = thp
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
    def take_damage(self):
        self.hp = self.hp - en_dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    def take_total_damage(self):
        self.thp = self.thp - en_dmg
        if self.thp < 0:
            self.thp = 0
        return self.thp
    def get_hp(self):
        return self.hp
    def get_atk(self):
        return self.atk
    def get_thp(self):
        return self.thp

l = ["Welcome", "to", "'The Dungeon World'"]
name = input("Profile name: ")
print('')
for i in l:
    time.sleep(.8)
    sys.stdout.flush()
    print(i, end=" ")
'''
for i in range(1):
    print('Welcome', end=" ")
    time.sleep(.2)
    print('to', end=" ")
    time.sleep(.5)
    print('"The Dungeon World"')
    '''
print('')
print("Loading", end="")
for i in range(3):
    time.sleep(1)
    sys.stdout.flush()
    print(".",end=" ")
print('\n')
print("Hello ", name + '.')
intro = '''Today is 28/11/2033 and you just turned 17. You just had an amazing party at your home and you really enjoyed.
All of your friends arrived and you had a great time. After the party was over, you were really tired so you decided to
go to bed. You were sleeping and in the middle of the night you heard screaming and shouting and some weird noises because
of which you woke up. You looked at the clock and it was 3:27am. Half sleepy, you got of your bed and left your room to see
what's going on. Rubbing your eyes, you saw everyone running here and there. It was bright outside but not because of the sun.
The entire town appeared like it was in a state of war.'''
for letter in intro:
    time.sleep(.011)
    sys.stdout.flush()
    print(letter, end='')
print("Your mother was panicking. She grabbed your hand and said," + name + '!',"We need to get out of here!")
intro2 = '''Quick! Wear your shoes. I got your stuff.'"' You wanted to ask what was going on but not a word came out of
your mouth. You went to brush your teeth because no matter what's going on in this world, you believe that hygiene is
very important. So you were brushing your teeth while everyone was scared and running here and there. 'Just kidding XD'",
"No, you did not go to brush your teeth. You were also scared af. So, where was I? Yea! You wanted to ask what's going on
but not a word came out of your mouth. Suddenly! The house started to quiver. The walls were trembling and the roof began
to fall. You and the others started running in order to get out of the house. It was a complete chaos. Suddenly, the floor
below you collapsed and you fell straight down to nowhere. While falling, you took a last look above and saw everyone was watching
you fall. They had stunned look on their faces as they could'nt do anything. You felt like it was the end of you.'''
for letter in intro2:
    time.sleep(.012)
    sys.stdout.flush()
    print(letter, end='')

'''
for i in range(100):
    print('=', end="")
    time.sleep(.2)
'''
#print(input("Press enter to continue:")
scene_one = '''After some time, You wake up and find yourself in a dark room. There is dirt all over you.
You take a look around. The walls appeared like those from medieval period and flambeaux were attached to them.
You stand up and check if you are hurt or not. Suddenly, you hear a sound of someone walking. But they were
no normal person's footsteps. It sounded as if with ever step, it was smashing the floor with it.
The sound was getting louder every second and you realize it was coming to you.
What would you do?
1. Hide
2. Stay and fight whoever is coming '''

print('\n')
for letter in scene_one:
    time.sleep(.015)
    sys.stdout.flush()
    print(letter, end='')


while True:
    choice1 = input("Enter Choice(1 or 2): ")
    try:
        choice1 = int(choice1)
    except:
        print("Invalid input!")
    if choice1 == 1 or choice1 == 2:
        break
print('')
if choice1 < 1 or choice1 > 2:
    print('Invalid input')
elif choice1 == 2:
    print(">>>It was a Giant Gorilla with red flashy eyes. It smashed you with both his hands.")
    print(">>>YOU DIED!")
    quit()
elif choice1 == 1:
    print(">>>A Giant Gorilla with red flashy eyes appeared. It did'nt see you and went ahead.")
    print(">>>You're safe.")

print('')
print(input("Press enter to continue"))

scene_two = '''You started walking in order to find a way out. As you were walking you heard a loud roar behind you.
You turned and saw that Giant Gorilla coming at you at full speed. You screamed and closed your eyes. Nothing happened!
You hear someone saying,"It's fine now". You opened your eyes and saw that Gorilla being slashed in half. Its body
fell and soon vanished in the ground.
Boy: There's nothing to worry about.
You: Who are you? and Where are we?
Boy: My name is Midoriya. It looks like something happened in the real world and we fell down here in the Dungeon.
You: IN THE WHAT??
Midoriya: Relax! I know it's hard to believe but right now, we need to find a way to get out of here. Here you have to
     those freaking monsters or else you will die. You were lucky I showed up in time.
You: That Gorilla Vanished. How?
Midoriya: We call it 'Ape-X'. It looks like the monsters cannot die here. You kill them and their bodies are absorbed
     by the ground. Soon they are respawned from the walls.
You: What the hell!
Midoriya: Yeah! I know it's crazy.
You: And what do you mean by 'WE'? Are there other people here?
Midoriya: Yea, there are many. I met a group of 5 individuals but got separated when a Demogorgan attacked us. It's the
     strongest monster in the dungeon. It spits fire and is really strong.
"LOUD ROAR"
Midoriya: Speak of the devil.
You: What was that?
Midoriya: It's a Demogorgan. Quick! Run!

The Demogorgan attacked you and Midoriya. It punched the groud and it tore apart. You fell down while screaming.
Midoriya was fighting the Demogorgan and you thought that he will die. But he asked you to keep going and he will find you.
So you went ahead.

You witnessed a really bright blue light coming for a room. You started walking towards it. When you entered the room,
you saw that a sword was standing stuck inside dozens of Big Crystals and the blue light was coming from those
Crystals.

What would you do?
1. Take out the sword
2. Take the Crystals and leave
'''
for letter in scene_two:
    time.sleep(.015)
    sys.stdout.flush()
    print(letter, end='')


while True:
    choice2 = input("Enter Choice(1 or 2): ")
    try:
        choice2 = int(choice2)
    except:
        print('Invalid input')
    if choice2 == 1 or choice2 == 2:
        break
print('')

if choice2 == 2:
    var = '''>>>You tried to move the Crystals but it didn't move. One of the Crystals move a bit so you pulled it out.
    The moment you pulled the Crystal out, The place started to break apart. The roof broke into pieces of
    big boulders and fell on you.
    YOU DIED!'''
    for letter in var:
        time.sleep(.015)
        sys.stdout.flush()
        print(letter, end='')
    quit()
elif choice2 == 1:
    var2 = '''>>>You grab hold of the sword and pulled it out. A weird sensation came from the sword and Blue shiny letters
    appeared on the sword and then disappeared. The Crystals buried itself in the floor.

    '''
    for letter in var2:
        time.sleep(.02)
        sys.stdout.flush()
        print(letter, end='')
print('\n')
scene_three = '''After you release the sword, you head out of the room where you find a big round monster
with about 10 tentacles, each having an eyeball at the end. It has one big eye at the center of the face
and a huge mouth with hundreds of sharp pointed teeth. It's name is "Beholder".
What would you do?
1. Fight it
2. Try to get out of there

'''

for letter in scene_three:
    time.sleep(.015)
    sys.stdout.flush()
    print(letter, end='')

while True:
    try:
        choice3 = int(input("Enter Choice(1 or 2): "))
    except:
        print('Invalid input')
    if choice3 == 1 or choice3 == 2:
        break

if choice3 == 1:
    var3 = '''>>>You plant your feet, tense your back, hold the sword firmly and get ready to fight.
Beholder rushes towards you and you bash with your sword. Beholder dodges and strikes the sword.
The sword fell down. Beholder came to attack again. You get scared and put both your hands in front
in a defensive position. That's when your hands throw fire and burned Beholder down to ashes. '''
    for letter in var3:
        time.sleep(.015)
        sys.stdout.flush()
        print(letter, end='')
elif choice3 == 2:
    var4 = '''>>>You try to find a way out. You are trying to go back to the sword room but Beholder
throws a boulder at you. you dodge by jumping out of its way. The boulder hit the wall and many rocks
fall down to cover the door of the sword room. Now there's only one way out for which you need to get
past Beholder. You decide that have to fight in order to survive.
    You plant your feet, tense your back, hold the sword firmly and get ready to fight.
Beholder rushes towards you and you bash with your sword. Beholder dodges and strikes the sword.
The sword fell down. Beholder came to attack again. You get scared and put both your hands in front
in a defensive position. That's when your hands throw fire and burned Beholder down to ashes.'''
    for letter in var4:
        time.sleep(.015)
        sys.stdout.flush()
        print(letter, end='')
print('')
print(input("Press any key to continue: "))
print('')
print("***Minotaur's Rage***")

print('')
scene_four = '''You have no clue what just happened but you feel happy that you just made it through.
The sword was alive and it give you some Magic Powers. Not everyone can pull out the sword. You were
able to pull out the sword because the sword chose you. It picks someone who has a good soul. Now,
you head forward. After walking for a while hoping that you don't witness any other monster, you hear
a loud roar and a Minotaur(a combination of a man and a bull) appeared in front of you with a morning
star in its hand. It's time for you to actually fight it.'''
for letter in scene_four:
    time.sleep(.015)
    sys.stdout.flush()
    print(letter, end='')
print('')
p1 = player(name, 100, 30, 25, 0, magic, 800)
e1 = enemy('Minotaur', 160, 15, 50)
e2 = enemy('Demogorgan', 1500, 110, 0)
tm = team(650, 1000, 60)
#enemy_hp = e1.get_hp()
#player_hp = p1.get_hp()
running = True
while running:
    print('============')
    print("ACTIONS")
    player.choose_action(p1)
    choice = input("Choose action: ")
    try:
        choice = int(choice)
    except:
        print("Invalid Input! Try Again...")
    print("You chose", choice)
    #if choice == 1 or choice ==2:
    #running = False

    if choice == 1:
        pl_dmg = p1.generate_damage()
        print("Damage given: ", pl_dmg)
        print("Enemy HP:",e1.take_damage())
        #enemy_hp = e1.get_hp()
        en_dmg = e1.generate_damage()
        print("Damage taken:", en_dmg)
        print("HP: ",p1.take_damage())
        #player_hp = p1.get_hp()
        #print("HP: ", player_hp)
        #print("Enemy HP: ", enemy_hp)
        if e1.get_hp() <= 8:
            print("FINAL BLOW!")
            print("Enemy Died. You Win!")
            break
        if p1.get_hp() == 0:
            print("You Died. Game Over!")
            break
        if e1.get_hp() == 0:
            print("Enemy died. You Win!")
            break
    elif p1.get_mp() > 0:
        if choice == 2:
            print(choice_magic)
            spell = int(input("Choose your Spell: ")) - 1
            if spell == 0:
                pl_dmg = p1.generate_spell_damage(0)
                print("Damage given: ",pl_dmg)
                print("Enemy HP: ", e1.take_damage())
                en_dmg = e1.generate_damage()
                print("Damage taken:", en_dmg)
                print("HP: ",p1.take_damage())
                print("MP: ", p1.get_spell_mp_cost(0))
                if e1.get_hp() <= 8:
                    print("FINAL BLOW!")
                    print("Enemy Died. You Win!")
                    break
                if p1.get_hp() == 0:
                    print("You Died. Game Over!")
                    break
                if e1.get_hp() == 0:
                    print("Enemy died. You Win!")
                    break
            if spell == 1:
                pl_dmg = p1.generate_spell_damage(1)
                print("Damage given: ",pl_dmg)
                print("Enemy HP: ", e1.take_damage())
                en_dmg = e1.generate_damage()
                print("Damage taken:", en_dmg)
                print("HP: ",p1.take_damage())
                print("MP: ", p1.get_spell_mp_cost(1))
                if e1.get_hp() <= 8:
                    print("FINAL BLOW!")
                    print("Enemy Died. You Win!")
                    break
                if p1.get_hp() == 0:
                    print("You Died. Game Over!")
                    break
                if e1.get_hp() == 0:
                    print("Enemy died. You Win!")
                    break
            if spell == 2:
                pl_dmg = p1.generate_spell_damage(2)
                print("Damage given: ",pl_dmg)
                print("Enemy HP: ", e1.take_damage())
                en_dmg = e1.generate_damage()
                print("Damage taken:", en_dmg)
                print("HP: ",p1.take_damage())
                print("MP: ", p1.get_spell_mp_cost(2))
                if e1.get_hp() <= 8:
                    print("YOU WIN!")
                    break
                if e1.get_hp() == 0:
                    print("FINAL BLOW!")
                    print("Enemy Died. You Win!")
                    break
                if p1.get_hp() == 0:
                    print("You Died. Game Over!")
                    break
                if e1.get_hp() == 0:
                    print("Enemy died. You Win!")
                    break
    elif p1.get_mp() == 0:
        print("No more Magic Points left!")

if e1.get_hp() <= 8 or e1.get_hp() == 0:
    print("You killed Minotaur")
    if e1.get_hp() <=8 and p1.get_hp() == 0:
        print("You managed to kill Minotaur but got seriously injured yourself in the batlle.")
        print("YOU DIED!")
#if e1.get_hp() == 0:
    #print("You Killed Minotaur!")
    #p1.player(name, 1, 30, 25, 0, magic)
if p1.get_hp() == 0:
    quit()

print(input("Press enter to continue:"))
print('')
var5 = '''When Minotaur died, it dropped a Polyjuice Potion and some small crystals.
You picked'em up and consumed the potion which restored your health. Infact, it gave
you 150% of the health, i.e. HP = 150.
Without wasting much time, you started moving again. On the way, you find a small
piece of metal in the ground. You try to pick it up but it would'nt come out.
What would you do?
1. Dig it out
2. Leave it and keep going
'''
for letter in var5:
    time.sleep(.015)
    sys.stdout.flush()
    print(letter, end='')

while True:
    try:
        choice4 = int(input("Enter Choice(1 or 2): "))
    except:
        print("Invalid input")
    if choice4 == 1 or choice4 == 2:
        break
print('')
if choice4 == 1:
    var6 = '''>>>You used your sword to dig in the ground. After a larger part of that metal
was visible, you used your hand to remove the rest of the dirt and take that thing out.
"I think there's something big in there", you said. You grabbed that thing with both
your hands and pulled it out.
    It looks like an old shield with some metal leg and arm pads. The shield was half
golden and half silver and had a big mark of a claw at the center. However, it does'nt
seem like that claw mark did any damage to the shield. You wear all the equipments.
The shield gave you the defence of 200 points which is added to your HP and raised your
magic points to 50.'''
    for letter in var6:
        time.sleep(.015)
        sys.stdout.flush()
        print(letter, end='')
    print(input('\n'"Press enter to view stats:"))
    print('')
    p1 = player(name, 350, 50, 25, 0, magic, 800)
    print("HP: ", p1.get_hp())
    print("MP: ", p1.get_mp())
    print('')
    print(input("Press enter to continue:"))

    scene_five = '''A bunch of other monsters appeared who are not as strong as Minotaur and you killed
them all. Your skills improve with every kill and so does your sword which also keeps on getting stronger with
every fight which increased your Attack Power by 5 points.'''
    print('')
    for letter in scene_five:
        time.sleep(.015)
        sys.stdout.flush()
        print(letter, end='')
    print('')
    print(input("Press enter to view stats:"))
    print("Current Stats:")
    p1 = player(name, 350, 50, 30, 0, magic, 800)
    print("HP: ", p1.get_hp())
    print("MP: ", p1.get_mp())
    print("AP: ", p1.get_atk())
    print(input("Press enter to continue:"))
    print('')
    print("In a hope to find the way out, you keep going forward where you finally meet Midoriya.")
    print("He was with a group of 8 people all wearing shields and had weapons. Midoriya introduced you with the group.")
    print("Midoriya: I forgot to ask your name.")
    print("You: Oh! Yea sorry.. My name is", name)
    scene_six = '''Midoriya: I am glad you are safe and woah! where did you find that sword and shield?
You: Well, the sword was in a room and it was stuck in a bunch of crystals. They were really big.
And the shield was buried in the ground.
Midoriya: Do you know to whom that sword and shield belong?
You: No. Who?
Midoriya: They belong to the most powerful person who was ever born 200 years ago. He fought the most powerful
          monster ever, The Black Dragon. Nobody knows his name but everyone call him " The Legendary Ace".
          There are rumours that he is still around somewhere living a normal life after defeating the Black
          Dragon. I think the real world was attacked by the monsters and it's the first attack since then.
You: *Amazed* WOW! He was that strong? I did'nt know that.
Midoriya: Also nobody was every able to find his sword and shield. This is the first time in 200 years that it
          showed itself.
You: Is that so?
Midoriya: Anyway, I am glad we found you. We found a way out of this Dungeon and we were about to head there.
You: That's amazing!

Midoriya said, "Let's move everybody! Let's not waste any more time."
Everyone headed towards the exit. You and the others killed some monsters that came in the way. "You have gotten
stronger since we last met", Midoriya said. "Thanks", you replied.
'''
    for letter in scene_six:
        time.sleep(.015)
        sys.stdout.flush()
        print(letter, end='')
    print(input('\n'"Press enter to view stats:"))
    print("Current Stats:")
    p1 = player(name, 350, 50, 32, 0, magic, 800)
    print("HP: ", p1.get_hp())
    print("MP: ", p1.get_mp())
    print("AP: ", p1.get_atk())
    print('')
    print(input('\n'"Press enter to continue:"))
    scene_seven = '''Everyone reached the exit and could see the light from outside. Everyone was so happy.
They started running towards the weird looking gate when the whole place started to vibrate and those vibrations
set the whole dungeon quaking. Suddenly! A huge Demogorgan showed up covering the exit of the Dungeon.
Everyone got scared but there was no other way to fight him. Everyone got into their fighting stance ready
fight that freaky thing. There was one religious guy in the group who saw the Demogorgan and said, "Oh Mighty Lord!
I feel so bad for this ugly faced creature. How can be someone so ugly? He must be dying because of his ugliness.
Give me the power to end his misery."
    Everyone said, "SHUT THE HELL UP!" and Midoriya reminded everyone that we need to fight together in order
to win. "IT'S ON!"
'''
    for letter in scene_seven:
        time.sleep(.015)
        sys.stdout.flush()
        print(letter, end='')
    print('')
    print("Your Stats:")
    print("HP: ", p1.get_hp())
    print("MP: ", p1.get_mp())
    print("AP: ", p1.get_atk())
    print("Team Stats:")
    print("Combined Team HP: ", tm.get_hp())
    print("Combined Team Attack: ", tm.get_atk())
    print("Total Team HP: ", tm.get_thp())
    print("Enemy Stats:")
    print("Demogorgan HP: ", e2.get_hp())
    print("Demogorgan Attack: ", e2.get_atk())

    while running:
        print('============')
        print("ACTIONS")
        player.choose_action(p1)
        choice = input("Choose action: ")
        try:
            choice = int(choice)
        except:
            print("Invalid Input! Try Again...")
        print("You chose", choice)

        if choice == 1:
            pl_dmg = p1.generate_damage()
            print("Damage Given: ", pl_dmg)
            #print("Demogorgan HP: ", e2.take_damage())
            team_dmg = tm.generate_damage()
            print("Team Damage Given: ", team_dmg)
            print("Demogorgan HP: ", e2.take_total_damage())
            en_dmg = e2.generate_damage()
            print("Damage Taken: ", en_dmg)
            print("Total Team HP:", tm.take_total_damage())
            if tm.get_thp() <= 100:
                print('')
                print("Team: We won't make it.")
                time.sleep(2)
                print("You: We will...no matter what...I WILL SAVE YOU!!")
                time.sleep(2)
                print("*Sword flashing producing lightening*")
                time.sleep(2)
                print("!!!!!VIOLENT STRIKE!!!!!")
                sp_dmg = p1.generate_sp_damage()
                time.sleep(2)
                print("Damage Given: ", sp_dmg)
                time.sleep(2)
                print("Demogorgan HP: ", e2.take_sp_damage())
                break
        elif p1.get_mp() > 0:
            if choice == 2:
                print(choice_magic)
                spell = int(input("Choose your Spell: ")) - 1
                if spell == 0:
                    pl_dmg = p1.generate_spell_damage(0)
                    print("Damage Given: ", pl_dmg)
                    print("Enemy HP:", e2.take_damage())
                    en_dmg = e2.generate_damage()
                    print("Damage Taken: ", en_dmg)
                    print("Total Team HP: ", tm.take_total_damage())
                    print("MP: ", p1.get_spell_mp_cost(0))
                    if tm.get_thp() <= 100:
                        print('')
                        print("Team: We won't make it.")
                        time.sleep(2)
                        print("You: We will...no matter what...I WILL SAVE YOU!!")
                        time.sleep(2)
                        print("*Sword flashing producing lightening*")
                        time.sleep(2)
                        print("!!!!!VIOLENT STRIKE!!!!!")
                        sp_dmg = p1.generate_sp_damage()
                        time.sleep(2)
                        print("Damage Given: ", sp_dmg)
                        time.sleep(2)
                        print("Demogorgan HP: ", e2.take_sp_damage())
                        break
                if spell == 1:
                    pl_dmg = p1.generate_spell_damage(1)
                    print("Damage Given: ", pl_dmg)
                    print("Enemy HP:", e2.take_damage())
                    en_dmg = e2.generate_damage()
                    print("Damage Taken: ", en_dmg)
                    print("Total Team HP: ", tm.take_total_damage())
                    print("MP: ", p1.get_spell_mp_cost(1))
                    if tm.get_thp() <= 100:
                        print('')
                        print("Team: We won't make it.")
                        time.sleep(2)
                        print("You: We will...no matter what...I WILL SAVE YOU!!")
                        time.sleep(2)
                        print("*Sword flashing producing lightening*")
                        time.sleep(2)
                        print("!!!!!VIOLENT STRIKE!!!!!")
                        sp_dmg = p1.generate_sp_damage()
                        time.sleep(2)
                        print("Damage Given: ", sp_dmg)
                        time.sleep(2)
                        print("Demogorgan HP: ", e2.take_sp_damage())
                        break
                if spell == 2:
                    pl_dmg = p1.generate_spell_damage(2)
                    print("Damage Given: ", pl_dmg)
                    print("Enemy HP:", e2.take_damage())
                    en_dmg = e2.generate_damage()
                    print("Damage Taken: ", en_dmg)
                    print("Total Team HP: ", tm.take_total_damage())
                    print("MP: ", p1.get_spell_mp_cost(2))
                    if tm.get_thp() <= 100:
                        print('')
                        print("Team: We won't make it.")
                        time.sleep(2)
                        print("You: We will...no matter what...I WILL SAVE YOU!!")
                        time.sleep(2)
                        print("*Sword flashing producing lightening*")
                        time.sleep(2)
                        print("!!!!!VIOLENT STRIKE!!!!!")
                        sp_dmg = p1.generate_sp_damage()
                        time.sleep(2)
                        print("Damage Given: ", sp_dmg)
                        time.sleep(2)
                        print("!!!!!Demogorgan HP: ", e2.take_sp_damage())
                        break
        elif p1.get_mp() == 0:
            print("No more Magic Points left!")

    print('')
    print("Midoriya: He did it!")
    print('')
    scene_eight = '''Everyone was barely able to stand but was feeling really happy. It was finally over and now the adventurers
could head out in the real world. They gathered energy and got out of the Dungeon. But when they got out, they saw that the
world has become a mess. There was no person around and the sky was bright red and black. There were some monsters roaming
here and there. Everyone was shocked and perplexed when they saw The Black Dragon sitting on the tallest building.
Midoriya: So the rumours were correct. There is a Black Dragon who had devastated the entire world 200 years ago and is now back.
You: There's no time to rest. We have to kill all those monsters.
Midoriya: No need. Even if we manage to kill all the monsters, we will never be able to leave a scratch on the Black Dragon.
You: It does'nt matter. We even thought we won't be able to defeat Demogorgan. But we did. We should atleast try. Someone
has to try.
Others: I agree with this kid. I think we should give everything we have got.
*Everyone got energized and started kill monsters - 10, 20, 50, 70. That's when The Black Dragon showed up in front of them.
They thought it's their end but then suddenly a knife flew over them and left a cut the Dragon's face. It got furious.
A voice said: It's alright now. You did good.*
Miidoriya: I...It...It's the Legendary Ace!!!!
Legendary Ace: No need to worry now. It's gonna be alright.
You: *Stare in shock*
Legendary Ace: You took good care of my equipments. Can I have it back now?
You: Yes please *You gave the sword and shield to Legendary Ace*
*The moment he held the sword in his hand, bright red symbols appeared on the sword and the size of the sword increased. The
Shield started to shine*
'''
    print(input("Press enter to continue: "))
    for letter in scene_eight:
        time.sleep(.007)
        sys.stdout.flush()
        print(letter, end='')

    scene_nine = '''Everyone saw the Legendary Ace fight the Black Dragon. He slashed the Dragon continuously with his sword and realeased some
sort of power which was capable of sealing the Dragon deep inside the Dungeon.
After that we never saw The Legendary Ace again. People say that he is an immortal God who is here to look after his children.
Some say he is an angel sent by god and some still think that he is just in stories.

                                                              **THE END**
'''
    for letter in scene_nine:
        time.sleep(.007)
        sys.stdout.flush()
        print(letter, end='')






elif choice4 == 2:
    print('''You did'nt waste any time trying to see what's in there so you just left.''')
    print('')
    p1 = player(name, 150, 30, 25, 0, magic, 0)
    print("HP: ", p1.get_hp())
    print("MP: ", p1.get_mp())

    scene_five = '''A bunch of other monsters appeared who are not as strong as Minotaur and you killed
them all. Your skills improve with every kill and so does your sword which also keeps on getting stronger with
every fight which increased your Attack Power by 5 points.'''
    print('')
    for letter in scene_five:
        time.sleep(.015)
        sys.stdout.flush()
        print(letter, end='')
    print('')
    print("Current Stats:")
    p1 = player(name, 150, 30, 30, 0, magic, 0)
    print("HP: ", p1.get_hp())
    print("MP: ", p1.get_mp())
    print("AP: ", p1.get_atk())

    print("In a hope to find the way out, you keep going forward where you finally meet Midoriya.")
    print("He was with a group of 8 people all wearing shields and had weapons. Midoriya introduced you with the group.")
    print("Midoriya: I forgot to ask your name.")
    print("You: Oh! Yea sorry.. My name is", name)
    scene_six = '''Midoriya: I am glad you are safe and woah! where did you find that sword?
You: Well, the sword was in a room and it was stuck in a bunch of crystals. They were really big.
Midoriya: Do you know to whom that sword belong?
You: No. Who?
Midoriya: It belongs to the most powerful person who was ever born 200 years ago. He fought the most powerful
          monster ever, The Black Dragon. Nobody knows his name but everyone call him " The Legendary Ace".
          There are rumours that he is still around somewhere living a normal life after defeating the Black
          Dragon. I think the real world was attacked by the monsters and it's the first attack since then.
You: *Amazed* WOW! He was that strong? I did'nt know that.
Midoriya: Also nobody was every able to find his sword. This is the first time in 200 years that it
          showed itself.
You: Is that so?
Midoriya: Anyway, I am glad we found you. We found a way out of this Dungeon and we were about to head there.
You: That's amazing!

Midoriya said, "Let's move everybody! Let's not waste any more time."
Everyone headed towards the exit. You and the others killed some monsters that came in the way. "You have gotten
stronger since we last met", Midoriya said. "Thanks", you replied.
'''
    for letter in scene_six:
        time.sleep(.015)
        sys.stdout.flush()
        print(letter, end='')
    print("Current Stats:")
    p1 = player(name, 150, 30, 32, 0, magic, 800)
    print("HP: ", p1.get_hp())
    print("MP: ", p1.get_mp())
    print("AP: ", p1.get_atk())
    print('')
    scene_seven = '''Everyone reached the exit and could see the light from outside. Everyone was so happy.
They started running towards the weird looking gate when the whole place started to vibrate and those vibrations
set the whole dungeon quaking. Suddenly! A huge sized Demogorgan showed up covering the exit of the Dungeon.
Everyone got scared but there was no other way to fight him. Everyone got into their fighting stance ready
fight that freaky thing. There was one religious guy in the group who saw the Demogorgan and said, "Oh Mighty Lord!
I feel so bad for this ugly faced creature. How can be someone so ugly? He must be dying because of his ugliness.
Give me the power to end his misery."
    Everyone said, "SHUT THE HELL UP!" and Midoriya reminded everyone that we need to fight together in order
to win. "IT'S ON!"
'''
    for letter in scene_seven:
        time.sleep(.015)
        sys.stdout.flush()
        print(letter, end='')
    print('')
    tm = team(650, 800, 60)
    print("Your Stats:")
    print("HP: ", p1.get_hp())
    print("MP: ", p1.get_mp())
    print("AP: ", p1.get_atk())
    print("Team Stats:")
    print("Combined Team HP: ", tm.get_hp())
    print("Combined Team Attack: ", tm.get_atk())
    print("Total Team HP: ", tm.get_thp())
    print("Enemy Stats:")
    print("Demogorgan HP: ", e2.get_hp())
    print("Demogorgan Attack: ", e2.get_atk())

    while running:
        print('============')
        print("ACTIONS")
        player.choose_action(p1)
        choice = input("Choose action: ")
        try:
            choice = int(choice)
        except:
            print("Invalid Input! Try Again...")
        print("You chose", choice)

        if choice == 1:
            pl_dmg = p1.generate_damage()
            print("Damage Given: ", pl_dmg)
            #print("Demogorgan HP: ", e2.take_damage())
            team_dmg = tm.generate_damage()
            print("Team Damage Given: ", team_dmg)
            print("Demogorgan HP: ", e2.take_total_damage())
            en_dmg = e2.generate_damage()
            print("Damage Taken: ", en_dmg)
            print("Damage Taken: ", en_dmg)
            print("Total Team HP:", tm.take_total_damage())
            if tm.get_thp() == 0:
                break

        elif p1.get_mp() > 0:
            if choice == 2:
                print(choice_magic)
                spell = int(input("Choose your Spell: ")) - 1
                if spell == 0:
                    pl_dmg = p1.generate_spell_damage(0)
                    print("Damage Given: ", pl_dmg)
                    print("Enemy HP:", e2.take_damage())
                    en_dmg = e2.generate_damage()
                    print("Damage Taken: ", en_dmg)
                    print("Total Team HP: ", tm.take_total_damage())
                    print("MP: ", p1.get_spell_mp_cost(0))
                    if tm.get_thp() == 0:
                        break

                if spell == 1:
                    pl_dmg = p1.generate_spell_damage(1)
                    print("Damage Given: ", pl_dmg)
                    print("Enemy HP:", e2.take_damage())
                    en_dmg = e2.generate_damage()
                    print("Damage Taken: ", en_dmg)
                    print("Total Team HP: ", tm.take_total_damage())
                    print("MP: ", p1.get_spell_mp_cost(1))
                    if tm.get_thp() == 0:
                        break

                if spell == 2:
                    pl_dmg = p1.generate_spell_damage(2)
                    print("Damage Given: ", pl_dmg)
                    print("Enemy HP:", e2.take_damage())
                    en_dmg = e2.generate_damage()
                    print("Damage Taken: ", en_dmg)
                    print("Total Team HP: ", tm.take_total_damage())
                    print("MP: ", p1.get_spell_mp_cost(2))
                    if tm.get_thp() == 0:
                        break

        elif p1.get_mp() == 0:
            print("No more Magic Points left!")
    print('')
    time.sleep(1)
    print("Demogorgan was too strong for you. You all had no chance against it.")
    time.sleep(.5)
    print("YOU DIED!!")
