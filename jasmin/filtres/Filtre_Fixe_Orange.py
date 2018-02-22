destination_addr = routable.pdu.params['destination_addr']
if destination_addr[:3] == "212" :
    destination_addr = destination_addr[3:]
    destination_addr = '0'+ destination_addr
elif destination_addr[:4] == "+212" :
    destination_addr = destination_addr[4:]
    destination_addr = '0' + destination_addr
destination_addr = destination_addr[1:4]
result = False
orange_fixe = ["612", "614", "617", "619", "620", "621", "625", "631", "632", "644", "645", "649", "656", "657", "660", "663", "664", "665", "669", "674", "675", "679", "684", "688", "691", "693", "694", "770", "777"]
for num in orange_fixe :
    if num == destination_addr :
        result = True

