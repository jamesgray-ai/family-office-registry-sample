#!/usr/bin/env python3
"""Pull each skill's and agent's change history from GitHub into skill-history.json.

For every commit that touched a skill or agent, it records the date, who made it,
the pull request it came from and that PR's "Why" section. Needs the GitHub CLI (gh), signed in.
Run from the repository root: python3 tools/skill-history.py
"""
import json, os, re, subprocess

REPO = "jamesgray-ai/family-office-registry-sample"

def gh(path):
    return json.loads(subprocess.check_output(["gh", "api", path]))

def cap(t):
    return t[:1].upper() + t[1:]

def why(body):
    m = re.search(r"## Why\s*\n(.+?)(\n## |\Z)", body or "", re.S)
    return " ".join(m.group(1).split()) if m else ""

targets = [(d, f".claude/skills/{d}") for d in sorted(os.listdir(".claude/skills"))]
targets += [(f[:-3], f".claude/agents/{f}") for f in sorted(os.listdir(".claude/agents")) if f.endswith(".md")]

out = {}
for name, path in targets:
    entries = []
    for c in gh(f"repos/{REPO}/commits?path={path}&per_page=100"):
        sha = c["sha"]
        pulls = gh(f"repos/{REPO}/commits/{sha}/pulls")
        pr = pulls[0] if pulls else None
        entries.append({
            "date": c["commit"]["committer"]["date"][:10],
            "title": cap(pr["title"].split(": ", 1)[-1]) if pr else "First version saved to GitHub",
            "why": why(pr["body"]) if pr else "",
            "author": (c.get("author") or {}).get("login") or c["commit"]["author"]["name"],
            "pr": pr["number"] if pr else None,
            "url": pr["html_url"] if pr else c["html_url"],
        })
    out[name] = {"history_url": f"https://github.com/{REPO}/commits/main/{path}", "changes": entries}

with open("skill-history.json", "w") as f:
    json.dump(out, f, indent=2)
    f.write("\n")
print({k: len(v["changes"]) for k, v in out.items()})
