import hashlib
import requests
import os
from dotenv import load_dotenv

load_dotenv()

virustotal_key = os.getenv('virus_total_key')
HEADERS = {"x-apikey": virustotal_key}

def virustotal_scanningurl(url):
    submitting_url = "https://www.virustotal.com/api/v3/urls"
    response = requests.post(submitting_url, headers=HEADERS, data={"url": url})
    if response.status_code != 200:
        return {"error": "The operation failed: failed to submit URL"}
    id_scanner = response.json()['data']['id']
    url_reporting = f"https://www.virustotal.com/api/v3/analyses/{id_scanner}"
    output = requests.get(url_reporting, headers=HEADERS).json()
    return {
        "url": url,
        "status": output['data']['attributes']['status'],
        "malicious": output['data']['attributes']['stats']['malicious'],
        "suspicious": output['data']['attributes']['stats']['suspicious'],
        "details": "The Scan completed using VirusTotal API"
    }

def virustotal_scanningfile(filepath):
    with open(filepath, 'rb') as file:
        files = {'file': (os.path.basename(filepath), file)}
        response = requests.post("https://www.virustotal.com/api/v3/files", headers=HEADERS, files=files)
    if response.status_code != 200:
        return {"error": "The File Uploading Operation has failed"} 
    id_scanner = response.json()['data']['id']
    url_reporting = f"https://www.virustotal.com/api/v3/analyses/{id_scanner}"
    output = requests.get(url_reporting, headers=HEADERS).json()
    sha256 = hashlib.sha256(open(filepath, 'rb').read()).hexdigest()
    return {
        "file": os.path.basename(filepath),
        "sha256": sha256,
        "status": output['data']['attributes']['status'],
        "malicious": output['data']['attributes']['stats']['malicious'],
        "suspicious": output['data']['attributes']['stats']['suspicious'],
        "details": "The scan operation completed using VirusTotal API to scan a file."
    }