Q = "On the %s%s day of Christmas\nmy true love sent to me:\n%s\n"
L = [
    "Twelve Drummers Drumming",
    "Eleven Pipers Piping",
    "Ten Lords a Leaping",
    "Nine Ladies Dancing",
    "Eight Maids a Milking",
    "Seven Swans a Swimming",
    "Six Geese a Laying",
    "Five Golden Rings",
    "Four Calling Birds",
    "Three French Hens",
    "Two Turtle Doves",
    "and a Partridge in a Pear Tree"
]

N = {1: "st", 2: "nd", 3: "rd"}

def J(*a):
    print Q % (x, N.get(x, "th"), "\n".join(a))

x = 1
J(L[-1][4:])
for x in range(2, 13):
    J(*L[12-x:])
