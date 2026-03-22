---
name: notion-smart-collector
description: 智能收藏链接到 Notion（自动路由到多数据表、生成一句中文简介、写入收藏时间）。当用户说“收藏/收藏下”并提供 URL，或要求保存网页/GitHub/X(Twitter) 链接到 Notion 时使用。支持 GitHub/文章/视频/工具/社媒/OpenClaw 识别与路由，默认直接追加一行，不查重。
---

按以下顺序执行（纯指令版，不依赖本地脚本）：

1. 从用户消息提取 URL（支持多链接）。
2. 按 `references/routing-rules.md` 判断目标 Notion 表。
3. 按 `references/summarizer-rules.md` 生成：
   - 名称（短标题）
   - 中文简介（一句话）
4. 按 `references/notion-schema.md` 将每条链接直接追加到对应数据源，字段固定：
   - 名称
   - 链接
   - 中文简介
   - 收藏时间（UTC+8）
5. 默认不查重、不读取整表；仅在用户明确要求时做查重。
6. 完成后简短反馈：`完成✅｜<Notion表格名>`。

执行约束：
- 优先轻量抓取（title/meta）；不足时最多补读一次正文前几段或 README 前几段。
- X/Twitter 链接优先走 `api.vxtwitter.com`；不足时回退 `publish.twitter.com/oembed` 与 `cdn.syndication.twimg.com/tweet-result`。
- 批量链接时串行写入，避免触发限速。
