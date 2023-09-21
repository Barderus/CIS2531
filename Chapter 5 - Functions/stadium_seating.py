'''
'''
A = 20
B = 15
C = 10

def class_A(ticket):
    ttl_tickets = ticket * A
    return ttl_tickets

def class_B(ticket):
    ttl_tickets = ticket * B
    return ttl_tickets

def class_C(ticket):
    ttl_tickets = ticket * C
    return ttl_tickets


def main():
    Aseats = int(input("How many seats of class A were sold?: "))
    Bseats = int(input("How many seats of class B were sold?: "))
    Cseats = int(input("How many seats of class C were sold?: "))
    ttl_sold = class_A(Aseats) + class_B(Bseats) + class_C(Cseats)
    print("The total income generated from tickets was", format(ttl_sold,".2f"), "dollars" )

if __name__ == "__main__":
    main()
    