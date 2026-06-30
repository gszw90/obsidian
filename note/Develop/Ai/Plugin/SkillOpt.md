## 简介
像训练模型一样训练skill，通过一步步迭代skill来达到优化skill的目的
[github](https://github.com/microsoft/SkillOpt)

## 核心工作流程
1. **Harvest(收割)**: 收集过去的会话记录
2. **Mine(挖掘)**: 发现你反复在做/反复出错的任务
3. **Replay（重放）**：离线重跑这些任务
4. **Reflect（反思）**：分析失败原因，提出规则修改
5. **Gate（门控验证）**：只在修改确实提升留出集分数时才保留
6. **Stage & Adopt**：生成提案，你审核后才正式采纳

## 安装

[安装文档](https://github.com/microsoft/SkillOpt/blob/main/docs/sleep/README.md)

```bash
# clone repo
git clone git@github.com:microsoft/SkillOpt.git

# 进入文件夹
cd SkillOpt

## 打开claude code
claude

## 添加plugin market
/plugin marketplace add ./plugins/claude-code
/plugin instll skillopt-sleep
/reload plugins
```

## 命令参数
```bash
# 在claude中的斜杠命令
/skillopt-sleep:skillopt-sleep [ run | dry-run | status | adopt | harvest | schedule | unschedule ] (default: status)
```

| 命令         | 作用                                          | 示例                                                                               |
| ---------- | ------------------------------------------- | -------------------------------------------------------------------------------- |
| status     | 查看历史运行次数+最新暂存提案(只读)                         |                                                                                  |
| dry-run    | 完整执行 harvest→mine→replay→report，**不暂存任何改动** |                                                                                  |
| run        | 完整执行并**暂存**提案，但不会修改线上文件                     |                                                                                  |
| adopt      | 将暂存提案写入 `CLAUDE.md` / `SKILL.md`（自动备份旧文件）   |                                                                                  |
| havest     | 调试用：仅打印挖掘到的重复任务                             |                                                                                  |
| schedule   | 设置夜间定时任务                                    | schedule --hour 3 --backend alcude <br><br>schedule --minute 25 --backend claude |
| unschedule | 移除夜间定时任务                                    |                                                                                  |
