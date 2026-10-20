# 抖音同城获客与0粉起号 Skill

为本地门店和上门服务商家，把真实业务变成可直接拍摄、发布和承接咨询的抖音内容。

适用于宽带安装、通信门店、手机维修、家政、餐饮、汽修、美业等本地业务。支持真人出镜、只拍手和现场、兼职运营等情况。

## 下载即用

| 你用什么工具 | 下载什么 | 怎样用 |
|---|---|---|
| 豆包或其他支持文档的AI | [完整Markdown文档](docs/抖音同城获客起号-Skill完整文档.md?raw=true) | 上传文档，再提供业务信息 |
| 支持Skills的AI工具 | [技能导入ZIP包](downloads/抖音同城获客起号-技能导入包.zip?raw=true) | 解压后按工具支持的方式安装技能文件夹 |
| 支持.skill导入的工具 | [.skill安装包](downloads/douyin-local-acquisition.skill?raw=true) | 按工具实际导入能力使用 |

查看文档：[开始使用](docs/开始使用.md) · [Skill入口](douyin-local-acquisition/SKILL.md)

如果下载链接在当前浏览器只显示文本，可用页面上的下载按钮；完整仓库也可从 **Code → Download ZIP** 获取。

## 复制这句话开始

> 按这份同城获客起号Skill，为我制作完整方案。我在苏州吴中做手机基础使用辅导和服务答疑，主要服务租房和家庭用户，目前0粉，只拍成年工作人员的手部演示，每周能拍4条。请给我账号搭建、三条置顶完整稿、40条选题、首周完整拍摄包、30天排期、咨询接待话术和复盘表。缺少的关键信息一次问清，不要编造价格、年限和客户案例。

把城市、业务、客户和拍摄条件换成自己的即可。

安装到Codex后，可以直接说：

> 使用 douyin-local-acquisition，为我的本地业务制作0粉起号方案。

也可以让支持安装GitHub Skills的助手完成安装：

> 安装 https://github.com/isllyy/dyhk 仓库里的 douyin-local-acquisition Skill。

## 会得到什么

- 账号定位、人设、昵称、简介、头像和背景图方案。
- 三条置顶视频完整稿、四类各10条的选题库。
- 首周完整口播、镜头表、封面字、发布文案和行动引导。
- 根据拍摄能力安排的30天执行计划。
- 评论与私信话术、咨询筛选、预约承接及空白CSV台账。
- 第7/14/30天复盘规则，帮助决定下一轮具体改什么。

首周以后的选题按需展开。如果需要30条或40条完整口播稿，请明确提出；选题提纲不会冒充完整稿。

## 日常继续用

**出稿：**“沿用已确认的商家资料，把Z03展开成40秒完整拍摄包。”

**复盘：**“按这个Skill复盘下面的首周数据，安排下一周最值得验证的一项改动。”

**多店：**“为这几家门店分别生成首周内容，根据区域和真实素材设计，别只换人名。”

## 内容原则

优先解决服务区内客户的真实问题。从第一周交叉安排本地需求、专业解答、服务证据和咨询入口。

不编造客户故事、从业年限、资质、价格或统计数字；不承诺固定播放量、粉丝或订单；不把所谓养号、破池阈值当作官方规则。公开内容同时执行下方运营红线。公开内容同时执行下方运营红线。

Skill提供策略和内容，账号实际功能、发布结果、咨询、预约与成交分别核实。平台功能和行业规则以当前官方资料、账号后台为准。[官方资料与核验边界](douyin-local-acquisition/references/sources.md)

## 文件结构

```text
douyin-local-acquisition/
  SKILL.md
  agents/openai.yaml
  references/
    content-production.md
    execution-conversion-review.md
    sources.md
  assets/
    content-tracker.csv
    lead-tracker.csv
docs/
  开始使用.md
  抖音同城获客起号-Skill完整文档.md
downloads/
  douyin-local-acquisition.zip
  douyin-local-acquisition.skill
```

版本：v1.1.0。运营红线更新：2026-10-20。


## v1.1.0：运营红线与审核

此版纳入用户提供的内部运营要求，非平台官方完整禁词表。使用前先读[运营红线与发布审核](douyin-local-acquisition/references/operating-redlines.md)，并在新会话加载新版；旧安装和旧稿件不会自动更新。

- 违禁词及语义：政策、运营商、金融、绝对化、虚假承诺、诱导消费、明确禁提业务、站外引流与靓号相关话题；“免费”也不提。公开内容不能用否定句重复禁词，不能换词推销同一禁题。
- 画面：联系方式/二维码、未授权用户人脸和隐私、未成年人、运营商Logo、号卡实物、横幅均按要求检查。
- 流程：生成前筛题，公开稿固定词初查，再做语义、画面/声音和真实人工审核。脚本未检出不代表审核通过。

对独立公开稿可运行：

```bash
python3 douyin-local-acquisition/scripts/check_redlines.py 公开稿.md
```

[根目录含SKILL.md的本地导入包](downloads/抖音同城获客起号-技能导入包.zip?raw=true)可转发给同事在支持本地技能导入的工具中使用，无需访问GitHub；是否导入成功需在目标工具核实。已有用户请重新导入本版。
