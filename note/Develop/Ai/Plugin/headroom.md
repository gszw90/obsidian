## 简介
Headroom 是一款专为 AI Agent 和 LLM 应用打造的开源**上下文压缩层**。它部署在你的 Agent 或应用与 LLM 提供商之间，在数据抵达模型之前，会拦截每一项提示词、工具输出、日志、文件及对话片段——随后在保持回答准确率的前提下，将其**压缩 60%–95%**。该系统**本地**运行，支持通过按需检索进行**可逆**压缩，并以 Python 库、即插即用代理、MCP 服务器以及 TypeScript SDK 等多种形式交付。
[GitHub](https://github.com/headroomlabs-ai/headroom)

## 安装
```bash
uv tool install "headroom-ai[all]"
```

### 文档
[简介](https://headroomlabs-ai.github.io/headroom/)
[快速开始](https://headroomlabs-ai.github.io/headroom/quickstart/)
[用户指南](https://headroomlabs-ai.github.io/headroom/proxy/)
[集成](https://headroomlabs-ai.github.io/headroom/integration-guide/)
[原理](https://headroomlabs-ai.github.io/headroom/ARCHITECTURE/)
[部署](https://headroomlabs-ai.github.io/headroom/macos-deployment/)

## 痛点解决
使用`claude code` ,`codex`等工具时工具的输出非常庞大，大部分数据是冗余的，会造成token紧张，费用上升，上下文空间被填满。该工具的作用是拦截你的api调用，变换流水线运行消息，调用带有优化消息的api，将度量记录到数据库，返回不变的响应，通过这一些列的操作来降低token的消耗。

## 启动

**原生**
如果是直接使用的cluade code，codex的原生模型，可以使用以下命令:
```bash
headroom wrap claude
headroom wrap codex

headroom unwrap claude
headroom unwrap codex
```

## 组装
#### claude code + glm
1. 启动代理
```bash
headroom proxy --port 8787 --anthropic-api-url https://open.bigmodel.cn/api/anthropic
```
2. 修改 ~/.claude/setting.json 中的ANTHROPIC_BASE_URL的值
```json
{
 "env":{
 "ANTHROPIC_BASE_URL":"127.0.0.1:8787"
 }
}
```
3. 直接启动claude
```bash
claude
```