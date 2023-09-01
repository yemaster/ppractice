import json
oriText = []
with open("problem1.txt", encoding="utf-8") as f:
    oriText = f.read().split("\n")

num = ["①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨"]
chs = ["A", "B", "C", "D"]
problems = []
now = {
    "content": [],
    "choices": [],
    "answer": 0
}
for i in oriText:
    if len(i.strip()) == 0:
        continue
    d = i.split(".")
    if len(d) > 1 and not d[0].upper() in chs:
        problems.append(now)
        now = {
            "content": "",
            "choices": [],
            "answer": 0
        }
    if len(i) > 0 and i[-1] in chs:
        now["answer"] = chs.index(i[-1])
        i = i[:-1]
        d = i.split(".")
    if len(i) > 0 and i[0].upper() in chs and len(d) > 1:
        now["choices"].append(d[1])
    else:
        if len(now["choices"]) > 0:
            now["choices"][-1] += d[-1]
        else:
            if len(i) > 0 and i[0] in num:
                now["content"] += "\n"
            now["content"] += d[-1]
problems.append(now)
print(len(problems[1:]))
with open("problems1.json", "w", encoding="utf-8") as f:
    json.dump(problems[1:], f)
