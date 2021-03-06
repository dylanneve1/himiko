if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)

class Config(object): ## Real info is in sample config which is included in .gitignore for obvious reasons.
    LOGGER = True

    # REQUIRED
    API_KEY = "YOUR KEY HERE"
    OWNER_ID = "YOUR ID HERE"
    OWNER_USERNAME = "YOUR USERNAME HERE"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADtwADYB_6Ci-ljuhGOm3PAg'  # banhammer himiko sticker
    CANNOTFINDBAN_STICKER = 'CAADAgADnQADYB_6Cm74rLoxg2cfAg'
    STFU_STICKER = 'CAADAgADuAADYB_6CkF2_5GXFZ2BAg'
    SPAGET_STICKER = 'CAADAgAD6QADYB_6Csgh2TWRq0laAg'
    ALLOW_EXCL = True  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
