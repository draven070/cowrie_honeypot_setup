import streamlit as st
import pandas as pd
import json
from collections import Counter
import os

LOG_PATH = os.path.expanduser("enter _path_for_cowrie.json")

#for loading JSON logs
def load_logs(path):
    logs = []
    try:
        with open(path, "r") as file:
            for line in file:
                try:
                    logs.append(json.loads(line.strip()))
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        st.error("Log file not found.")
        return pd.DataFrame()
    return pd.DataFrame(logs)

st.title("Cowrie Honeypot Log Visualization")
df = load_logs(LOG_PATH)

if df.empty:
    st.warning("No data loaded.")
else:
    st.success(f"Loaded {len(df)} log entries.")

    #  filtering
    selected_event = st.sidebar.selectbox("Filter by event type", df['eventid'].unique())
    filtered = df[df['eventid'] == selected_event]

    st.write(f"## Showing logs for `{selected_event}`")
    st.dataframe(filtered)

    if 'src_ip' in filtered.columns:
        st.write("### Top Source IPs")
        ip_counts = Counter(filtered['src_ip'])
        st.bar_chart(pd.Series(ip_counts).sort_values(ascending=False).head(10))

    if 'username' in filtered.columns:
        st.write("### Top Usernames")
        user_counts = Counter(filtered['username'])
        st.bar_chart(pd.Series(user_counts).sort_values(ascending=False).head(10))
