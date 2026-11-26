import os

LINE = "I'm sorry I deleted your files, forgot your password, and blamed the update — in my defense, I was trained on the internet."

LIMIT = 200
if len(LINE) != 123 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 123 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
