统一字段（默认映射，可由用户覆盖）：
- 名称: title
- 链接: url
- 中文简介: rich_text
- 收藏时间: date

⚠️ 首次使用前必须向用户确认以下信息（禁止写死个人配置）：
1) Notion 凭证来源
   - 环境变量名（示例：NOTION_API_TOKEN）
   - 或凭证文件路径（如 .env）
2) 目标工作区/总页面（可选）
   - 收藏入口页面 URL（若用户需要）
3) 路由目标数据源 ID（必填）
   - GitHub收藏表: <USER_PROVIDED_DATA_SOURCE_ID>
   - 文章收藏表: <USER_PROVIDED_DATA_SOURCE_ID>
   - 视频收藏表: <USER_PROVIDED_DATA_SOURCE_ID>
   - 工具收藏表: <USER_PROVIDED_DATA_SOURCE_ID>
   - 社媒收藏表: <USER_PROVIDED_DATA_SOURCE_ID>
   - 默认收藏表: <USER_PROVIDED_DATA_SOURCE_ID>
   - OpenClaw收藏表: <USER_PROVIDED_DATA_SOURCE_ID>
4) 字段名映射
   - 名称/链接/中文简介/收藏时间 在用户 Notion 表中的真实字段名
5) 收藏时间时区
   - 例如 Asia/Shanghai（UTC+8）

运行时规则：
- 若任一必填配置缺失或不确定，先提问用户补齐，再执行写入。
- 用户确认后可在本地私有配置中保存；再次使用时若检测到变更需重新确认。
- 未经用户明确同意，不把用户的 token、数据库 ID 等敏感信息写入可公开分发的技能文件。