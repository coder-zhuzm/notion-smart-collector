#!/usr/bin/env python3
"""Minimal URL classifier for notion-smart-collector."""
from urllib.parse import urlparse
import sys

URL = sys.argv[1] if len(sys.argv) > 1 else ""
host = (urlparse(URL).netloc or "").lower()

if "openclaw" in URL.lower() or "openclaw" in host:
    print("OpenClaw收藏表")
elif "github.com" in host:
    print("GitHub收藏表")
elif any(x in host for x in ["youtube.com", "youtu.be", "bilibili.com", "vimeo.com"]):
    print("视频收藏表")
elif any(x in host for x in ["x.com", "twitter.com", "weibo.com"]):
    print("社媒收藏表")
else:
    print("默认收藏表")
