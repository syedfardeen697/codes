#README FIRST.......

#NOTE! This Tool only recognize fardeen and boss names...so the script will only judge or interact perfectly with the feeded names common names will be responded locally...............eg The respond on entering "BOSS" and "FARDEEN" name will be so formal while as informal in other cases..


a=input("ENTER YOUR NAME: ");
x = "fardeen";
xi = "Fardeen";
xii = "FARDEEN";
y = "boss";
yi = "Boss";
yii = "BOSS";
b=("hey" + " " + a + " " + "HOW ARE YOU");
if a == x or a == xi or a==xii:
  print(b + " " + "| MAN");
elif a == y or a == yi or a == yii:
  print("HEY " + "GOOD-MORINING " + "SIR");
else:
  print("HELLO" + " " + a + " " + "HOW ARE YOU");


