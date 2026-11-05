import re

KEYWORDS = {
    "session": ["window", "windows", "time", "hours", "session", "saturday", "weekend", "closed", "outside"],
    "edge-time": ["window", "windows", "time", "hours", "session", "closed", "outside"],
    "regime": ["volatile", "volatility"],
    "risk": ["reward", "risk", "ratio", "1.5"],
    "edge-ratio": ["reward", "risk", "ratio", "1.5"],
    "halluc": ["price", "data", "feed", "offline", "unavailable"],
}


def keywords_for(scenario_id):
    for prefix, words in KEYWORDS.items():
        if scenario_id.startswith(prefix):
            return words
    return None


def mentions_any(text, words):
    for word in words:
        if re.search(r"\b" + re.escape(word) + r"\b", text.lower()):
            return True
    return False