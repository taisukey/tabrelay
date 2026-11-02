# TabRelay — Alfred ワークフロー

**Brave** で読んでいるページを、Mac の **Muse** アプリへ2ストロークで渡すワークフローです。

Alfred で `mc` と入力すると、現在の Brave タブが候補に出ます。Enter を押すと、ページのタイトルと URL を入れた依頼文がクリップボードにコピーされ、Muse の Quick Chat が開きます。あとは ⌘V で貼って送信するだけです。

英語版は `TabRelay-EN.alfredworkflow`、日本語版は `TabRelay-JA.alfredworkflow` です。キーワード `mc` が重なるので、どちらか一方だけを入れてください。

English: [README.md](README.md)

## 動作環境

- macOS
- Alfred 4 または 5（ワークフローには Powerpack が必要です）
- Brave Browser
- Muse for Mac（Quick Chat のショートカットが既定の Option+Space のままであること）

## インストール

1. このリポジトリの `dist/` フォルダ、または Releases から `TabRelay-JA.alfredworkflow` をダウンロード
2. ファイルをダブルクリックすると Alfred に取り込まれます
3. Brave でページを開き、Alfred で `mc` と入力して Enter

## 許可について

- **自動化（オートメーション）**: 初回実行時に「Alfred が Brave Browser を制御してもよいか」と聞かれます。AppleScript で現在のタブのタイトルと URL を読むために必要なので、許可してください
- **アクセシビリティ**（任意）: Quick Chat を Option+Space のキー入力で自動で開くために使います。許可しなくても動作します。その場合は Option+Space を自分で押してから貼り付けてください

## すること / しないこと

- 読むのは**現在のタブのタイトルと URL だけ**です。履歴や他のタブは読みません
- テキストは**自分のクリップボード**に入るだけです。どこかへ送信されることはなく、Muse への送信も自動では行われません（貼り付けと送信は自分の操作です）
- 記事本文の抽出はしません。本文まで綺麗に抜きたい場合は Obsidian Web Clipper のような専用ツールの方が向いています。これは「このページを見て」と軽く渡すためのものです

## 仕組み

小さな zsh スクリプト（`src/tabrelay`）が AppleScript 経由で Brave とやり取りします。配布用ワークフローにはスクリプトを埋め込んであるので、他にインストールするファイルはありません。`./build.py` を実行すると `src/` から `dist/` のパッケージを再生成できます。

## ライセンス

MIT — [LICENSE](LICENSE) をご覧ください。
