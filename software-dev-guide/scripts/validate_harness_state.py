#!/usr/bin/env python3
"""Validate software-dev-guide harness state."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_BY_MODE = {
    "light": [
        "00-项目状态总览.md",
        "04-开发任务看板.md",
        "05-开发日志.md",
        "07-测试报告.md",
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
        "10-需求模块测试追踪矩阵.md",
        "12-用户确认门禁.md",
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


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def parse_table_rows(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "---" in stripped:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells:
            rows.append(cells)
    return rows


def has_pending_gate(text: str) -> bool:
    return "待确认" in text and "必须确认" in text


def has_unresolved_exception(text: str) -> bool:
    return any(marker in text for marker in ["状态：待处理", "状态：处理中"])


def has_unverified_rollback(text: str) -> bool:
    return any(marker in text for marker in ["待执行", "已执行"]) and "已验证" not in text


def validate(project_path: Path, mode: str) -> dict:
    docs = project_path / "docs"
    issues: list[dict] = []
    warnings: list[dict] = []

    if not docs.exists():
        issues.append({"code": "NO_DOCS_DIR", "message": f"Missing docs directory: {docs}"})
        return {"status": "fail", "issues": issues, "warnings": warnings}

    for name in REQUIRED_BY_MODE[mode]:
        if not (docs / name).exists():
            issues.append({"code": "MISSING_DOC", "message": f"Missing required doc for {mode}: {name}"})

    gates = read(docs / "12-用户确认门禁.md")
    if gates and has_pending_gate(gates):
        issues.append({"code": "PENDING_GATE", "message": "User confirmation gate is pending."})

    exceptions = read(docs / "13-异常处理记录.md")
    if exceptions and has_unresolved_exception(exceptions):
        issues.append({"code": "UNRESOLVED_EXCEPTION", "message": "Unresolved exception exists."})

    rollbacks = read(docs / "14-回滚与撤销记录.md")
    if rollbacks and has_unverified_rollback(rollbacks):
        warnings.append({"code": "ROLLBACK_NOT_VERIFIED", "message": "Rollback record may need verification."})

    board = read(docs / "04-开发任务看板.md")
    if "已锁定" in board:
        warnings.append({"code": "MODULE_LOCKED", "message": "At least one module appears locked."})
    if "待修复" in board:
        issues.append({"code": "PENDING_FIX", "message": "Task board contains pending fixes."})

    matrix = read(docs / "10-需求模块测试追踪矩阵.md")
    for row in parse_table_rows(matrix):
        if row and row[0] == "需求ID":
            continue
        if len(row) >= 11 and row[3] == "P0":
            req_id, module_id, test_id, test_status = row[0], row[5], row[8], row[9]
            if not module_id or module_id in {"待拆分", "待生成"}:
                issues.append({"code": "TRACE_NO_MODULE", "message": f"P0 requirement {req_id} has no module."})
            if not test_id or test_id in {"待生成", "待测"}:
                warnings.append({"code": "TRACE_NO_TEST", "message": f"P0 requirement {req_id} has no test case."})
            if test_status and test_status not in {"通过", "待测"}:
                issues.append({"code": "TRACE_TEST_NOT_PASSING", "message": f"P0 requirement {req_id} test status: {test_status}"})

    status = "pass"
    if issues:
        status = "fail"
    elif warnings:
        status = "warning"
    return {"status": status, "issues": issues, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-path", required=True)
    parser.add_argument("--mode", choices=sorted(REQUIRED_BY_MODE), default="standard")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()

    result = validate(Path(args.project_path).expanduser().resolve(), args.mode)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("status:", result["status"])
        for issue in result["issues"]:
            print("issue:", issue["code"], "-", issue["message"])
        for warning in result["warnings"]:
            print("warning:", warning["code"], "-", warning["message"])
    return 0 if result["status"] in {"pass", "warning"} else 1


if __name__ == "__main__":
    raise SystemExit(main())

