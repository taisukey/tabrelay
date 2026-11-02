#!/usr/bin/env python3
"""TabRelay 公開パッケージのビルダー。
src/tabrelay を Alfred ワークフロー（日英2種）に埋め込み、
dist/ に .alfredworkflow（zip）を書き出す。
"""
import os
import plistlib
import shutil
import uuid
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
ICON = os.path.join(ROOT, "assets", "icon.png")

with open(os.path.join(ROOT, "src", "tabrelay"), encoding="utf-8") as f:
    body = f.read()
if body.startswith("#!"):
    body = body.split("\n", 1)[1]


def inline(lang, mode):
    return "TABRELAY_LANG=%s\nTABRELAY_MODE=%s\n%s" % (lang, mode, body)


def make_workflow(lang, name, bundleid, description, f_title, f_sub, f_run, out_name):
    sf, act, nt = (str(uuid.uuid4()).upper() for _ in range(3))
    plist = {
        "bundleid": bundleid,
        "category": "Productivity",
        "createdby": "taisukey",
        "description": description,
        "disabled": False,
        "name": name,
        "version": "0.1.0",
        "objects": [
            {"type": "alfred.workflow.input.scriptfilter", "uid": sf, "version": 1,
             "config": {"script": inline(lang, "--list"), "keyword": "mc",
                        "title": f_title, "subtext": f_sub,
                        "runningsubtext": f_run, "withspace": "False",
                        "escaping": "102", "type": "0", "argumenttype": "1"}},
            {"type": "alfred.workflow.action.script", "uid": act, "version": 1,
             "config": {"script": inline(lang, "--send"), "escaping": "102",
                        "scriptfile": "", "scriptargtype": "0", "type": "0",
                        "concurrently": "False"}},
            {"type": "alfred.workflow.output.notification", "uid": nt, "version": 1,
             "config": {"title": "{query}", "text": ""}},
        ],
        "connections": {
            sf: [{"destinationuid": act, "modifiers": 0, "modifiersubtext": ""}],
            act: [{"destinationuid": nt, "modifiers": 0, "modifiersubtext": ""}],
        },
        "uidata": {sf: {"ypos": 10}, act: {"ypos": 10}, nt: {"ypos": 10}},
    }
    wdir = os.path.join(ROOT, "workflows", lang)
    shutil.rmtree(wdir, ignore_errors=True)
    os.makedirs(wdir)
    with open(os.path.join(wdir, "info.plist"), "wb") as fp:
        plistlib.dump(plist, fp)
    if os.path.exists(ICON):
        shutil.copy(ICON, os.path.join(wdir, "icon.png"))
    os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
    zpath = os.path.join(ROOT, "dist", out_name)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for fn in sorted(os.listdir(wdir)):
            z.write(os.path.join(wdir, fn), fn)
    print("built", zpath)


make_workflow(
    "ja", "TabRelay", "jp.taisukey.tabrelay.ja",
    "Brave の現在のタブ（タイトルとURL）を Muse へ渡す",
    "Muse へ渡す", "Brave の現在のタブを Muse へ渡す", "Brave を確認中…",
    "TabRelay-JA.alfredworkflow")
make_workflow(
    "en", "TabRelay", "jp.taisukey.tabrelay",
    "Pass the current Brave tab (title and URL) to Muse",
    "Pass to Muse", "Send the current Brave tab to Muse", "Checking Brave…",
    "TabRelay-EN.alfredworkflow")
