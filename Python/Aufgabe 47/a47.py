import re

#Datum TT.MM.JJ
pattern = re.compile("[\d]{2}\.[01][0-9]\.[12][\d]{2}")



match = pattern.match("18.12.1992")
print(match)