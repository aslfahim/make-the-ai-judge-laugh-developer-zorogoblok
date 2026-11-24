import os

LINE = (
    "Okay, it was me — I pushed the deploy at 4:59pm on a Friday because "
    "the ticket said urgent. The code can be rolled back; my weekend can't, "
    "and neither can my dignity."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
