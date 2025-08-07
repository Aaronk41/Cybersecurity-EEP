def analyze_logs(df):
    stats = {}
    stats['top_blocked_ips'] = df[df['action'] == 'DROP']['src_ip'].value_counts().head(10)
    stats['protocol_counts'] = df['proto'].value_counts()
    stats['port_counts'] = df[df['action'] == 'DROP']['dst_port'].value_counts().head(10)
    return stats
