import hashlib, os, urllib.request, pathlib, sys

# CC0/MIT only here; GPL datasets are linked but not fetched to avoid license drift.
DATA = [
  {
    "name":"splunk-bots-v3",
    "url":"https://botsdataset.s3.amazonaws.com/botsv3/botsv3_data_set.tgz",
    "out":"downloads/botsv3/botsv3_data_set.tgz",
    "md5":"d7ccca99a01cff070dff3c139cdc10eb"
  },
  # Example of LANL file (partner can add more days/files)
  {
    "name":"lanl-uhnd-wls-day01",
    "url":"https://csr.lanl.gov/data/unified-host-network-dataset-2017/wls/wls_day-01.bz2",
    "out":"downloads/lanl/wls_day-01.bz2",
    "md5": None
  }
]

def md5sum(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

for item in DATA:
    pathlib.Path(os.path.dirname(item["out"])).mkdir(parents=True, exist_ok=True)
    print(f"[*] Fetching {item['name']} -> {item['out']}")
    urllib.request.urlretrieve(item["url"], item["out"])
    m = md5sum(item["out"])
    print(f"[+] MD5={m}")
    if item["md5"]:
        if m.lower() != item["md5"].lower():
            print(f"[!] MD5 mismatch for {item['name']} (expected {item['md5']})", file=sys.stderr)
            sys.exit(2)
print("[+] All downloads complete")
