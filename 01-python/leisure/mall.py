def draw_mall(height=14):
    if (height < 13):
        raise ValueError("Height must be at least 13.")

    print("                 __________________                 ")
    print("                |     |      |     |                ")
    print("                |     |      |     |                ")
    print("                |_____|______|_____|                ")
    print(" _______________|                  |_______________ ")
    print("|   _________   |      M A L L     |   _________   |")

    for i in range(height-13):
        print("|               |                  |               |")

    print("|               |      ______      |               |")
    print("|               |     |      |     |               |")
    print("|   _________   |     |      |     |   _________   |")
    print("|  |         |  |     |      |     |  |         |  |")
    print("|  |         |  |     |      |     |  |         |  |")
    print("|  |         |  |     |    o |     |  |         |  |")
    print("|__|_________|__|_____|______|_____|__|_________|__|")
    return
