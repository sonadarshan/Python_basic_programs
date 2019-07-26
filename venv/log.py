import logging

# Create and configure logger
logging.basicConfig(filename="C:\\Users\\sogangadhara\\PycharmProjects\\untitled\\new_log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

ch = 'n'
# Test messages
while ch == 'n' or ch == 'N':
    try:
        a = int(input("Enter a number : "))
        b = int(input("Enter another number : "))
        logger.info("Got into try block now")
        c = a+b
        print (c)
        logger.debug("Addition done and displayed")
        c = a*b
        print(c)
        logger.debug("Multiplication done and displyed")
        c = a//b
        print(c)
        logger.info("Division done and displayed")
    except ZeroDivisionError as e1:
        logger.error("Zero division error")
        logger.warning("Division by 0 is not possible")
    except NameError as e2:
        logger.error("Name error")
        logger.warning("Onlu numbers are allowed")
    except Exception as e:
        logger.critical("Unknown Error")
        logger.info(e)
    ch = input("Want to terminate(y/n) : ")
