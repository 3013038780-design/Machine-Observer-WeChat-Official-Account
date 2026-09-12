# 微信公众号美化组件库

适用：**微信公众号原生编辑器** + **135 编辑器** + **秀米**。
所有组件**全部内联样式、零外部依赖、零 class / id 引用**——粘贴即用，不会被任何编辑器剥离。

---

## 📐 设计原则

1. **inline styles only** — 微信会扒掉 `<style>` 和 `class`，所有样式必须落在标签的 `style=""` 属性里
2. **避免 flexbox / position:absolute / pseudo-elements** — 容易被编辑器吃掉
3. **保留 background / border / border-radius / padding / margin / display:inline-block** — 这些都安全
4. **红色 (#B91C1C) 仅作 accent**，不要大面积使用，否则视觉疲劳
5. **白色 / 浅米色 (#FAFAFA) / 浅红 (#FDF6F5) 三层背景循环使用** — 避免单调
6. **letter-spacing 0.3-0.5px / line-height 1.85** 是中文公众号最佳阅读区间

---

## 🎨 配色系统

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色 (accent) | `#B91C1C` | 装饰条、强调词、标题色 |
| 辅助红 | `#C0392B` | 链接、小标题 |
| 浅红边框 | `#E5C4C0` | 分割线、链接下划线 |
| 极浅红背景 | `#FDF6F5` | 引语框、目录卡背景 |
| 米色背景 | `#FAFAFA` | 事实卡、来源框背景 |
| 浅灰边框 | `#EAEAEA` | bio 卡、数据卡边框 |
| 正文深色 | `#2c2c2c` | 段落正文 |
| 标题深色 | `#1a1a1a` | h1/h2 标题、bio 名 |
| 灰色辅文 | `#555` | 事实卡内容 |
| 浅灰辅文 | `#888` | 引语出处、副标题 |

---

## ✍️ 字体与间距系统

| 元素 | 字号 | 行高 | 字间距 | 颜色 |
|---|---|---|---|---|
| h1 主标题 | 22px | 1.5 | 0.5px | #1a1a1a / 居中 |
| 副标题 | 14px | 1.5 | 0.5px | #888 / 居中 / italic |
| h2 章节标题 | 18px | 1.5 | 0.5px | #1a1a1a / 居中 |
| h3 小标题 | 16px | 1.5 | 0.5px | #1a1a1a |
| 正文段落 | 14.5–15px | 1.85 | 0.3px | #2c2c2c / text-align:justify |
| 引语 | 15px | 1.85 | 0.3px | #1a1a1a / italic |
| 事实卡 | 14px | 1.85 | 0.3px | #2c2c2c |
| 来源 / 出处 | 13px | 1.75 | 0.3px | #555 / #888 |
| 容器边距 | padding: 16-24px / margin: 14-32px | | | |

---

## 🧱 组件清单（10 个）

> 所有组件代码可直接复制 → 粘贴进 .md 或 135 编辑器源码模式 → 改文字内容即用。

---

### 1️⃣ 顶部栏目 Tag

**用途**：文章最顶部，标识所属栏目（如「深度·人物故事」、「治理双周报」）

```html
<section style="margin:0 0 8px;text-align:center;">
<div style="display:inline-block;padding:4px 12px;background:#B91C1C;color:#ffffff;font-size:12px;letter-spacing:3px;border-radius:2px;">深 度 · 人 物 故 事</div>
</section>
```

**变体**：可换色（深度族用红、速读族用浅米色 + 红字）

---

### 2️⃣ 主标题 + 副标题

**用途**：文章主标题区域

```html
<h1 style="font-size:22px;font-weight:bold;color:#1a1a1a;text-align:center;margin:18px 0 8px;line-height:1.5;letter-spacing:0.5px;">华为芯片女王何庭波：一个 30 年的"备胎"故事</h1>

<p style="text-align:center;font-size:14px;color:#888;letter-spacing:0.5px;margin:0 0 26px;">从光通信芯片设计师，到提出全球首个由中国企业发表的半导体演进原则</p>
```

---

### 3️⃣ 目录卡 / 摘要卡

**用途**：本期目录、要点摘要、章节索引

```html
<section style="margin:0 0 16px;background:#FDF6F5;border-radius:6px;padding:18px 22px;border-left:3px solid #B91C1C;">
<div style="font-size:15px;font-weight:bold;color:#B91C1C;letter-spacing:3px;margin-bottom:14px;">本 期 目 录</div>
<p style="margin:10px 0;line-height:1.75;color:#333;font-size:15px;letter-spacing:0.5px;"><strong style="color:#B91C1C;font-weight:bold;">01</strong>　[条目标题]<br/><span style="color:#999;font-size:13px;">[来源标注]</span></p>
<p style="margin:10px 0;line-height:1.75;color:#333;font-size:15px;letter-spacing:0.5px;"><strong style="color:#B91C1C;font-weight:bold;">02</strong>　[条目标题]<br/><span style="color:#999;font-size:13px;">[来源标注]</span></p>
</section>
```

**适用**：周报、综述类、长文导航

---

### 4️⃣ 总览框 / 重磅框

**用途**：本期总览、核心摘要、editor's note

```html
<section style="margin:16px 0 20px;border-radius:8px;overflow:hidden;border:1px solid #f0d6d4;">
<section style="background:#B91C1C;padding:12px 20px;">
<span style="color:#ffffff;font-size:16px;font-weight:bold;letter-spacing:4px;">本 期 总 览</span>
<span style="float:right;">
<span style="display:inline-block;width:8px;height:8px;background:#ffffff;opacity:0.5;margin-right:4px;vertical-align:middle;"></span>
<span style="display:inline-block;width:8px;height:8px;background:#ffffff;opacity:0.9;vertical-align:middle;"></span>
</span>
</section>
<section style="background:#ffffff;padding:20px 22px 6px;">
<p style="margin:14px 0;line-height:1.85;color:#333;letter-spacing:0.5px;text-align:justify;font-size:15px;"><strong style="color:#B91C1C;font-weight:bold;">第一，[要点 1]。</strong> [论述...]</p>
<p style="margin:14px 0;line-height:1.85;color:#333;letter-spacing:0.5px;text-align:justify;font-size:15px;"><strong style="color:#B91C1C;font-weight:bold;">第二，[要点 2]。</strong> [论述...]</p>
<p style="margin:14px 0;line-height:1.85;color:#333;letter-spacing:0.5px;text-align:justify;font-size:15px;"><strong style="color:#B91C1C;font-weight:bold;">第三，[要点 3]。</strong> [论述...]</p>
</section>
</section>
```

**视觉效果**：深红色 header bar（带 2 个白色装饰点）+ 白色内容区。右上角小白点是装饰，可保可删

---

### 5️⃣ 编号章节标题

**用途**：长文章节分隔、有序内容展开

```html
<section style="margin:32px 0 14px;text-align:center;">
<span style="display:inline-block;width:60px;height:1px;background:#E5C4C0;vertical-align:middle;"></span>
<span style="display:inline-block;width:32px;height:32px;background:#B91C1C;color:#ffffff;font-size:14px;font-weight:bold;line-height:32px;text-align:center;vertical-align:middle;margin:0 12px;border-radius:2px;">1</span>
<span style="display:inline-block;width:60px;height:1px;background:#E5C4C0;vertical-align:middle;"></span>
<h2 style="font-size:18px;font-weight:bold;color:#1a1a1a;margin:10px 12px 0;line-height:1.5;letter-spacing:0.5px;display:block;border:none;padding:0;">[章节标题]</h2>
</section>
```

**视觉效果**：横线─[红色编号方块]─横线 + 居中标题
**变体**：把编号「1」换成中文「来源」「附录」等也好看

---

### 6️⃣ 小标题装饰（簡）

**用途**：章节内的二级小标题、分组标题

```html
<h3 style="font-size:16px;font-weight:bold;color:#1a1a1a;margin:36px 0 14px;padding:6px 0 6px 12px;border-left:3px solid #B91C1C;line-height:1.5;letter-spacing:0.5px;">[小标题文本]</h3>
```

**视觉效果**：3px 红色左条 + 深色加粗标题（轻量、不抢眼）

---

### 7️⃣ Bio 卡片 / 信息卡

**用途**：人物简介、产品介绍、案例列表（适合多个并列）

```html
<section style="margin:16px 0;padding:16px 20px;background:#ffffff;border:1px solid #EAEAEA;border-left:3px solid #B91C1C;border-radius:4px;">
<div style="font-size:16px;font-weight:bold;color:#1a1a1a;margin-bottom:6px;letter-spacing:0.3px;">01　[名称 / 标题]</div>
<div style="font-size:13px;color:#555;margin-bottom:12px;letter-spacing:0.3px;line-height:1.7;">[元数据：日期/出处/属性等]</div>
<p style="margin:6px 0;font-size:14.5px;line-height:1.85;color:#2c2c2c;letter-spacing:0.3px;">[正文内容...]</p>
</section>
```

**视觉效果**：白底 + 浅灰边框 + 3px 红色左条
**适用**：人物清单、产品对比、案例罗列、知识卡

---

### 8️⃣ 引语框 / Quote Box

**用途**：突出原话、引用、关键发言

```html
<section style="margin:22px 0;padding:18px 22px;background:#FDF6F5;border-left:4px solid #B91C1C;border-radius:2px;">
<p style="margin:0;line-height:1.85;color:#1a1a1a;font-size:15px;letter-spacing:0.3px;font-style:italic;">"[引语内容]"</p>
<p style="margin:8px 0 0 0;font-size:13px;color:#888;letter-spacing:0.3px;">——[说话人]，[场合 / 时间]</p>
</section>
```

**长引语变体**：多段引语用多个 `<p>` 包，最后一段加出处即可

---

### 9️⃣ 事实卡 / Factbox

**用途**：关键事实速读、产品参数、数据汇总

```html
<section style="margin:24px 0;padding:20px 24px;background:#FAFAFA;border-radius:4px;border-top:2px solid #B91C1C;">
<div style="font-size:14px;font-weight:bold;color:#B91C1C;letter-spacing:3px;margin-bottom:14px;">关 键 事 实</div>
<p style="margin:6px 0;font-size:14px;line-height:1.85;color:#2c2c2c;letter-spacing:0.3px;"><strong style="color:#1a1a1a;">[标签]</strong>　[内容]</p>
<p style="margin:6px 0;font-size:14px;line-height:1.85;color:#2c2c2c;letter-spacing:0.3px;"><strong style="color:#1a1a1a;">[标签]</strong>　[内容]</p>
</section>
```

**视觉效果**：米色背景 + 2px 红色顶部边框 + 标签栏内容对照
**适用**：人物 factbox、产品规格、政策要点速读、本期作者署名

---

### 🔟 数据 / 路线图卡

**用途**：表格式数据、时间线、路线图

```html
<section style="margin:20px 0;padding:14px 18px;background:#FAFAFA;border-radius:4px;border:1px solid #EAEAEA;">
<div style="font-size:13px;font-weight:bold;color:#B91C1C;letter-spacing:1px;margin-bottom:10px;">[卡片标题]</div>
<p style="margin:4px 0;font-size:13px;line-height:1.7;color:#2c2c2c;letter-spacing:0.3px;"><strong style="color:#1a1a1a;">[标签]</strong>　[内容]</p>
<p style="margin:4px 0;font-size:13px;line-height:1.7;color:#2c2c2c;letter-spacing:0.3px;"><strong style="color:#1a1a1a;">[标签]</strong>　[内容]</p>
<p style="margin:8px 0 0 0;font-size:12px;color:#888;letter-spacing:0.3px;">[补充说明 / 备注]</p>
</section>
```

**视觉效果**：完整边框 + 米色背景 + 紧凑行高
**适用**：年代时间线、产品路线图、价格表

---

### 1️⃣1️⃣ 来源框 / References

**用途**：文末参考文献、来源声明、版权说明

```html
<section style="margin:36px 0 14px;padding:18px 22px;background:#FAFAFA;border-radius:4px;border-top:2px solid #B91C1C;">
<div style="font-size:14px;font-weight:bold;color:#B91C1C;letter-spacing:3px;margin-bottom:12px;">来 源</div>
<p style="margin:5px 0;font-size:13px;line-height:1.75;color:#555;letter-spacing:0.3px;">[机构名]｜<a href="[URL]" style="color:#B91C1C;text-decoration:none;border-bottom:1px solid #E5C4C0;">[文章标题]</a>（[日期]）</p>
<p style="margin:5px 0;font-size:13px;line-height:1.75;color:#555;letter-spacing:0.3px;">[机构名]｜<a href="[URL]" style="color:#B91C1C;text-decoration:none;border-bottom:1px solid #E5C4C0;">[文章标题]</a>（[日期]）</p>
</section>
```

---

## ⚠️ 135 编辑器兼容性注意事项

| ✅ 安全使用 | ❌ 容易被剥离 |
|---|---|
| `background-color`（实色） | `linear-gradient`（部分版本会丢） |
| `border` / `border-radius` | `flexbox`（display:flex） |
| `padding` / `margin` | `position:absolute / fixed / sticky` |
| `display:inline-block` | `transform / animation` |
| `font-size / color / line-height` | `:before / :after` 伪元素 |
| `text-align` | `box-shadow`（部分版本简化） |
| `float:right`（小心使用） | `media query` |
| `letter-spacing` | `class / id` 选择器（必被去） |
| `<section> / <div> / <p> / <span>` 嵌套 | `<style>` 标签 |

**关键经验**：
1. **优先用 `<section>` 而不是 `<div>`** — 微信对 section 处理更稳定
2. **避免连续超过 3 层 nested section** — 嵌套深度过深可能被简化
3. **opacity 在文字上用 OK，但在背景上有时失效** — 不要靠 opacity 做色阶
4. **inline-block + width + height 模拟分割线** 是最稳定的「画图」方法（不用 hr）
5. **粘贴姿势**：浏览器打开 .html → Cmd+A 全选 → Cmd+C 复制 →（不要复制 .html 源码）→ 编辑器粘贴。复制源码会被识别为代码块

---

## 🧩 组件搭配示例

### 示例 A：标准长文结构（如双周报）
```
顶部栏目 Tag (1)
主标题 + 副标题 (2)
目录卡 (3)  ← 列出本期 7-9 条
总览框 (4)  ← 3-4 段编辑视角综述
编号章节标题 (5)  ← × N（每条事件一个）
  └ 正文段落
来源框 (11)
```

### 示例 B：人物深度文章
```
顶部栏目 Tag (1)  ← 「深度·人物故事」
主标题 + 副标题 (2)
引子段落（无装饰）
关键事实卡 (9)  ← 出生 / 学历 / 现任 / 履历速读
编号章节标题 (5)  ← × N（按时间线或主题）
  └ 正文段落
  └ 引语框 (8)  ← 关键原话
  └ 数据卡 (10)  ← 路线图 / 时间线
来源框 (11)
```

### 示例 C：清单合集文章（如「20 人小传」）
```
顶部栏目 Tag (1)
主标题 + 副标题 (2)
摘要卡 (3)  ← 简要说明
编号章节标题 (5)  ← 大类划分
  └ 小标题装饰 (6)  ← 子类
    └ Bio 卡片 (7)  ← × N 并列
来源框 (11)
```

---

## 📁 配套文件

- `~/.claude/skills/wechat-article/assets/theme.json` — 这套配色已写入主题文件（render.py 默认使用）
- `~/.claude/skills/wechat-article/scripts/render.py` — Markdown → 公众号 HTML 渲染脚本，已支持 raw HTML 块透传（即在 .md 中可以直接嵌入本组件库的 HTML 代码）

## 🛠️ 在 Claude Code 工作流中使用

1. **写 .md 草稿** — 段落用 markdown 写，需要装饰处直接粘贴本库 HTML 代码块
2. **render.py 渲染** — `python3 scripts/render.py drafts/foo.md -o drafts/foo.html`
3. **浏览器预览** — 打开 .html 检查视觉
4. **复制到公众号** — Cmd+A 全选 → 复制 → 粘贴进 135 / 公众号原生编辑器

---

## 🔄 维护与扩展

- 每出一篇新文章，如果用到了本库**没有**的视觉元素 → 沉淀进本文件作为第 N+1 组件
- 配色 / 字号有改动 → 同步更新 `assets/theme.json`
- 不要为每个栏目独立设计视觉系统 → 复用本库，按栏目族（旗舰 / 深度 / 速读）分组用不同 tag
