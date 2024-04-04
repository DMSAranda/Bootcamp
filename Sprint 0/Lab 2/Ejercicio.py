import datetime

def my_ticket(ticket) :

    total = 0

    for var in ticket :
        
        array = var.split(" - ")
       
        ud = float(array[0])
        price = float(array[2].replace(',','.'))

        sum = ud * price
        total = total + sum

    return total     


ticket = [ 
           "1 - filete de ternera - 30,23",
           "4 - coca cola - 4,20",
           "-2 - coca cola - 1,40",
           "1 - pan - 0,90"
         ]

result = my_ticket(ticket)

total = result * 1.16

total = f"Total a pagar: {total}"
date = f"Fecha de compra: {datetime.date.today()}"

print(total)
print(date)

