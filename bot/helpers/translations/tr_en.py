class EN(object):
    

#----------------
#
# BASICS
#
#----------------
    WELCOME_MSG = "👋🏽 Hi {}"
    START_DOWNLOAD = "⏬ Downloading.."
    ANTI_SPAM_WAIT = "🔂 Wait task to complete!"
    TASK_COMPLETED = "✅ Downloaded"    



#----------------
#
# AUTHENTICATIONS
#
#----------------
    CHAT_AUTH_SUCCESS = "✅ Successfully authed {0} <code>{1}</code>"
    ADD_ADMIN_SUCCESS = "✅ Successfully added {} as an admin"
    NO_ID_TO_AUTH = "⛔️ No ID provided to add!"
    # TIDAL
    TIDAL_NOT_AUTH = "❌ No Tidal Logins"
    TIDAL_AUTH_NEXT_STEP = "Go to {0} within the next {1} to complete tidal authentication."
    TIDAL_AUTH_SUCCESS = "✅ Tidal authentication successful.\n\nIt is now valid for {}"
    TIDAL_ALREADY_AUTH = "✅ Your authentication is already done.\nIts is valid for {}"
    # KKBOX
    KKBOX_NOT_AUTH = "❌ KKBOX credentials not provided"
    # DEEZER
    DEEZER_NOT_AUTH = "❌ Deezer credentials not provided"
    # QOBUZ
    QOBUZ_NOT_AUTH = "❌ Qobuz credentials not provided"



#----------------
#
# MUSIC DETAILS - TELEGRAM
#
#----------------
    USER_MENTION_ALBUM = "◉ <b>User: </b> {}"
    USER_MENTION_TRACK = "<b>User: </b> {}"

    # TIDAL
    TIDAL_ALBUM_DETAILS = """
◉ <b>Title :</b> {0}
◉ <b>Artist :</b> {1}
◉ <b>Release Date :</b> {2}
◉ <b>Number of Tracks :</b> {3}
◉ <b>Duration :</b> {4}
◉ <b>Number of Volumes :</b> {5}
"""
    # KKBOX
    KKBOX_ALBUM_DETAILS = """
◉ <b>Title :</b> {0}
◉ <b>Artist :</b> {1}
◉ <b>Release Date :</b> {2}
◉ <b>Number of Tracks :</b> {3}
"""

    # QOBUZ
    QOBUZ_ALBUM_DETAILS = """
◉ <b>Title :</b> {0}
◉ <b>Artist :</b> {1}
◉ <b>Release Date :</b> {2}
◉ <b>Number of Tracks :</b> {3}
"""

    
    # DEEZER
    DEEZER_ALBUM_DETAILS = """
◉ <b>Title :</b> {0}
◉ <b>Artist :</b> {1}
◉ <b>Release Date :</b> {2}
◉ <b>Total Tracks :</b> {3}
"""

    QUALITY_ADDON = "<b>Quality :</b> {} \n"

    

    

#----------------
#
# SETTINGS PANEL
#
#----------------
    INIT_SETTINGS_MENU = "<b>Welcome to Bot Settings Menu.</b>\n\nChoose the option to open its settings."
    WARN_REMOVE_AUTH = "<b>Are you sure you want to remove {} auth?</b>"
    RM_AUTH_SUCCESSFULL = "Successfully removed {} auth details."
    QUALITY_SET_PANEL = "<b>Choose the required quality for {0}\n\nCurrent Quality :</b> <code>{1}</code>"
    COMMON_AUTH_PANEL = "<b>Configure {0} Authentication\n\nAuth Status : </b>{1}"
    #
    # TIDAL PANEL
    #
    TIDAL_SETTINGS_PANEL = """
<b>Configure Tidal Settings Here</b>

<b><u>SETTINGS</u></b>

<b>Quality : </b><code>{0}</code>
<b>API : </b><code>{1}</code>
<b>Auth Status : </b><code>{2}</code>
"""
    TIDAL_SELECT_API_KEY = """
<b><u>API KEY SETTING PANEL</u></b>
Current API Platform : <code>{0}</code>
Available Formats : <code>{1}</code>
API Key Valid : <code>{2}</code>
<b><u>API PLATFORM INFO</u></b>
{3}
<b>RELOGIN NEEDED AFTER CHANGING API PLATFORM</b>
"""
    #
    # KKBOX PANEL
    #
    KKBOX_SETTINGS_PANEL = """
<b>Configure KKBOX Settings Here</b>

<b><u>CURRENT SETTINGS</u></b>

<b>Quality : </b><code>{0}</code>
<b>Auth Status : </b><code>{1}</code>
"""
    #
    # QOBUZ PANEL
    #
    QOBUZ_SETTINGS_PANEL = """
<b>Configure Qobuz Settings Here</b>

<b><u>CURRENT SETTINGS</u></b>

<b>Quality : </b><code>{0}</code>
<b>Auth Status : </b><code>{1}</code>
    """

    



#----------------
#
# BUTTONS
#
#----------------
    # MAIN MENU
    MAIN_MENU_BUTTON = "MENU"
    TG_AUTH_BUTTON = "TELEGRAM"
    TIDAL_BUTTON = "TIDAL"
    QOBUZ_BUTTON = "QOBUZ"
    DEEZER_BUTTON = "DEEZER"
    KKBOX_BUTTON = 'KKBOX'
    SOUNDCLOUD_BUTTON = "SOUNDCLOUD"
    CLOSE_BUTTON = "CLOSE"
    API_BUTTON = "API"
    # COMMON BUTTONS
    QUALITY_BUTTON = "QUALITY"
    AUTH_BUTTON = "AUTH"
    REMOVE_AUTH_BUTTON = "REMOVE AUTH"
    ADD_AUTH_BUTTON = "ADD AUTH"
    YES_BUTTON = "YES"
    NO_BUTTON = "NO"
    # TIDAL QUALITY
    MASTER_QUALITY = "Master - FLAC"
    HIFI_QUALITY = "HiFi"
    HIGH_QUALITY = "High"
    NORMAL_QUALITY = "Normal"
    # QOBUZ_QUALIY
    Q_LOSELESS = "LOSELESS"
    Q_320 = "320K"
    Q_HIRES_7 = "HiRes =< 96"
    Q_HIRES_27 = "HiRes > 96"


#----------------
#
# ERRORS
#
#----------------
    # QOBUZ
    ERR_QOBUZ_NOT_STREAMABLE = "⛔️ This album is not available to download."
    ERR_NO_LINK = "⛔️ No download Source"
