
from follow_bot import InstaFollower

USER = "iobi1907@gmail.com"
PASS = "congxp1996"
KEY_WORD = "hoang dung"

follow_bot = InstaFollower()
follow_bot.login(USER=USER, PASS=PASS)
follow_bot.find_followers(KEY_WORD=KEY_WORD)
follow_bot.follow()
