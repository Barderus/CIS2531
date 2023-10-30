'''
'''
import coin2 as c

def main():
    c.Coin.purpose()
    c.Coin.show_count()
    myCoin = c.Coin()
    print("Coins =", c.Coin.num_coins)
    myCoin.purpose()
    del myCoin
    c.Coin.show_count()

main()