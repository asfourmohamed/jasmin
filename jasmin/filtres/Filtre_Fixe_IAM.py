destination_addr = routable.pdu.params['destination_addr']
if destination_addr[:3] == "212" :
    destination_addr = destination_addr[3:]
    destination_addr = '0'+ destination_addr
elif destination_addr[:4] == "+212" :
    destination_addr = destination_addr[4:]
    destination_addr = '0' + destination_addr
destination_addr = destination_addr[1:4]
result = False
iam_fixe = ["610", "611", "613", "615", "616", "618", "622", "623", "624", "628", "636", "637", "639", "641", "642", "643", "648", "650", "651", "652", "653", "654", "655", "658", "659", "661", "662", "666", "667", "668", "670", "671", "672", "673", "676", "677", "678", "682", "689", "696", "697", "761", "762"]
for num in iam_fixe :
    if num == destination_addr :
        result = True






