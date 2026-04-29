#!/usr/bin/env python3
"""Find the next safe software-dev-guide harness action."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def parse_rows(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "---" in stripped:
            continue
        rows.append([cell.strip() for cell in stripped.strip("|").split("|")])
    return rows


def first_task_from_board(board: str) -> dict | None:
    rows = parse_rows(board)
    for row in rows:
        if row and row[0] == "模块":
            continue
        if len(row) < 7:
            continue
        module, name, status = row[0], row[1], row[6]
        if status in {"待开发", "开发中", "待完整度检查"}:
            return {"action": "dispatch_b", "module": module, "reason": f"{module} {name} is {status}"}
        if status == "待测试":
            return {"action": "dispatch_c", "module": module, "reason": f"{module} {name} is ready for testing"}
        if status == "待修复":
            return {"action": "dispatch_b", "module": module, "reason": f"{module} {name} needs repair"}
    return None


def find_next(project_path: Path) -> dict:
    docs = project_path / "docs"
    if not docs.exists():
        return {
            "next_action": "init_docs",
            "target_module": "",
            "target_doc": "docs/",
            "reason": "Project has no docs directory.",
            "blocking_items": [],
        }

    blockers: list[str] = []
    exceptions = read(docs / "13-异常处理记录.md")
    if "状态：待处理" in exceptions or "状态：处理中" in exceptions:
        return {
            "next_action": "handle_exception",
            "target_module": "",
            "target_doc": "docs/13-异常处理记录.md",
            "reason": "Unresolved exception exists.",
            "blocking_items": ["unresolved_exception"],
        }

    rollbacks = read(docs / "14-回滚与撤销记录.md")
    if "待执行" in rollbacks or ("已执行" in rollbacks and "已验证" not in rollbacks):
        return {
            "next_action": "handle_rollback",
            "target_module": "",
            "target_doc": "docs/14-回滚与撤销记录.md",
            "reason": "Rollback needs execution or verification.",
            "blocking_items": ["rollback_not_verified"],
        }

    gates = read(docs / "12-用户确认门禁.md")
    if "待确认" in gates:
        return {
            "next_action": "ask_user",
            "target_module": "",
            "target_doc": "docs/12-用户确认门禁.md",
            "reason": "User confirmation gate is pending.",
            "blocking_items": ["pending_gate"],
        }

    board_task = first_task_from_board(read(docs / "04-开发任务看板.md"))
    if board_task:
        return {
            "next_action": board_task["action"],
            "target_module": board_task["module"],
            "target_doc": "docs/04-开发任务看板.md",
            "reason": board_task["reason"],
            "blocking_items": blockers,
        }

    matrix = read(docs / "10-需求模块测试追踪矩阵.md")
    if "P0" in matrix and "待开发" in matrix:
        return {
            "next_action": "dispatch_b",
            "target_module": "",
            "target_doc": "docs/10-需求模块测试追踪矩阵.md",
            "reason": "Traceability matrix contains P0 work not developed.",
            "blocking_items": blockers,
        }
    if "P0" in matrix and "待测" in matrix:
        return {
            "next_action": "dispatch_c",
            "target_module": "",
            "target_doc": "docs/10-需求模块测试追踪矩阵.md",
            "reason": "Traceability matrix contains P0 work not tested.",
            "blocking_items": blockers,
        }

    delivery = docs / "16-最终交付包说明.md"
    if not delivery.exists() or "## 已完成功能" not in read(delivery):
        return {
            "next_action": "prepare_delivery",
            "target_module": "",
            "target_doc": "docs/16-最终交付包说明.md",
            "reason": "Final delivery package is missing or incomplete.",
            "blocking_items": blockers,
        }

    return {
        "next_action": "ask_user",
        "target_module": "",
        "target_doc": "",
        "reason": "No obvious pending task found. Ask user for next goal.",
        "blocking_items": blockers,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-path", required=True)
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()

    result = find_next(Path(args.project_path).expanduser().resolve())
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("next_action:", result["next_action"])
        print("target_module:", result["target_module"] or "(none)")
        print("target_doc:", result["target_doc"] or "(none)")
        print("reason:", result["reason"])
        if result["blocking_items"]:
            print("blocking_items:", ", ".join(result["blocking_items"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

