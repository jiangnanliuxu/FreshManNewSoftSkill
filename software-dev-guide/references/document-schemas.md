# Document Schemas

## Docs By Mode

| Doc | light | standard | strict |
| --- | --- | --- | --- |
| 00-项目状态总览.md | required | required | required |
| 01-项目需求说明书.md | simplified | required | required |
| 02-产品页面与业务流程.md | simplified | required | required |
| 03-技术方案与模块拆分.md | simplified | required | required |
| 04-开发任务看板.md | required | required | required |
| 05-开发日志.md | required | required | required |
| 06-测试计划.md | simplified | required | required |
| 07-测试报告.md | required | required | required |
| 08-上线检查清单.md | optional | required | required |
| 09-需求变更记录.md | optional | required | required |
| 10-需求模块测试追踪矩阵.md | optional | required | required |
| 11-协同事件日志.md | optional | recommended | required |
| 12-用户确认门禁.md | optional | required | required |
| 13-异常处理记录.md | optional | recommended | required |
| 14-回滚与撤销记录.md | optional | recommended | required |
| 15-UI交互验收标准.md | simplified | required | required |
| 16-最终交付包说明.md | required | required | required |

## Status Values

Use only:

```text
未开始
待确认
已确认
待拆分
已拆分
待开发
开发中
待完整度检查
待测试
测试中
待修复
待回滚
已暂停
已取消
已完成
已交付
```

## 00-项目状态总览.md

```markdown
# 项目状态总览

## 基本信息
项目名称：
项目类型：
技术栈：
项目路径：
复杂度模式：
当前阶段：
当前模块：
当前阻塞点：
最后更新时间：

## 总体进度
| 阶段 | 状态 | 产物 | 是否完成 |
| --- | --- | --- | --- |

## 模块状态
| 模块 | 名称 | 需求拆分 | 开发 | 完整度检查 | 测试 | 当前状态 | 锁定状态 | 锁定 Agent | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 待处理事项
| 编号 | 来源 | 内容 | 所属模块 | 优先级 | 状态 |
| --- | --- | --- | --- | --- | --- |
```

## 04-开发任务看板.md

```markdown
| 模块 | 名称 | 需求拆分 | 开发 | 完整度检查 | 测试 | 状态 | 锁定状态 | 负责人 | 日志位置 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

## 10-需求模块测试追踪矩阵.md

```markdown
| 需求ID | 来源 | 需求名称 | 优先级 | 页面ID | 模块ID | 接口 / 数据 | 开发状态 | 测试用例ID | 测试状态 | 是否阻塞上线 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

断链:

- Requirement without module: requirements not decomposed.
- Module without development status: not in task board.
- Developed P0 without test case: testing not arranged.
- Failed test without repair task: defect not routed back.

## 16-最终交付包说明.md

```markdown
# 最终交付包说明

## 项目基本信息
项目名称：
项目类型：
技术栈：
项目路径：
当前版本：
交付日期：

## 项目简介

## 已完成功能
| 功能ID | 功能名称 | 所属模块 | 状态 | 说明 |
| --- | --- | --- | --- | --- |

## 如何运行项目
1. 安装依赖：
2. 启动命令：
3. 本地访问地址：
4. 构建命令：

## 如何测试项目
1. 核心测试路径：
2. 测试账号：
3. 测试数据：
4. 已通过测试：

## 已知问题
| 问题 | 影响 | 建议处理 |
| --- | --- | --- |

## 后续优化建议
| 优化项 | 优先级 | 原因 |
| --- | --- | --- |
```

