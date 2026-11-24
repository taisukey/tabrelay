# Accessibility

TabRelay is a keyboard-first tool by design: you type `mc` in Alfred, pick a tab from the list, and press Enter. There is no custom interface of its own — everything happens inside Alfred's standard result list, so the experience inherits Alfred's own keyboard and assistive-technology behaviour.

## Supported environment

- macOS with Alfred 4 or 5 (Powerpack)
- Brave, Google Chrome, or Chromium
- Muse for Mac, with Quick Chat on its default shortcut (Option+Space)

## Known limitations

- **Not tested with VoiceOver or other screen readers.** The workflow adds no screens of its own, but no dedicated assistive-technology testing has been done. Reports from screen-reader users are especially welcome.
- **Auto-paste cannot be verified.** With the `mca` keyword (or `TABRELAY_AUTO_PASTE=1`), TabRelay simulates ⌘V after opening Quick Chat. It cannot confirm the paste landed, so a notification asks you to check Quick Chat before sending. If you prefer full control, use `mc` and paste manually.
- **Auto-open and auto-paste need macOS Accessibility permission for Alfred.** Without it, the core flow still works: copy with `mc`, open Quick Chat yourself (Option+Space), paste with ⌘V.
- **Only the three supported browsers appear.** Tabs in other browsers are not listed.
- Reading the active tab requires the macOS Automation permission for your browser; if it is denied, no tab information can be read.

## Reporting a barrier

Open a GitHub Issue in this repository. You never need to disclose a disability, and screenshots or recordings are optional. It helps to include:

- What you tried to do, and what happened instead
- Your macOS, Alfred, and browser versions
- Whether you used `mc` or `mca`, and whether Alfred has Accessibility permission

TabRelay is maintained by one person, so replies are best-effort — but every report is read, and if a fix is possible it will be tracked in the open.

---

## 日本語

TabRelay はもともとキーボード操作が前提の道具です。Alfred で `mc` と打ってタブを選び、Enter を押すだけです。独自の画面はなく、すべて Alfred の標準の結果リストの中で起こるため、操作感は Alfred 自身のキーボード／支援技術への対応を引き継ぎます。

**対応環境**：macOS、Alfred 4 または 5（Powerpack）、Brave / Google Chrome / Chromium、Muse for Mac（Quick Chat は既定の Option+Space）。

**既知の制限**

- VoiceOver 等のスクリーンリーダーでの検証は行っていません。ワークフロー自体に画面はないものの、専用の検証は未実施です。スクリーンリーダー利用者の報告は特に歓迎します
- 自動ペースト（`mca` キーワード、または `TABRELAY_AUTO_PASTE=1`）は、貼り付けが成功したかを確認できません。送信前に Quick Chat を確認する通知が出ます。確実に操作したい場合は `mc` でコピーし、手で貼ってください
- Quick Chat の自動オープンと自動ペーストには、Alfred への「アクセシビリティ」許可が必要です。許可がなくても、コピーまでの基本動作は使えます
- 表示されるのは対応ブラウザ（上記3種）のタブだけです

**バリアの報告**：このリポジトリの GitHub Issues へどうぞ。障害の開示は不要で、スクリーンショットや録画も任意です。「何をしようとして、どうなったか」「macOS / Alfred / ブラウザのバージョン」「`mc` か `mca` か、Alfred にアクセシビリティ許可があるか」を書いてもらえると助かります。個人で維持しているため返信はベストエフォートですが、報告はすべて読み、直せるものは公開の場で追跡します。
