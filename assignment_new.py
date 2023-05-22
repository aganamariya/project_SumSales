def sum_sales():
    _A = int(input("Enter the no.of Product A you want: "))
    _B = int(input("Enter the no.of Product B you want: "))
    _C = int(input("Enter the no.of Product C you want: "))
    gift = input("enter if u want gift: ").lower()
    while True:
        
        if gift == "yes" or gift == "y" or gift =="no" or gift== "n":
            break
        else:
            print("Please Enter Yes or No for gift !")

    Total = 20*_A + 40*_B + 50*_C

    ## -----------------DISCOUNT SECTION--------------------- ##
    discount = {}

    #flat_10_discount
    if Total>200:
        discount["flat_10_discount"]=Total-10

    #bulk_5_discount
    if _A >10 or _B>10 or _C >10:
        discount["bulk_5_discount"] = Total*0.95  # same as 5% discount

    #bulk_10_discount
    if _A+_B+_C > 20:
        discount["bulk_10_discount"] = Total*0.90  # same as 10% discount

    #tiered_50_discount
    if _A+_B+_C>30 and (_A>15 or _B>15 or _C>15):
        if _A>15:
            resA=(_A-15)*20*0.5
            discount["tiered_50_discount"] = Total-resA

        if _B>15:
            resB=(_B-15)*40*0.5
            discount["tiered_50_discount"] = Total-resB

        if _C>15:
            resC=(_A-15)*50*0.5
            discount["tiered_50_discount"] = Total-resC
    print(discount)
## ------------- PACKAGING SECTION --------------------##

    no_of_packages = (_A+_B+_C)//10
    remainder = (_A+_B+_C) % 10


    if remainder:
        Total_packages = no_of_packages+1    ## 1$ for packing #in gift
    else:
        Total_packages = no_of_packages
    
    if gift =='yes' or gift == 'y':
        gift_fee = _A+_B+_C
    else:
        gift_fee = 0
        
    shipping_fee = Total_packages*5



## -------------------------- BILLING SECTION ----------------------------------------------- ##
    print("The Bill is here")
    print("Product_Name\tQuantity\n")
    print("Product A\t",_A)
    print("Product B\t",_B)
    print("Product C\t",_C)
    print("Tototal amount of product :",Total)
  ## print("\ndiscount name:",[i for i in discount if discount[i]==min(discount.values())][0],"discount amnt:",min(discount.values()))
    print("shipping fee:",shipping_fee,"\ngift_wrap_Fee:",gift_fee)
    print("Grant_ Total:",(min(discount.values()))+shipping_fee+gift_fee)

if __name__ == "__main__":
    sum_sales()
