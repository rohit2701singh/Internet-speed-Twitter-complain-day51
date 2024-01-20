from internet_speed_file import InternetSpeed
from twitter import TwitterFile

net_speed_check = InternetSpeed()
speed = net_speed_check.get_speed_detail()
print(speed)

twitter = TwitterFile(
    login_id="xxxxxxxxxxxxxxxxc",
    login_password="cccccccccccvx89$",
    # username="",    # optional parameter
)

twitter.internet_speed_complaint(
    current_speed=(12, 15),
    promised_up_speed=30,
    promised_down_speed=speed,
    # tweet="this is my customised tweet"
)

twitter.tweet_message(
    message="this is my new message"
)