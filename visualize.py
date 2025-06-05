import streamlit as st
import pandas as pd
import json
from collections import Counter
import os
import plotly.express as px

LOG_PATH = os.path.expanduser("/home/cowrie/cowrie/var/log/cowrie/cowrie.json")

# Load Cowrie JSON logs
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

    # Sidebar filtering
    selected_event = st.sidebar.selectbox("Filter by event type", df['eventid'].unique())
    filtered = df[df['eventid'] == selected_event]

    st.write(f"## Showing logs for `{selected_event}`")
    st.dataframe(filtered)

    if 'src_ip' in filtered.columns:
        st.write("### Top Source IPs")
        ip_counts = Counter(filtered['src_ip'])
        ip_df = pd.DataFrame(ip_counts.items(), columns=['IP Address', 'Count']).sort_values(by="Count", ascending=False).head(10)
        fig = px.pie(ip_df, names='IP Address', values='Count', title="Top Source IPs")
        st.plotly_chart(fig)

    if 'username' in filtered.columns:
        st.write("### Top Usernames")
        user_counts = Counter(filtered['username'])
        user_df = pd.DataFrame(user_counts.items(), columns=['Username', 'Count']).sort_values(by="Count", ascending=False).head(10)
        fig = px.pie(user_df, names='Username', values='Count', title="Top Usernames")
        st.plotly_chart(fig)
