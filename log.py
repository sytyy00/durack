import logging
import sys
game_logger = logging.getLogger("Game")
game_logger.setLevel(logging.INFO)
handler_1 = logging.FileHandler('log_game.log', 'a')
handler_1.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_1.setFormatter(formatter)
game_logger.addHandler(handler_1)

error = logging.getLogger("Error")
error.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('log_errors.log', 'a')
file_handler.setLevel(logging.DEBUG)
#formatter_2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
error.addHandler(file_handler)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
error.addHandler(console_handler)
