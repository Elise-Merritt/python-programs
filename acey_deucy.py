# Elise Merritt
#
# A program that stimulates the card game Acey Deucey

from card_deck_class import PlayingCardDeck

#helper function for getting value of cards
def get_card_value(card):
    if(card[0]=='J'):
        return 11
    elif(card[0]=='K'):
        return 12
    elif(card[0]=='Q'):
        return 13
    elif(card[0]=='A'):
        return 14
    else:
        return int(card[0])

#Player starts by making initial bet
pot=float(input("Please put your initial bet into the pot. "))

#Sets up game by creating deck of cards
stop_game=False
cards_in_deck=['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD',
             'QD', 'KD', 'AD', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S'
             '10S', 'JS', 'QS', 'KS', 'AS']
playing_deck=PlayingCardDeck(cards_in_deck)

#Game goes until player wants to stop
while(stop_game==False):
    #assume deck is shuffled after every round because wikipedia game page doesn't say
    playing_deck.shuffle()
    #Deals first card and sets value
    card1=playing_deck.deal()
    print(card1)
    #if first card is ace, player decides if it is high (value 14) or low (value 1)
    if(card1[0]=='A'):
        is_High=int(input("Please enter 1 if this is the high Ace and 2 if this is the low Ace. "))
        if(is_High==2):
            card_val_1=1
    card_val1=get_card_value(card1)
    #Deals second and third cards and sets values
    card2=playing_deck.deal()
    print(card2)
    card_val2=get_card_value(card2)
    card3=playing_deck.deal()
    card_val3=get_card_value(card3)
    #If first and second card are equal, player can bet if third card is higher or lower
    if(card_val1==card_val2):
        #Player automatically loses if third card is an ace
        if(card_val3==14):
            print(card3)
            pot=pot+curr_bet
            print("Lost, new pot is"+str(pot))
        else:
            isHigh=int(input("Please enter 1 if you want to bet the third card is higher and 2 if you want to bet the third card is lower. "))
            print(card3)
            #Note bet is tripled if third card equals first two cards
            if(isHigh==1):
                if(card_val3<card_val1):
                    pot=pot+curr_bet
                    print("Lost, new pot is "+str(pot))
                elif(card_val3==card_val1):
                    pot=pot+curr_bet*3
                    print("Lost, new pot is "+str(pot))
                else:
                    pot=pot-curr_bet
                    print("Won, new pot is "+str(pot))
            else:
                if(card_val3<card_val1):
                    pot=pot-curr_bet
                    print("Won, new pot is "+str(pot))
                elif(card_val3==card_val1):
                    pot=pot+curr_bet*3
                    print("Lost, new pot is "+str(pot))
                else:
                    pot=pot+curr_bet
                    print("Lost, new pot is "+str(pot))
    else:
        #If first two cards are not equal, player bets if third card is between them
        curr_bet=float(input("How much do you want to bet the third card is between the other two? "))
        print(card3)
        if((card_val1<card_val3 and card_val2>card_val3) or (card_val2<card_val3 and card_val1>card_val3)):
            pot=pot-curr_bet
            print("Won, new pot is "+str(pot))
        elif((card_val1>card_val3  and card_val2>card_val3) or (card_val1<card_val3 and card_val2<card_val3)):
            pot=pot+curr_bet
            print("Lost, new pot is "+str(pot))
        elif(card_val1==card_val3 or card_val2==card_val3):
        #If third card equals one of first two cards, bet is doubled (quadrupled if third card is ace)
            if(card_val3==14):
                pot=pot+4*curr_bet
                print("Lost, new pot is "+str(pot))
            else:
                pot=pot+2*curr_bet
                print("Lost, new pot is "+str(pot))
    #Player decides whether or not to keep playing after every round
    keep_playing=int(input("Please enter 1 if you want to keep playing and 2 if you don't. "))
    if(keep_playing==2):
        stop_game=True
        
    
