目标：生成“一句中文简介”，信息密度高、不过长。

步骤：
1. 轻量读取：title/meta/仓库描述。
2. 若不足：补读正文前几段或 README 前几段（一次）。
3. 仍不足：使用“主题 + 用途 + 受众”模板兜底。

X/Twitter 专用：
1) api.vxtwitter.com
2) publish.twitter.com/oembed
3) cdn.syndication.twimg.com/tweet-result
4) 兜底：作者 + 日期 + 媒体/外链说明
