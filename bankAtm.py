class Atm(object):
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    
    def cashWithdrawl(self):
        print('How much cash do you want to withdraw')

    def balanceEnquiry(self):
        print('You balance is 0')
    
    def expiredCard(self):
        print('Your card is expired')

    def withdrawing(self):
        print('Your money is withdrawing')

card = Atm('840398502', '584023850432')
print(card.card_number, card.pin_number)