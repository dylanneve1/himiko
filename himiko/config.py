from himiko.sample_config import Config


class Development(Config):
    OWNER_ID =   352042062
    OWNER_USERNAME = "dylanneve1"  # my telegram username
    API_KEY = "573480537:AAHUWJ_ArAOQZSjMkEmlOxqrlAwBIyj7lmM"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://dylanneve1:Ziggy123a@localhost:5432/YOUR_DB_NAME'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [352042062]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
    DONATION_LINK = "paypal.me/dylanneve1"
