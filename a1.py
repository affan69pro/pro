print("wanna play a game")
print("press 1 for car🚗")
print("press 2 for cycle🚲")
print("press 3 for jeep🚙")
print("press 4 for bus🚌")
ans=int(input())
if ans==1:
    print("you have chosen car🚗")
    print("press 1 for police car🚓")
    print("press 2 for F1 race car🏎")
    print("press 3 for rickshaw🛺")
    ans1=int(input())
    if ans1==1:
        print("you have chosen police car🚓")
        print("Hmm....you are a police 👮‍♂️")
    elif ans1==2:
        print("you have chosen F1 race car🏎")
        print("Hmm....you like to race🏃🏽‍♂️")
    else:
        print("you have chosen rckshaw🛺")
        print("Hmm....you are form south asia")
elif ans==2:
    print("you have chosen cycle 🚲")
    print("press 1 for scooter 🛴")
    print("press 2 for scooter motor 🛵")
    print("press 3 for motorbike 🏍")
    ans2=int(input())
    if ans2==1:
        print("you have chosen scooter 🛴")
        print("Hmm....you like scooters")
    elif ans2==2:
        print("you have chosen scooter motor 🛵")
        print("Hmm....you have a scooter motor")
    else:
        print("you have chosen motorbike 🏍")
        print("Hmm....you like riding motorbikes")
elif ans==3:
    print("you have chosen jeep🚙")
    print("press 1 for van🚐 ")
    print("press 2 for truck🚛")
    print("press 3 for truck2🚚")
    ans3=int(input())
    if ans3==1:
        print("you have chosen van🚐")
        print("Hmm....you have traveled in a van")
    elif ans3==2:
        print("you have chosen truck🚛")
        print("Hmm....are you a truck driver")
    else:
        print("you have chosen truck2🚚")
        print("Hmm....you like trucks")
else:
    print("you have chosen bus🚌")
    print("press 1 for bus2🚎")
    print("press 2 for ambulance🚑")
    print("press 3 for fire engine🚒")
    ans3=int(input())
    if ans3==1:
        print("you have bus2🚎")
        print("Hmm....you like buses")
    elif ans3==2:
        print("you have chosen ambulance🚑")
        print("Hmm....you wanna be a doctor")
    else:
        print("you have chosen fire engine🚒")
        print("Hmm....you are a firefighter👨🏽‍🚒")
        