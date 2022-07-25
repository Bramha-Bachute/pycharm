import logging

logging.basicConfig(filename="log.log", level=logging.DEBUG, filemode='w', format="%(asctime)s : %(name)s : %(levelname)s : %(message)s")

a = 0
b = 1

try:
    for i in range(10):
        print(a)
        a,b = b, a+b
        logging.info(a)
except Exception as e:
    logging.error(e)