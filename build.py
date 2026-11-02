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
ALT_ICONS = [("icon-b.png", os.path.join(ROOT, "assets", "icon-b.png")),
             ("icon-c.png", os.path.join(ROOT, "assets", "icon-c.png"))]

with open(os.path.join(ROOT, "src", "tabrelay"), encoding="utf-8") as f:
    body = f.read()
if body.startswith("#!"):
    body = body.split("\n", 1)[1]


def inline(lang, mode):
    head = "TABRELAY_LANG=%s\nTABRELAY_MODE=%s\n" % (lang, mode)
    if mode == "--send":
        head += 'TABRELAY_PAYLOAD="{query}"\n'
    return head + body


def make_workflow(lang, name, bundleid, description, f_title, f_sub, f_run, out_name):
    sf, act, nt = (str(uuid.uuid4()).upper() for _ in range(3))
    plist = {
        "bundleid": bundleid,
        "category": "Productivity",
        "createdby": "taisukey",
        "description": description,
        "disabled": False,
        "name": name,
        "version": "0.2.0",
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
    for alt_name, alt_path in ALT_ICONS:
        if os.path.exists(alt_path):
            shutil.copy(alt_path, os.path.join(wdir, alt_name))
    os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
    zpath = os.path.join(ROOT, "dist", out_name)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for fn in sorted(os.listdir(wdir)):
            z.write(os.path.join(wdir, fn), fn)
    print("built", zpath)


make_workflow(
    "ja", "TabRelay", "jp.taisukey.tabrelay.ja",
    "対応ブラウザ（Brave / Chrome / Chromium）の現在のタブを Muse へ渡す",
    "Muse へ渡す", "開いている対応ブラウザのタブを Muse へ渡す", "ブラウザを確認中…",
    "TabRelay-JA.alfredworkflow")
make_workflow(
    "en", "TabRelay", "jp.taisukey.tabrelay",
    "Pass the current tab of a supported browser (Brave, Chrome, Chromium) to Muse",
    "Pass to Muse", "Send a tab from Brave, Chrome or Chromium to Muse", "Checking browsers…",
    "TabRelay-EN.alfredworkflow")
