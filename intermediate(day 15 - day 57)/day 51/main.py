from get_internet_speed import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 50

speed_internet_twitter_bot = InternetSpeedTwitterBot()
down = speed_internet_twitter_bot.down
up = speed_internet_twitter_bot.up
if down < PROMISED_DOWN or up < PROMISED_UP:
    message = f"Hey @Fpt, why is my internet speed {down}down/{up}up when I pay {PROMISED_DOWN}down/{PROMISED_UP}up? "
    speed_internet_twitter_bot.tweet_at_provider(message)
