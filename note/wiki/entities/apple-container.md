---
title: Apple Container
aliases: [Apple Container, apple/container, apple container]
type: entity
created: 2026-07-11
updated: 2026-07-11
tags: [容器, Apple, Swift, macOS, 实体]
---

# Apple Container

Apple 官方开源的 macOS 上创建与运行 **Linux 容器**的工具，基于轻量虚拟机，**Swift 编写**。

- **仓库**：[apple/container](https://github.com/apple/container) · Apache-2.0
- **语言**：Swift
- **文档**：https://apple.github.io/container/documentation/
- **场景**：Mac 上跑 Linux 容器，不依赖 Docker

## 与同域对比

| 工具 | 内核 | 定位 |
|------|------|------|
| **apple/container** | 轻量 VM（Swift） | Apple 官方，原生集成，极简 |
| [[OrbStack]] | 轻量 VM | 第三方，Docker/K8s/Linux VM 一体，性能优 |
| Docker Desktop | VM | 老牌，重 |

> [!key-insight] apple/container 是 Apple 对容器赛道的官方入场——轻量、Swift 原生，但功能面窄于 [[OrbStack]]（无 K8s/VM 一体）。适合只需 Linux 容器、追求 Apple 原生体验者。

## 出现

- [[GitHub Trending 月榜 2026-07]] #4（19,234 stars/月，47.5k 总）

## 待扩展

- 实测性能 vs OrbStack（启动/内存/IO）
- K8s 支持路线（当前仅容器）
