tidal = ["https://tidal.com", "https://listen.tidal.com", "tidal.com", "listen.tidal.com"]
deezer = ["https://deezer.page.link", "https://deezer.com", "deezer.com"]
qobuz = ["https://play.qobuz.com", "https://open.qobuz.com", "https://www.qobuz.com"]
sc = []
kkbox = ["https://www.kkbox.com"]

async def check_link(link):
    if link.startswith(tuple(tidal)):
        return "tidal"
    elif link.startswith(tuple(deezer)):
        return "deezer"
    elif link.startswith(tuple(qobuz)):
        return "qobuz"
    elif link.startswith(tuple(sc)):
        return "sc"
    elif link.startswith(tuple(kkbox)):
        return "kkbox"
    else:
        return None
