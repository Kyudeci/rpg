import random
jack_squat_phys={'Nil': "Jack Squat lounges about...",'Squat': random.randint(10,15)}
jack_squat_magic={'Schwave': random.randint(20,25),'Sleep': random.randint(14,30)}
for x in range(1):
    y=random.randint(0,1)
    if y==0:
        print(jack_squat_phys['Nil'])
    else:
        print(jack_squat_phys['Squat'])
