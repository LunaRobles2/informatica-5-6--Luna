def main():
    receivers = ("Mario","Luigi","Daisy","Yoshi","Toad","Princess Peach","Bowser")
    for receiver in receivers:
        if receiver != "Princess Peach":
            print_letter("Princess Peach",receiver)

def print_letter(sender,receiver):
    print(f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {receiver},

    You are cordially invited to a ball at
    Peach's Castle this evening, 7:00 PM.

    Sincerely,
    {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
""")
main()