import logging

game_logger = logging.getLogger("Game")
game_logger.setLevel(logging.INFO)
handler_1 = logging.FileHandler('log_1.log')
handler_1.setLevel(logging.INFO)
formatter_1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_1.setFormatter(formatter_1)
game_logger.addHandler(handler_1)



