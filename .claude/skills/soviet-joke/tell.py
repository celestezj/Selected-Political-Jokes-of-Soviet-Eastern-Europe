#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""随机从 corpus.md 选一条苏联笑话并干净地打印出来。

保证两件事（不依赖调用方/模型自觉）：
  1. 主题标签剥离 `一、/二、/三、/四、` 等序号前缀；
  2. 输出末尾没有多余空行——正文最后一个字符后即以单个换行结束。
"""
import os
import random
import re
import sys

BASE = os.path.dirname(os.path.realpath(__file__))
CORPUS = os.path.join(BASE, "corpus.md")

# 形如 “一、” 的前缀
NUM_PREFIX = re.compile(r'^[一二三四五六七八九十]、')


def main():
    with open(CORPUS, encoding="utf-8") as f:
        raw = f.read()
    lines = raw.split("\n")

    jokes = []  # (clean_theme, title, [body_lines])
    theme = ""
    title = None
    body = []

    def flush():
        nonlocal title, body
        if title is not None and body:
            clean = NUM_PREFIX.sub("", theme).strip()
            jokes.append((clean, title, body))
        title = None
        body = []

    for ln in lines:
        st = ln.strip()
        if st.startswith("# "):           # 主题分节（`# `）
            flush()
            theme = st[2:].strip()
        elif st.startswith("## "):        # 单条笑话（`## `）
            flush()
            title = st[3:].strip()
        elif title is not None:
            body.append(ln)               # 保留原始行（含正文内部的空行）

    flush()

    if not jokes:
        sys.exit("corpus.md 中未找到任何笑话")

    clean, title, body = random.choice(jokes)
    # 去掉正文首尾的空行（标题后往往有一空行），但保留正文内部的多段空行
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    body_text = "\n".join(body).rstrip("\n")

    header = f"【{clean} · 《{title}》】"
    out = header + "\n\n" + body_text
    # 末尾只保留一个换行，绝不在末尾留空行
    sys.stdout.write(out.rstrip("\n") + "\n")


if __name__ == "__main__":
    main()