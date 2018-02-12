import logging

game_logger = logging.getLogger("Game")
game_logger.setLevel(logging.INFO)
handler_1 = logging.FileHandler('log_1.log', 'a')
handler_1.setLevel(logging.INFO)
formatter_1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_1.setFormatter(formatter_1)
game_logger.addHandler(handler_1)

error = logging.getLogger("Error")
error.setLevel(logging.INFO)
handler_2 = logging.FileHandler('log_2.log', 'a')
handler_2.setLevel(logging.INFO)
formatter_2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_2.setFormatter(formatter_2)
error.addHandler(handler_2)