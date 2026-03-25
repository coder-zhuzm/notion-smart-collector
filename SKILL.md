---
name: notion-smart-collector
description: 智能收藏链接到 Notion（自动路由到多数据表、生成一句中文简介、写入收藏时间）。当用户说“收藏/收藏下”并提供 URL，或要求保存网页/GitHub/X(Twitter) 链接到 Notion 时使用。支持 GitHub/文章/视频/工具/社媒/OpenClaw 识别与路由，默认直接追加一行，不查重。
---

执行流程（固定顺序）：
1) 提取消息中的 URL（支持多个）。
2) 读取 `references/routing-rules.md`，判断每个 URL 的目标数据表。
3) 读取 `references/summarizer-rules.md`，为每个 URL 生成：
   - 名称（短标题）
   - 一句中文简介（优先轻量信息）
4) 读取 `references/notion-schema.md`，按统一字段写入 Notion：
   - 名称
   - 链接
   - 中文简介
   - 收藏时间（UTC+8）
5) 默认“直接追加一行”，不查重、不全表读取。
6) 完成后简短回复：`完成✅｜<Notion表格名>`

实现约束：
- 优先少请求：先轻量抓取，信息不足再补读一次。
- X/Twitter 链接优先走 vxtwitter；不足再回退 oEmbed/syndication。
- 批量链接时串行写入，避免触发速率限制。
- Notion 认证沿用当前运行时配置：每次调用前先执行 `set -a; source /root/.openclaw/workspace/.notion.env; set +a`，再读取 `NOTION_API_TOKEN`。
- Notion API 版本固定使用 `2025-09-03`。
- 收藏目标页面与现有各数据源 ID 沿用当前配置，不新增、不替换。
- GitHub 链接命名优先使用短标题：
  - 仓库主页：优先用 `owner/repo`
  - 仓库内文档页（如 README、docs、blob 页面）：优先用 `owner/repo + 文档名` 的简洁形式；若可识别语言，如 `README.zh.md`，优先整理成 `owner/repo README（中文）`
  - 避免直接使用 GitHub 默认网页标题中的长尾文本（如 `at main · owner/repo`）作为最终名称。
