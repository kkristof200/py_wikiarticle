# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional

# Pip
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ Public methods ------------------------------------------------------------ #

def get_text(element) -> Optional[str]:
    try:
        import re

        text = element.get_text()

        for s in re.findall('\\[.*?\\]', text):
            text = text.replace(s, '')

        return text.strip()
    except:
        return None


# ---------------------------------------------------------------------------------------------------------------------------------------- #