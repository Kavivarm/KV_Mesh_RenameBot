from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://rojagopimcom:XziyOxnfRczKbcg9@cluster0.qwfro.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"]
        API_HASH = [str, "a3df4aae09f5add6c74658ecf4e98803"]
        API_ID = [int, 15090480]
        BOT_TOKEN = [str, "7252518732:AAG3s6nP8lqXOqEEjCvVGVUb5JKlofbRQV0"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, True]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[400772525]]
        OWNER_ID = [int, 400772525]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,""]
        FORCEJOIN_ID = [int,-1002441121364]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
