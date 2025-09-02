import sys, json, pathlib
REQ = {"time","host","ch","event_id","image","command_line"}
missing,total=0,0
base = pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(".")
for p in base.rglob("*.jsonl"):
    with p.open("r", encoding="utf-8") as f:
        for i,line in enumerate(f,1):
            if not line.strip():
                continue
            total+=1
            try:
                rec=json.loads(line)
            except Exception as e:
                print(f"[{p}:{i}] invalid JSON: {e}")
                missing+=1
                continue
            miss=REQ- rec.keys()
            if miss:
                print(f"[{p}:{i}] missing fields: {sorted(miss)}")
                missing+=1
print(f"Checked {total} records; {missing} issues.")
