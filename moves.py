import random
import monster as mon
jack_squat_phys={'Nil': "Jack Squat lounges about...",'Squat': random.randint(10,15),'Exist': random.randint(5,10)}
jack_squat_magic={'Nil': "Jack Squat lounges about...",'Schwave': random.randint(20,25),'Sleep': random.randint(14,30)}

def js_moves(attack):
    if attack==1:
        chance=random.randint(0,14)
        if chance>=4:
            print(mon.monster_type(),"used",list(jack_squat_phys.items())[0][0],"!")
            print(list(jack_squat_phys.items())[0][1])
            return 0
        elif chance>=2:
            print(mon.monster_type(),"used",list(jack_squat_phys.items())[1][0],"!")
            return list(jack_squat_phys.items())[1][1]
        else:
            print(mon.monster_type(),"used",list(jack_squat_phys.items())[2][0],"!")
            return list(jack_squat_phys.items())[2][1]
    else:
        chance=random.randint(0,14)
        if chance>=4:
            print(mon.monster_type(),"used",list(jack_squat_magic.items())[0][0],"!")
            print(list(jack_squat_phys.items())[0][1])
            return 0
        elif chance>=2:
            print(mon.monster_type(),"used",list(jack_squat_magic.items())[1][0],"!")
            return list(jack_squat_magic.items())[1][1]
        else:
            print(mon.monster_type(),"used",list(jack_squat_magic.items())[2][0],"!")
            defender.hp=defender.hp+list(jack_squat_magic.items())[2][1]
            return 0
