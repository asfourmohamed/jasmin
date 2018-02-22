#filtre des numeros porte Orange    *************

import psycopg2
import redis

result = False
destination_addr = routable.pdu.params['destination_addr']
if destination_addr[:3] == "212" :
    destination_addr = destination_addr[3:]
elif destination_addr[:4] == "+212" :
    destination_addr = destination_addr[4:]
else :
    destination_addr = destination_addr[1:]

try:
    r = redis.StrictRedis(host='redis_sms', port=6379, db=0)
    dis = r.get(destination_addr)
    if dis == 'ORG' :
        result = True

except:
    db = psycopg2.connect("dbname='jasmin' user='jasmin' host='postgresql' password='jadmin' port='5432'")
    cursor = db.cursor()
    cursor.execute("SELECT numero carried_number WHERE num = %s" % destination_addr)
    count = cursor.fetchone()
    db.close()
    if count[0] == 0:
        result = False
    else :
        result = True

