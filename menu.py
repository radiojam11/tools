
def menu():
  
  x = 1
  while x !=0 :
    print ("                   Menu'")
    print("            Descrizione Menu")
    print(" VOCE MENU.....digita 1 --> ")
    print(" VOCE MENU.... digita 2 --> ")
    x = input("scegli cosa vuoi fare digita 0 per uscire............... --> ")
    if x == "1":
      return 1
    elif x == "2":
      return 2
    elif x == "0":
      x = 0
    else:
      print(" sei di coccio!!")
      x = 1
  print("Hai scelto di uscire, Ciao!")
  return 0


scelta = menu()
if scelta == 1:
  pass
elif scelta == 2:
  pass
else:
  pass


