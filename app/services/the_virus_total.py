import requests
import os
from dotenv import load_dotenv

load_dotenv()

AI_API_key_one = os.getenv("vtotal")
virustotal_file = "https://www.virustotal.com/api/v3/files"
virustotal_url = "https://www.virustotal.com/api/v3/urls"
headers = {"x-apikey": os.getenv("vtotal")}

def scanning_with_virustotal(file_bytes = None, filename = None, url = None):
    if file_bytes:
        Files_f = {"file": (filename, file_bytes)}
        response = requests.post(virustotal_file, headers = headers, files = Files_f)
    elif url: 
        import base64
        link_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        response = requests.get(f"{virustotal_url}/{link_id}", headers = headers)
        if response.status_code == 404:
            response = requests.post(virustotal_url, headers = headers, data = {"url": url})
    else:
        return "There is no file or URL provided to scan."        
    if response.status_code in [200, 201]:
        return response.json()
    return f"There is an error from VirusTotal: {response.status_code} - {response.text}"