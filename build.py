#!/usr/bin/env python3
"""TabRelay 公開パッケージのビルダー。
src/tabrelay を Alfred ワークフロー（日英2種）に埋め込み、
dist/ に .alfredworkflow（zip）を書き出す。
キーワードは mc（コピーのみ）と mca（自動ペースト）の2系統。
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


def inline(lang, mode, extra=None):
    head = "TABRELAY_LANG=%s\nTABRELAY_MODE=%s\n" % (lang, mode)
    if mode == "--send":
        head += 'TABRELAY_PAYLOAD="{query}"\n'
    if extra:
        head += extra + "\n"
    return head + body


def scriptfilter(uid, lang, keyword, title, sub, run):
    return {"type": "alfred.workflow.input.scriptfilter", "uid": uid, "version": 1,
            "config": {"script": inline(lang, "--list"), "keyword": keyword,
                       "title": title, "subtext": sub,
                       "runningsubtext": run, "withspace": "False",
                       "escaping": "102", "type": "0", "argumenttype": "2"}}


def action(uid, lang, extra=None):
    return {"type": "alfred.workflow.action.script", "uid": uid, "version": 1,
            "config": {"script": inline(lang, "--send", extra), "escaping": "102",
                       "scriptfile": "", "scriptargtype": "0", "type": "0",
                       "concurrently": "False"}}


def make_workflow(lang, name, bundleid, description,
                  f_title, f_sub, f_run, f2_title, f2_sub, out_name):
    sf, act, nt, sf2, act2 = (str(uuid.uuid4()).upper() for _ in range(5))
    plist = {
        "bundleid": bundleid,
        "category": "Productivity",
        "createdby": "taisukey",
        "description": description,
        "disabled": False,
        "variables": {"TABRELAY_AUTO_PASTE": "0"},
        "name": name,
        "version": "0.2.3",
        "objects": [
            scriptfilter(sf, lang, "mc", f_title, f_sub, f_run),
            action(act, lang),
            {"type": "alfred.workflow.output.notification", "uid": nt, "version": 1,
             "config": {"title": "{query}", "text": ""}},
            scriptfilter(sf2, lang, "mca", f2_title, f2_sub, f_run),
            action(act2, lang, extra="TABRELAY_AUTO_PASTE=1"),
        ],
        "connections": {
            sf: [{"destinationuid": act, "modifiers": 0, "modifiersubtext": ""}],
            act: [{"destinationuid": nt, "modifiers": 0, "modifiersubtext": ""}],
            sf2: [{"destinationuid": act2, "modifiers": 0, "modifiersubtext": ""}],
            act2: [{"destinationuid": nt, "modifiers": 0, "modifiersubtext": ""}],
        },
        "uidata": {sf: {"ypos": 10}, act: {"ypos": 10}, nt: {"ypos": 10},
                   sf2: {"ypos": 130}, act2: {"ypos": 130}},
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
    "Muse へ渡す（自動ペースト）", "選んだタブを Quick Chat へ貼り付けまで行う",
    "TabRelay-JA.alfredworkflow")
make_workflow(
    "en", "TabRelay", "jp.taisukey.tabrelay",
    "Pass the current tab of a supported browser (Brave, Chrome, Chromium) to Muse",
    "Pass to Muse", "Send a tab from Brave, Chrome or Chromium to Muse", "Checking browsers…",
    "Pass to Muse (auto-paste)", "Pass the tab and paste it into Quick Chat",
    "TabRelay-EN.alfredworkflow")
