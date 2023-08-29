print("Welcome To Ahmed Calculator")
wwo = "y"
while wwo == "y":
    wow = input("IF you Want to Add type + To subtract type - type / for division for multiplication type * ")
    rog = input("First Digit ")
    rog1 = input("Second Digit ")
    wwo = "n"
    if wow == "+":
        OL = int(rog) + int(rog1)
        print(OL)
        que = input("Do you want to Calculate Again ")
        if que == "y" or que == "yes" or que == "Y" or que == "Yes":
            wwo = "y"
        else:
            break    
    elif wow == "-":
          OL = int(rog) - int(rog1)
          print(OL)
          que = input("Do you want to Calculate Again ")
          if que == "y" or que == "yes" or que == "Y" or que == "Yes":
              wwo = "y"
          else:
              break
    else:
        if wow == "/":
            OL = int(rog) / int(rog1)
            print(OL)
            que = input("Do you want to Calculate Again ")
            if que == "y" or que == "yes" or que == "Y" or que == "Yes":
                wwo = "y"
            else:
                break
        else:
            OL = int(rog) * int(rog1)
            print(OL)
            que = input("Do you want to Calculate Again ")
            if que == "y" or que == "yes" or que == "Y" or que == "Yes":
                wwo = "y"
            else:
                break    


