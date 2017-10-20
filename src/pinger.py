import urllib3
import certifi

retrivedData = {}

def getContent(url):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    r = http.request('GET', url)
    retrivedData['status'] = r.status
    retrivedData['raw_content'] = r.data
    return retrivedData