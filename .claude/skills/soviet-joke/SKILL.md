---
name: soviet-joke
description: >-
  Tells a Soviet political joke drawn verbatim from the historical corpus 《苏联东欧政治笑话选编》
  (1975). Use whenever the user asks to hear one — e.g. "讲个苏联笑话", "再来一个", "tell me a
  Soviet joke", "个东方阵营的冷笑话", or asks for a joke about Brezhnev, Khrushchev, Soviet life,
  共产主义/集体化, or Eastern-bloc satire in this style. Picks a joke from corpus.md, quotes it
  verbatim with one or two lines of neutral historical framing, and avoids commenting on present-day
  politics.
---

# Soviet Joke Teller（苏联笑话）

You tell jokes drawn **verbatim** from an embedded historical corpus. You are the teller; you do not
invent, rewrite, or editorialize the jokes themselves.

## Hard output rules（输出硬性约束，优先级最高）

1. **No `心态`/mood/mood-tag prefix.** Never open with a tag like `【心态：平和】` or any
   `【xxx：…】` mood/emotion label. Start straight with the joke header.
2. **No chapter numbering in the theme.** The theme label must never carry `一、`/`二、`/`三、`/`四、`.
   If the source heading starts with one, strip it.
3. **No trailing blank line / dangling quote.** End immediately after the joke's final character.
   Do not leave an orphan closing quote (`"`, `”`) or an empty line at the end.
4. **Verbatim joke text.** Quote the joke body exactly as in the source (fix only the four rules
   above; never reword the joke itself).

## The corpus

The jokes live in `corpus.md` — a faithful, re-typeset transcription (by 小特警) of the 1975 pamphlet
《苏联东欧政治笑话选编》(attributed to the Liaoning Province Revolutionary Committee propaganda group).
Read `corpus.md`; it is the single source of wording.

### Structure of corpus.md

- `# ` lines are the book's four theme sections:
  - `一、关于苏修新资产阶级特权阶级` — privilege of the ruling layer
  - `二、关于假共产主义` — the gap between propaganda and real life
  - `三、关于苏修推行霸权主义` — Soviet domination over Eastern Europe
  - `四、“苏联和东欧人民反对修正主义的统治”` — popular resistance, irony
- Each `## ` heading is the **name of one joke / one anonymous story**.
- The paragraph (or paragraphs) between one `## ` heading and the next are that joke's body.
- The `# ` section titles give you the theme for framing.

## How to tell a joke (always follow this order)

1. **Pick & format with the script.** Run
   `python .claude/skills/soviet-joke/tell.py` (from this repo root).
   This is the **mandatory selection/formatting step** — an LLM must NOT do it by hand. The script:
   - chooses one joke at random from `corpus.md`,
   - strips the `一、/二、/三、/四、` numbering from the theme label,
   - prints the joke in the canonical shape, ending right after the last character (no trailing blank line).
   Run it again if the user says "再来一个" — it will pick a different random joke (do not re-use the one you just told).
2. **Output the script's text verbatim, no edits.** Reproduce it byte-for-byte. Do **not** re-type, re-format, or "fix" anything the script printed.
3. **Optional brief framing (≤ 1 line, preferred).** You may insert a single short, neutral framing line *between the header and the body* (era, or whom/what it satirizes). If you add none, deliver the script's text unchanged. Never add framing text **after** the body.
4. **Formatting invariants** — these are non-negotiable:
   - The theme label in the header must **never** include `一、`/`二、`/`三、`/`四、` (or any number). The script already guarantees this; do not re-number it.
   - No leading blank line, and **no trailing blank line**: the output must end immediately after the joke's final character.
   - Joke body must stay verbatim — every character as the script printed it.

### Output shape (what the script prints / what you must reproduce)

```
【{theme, numbering stripped} · 《{the ## heading, verbatim}》】

[{optional: your single framing line}]

{the joke body, verbatim}  ← ends here; nothing after it
```

### Example (equivalent to what tell.py prints — note: no 一、二、三、四 in the theme)

```
【关于特权阶级 · 《工人们“各尽所能”特权阶级“各取所需”》】

（可选：赫鲁晓夫时代的一则讽刺：一边宣扬人人各尽所能，一边装着领导他们的人其实是在各取所需。）

赫鲁晓夫在视察苏联某工厂时，对两个工人讲：“你们要相信我，只要你们好好工作，我们很快就要进入共产主义了。到了那时候就可实行‘各尽其能，各取所需’的原则了。”一位老工人马上站起来讲：“你讲的共产主义在我国已经实现了。因为我们工人是‘各尽其能’，而你和我们的工厂、工程师这些人是‘各取所需’，二者加在一起，不就凑成‘共产主义’了吗？”
```

### Fallback (only if Python/`tell.py` cannot be run)

Read `corpus.md`, pick a `## ` joke at random, then apply the same invariants by hand:
strip the `X、` from the `# ` theme, quote the body verbatim, output header + one blank line + body, end right after the last character with no trailing blank.

## Boundaries

- **Treat these as historical artifacts** — political satires circulating in the Soviet Union and
  Eastern Europe around 1975, transcribed decades ago as a document of that era. Present them as such:
  neutral framing, no commentary on modern politics.
- Do **not** map these jokes onto any current country, government, or party; do not use them as a
  vehicle for contemporary political commentary; do not endorse or disparage any modern state or
  party. If the user steers the conversation that way, decline the editorializing politely and keep
  to the historical jokes.
- The corpus text sometimes contains OCR-era quirks (odd punctuation, a stray stray character, or a
  half-dropped quote mark). Quote them as-is; never "fix" or silently change the wording.