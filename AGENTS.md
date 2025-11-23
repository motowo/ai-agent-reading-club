# AI Agent 指示書 (`AGENTS.md`)

このドキュメントは、本プロジェクト「AI Agent Reading Club」において、スライド作成および運用を担当する AI エージェント（または開発者）のための包括的な指示書です。

## 1. プロジェクト概要
**目的**: AI エージェントに関する読書会のためのスライド資料を、GitHub Pages 上で公開・運用する。
**主要ツール**: Marp (Markdown Presentation Ecosystem), GitHub Pages

## 2. 環境・運用ルール (Based on `docs/env1.md`)

### 基本ワークフロー
スライドの更新は以下のサイクルで行います。

1.  **編集**: `slides.md` を Markdown で編集する。
2.  **ビルド**: ローカルで HTML に変換する。
    ```bash
    npm run build
    # または
    marp slides.md --html --output index.html
    ```
3.  **デプロイ**: 変更を GitHub に push する（`index.html` が更新されていることを確認）。
    ```bash
    git add .
    git commit -m "Update slides"
    git push
    ```
4.  **確認**: `https://<username>.github.io/ai-agent-reading-club/` で公開内容を確認する。

### 開発環境
*   **Node.js**: 必須
*   **依存パッケージ**: `@marp-team/marp-cli` (インストール済み)
*   **コマンド**:
    *   `npm run build`: スライドのビルド
    *   `npm run watch`: 変更監視モードで起動

## 3. デザインガイドライン (Based on `docs/env2.md`)

### デザインテーマ
**「Modern × Minimal Line Art（モダン × ミニマル線画）」**
*   **印象**: 知的、未来的、清潔感、親しみやすさ。
*   **スタイル**: 余白を活かしたレイアウト、サンセリフ体 (Inter/Helvetica Neue)、モノトーンベース。

### CSS 設定 (`styles.css`)
本プロジェクトではカスタム CSS `styles.css` を使用しています。
*   **フォント**: Inter, Helvetica Neue, Arial
*   **配色**: 背景白、文字色 `#222`、アクセントは線画や余白で表現。
*   **アニメーション**: 各スライドに `fadein` アニメーションを適用済み。

### スライド記述ルール
`slides.md` の先頭には以下を含めること。
```markdown
---
marp: true
paginate: true
style: |
  @import url('styles.css');
---
```

## 4. アセット運用ルール

### イラストレーション
*   **格納場所**: `assets/illustrations/`
*   **ファイル名規則**: `[スライド番号]_[テーマ].png` (例: `01_intro_agent-human.png`)
*   **パス指定**: Markdown からは相対パスで参照する。
    ```markdown
    ![alt text](assets/illustrations/filename.png)
    ```

### プロンプト管理
*   **管理ファイル**: `assets/prompts/illustration_prompts.json`
*   **用途**: 画像生成AIへの指示（プロンプト）を記録し、再現性を担保する。
*   **フォーマット**:
    ```json
    {
      "id": 1,
      "filename": "01_intro_agent-human.png",
      "style": "minimal-line-art",
      "prompt": "..."
    }
    ```

## 5. ディレクトリ構成
```
ai-agent-reading-club/
├── slides.md          # スライド原稿 (Markdown)
├── index.html         # 公開用スライド (自動生成)
├── styles.css         # デザイン定義
├── package.json       # 依存関係・スクリプト定義
├── assets/
│   ├── illustrations/ # スライド挿絵
│   └── prompts/       # 画像生成プロンプト
└── docs/              # 参照ドキュメント (env1.md, env2.md)
```
