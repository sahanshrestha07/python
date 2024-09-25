def shipping(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
        print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping("Dr.","Spongebob","Squarepants","III",
         street = "123 Fake ST",
         city = "Atlanta",
         state = "GA",
         zip = "30324",
         )