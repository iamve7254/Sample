import logging
logging.basicConfig(filename='log1.txt',level=logging.INFO)

logging.info("A new request came ")
try:
    a=int(input("enter first value"))
    b=int(input("entyer second value"))
    print("the value is:",a/b)
except ZeroDivisionError as msg:
    print("can't devide Zero")
    logging.exception(msg)

except ValueError as msg:
    print(" enter  onely int type value")
    logging.exception(msg)
logging.info("request massage compleated")

