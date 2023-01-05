class EN(object):
    

#----------------
#
# BASICS
#
#----------------
    WELCOME_MSG = "👋🏽 𝐇𝐢 {}"
    START_DOWNLOAD = "⏬ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠.."
    ANTI_SPAM_WAIT = "🔂 𝐖𝐚𝐢𝐭 𝐭𝐚𝐬𝐤 𝐭𝐨 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞!"
    TASK_COMPLETED = "✅ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝"    



#----------------
#
# AUTHENTICATIONS
#
#----------------
    CHAT_AUTH_SUCCESS = "✅ Successfully authed {0} <code>{1}</code>"
    ADD_ADMIN_SUCCESS = "✅ Successfully added {} as an admin"
    NO_ID_TO_AUTH = "⛔️ No ID provided to add!"
    # TIDAL
    TIDAL_NOT_AUTH = "❌ 𝗡𝗼 𝗧𝗶𝗱𝗮𝗹 𝗟𝗼𝗴𝗶𝗻𝘀"
    TIDAL_AUTH_NEXT_STEP = "Go to {0} within the next {1} to complete tidal authentication."
    TIDAL_AUTH_SUCCESS = "✅ Tidal authentication successful.\n\nIt is now valid for {}"
    TIDAL_ALREADY_AUTH = "✅ Your authentication is already done.\nIts is valid for {}"
    # KKBOX
    KKBOX_NOT_AUTH = "❌ 𝐊𝐊𝐁𝐎𝐗 𝐜𝐫𝐞𝐝𝐞𝐧𝐭𝐢𝐚𝐥𝐬 𝐧𝐨𝐭 𝐩𝐫𝐨𝐯𝐢𝐝𝐞𝐝"
    # DEEZER
    DEEZER_NOT_AUTH = "❌ 𝐃𝐞𝐞𝐳𝐞𝐫 𝐜𝐫𝐞𝐝𝐞𝐧𝐭𝐢𝐚𝐥𝐬 𝐧𝐨𝐭 𝐩𝐫𝐨𝐯𝐢𝐝𝐞𝐝"
    # QOBUZ
    QOBUZ_NOT_AUTH = "❌ 𝐐𝐨𝐛𝐮𝐳 𝐜𝐫𝐞𝐝𝐞𝐧𝐭𝐢𝐚𝐥𝐬 𝐧𝐨𝐭 𝐩𝐫𝐨𝐯𝐢𝐝𝐞𝐝"



#----------------
#
# MUSIC DETAILS - TELEGRAM
#
#----------------
    USER_MENTION_ALBUM = "◉ <b>ʀᴇQᴜᴇꜱᴛᴇᴅ ʙʏ : </b> {}"
    USER_MENTION_TRACK = "◉ <b>ʀᴇQᴜᴇꜱᴛᴇᴅ ʙʏ : </b> {}"

    # TIDAL
    TIDAL_ALBUM_DETAILS = """
◉ <b>ᴛɪᴛʟᴇ :</b> {0}
◉ <b>ᴀʀᴛɪsᴛ :</b> {1}
◉ <b>ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ :</b> {2}
◉ <b>ᴛʀᴀᴄᴋs :</b> {3}
◉ <b>ᴅᴜʀᴀᴛɪᴏɴ :</b> {4}
"""
    # KKBOX
    KKBOX_ALBUM_DETAILS = """
◉ <b>ᴛɪᴛʟᴇ :</b> {0}
◉ <b>ᴀʀᴛɪsᴛ :</b> {1}
◉ <b>ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ :</b> {2}
◉ <b>ᴛʀᴀᴄᴋs :</b> {3}
"""

    # QOBUZ
    QOBUZ_ALBUM_DETAILS = """
◉ <b>ᴛɪᴛʟᴇ :</b> {0}
◉ <b>ᴀʀᴛɪsᴛ :</b> {1}
◉ <b>ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ :</b> {2}
◉ <b>ᴛʀᴀᴄᴋs :</b> {3}
"""

    
    # DEEZER
    DEEZER_ALBUM_DETAILS = """
◉ <b>ᴛɪᴛʟᴇ :</b> {0}
◉ <b>ᴀʀᴛɪsᴛ :</b> {1}
◉ <b>ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ :</b> {2}
◉ <b>ᴛʀᴀᴄᴋs :</b> {3}
"""

    QUALITY_ADDON = "<b>◉ Qᴜᴀʟɪᴛʏ :</b> {} \n"

    

    

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
<b>Tidal Settings</b>

<b><u>Settings</u></b>

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
    ERR_QOBUZ_NOT_STREAMABLE = "⛔️ 𝐓𝐡𝐢𝐬 𝐚𝐥𝐛𝐮𝐦 𝐢𝐬 𝐧𝐨𝐭 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐭𝐨 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝."
    ERR_NO_LINK = "⛔️ 𝐍𝐨 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐒𝐨𝐮𝐫𝐜𝐞"
