import decimal
from decimal import *

class main:
    def __init__(self,item_to_offer,item_for_trade,calculation_type,average_item_per_block,price_of_block,price_per_stack_in_shop,margin_desired):
        setcontext(Context(prec=5))
        self.item_to_offer=Decimal(item_to_offer)
        self.item_for_trade=Decimal(item_for_trade)

        self.calculation_type=calculation_type
        self.average_item_per_block=average_item_per_block
        
        self.price_of_block=Decimal(price_of_block)
        self.price_per_stack_in_shop=Decimal(price_per_stack_in_shop)

        self.margin_desired=Decimal(margin_desired)


    def calculate(self):
        if self.calculation_type=="/":
            print "--------------------------------"
            price_per_item=self.price_of_block/self.average_item_per_block
            print "Price per item: ",Decimal(price_per_item)
            print "--------------------------------"
            trade_ratio=self.item_to_offer/self.item_for_trade*64
            print "Trade Ratio:",Decimal(trade_ratio)
            print "--------------------------------"
            final_int=1+price_per_item
            final_equation=trade_ratio*final_int
            print "Price per stack:",Decimal(final_equation)
            print "--------------------------------"
            profit_made=self.price_per_stack_in_shop-final_equation
            print "Profit Made:",Decimal(profit_made)
            print "--------------------------------"
            calculate_margin=Decimal(self.price_per_stack_in_shop*self.margin_desired)
            if profit_made<calculate_margin:
                print "WARNING: You will lose money with a margin of ",Decimal(self.margin_desired),"%"
            else:
                print "Success! Margin has been met!"
            print "--------------------------------"
            
def set_parameters():
    item_to_offer=int(raw_input("How many Emeralds you offer: "))
    item_for_trade=int(raw_input("How many items you are getting: "))
    average_item_per_block=int(raw_input("If you mined this block with a Fortune Pickaxe how many item(s) would you get?: "))
    price_of_block=Decimal(raw_input("Cost of block on RenMX shop:" ))
    price_per_stack_in_shop=Decimal(raw_input("Cost of stack of this item on RenMX shop:"))
    margin_desired=Decimal(raw_input("Margin Desired (decimal): "))
    this=main(item_to_offer,item_for_trade,"/",average_item_per_block,price_of_block,price_per_stack_in_shop,margin_desired)
    this.calculate()

#this=main(1,2,"/",4,3)
#this.calculate()
set_parameters()       
