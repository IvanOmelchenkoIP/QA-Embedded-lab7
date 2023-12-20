import re

REGEXP = '\[\s*[0-9]*\]\s*[0-9\.-]*\s*(sec)\s*[0-9\.]*\s*[A-Z]?(Bytes)\s*[0-9\.]*\s*[A-Z]?(bits/sec)\s*[0-9]*\s*[0-9\.]*\s*[A-Z]?(Bytes)'
KEYS = ('Interval', 'Transfer', 'Bitrate', 'Retr', 'Cwnd')