import random
from distlib.compat import raw_input


def guess(a, b, p):
    gs = int(raw_input("guess the no.\n"))
    gs1 = 1
    while gs != p:
        if gs > p:
            gs = int(input("try less one:\n"))
            gs1 += 1    # q1 is actual value...........
            print("this is your %d gs" % gs1)

        elif gs < p:
            gs = int(input("try grtr one:\n"))
            gs1 += 1
            print("this is your %d gs" % gs1)

        elif gs == p:
            print("oooohoooo!!!*&*&.... correct guess....***\n")
            print("this is your %d gs" % gs1)
            break

        else:
            print("...")

    print(f"u hve guessed the numbr in {gs1} trials...\n")
    return gs1

if __name__ == "__main__":
    print("✨😎 WEL-COME TO THE GAME 'GUESS THE NUMBER'😎✨\n")
    a = int(input("😉enter the first no......\n"))
    b = int(input("😁enter the second no......\n"))

    # q1 is actual value...........
    q1 = random.randint(a, b)
    # print(p)
    print("player 1, pls play ur turn...\n")
    p1 = guess(a, b, q1)

    print("player 2, pls play ur turn...\n")
    # q is actual value...........
    q = random.randint(a, b)
    p2 = guess(a, b, q)

    if p1 > p2:
        print("p2 won the gme.....\n")
    elif p1 < p2:
        print("p1 won the gme.....\n")
    elif p1 == p2:
        print("And it tie....\n")
    else:
        print("..........")



