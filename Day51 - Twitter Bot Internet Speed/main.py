from internetspeedtwitterbot import InternetSpeedTwitterBot

MIN_DOWN = 900
MIN_UP = 900

# Part One: Get Internet Speed
internet_speed_bot = InternetSpeedTwitterBot()
down_speed, up_speed = internet_speed_bot.get_internet_speed()
print(f"Download speed: {down_speed}")
print(f"Upload speed: {up_speed}")

if down_speed < MIN_DOWN or up_speed < MIN_UP:
    # Complain!
    # Part Two: Tweet (skipped)
    pass
