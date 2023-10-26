cp,sp = float(input("Enter Cost price : ")),float(input("Enter Selling price : "))
if sp<cp:
    print("Loss of rs.", cp-sp)
elif cp<sp:
    print("Profit of rs.", sp-cp)
else:
    print("No profit or loss.")