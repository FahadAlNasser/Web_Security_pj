def virustotal_summarization(data):
    if isinstance(data, dict) and "data" in data:
        attributes = data.get("data", {}).get("attributes", {})
        stats = attributes.get("last_analysis_stats", {})
        harmful = stats.get("malicious", 0)
        harmless = stats.get("harmless", 0)
        suspicious = stats.get("suspicious", 0)
        reputation = attributes.get("reputation", "Unknown")
        return (f"The virustotal analysis reveals {harmful} malicious, {suspicious} suspicious, "
                f"and {harmless} harmless detections. Reputation score: {reputation}.")
    return "The virus total data is unavailable or invalid"
    