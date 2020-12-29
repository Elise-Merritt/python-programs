# Elise Merritt
#
# Class that represents a deck of playing cards

#Random method shuffle used to shuffle card deck
from random import shuffle
class PlayingCardDeck:

    #Lists used as aids for functions in deck
    full_deck_in_order = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD',
             'QD', 'KD', 'AD', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S'
             '10S', 'JS', 'QS', 'KS', 'AS']
    jokers=['JC','JD','JH','JS']

    #Constructor that creates deck of cards
    def __init__(self, cards):
        self.actual_deck=cards
        #at start, no cards are dealt and deck isn't shuffled
        self.already_dealt=[]
        is_shuffled=False

    #Deals out card at top of deck
    def deal(self):
        for i in range(0, len(self.actual_deck)):
            curr_card=self.actual_deck[i]
            #Check if card at top of deck is valid
            if (not(curr_card in self.already_dealt) or self.is_shuffled==True):
                self.already_dealt.append(curr_card)
                self.actual_deck.remove(curr_card)
                return curr_card

    #Shuffles deck of cards
    def shuffle(self):
        shuffled_deck=[]
        #Adds cards to shuffled deck
        for i in range(0, len(self.actual_deck)):
            if(not(self.actual_deck[i] in self.jokers)):
                shuffled_deck.append(self.actual_deck[i])
        #Adds already-dealt cards to deck
        for i in range(0, len(self.already_dealt)-1):
            if(not(self.already_dealt[i] in self.jokers)):
                shuffled_deck.append(self.already_dealt[i])
        #Shuffles deck and updates needed variables
        self.is_shuffled=True
        shuffle(shuffled_deck)
        self.actual_deck=shuffled_deck
        return shuffled_deck

    #Fans out deck of cards by printing them
    def fan(self):
        for i in range(0, len(self.actual_deck)):
            print(self.actual_deck[i])

    #Puts deck of cards in order
    def Order(self):
        ordered_deck=[]
        #Uses list of all cards in order to order deck
        for i in range(0, len(self.full_deck_in_order)):
            if(self.full_deck_in_order[i] in self.actual_deck):
                ordered_deck.append(self.full_deck_in_order[i])
        self.actual_deck=ordered_deck
        return ordered_deck

    #Checks if deck is in order
    def isOrdered(self):
        ordered_deck=[]
        #First orders deck, then checks if result is actual deck
        for i in range(0, len(self.full_deck_in_order)):
            if(self.full_deck_in_order[i] in self.actual_deck):
                ordered_deck.append(self.full_deck_in_order[i])
        if(self.actual_deck==ordered_deck):
            return True
            

