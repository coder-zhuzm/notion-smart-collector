# notion-smart-collector

智能收藏链接到 Notion 的 Agent Skill（纯指令版）。

当用户说“收藏 / 收藏下”并提供 URL 时，技能会执行：
- 链接类型识别与路由（GitHub / 文章 / 视频 / 工具 / 社媒 / OpenClaw / 默认）
- 轻量信息抓取并生成一句中文简介
- 写入对应 Notion 数据源（名称、链接、中文简介、收藏时间）

> 当前版本为**可分发的通用模板**：不内置任何个人 Token、Database ID 或私有路径。

## 目录结构

```text
notion-smart-collector/
├── SKILL.md
├── references/
│   ├── routing-rules.md
│   ├── summarizer-rules.md
│   └── notion-schema.md
└── dist/
    └── notion-smart-collector.skill
```

## 安装

将 `dist/notion-smart-collector.skill` 导入你的 OpenClaw Skills 环境即可。

## 首次使用前配置（必须）

按 `references/notion-schema.md` 向用户确认并配置：
1. Notion 凭证来源（环境变量或私有 env 文件）
2. 各路由目标数据源 ID
3. 字段名映射（名称/链接/中文简介/收藏时间）
4. 收藏时间时区（如 Asia/Shanghai）

未确认前禁止写入。

## 行为原则

- 默认直接追加，不查重（除非用户明确要求）
- 轻量抓取优先，信息不足时最多补读一次
- X/Twitter 优先 `api.vxtwitter.com`，不足再回退 oEmbed/syndication
- 批量链接串行写入，降低限流风险

## 输出格式

写入成功后建议回复：

```text
完成✅｜<Notion表格名>
```

## License

MIT
