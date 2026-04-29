# Software Dev Guide Skill 使用说明

## 目录

```text
software-dev-guide/
├── SKILL.md
├── agents/openai.yaml
├── references/
└── scripts/
```

## 基本用法

在 Codex 中使用该 Skill 时，可以这样说：

```text
使用 software-dev-guide，带我从 0 开始做一个学生管理系统。
```

或者：

```text
使用 software-dev-guide，继续开发这个项目，项目路径是 /path/to/project。
```

## 初始化项目文档

```bash
python software-dev-guide/scripts/init_project_docs.py \
  --project-path /path/to/project \
  --mode standard \
  --project-name "学生管理系统" \
  --project-type "Web 后台系统"
```

## 校验 Harness 状态

```bash
python software-dev-guide/scripts/validate_harness_state.py \
  --project-path /path/to/project \
  --mode standard
```

## 查找下一步任务

```bash
python software-dev-guide/scripts/find_next_task.py \
  --project-path /path/to/project
```

## Stitch 增强设计

阶段 3 产品设计时，用户可以选择：

```text
1. Codex 原生 UI 设计
2. Stitch 增强 UI 设计
```

如果当前 Codex 环境有 Stitch MCP，Agent 可以走 Stitch 项目和页面读取流程；如果没有，就降级为 Codex 原生 UI、截图、导出文件或手动说明。

