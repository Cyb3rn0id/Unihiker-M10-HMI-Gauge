"""
Unihiker HMI Gauge
by Cyb3rn0id (Giovanni Bernardo)

module      : main.py (*launcher)
what it does: has to be copied in root/ so it's visible from unihiker menu
version     : 1.0
release date: 2026-01-10
"""

import os, sys
os.chdir("/home/gauge_hmi")
os.execv(sys.executable, [sys.executable, "main.py"])