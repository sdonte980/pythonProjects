############################
# Purpose: מחשבון ריבית    #
# Programmer: Alex Weiser  #
############################


def set_Up():
    print("מחשבון ריבית                                         ")
    print(" \n                      באמצעותו אפשר לחשב את ההחזר החודשי על סכום כספי מסויים"
           "\n                        לשם כך יש להזין ערכים מספריים לפי הנתונים / קטגוריות"
           "\n                                          סכום כספי, אחוז ריבית, תקופה בשנים"
           "\n .התוצאות שמתקבלות הן: - מספר חודשים ,תשלום לחודש, סה''כ לתשלום ,סה''כ ריבית")


def typeInputData():
    sumPrice = input("                                       \nיש להזין סכום כספי:\n")
    while ((not sumPrice.isdigit())):
        print("this type isn't valid please try again (0-9999999)")
        sumPrice = input("                               \nיש להזין שוב סכום כספי:\n")
    while (((int(sumPrice)) < 0) or ((int(sumPrice)) > 9999999)):
        print("this number isn't valid please try again (0-9999999)")
        sumPrice = input("                               \nיש להזין שוב סכום כספי:\n")
    interestPrecent = input("                               \nיש להזין אחוז ריבית:\n")
    while ((not interestPrecent.isdigit())):
        print("this type isn't valid please try again (0-100)")
        interestPrecent = input("                       \nיש להזין שוב אחוז ריבית:\n")
    if ((int(interestPrecent)) == 0):
        print("Know that I cant serve you because i have not earn from this deal,but you can see the results")
    while (((int(interestPrecent)) < 0) or ((int(interestPrecent)) > 100)):
        print("this number isn't valid please try again (0-100)")
        interestPrecent = input("                       \nיש להזין שוב אחוז ריבית:\n")
    yearPeriod = input("                                    \nיש להזין תקופה בשנים:\n")
    while((not yearPeriod.isdigit())):
        print("this type isn't valid please try again (1-50)")
        yearPeriod = input("                                    \nיש להזין תקופה בשנים:\n")
    while (((int(yearPeriod)) <= 0) or ((int(yearPeriod)) > 50)):
         if(int(yearPeriod) == 0):
          print("year period cannot be '0' Please increase to at least '1' year period")
          yearPeriod = input("                       \nיש להזין שוב אחוז בשנים:\n")
         else:
          print("this number isn't valid please try again (1-50)")
          yearPeriod = input("                       \nיש להזין שוב אחוז בשנים:\n")

    f_sumPrice = float(sumPrice)
    f_interestPrecent = (float(interestPrecent) / 100)
    i_yearPeriod = int(yearPeriod)
    return f_sumPrice, f_interestPrecent, i_yearPeriod


def calcInterst(sumPrice, interestPrecent, yearPeriod):
    final_sum_price_payment = sumPrice * ((interestPrecent * yearPeriod) + 1)
    month = yearPeriod * 12
    paymentPerMonth = (final_sum_price_payment / month)
    total_interest = (final_sum_price_payment - sumPrice)
    return month, paymentPerMonth, total_interest, final_sum_price_payment

def printOutputs(month, paymentPerMonth, total_interest, final_sum_price_payment):
    # ---- results
    print("\n###:תוצאות###")
    # ------------
    print("\n:מספר חודשים")
    print(month)
    # ----
    print("\n:תשלום לחודש")
    print("{:.2f}".format(paymentPerMonth))
    # ----
    print("\n:סה''כ לתשלום")
    print("{:.2f}".format(final_sum_price_payment))
    # ----
    print("\n:סה''כ ריבית")
    print("{:.2f}".format(total_interest))

# ---------

set_Up()
f_sumPrice, f_interestPrecent, i_yearPeriod = typeInputData()
month, paymentPerMonth, total_interest, final_sum_price_payment = calcInterst(f_sumPrice,f_interestPrecent,i_yearPeriod)
printOutputs(month, paymentPerMonth, total_interest, final_sum_price_payment)
