目标：生成“一句中文简介”，信息密度高、不过长，并以最少抓取完成。

默认策略：
- 先轻量，后补读；不要默认做两次抓取。
- 命中已知站点模式时，直接按模板生成，不额外展开分析。
- 简介以“主题 + 用途/亮点”优先，够用即可。

步骤：
1. 轻量读取：title / meta / 仓库描述。
2. 若信息已足够，直接生成名称与一句中文简介。
3. 仅当信息明显不足时：补读正文前几段或 README 前几段（一次）。
4. 仍不足：使用“主题 + 用途 + 受众”模板兜底。

命名补充规则：
- GitHub 仓库主页：名称优先使用 `owner/repo`。
- GitHub 仓库内文档页：名称优先使用 `owner/repo + 文档名` 的简洁形式。
- 若文档名包含语言标记（如 `README.zh.md`），优先整理为自然中文标题，例如：`owner/repo README（中文）`。
- 避免直接沿用 GitHub 网页 `<title>` 中的长尾片段（如 `at main · owner/repo`）。

X/Twitter 专用：
1) 优先 `api.vxtwitter.com`（默认只打这一层）
2) 信息不足再用 `publish.twitter.com/oembed`
3) 再不足才用 `cdn.syndication.twimg.com/tweet-result`
4) 兜底：作者 + 日期 + 媒体/外链说明
