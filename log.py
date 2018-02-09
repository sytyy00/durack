import logging
import card

logging.basicConfig(filename="log_1.log", filemode="w", level=logging.INFO, format='%(asctime)s  - %(levelname)s - %(message)s')
if __name__ == '__main__':
    logging.info("Start")

