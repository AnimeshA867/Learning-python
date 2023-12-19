def info(temp):
    # Something something
    if temp>40:
      print("Too hot don't go.");
    elif temp>=30:
      print("Go It's fine.");
    elif temp>=20:
      print("Chill. But you can make it work.");
    elif temp>=10:
      print("It's starting to get cold in here. Don't go maybe.");
    else:
        print("Where do you live? In Siberia??")


temp=float(input("Enter today's temperature in Celcius:"))

info(temp)