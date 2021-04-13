#Stock Transaction Program
#Willie Young
#Chapter2_12

#set constants:number of shares, commission percentage

NUM_SHARES = 2000
COMM_PCT = .03

#set variables: stock price before & after

stock_price_buy = 40
stock_price_sell = 42.75


#calculate buy values: amount paid & amount received

amt_paid = NUM_SHARES * stock_price_buy

amt_received = NUM_SHARES * stock_price_sell

#calculate buy & sell commission

comm_buy = amt_paid * COMM_PCT

comm_sell =  amt_received * COMM_PCT

#calculate profit/loss

prof_loss = (amt_received - comm_sell - comm_buy) 

pos_or_neg = prof_loss - amt_paid


#display amount paid, buy commission, amount received, sell commission, +/-
print('Amount Paid To Acquire: $', format(amt_paid, ',.2f'))
print('Acquisition Commission: $', format(comm_buy, ',.2f'))
print('Amount Received To Sell: $', format(amt_received, ',.2f'))
print('Sell Commission: $', format(comm_sell, ',.2f'))
print('Amount Left After Sell & Commissions: $', format(prof_loss, ',.2f'))
print('Joe made a profit of: $', format(pos_or_neg, ',.2f'))

