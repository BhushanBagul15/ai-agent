# utils/metrics.py
import pandas as pd
from datetime import datetime
import os

def log_metrics(eou_delay, ttft, ttfb, total_latency):
    filename = "logs/session_metrics.xlsx"
    os.makedirs("logs", exist_ok=True)

    data = {
        "Timestamp": [datetime.now()],
        "EOU Delay": [eou_delay],
        "TTFT": [ttft],
        "TTFB": [ttfb],
        "Total Latency": [total_latency]
    }

    df = pd.DataFrame(data)

    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        df_existing = pd.read_excel(filename, engine='openpyxl')
        df = pd.concat([df_existing, df], ignore_index=True)

    df.to_excel(filename, index=False, engine='openpyxl')
