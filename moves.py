import random
import monster as mon
jack_squat_phys={'Nil!': "Jack Squat lounges about...",'Squat!': random.randint(10,15),'Exist!': random.randint(5,10)}
jack_squat_magic={'Nil!': "Jack Squat lounges about...",'Schwave!': random.randint(20,25),'Sleep!': random.randint(14,30)}

gbPhys={'Gooblin Attack Force!': random.randint(10,20),'Pointy Assaulturu!': random.randint(5,16),'Full Charge!': 'Who knows?'}
gbMagic={'Gooblin Magic Force!': random.randint(10,20),'Magiku Assaulturu!': random.randint(5,16), 'Fireballs!': 'What will it be?' }

dgPhys={"Aerial Strike!": random.randint(15,21),"Shatter Scales!": random.randint(12,16),"Dragon's Fury!":random.randint(37,45)}
dgMagic={"Leftovers!": "maxHealth_D*0.4", "Bye!": "Dragonn makes its exit!", "Stall": "Both players did nothing"}
def js_moves(attack,enemy):
    if attack==1:
        chance=random.randint(0,14)
        if chance>=4:
            print(mon.monster_type(),"used",list(jack_squat_phys.items())[0][0])
            print(list(jack_squat_phys.items())[0][1])
            return 0
        elif chance>=2:
            print(mon.monster_type(),"used",list(jack_squat_phys.items())[1][0])
            return list(jack_squat_phys.items())[1][1]
        else:
            print(mon.monster_type(),"used",list(jack_squat_phys.items())[2][0])
            return list(jack_squat_phys.items())[2][1]
    else:
        chance=random.randint(0,14)
        if chance>=4:
            print(mon.monster_type(),"used",list(jack_squat_magic.items())[0][0])
            print(list(jack_squat_magic.items())[0][1])
            return 0
        elif chance>=2:
            print(mon.monster_type(),"used",list(jack_squat_magic.items())[1][0])
            return list(jack_squat_magic.items())[1][1]
        else:
            print(mon.monster_type(),"used",list(jack_squat_magic.items())[2][0])
            return 1

def gob_moves(attack):
    if attack==1:
        chance=random.randint(0,14)
        if chance>=8:
            print(mon.monster_type(),"used",list(gbPhys.items())[0][0])
            print("THE GOOBLINS ATTACK WITH ALL THEIR MIGHT!!!")
            return list(gbPhys.items())[0][1]
        elif chance>=4:
            print(mon.monster_type(),"used",list(gbPhys.items())[1][0])
            print("Teh pointiest of blades!")
            return list(gbPhys.items())[1][1]
        else:
            print(mon.monster_type(),"used",list(gbPhys.items())[2][0])
            choiceof3=random.randint(0,5)
            if choiceof3==0:
                print("A Full Scale Assualt!")
                return random.randint(17,22)
            elif choiceof3==2 or choiceof3==3:
                print("It's not all of them but it's something!")
                return random.randint(10,14)
            else:
                print("They tried their best...")
                return random.randint(3,7)
    else:
        chance=random.randint(0,14)
        if chance>=8:
            print(mon.monster_type(),"used",list(gbMagic.items())[0][0])
            print("THE GOOBLINS MAGIC WITH ALL THEIR MIGHT!!!")
            return list(gbMagic.items())[0][1]
        elif chance>=4:
            print(mon.monster_type(),"used",list(gbMagic.items())[1][0])
            print("Teh magicky of magics!")
            return list(gbMagic.items())[1][1]
        else:
            print(mon.monster_type(),"used",list(gbMagic.items())[2][0])
            choiceof3=random.randint(0,5)
            if choiceof3==0:
                print("A Full Scale Assualt!")
                return random.randint(17,22)
            elif choiceof3==2 or choiceof3==3:
                print("It's not all of them but it's something!")
                return random.randint(10,14)
            else:
                print("They tried their best...")
                return random.randint(3,7)

def dg_moves(attack,enemy):
    if attack==1:
        chance=random.randint(0,14)
        if chance>=8:
            print(mon.monster_type(),"used",list(dgPhys.items())[0][0])
            return list(dgPhys.items())[0][1]
        elif chance>=1:
            print(mon.monster_type(),"used",list(dgPhys.items())[1][0])
            return list(dgPhys.items())[1][1]
        else:
            print(mon.monster_type(),"used",list(dgPhys.items())[2][0])
            print("Dragonn is thrown into a frenzy!")
            return list(dgPhys.items())[2][1]
    else:
        chance=random.randint(0,14)
        if chance>=4:
            print(mon.monster_type(),"used",list(dgMagic.items())[0][0])
            return 0
        elif chance>=2:
            print(mon.monster_type(),"used",list(dgMagic.items())[1][0])
            return list(dgMagic.items())[1][1]
        else:
            print(mon.monster_type(),"used",list(dgMagic.items())[2][0])
            return 1
