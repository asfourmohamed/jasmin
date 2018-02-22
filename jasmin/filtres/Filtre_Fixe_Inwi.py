destination_addr = routable.pdu.params['destination_addr']
if destination_addr[:3] == "212" :
    destination_addr = destination_addr[3:]
    destination_addr = '0'+ destination_addr
elif destination_addr[:4] == "+212" :
    destination_addr = destination_addr[4:]
    destination_addr = '0' + destination_addr
destination_addr = destination_addr[1:4]
result = False
inwi_fixe = ["529", "538", "526", "527", "540", "546", "547", "533", "534", "550", "553", "600", "601", "602", "603", "604", "605", "606", "607", "608", "609", "626", "627", "629", "630", "633", "634", "635", "638", "640", "646", "647", "680", "681", "687", "690", "695", "698", "699", "700", "707"]
for num in inwi_fixe :
    if num == destination_addr :
        result = True

