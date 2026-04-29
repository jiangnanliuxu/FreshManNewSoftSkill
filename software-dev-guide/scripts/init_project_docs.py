#!/usr/bin/env python3
"""Initialize software-dev-guide project docs."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


DOCS_BY_MODE = {
    "light": [
        "00-项目状态总览.md",
        "01-项目需求说明书.md",
        "02-产品页面与业务流程.md",
        "03-技术方案与模块拆分.md",
        "04-开发任务看板.md",
        "05-开发日志.md",
        "06-测试计划.md",
        "07-测试报告.md",
        "15-UI交互验收标准.md",
        "16-最终交付包说明.md",
    ],
    "standard": [
        "00-项目状态总览.md",
        "01-项目需求说明书.md",
        "02-产品页面与业务流程.md",
        "03-技术方案与模块拆分.md",
        "04-开发任务看板.md",
        "05-开发日志.md",
        "06-测试计划.md",
        "07-测试报告.md",
        "08-上线检查清单.md",
        "09-需求变更记录.md",
        "10-需求模块测试追踪矩阵.md",
        "11-协同事件日志.md",
        "12-用户确认门禁.md",
        "13-异常处理记录.md",
        "14-回滚与撤销记录.md",
        "15-UI交互验收标准.md",
        "16-最终交付包说明.md",
    ],
    "strict": [
        "00-项目状态总览.md",
        "01-项目需求说明书.md",
        "02-产品页面与业务流程.md",
        "03-技术方案与模块拆分.md",
        "04-开发任务看板.md",
        "05-开发日志.md",
        "06-测试计划.md",
        "07-测试报告.md",
        "08-上线检查清单.md",
        "09-需求变更记录.md",
        "10-需求模块测试追踪矩阵.md",
        "11-协同事件日志.md",
        "12-用户确认门禁.md",
        "13-异常处理记录.md",
        "14-回滚与撤销记录.md",
        "15-UI交互验收标准.md",
        "16-最终交付包说明.md",
    ],
}


def table(headers: list[str]) -> str:
    return "| " + " | ".join(headers) + " |\n| " + " | ".join(["---"] * len(headers)) + " |\n"


def templates(project_path: Path, mode: str, project_name: str, project_type: str) -> dict[str, str]:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "00-项目状态总览.md": f"""# 项目状态总览

## 基本信息
项目名称：{project_name}
项目类型：{project_type}
技术栈：
项目路径：{project_path}
复杂度模式：{mode}
当前阶段：需求整理
当前模块：
当前阻塞点：
最后更新时间：{now}

## 总体进度
{table(["阶段", "状态", "产物", "是否完成"])}| 需求整理 | 未开始 | docs/01-项目需求说明书.md | [ ] |
| 产品设计 | 未开始 | docs/02-产品页面与业务流程.md | [ ] |
| 技术方案 | 未开始 | docs/03-技术方案与模块拆分.md | [ ] |
| 模块开发 | 未开始 | docs/04-开发任务看板.md | [ ] |
| 测试验证 | 未开始 | docs/07-测试报告.md | [ ] |
| 上线准备 | 未开始 | docs/08-上线检查清单.md | [ ] |
| 最终交付 | 未开始 | docs/16-最终交付包说明.md | [ ] |

## 模块状态
{table(["模块", "名称", "需求拆分", "开发", "完整度检查", "测试", "当前状态", "锁定状态", "锁定 Agent", "备注"])}
## 待处理事项
{table(["编号", "来源", "内容", "所属模块", "优先级", "状态"])}
""",
        "01-项目需求说明书.md": "# 项目需求说明书\n\n## 项目定位\n项目名称：\n一句话介绍：\n目标用户：\n用户痛点：\n核心场景：\n第一版目标：\n暂不做内容：\n\n## 功能清单\n" + table(["功能编号", "功能名称", "优先级", "用户价值", "验收标准", "状态"]),
        "02-产品页面与业务流程.md": "# 产品页面与业务流程\n\n## 页面列表\n" + table(["页面编号", "页面名称", "页面目标", "关联功能", "状态"]) + "\n## 用户流程\n",
        "03-技术方案与模块拆分.md": "# 技术方案与模块拆分\n\n## 技术栈\n前端：\n后端：\n数据库：\n部署方式：\n包管理器：\n启动命令：\n构建命令：\n测试命令：\n\n## 模块拆分\n",
        "04-开发任务看板.md": "# 开发任务看板\n\n" + table(["模块", "名称", "需求拆分", "开发", "完整度检查", "测试", "状态", "锁定状态", "负责人", "日志位置"]),
        "05-开发日志.md": "# 开发日志\n",
        "06-测试计划.md": "# 测试计划\n\n## 测试范围\n" + table(["模块", "来源", "是否开发完成", "是否需要测试", "原因"]),
        "07-测试报告.md": "# 测试报告\n\n## 测试结论\n待测试\n\n## 缺陷列表\n" + table(["BUG编号", "模块", "问题", "严重级别", "状态", "是否阻塞上线"]),
        "08-上线检查清单.md": "# 上线检查清单\n\n## 上线前检查\n" + table(["检查项", "状态", "说明"]),
        "09-需求变更记录.md": "# 需求变更记录\n",
        "10-需求模块测试追踪矩阵.md": "# 需求模块测试追踪矩阵\n\n" + table(["需求ID", "来源", "需求名称", "优先级", "页面ID", "模块ID", "接口 / 数据", "开发状态", "测试用例ID", "测试状态", "是否阻塞上线"]),
        "11-协同事件日志.md": "# 协同事件日志\n\n" + table(["时间", "Agent", "动作", "影响文件", "关联模块 / 需求", "结果", "下一步"]) + f"| {now} | Main Agent | 初始化项目文档 | docs/ |  | 创建 {mode} 模式文档 | 进入需求整理 |\n",
        "12-用户确认门禁.md": "# 用户确认门禁\n\n" + table(["确认点ID", "阶段", "确认事项", "影响范围", "必须确认", "当前状态", "用户结论", "记录时间"]),
        "13-异常处理记录.md": "# 异常处理记录\n",
        "14-回滚与撤销记录.md": "# 回滚与撤销记录\n",
        "15-UI交互验收标准.md": "# UI交互验收标准\n\n## 全局标准\n- [ ] 页面主操作清晰。\n- [ ] 加载、空数据、错误、成功都有反馈。\n- [ ] 表单有校验和错误提示。\n\n## 页面级验收\n" + table(["页面ID", "页面名称", "主操作", "空状态", "加载状态", "错误状态", "移动端", "验收状态"]),
        "16-最终交付包说明.md": "# 最终交付包说明\n\n## 项目基本信息\n项目名称：\n项目类型：\n技术栈：\n项目路径：\n当前版本：\n交付日期：\n\n## 项目简介\n\n## 已完成功能\n" + table(["功能ID", "功能名称", "所属模块", "状态", "说明"]) + "\n## 如何运行项目\n1. 安装依赖：\n2. 启动命令：\n3. 本地访问地址：\n4. 构建命令：\n\n## 已知问题\n" + table(["问题", "影响", "建议处理"]),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-path", required=True)
    parser.add_argument("--mode", choices=sorted(DOCS_BY_MODE), default="standard")
    parser.add_argument("--project-name", default="")
    parser.add_argument("--project-type", default="")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    project_path = Path(args.project_path).expanduser().resolve()
    if not project_path.exists():
        raise SystemExit(f"Project path does not exist: {project_path}")

    docs_dir = project_path / "docs"
    docs_dir.mkdir(exist_ok=True)
    content = templates(project_path, args.mode, args.project_name, args.project_type)
    created: list[str] = []
    skipped: list[str] = []

    for name in DOCS_BY_MODE[args.mode]:
        target = docs_dir / name
        if target.exists() and not args.force:
            skipped.append(name)
            continue
        target.write_text(content[name], encoding="utf-8")
        created.append(name)

    print("mode:", args.mode)
    print("docs_dir:", docs_dir)
    print("created:", ", ".join(created) if created else "(none)")
    print("skipped:", ", ".join(skipped) if skipped else "(none)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

