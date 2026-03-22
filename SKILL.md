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
