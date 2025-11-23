了解です！
ここからは **「パターン①（ローカルで HTML に変換 → GitHub に push → Pages で公開）」を完全に成功させるための超詳細な手順** を、迷いゼロで進められるように解説します。

すべて **コピペして実行するだけ** で動くようにしています。

---

# 🚀 パターン①：ローカルで HTML に変換して GitHub Pages にデプロイする手順

## 🎯 ゴール

* `slides.md` → `index.html` に変換（Marp）
* GitHub リポジトリに push
* GitHub Pages を有効化
* URL でスライド閲覧
  例：
  `https://yourname.github.io/ai-agent-reading-club/`

---

# ✅ STEP 1：リポジトリ作成

### 1. GitHub で新しいリポジトリを作ります

**GitHub → New repository**

* Repository name:
  例）`ai-agent-reading-club`
* Public（推奨）
* “Initialize this repository with …” はすべてオフでも OK
* **Create repository** を押す

---

# ✅ STEP 2：ローカルへ clone

ターミナルで：

```bash
git clone https://github.com/YOUR_NAME/ai-agent-reading-club.git
cd ai-agent-reading-club
```

※ `YOUR_NAME` はあなたの GitHub ID に置き換えてください。

---

# ✅ STEP 3：slides.md を配置

ChatGPT が生成した **30ページの Marp スライド（slides.md）** を
このフォルダに置きます。

```
ai-agent-reading-club/
  └─ slides.md
```

---

# ✅ STEP 4：marp-cli をインストール

### Node.js がまだの人

→ Node.js（LTS）をインストール:
[https://nodejs.org/](https://nodejs.org/)

### marp-cli を入れる

```bash
npm install -g @marp-team/marp-cli
```

バージョン確認：

```bash
marp --version
```

---

# ✅ STEP 5：slides.md → index.html を生成

GitHub Pages は通常 **`index.html`** をトップとして読むので、
出力ファイル名も **index.html** にします。

```bash
marp slides.md --html --output index.html
```

完了するとフォルダはこうなります：

```
ai-agent-reading-club/
  ├─ slides.md
  └─ index.html   ← GitHub Pages がこれを読み込む
```

---

# ✅ STEP 6：Git にコミットして push

```bash
git add .
git commit -m "Add Marp slides"
git branch -M main
git remote add origin https://github.com/YOUR_NAME/ai-agent-reading-club.git  # 初回のみ
git push -u origin main
```

---

# ✅ STEP 7：GitHub Pages を有効化

GitHub のリポジトリ画面で：

1. **Settings** を押す
2. 左メニューから **Pages**
3. **Build and deployment**

   * Source → *Deploy from a branch*
   * Branch → `main`
   * Folder → `/ (root)`
4. Save

---

# ⏳ STEP 8：デプロイ確認

数十秒後、GitHub Pages がビルドされると：

「**Your site is live at ...**」と表示されます。

URL は：

```
https://YOUR_NAME.github.io/ai-agent-reading-club/
```

ブラウザで開くと
**Marp のスライド表示になっています（左右キーで操作）**。

---

# 📝 STEP 9：更新の仕方（重要）

### 更新するたびにやることは 2つだけ：

```
slides.md を編集
→ marp で index.html を再生成
→ git push
```

手順：

```bash
marp slides.md --html --output index.html
git add .
git commit -m "Update slides"
git push
```

これで GitHub Pages が自動で更新されます。

---

# 🎁（オプション）カスタム CSS を使いたい場合

`styles.css` を追加して Marp の style で読み込みます。

例：

```markdown
---
marp: true
paginate: true
style: |
  @import url('styles.css');
---
```

フォルダ構成：

```
ai-agent-reading-club/
  ├─ slides.md
  ├─ index.html（生成される）
  └─ styles.css
```

---

# 🎉 完了！

これで **パターン①の GitHub Pages デプロイがすべて完了** です。

---

# 🔥 次に必要なものがあれば言ってください

* `styles.css`（モダン × ミニマル線画に相応しいデザイン）
* `assets/illustrations/` の構成テンプレート
* Markdown からリンクする図版の指定例
* スライドの別バリエーション
* 読書会90分ファシリテーション台本
* Google Docs ワークシートのテンプレート

どれを出しますか？
