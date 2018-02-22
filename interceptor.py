import redis
r = redis.StrictRedis(host='10.10.1.24', port=6379, db=0)
result = r.get(str(routable.pdu.params['destination_addr']))
file = open("/home/dialy/log.txt","w")
if result == '0' or result == 0:
    routable.addTag('iam')
elif result == '1' or result == 1:
    routable.addTag('orange')
elif result == '2' or result == 2:
    routable.addTag('inwi')
else:
    routable.addTag('orange')
