# YOTIME 悠享家 MCP Skill

> 让 AI 读懂悠享家 — 门店查询、产品介绍、外卖入口，一句话即可获取。

受 [金谷园饺子馆](https://github.com/JinGuYuan/jinguyuan-dumpling-skill) 启发，悠享家作为温州本地烘焙品牌，开源了自己的 MCP Skill，让 AI 助手可以直接回答关于悠享家的一切。

## 能问什么？

```
悠享家在哪里有门店？
鹿城区有哪些悠享家？
印象城那家悠享家几点开门？
悠享家有什么招牌产品？
悠享家时代店的外卖链接是什么？
怎么联系悠享家客服？
```

## 工具列表

| 工具 | 说明 |
|------|------|
| `get_brand_info` | 品牌介绍、热线、客服微信 |
| `list_stores` | 门店列表，支持按区域筛选 |
| `find_store` | 按关键词搜索门店 |
| `get_products` | 主推产品列表（含图片） |
| `get_delivery_links` | 美团/饿了么外卖链接 |
| `get_contact` | 客服联系方式 |

## 安装

### 最简单的方式：告诉你的 AI 助手

直接复制下面这句话发给你的 AI 助手：

> 帮我安装悠享家 Skill，仓库地址：https://github.com/yechengyu/yotime-mcp

Agent 会自动克隆仓库并安装到对应的 Skill 目录。

### 手动克隆到 Skill 目录

将本仓库克隆到你项目下的 Skill 目录，不同 IDE 对应的路径：

| IDE | Skill 目录 |
|-----|-----------|
| Qoder | `.qoder/skills/yotime-mcp/` |
| Cursor | `.cursor/skills/yotime-mcp/` |
| Trae | `.trae/skills/yotime-mcp/` |
| Windsurf | `.windsurf/skills/yotime-mcp/` |
| Claude Code | `.claude/skills/yotime-mcp/` |
| 通用 | `.agents/skills/yotime-mcp/` |

```bash
# 示例：安装到 Claude Code
git clone https://github.com/yechengyu/yotime-mcp.git \
    .claude/skills/yotime-mcp
```

只要目录下有 `SKILL.md`，Agent 下次启动就会自动加载这个 Skill。

## 关于悠享家

悠享家（YOTIME）起始于2009年，专注烘焙甜品，目前在温州拥有15家门店。

- 官网/小程序：有赞商城搜索"悠享家"
- 全国热线：4008273773
- 客服企微：yotime-wm1
- 品牌理念：**开心时刻，悠享家**

---

*当餐厅信息成为 AI 可读接口，万物皆可 CLI 化。*
