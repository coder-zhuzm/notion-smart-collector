#!/usr/bin/env python3
"""Minimal one-line Chinese summary fallback."""
import sys
url = sys.argv[1] if len(sys.argv) > 1 else ""
print(f"链接资源：{url}（建议接入 title/meta 抓取后生成更精准的一句话简介）。")
