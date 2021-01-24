import datetime
# bitcoin converter functions

#-------- current date and time
def time():
    return datetime.datetime.now()


#------ bitcoin-usd convert to bitcoin_gbp
def convert_to_gbp(bitcoin_to_usd, usd_to_gbp):
    return round(bitcoin_to_usd * usd_to_gbp, 2) # round to 2 decimal places

