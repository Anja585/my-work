# months.py
# This program prints out the summer months one at the time
# Authon: Anja Antolkovic

# all months in the year
months = ("January",
          "February",
          "March",
          "April",
          "May",
          "June", 
          "July",
          "August",
          "September",
          "October",
          "November",
          "December")

# only summer months
summerMonths = tuple(months[4:7])
for month in summerMonths: # looping though the list of summer months 
    print(month)

