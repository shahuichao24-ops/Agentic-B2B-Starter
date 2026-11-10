# Agentic B2B Starter (中文文档)

> **专为产品经理与 AI Agent 协同打造的现代化 Apple HIG B 端全栈交付母版**  
> *Transform business specs into production-grade, interactive prototypes in minutes using deterministic engineering guardrails.*

[English](README.md) | [简体中文](README.zh-CN.md)

[![React 19](https://img.shields.io/badge/React-19.x-blue?logo=react)](https://react.dev/)
[![Tailwind CSS v4](https://img.shields.io/badge/Tailwind-v4.x-38bdf8?logo=tailwindcss)](https://tailwindcss.com/)
[![shadcn/ui](https://img.shields.io/badge/shadcn%2Fui-Radix-black)](https://ui.shadcn.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLModel](https://img.shields.io/badge/SQLModel-Pydantic%20v2-orange)](https://sqlmodel.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 💡 为什么需要这个母版？

在 **AI Coding（Cursor / Claude Code / Antigravity）** 时代，产品经理常常面临两大困境：
1. **视觉失控与“说明书式”界面**：AI 喜欢随意手写 Hex 颜色、堆砌生硬大灰块、到处写问号说明小字和重复标题，UI 廉价且凌乱。
2. **后端无契约与隐性风险**：AI 习惯返回裸字典、硬删除数据、漏写分页与租户过滤，一上生产就漏洞百出。

**Agentic B2B Starter** 的核心哲学是：  
> **以工程确定性，压制模型玄学；少写说明书，用布局与结构自解释。**  
> *"Avoid unnecessary secondary labels and descriptions. Let the layout do the explaining."*

通过内置的 **`AGENTS.md`（全栈防幻觉军规）** 与严谨骨架，让 AI 在受控约束内，10 秒衍生项目、数分钟交付生产级企业原型。

---

## 🏛️ 系统架构

```text
Agentic-B2B-Starter/
├── AGENTS.md                # 🤖 AI 编程全栈统御军规（英文版，同步映射为 .cursorrules）
├── AGENTS.zh-CN.md          # 🤖 AI 编程全栈统御军规（中文版）
├── create-saas-project.sh   # 🚀 一键衍生全新独立项目脚本
├── docs/                    # 📚 设计规范与 Lucide 业务图标字典
│   └── icon-library.md
├── frontend/                # 🎨 Apple HIG 风格前端 (React 19 + Tailwind v4 + shadcn)
└── backend/                 # ⚙️ 契约化、自文档化 B 端后端 (FastAPI + SQLModel)
```

---

## 💎 核心工程特性

### 1. 前端：极致遵循 Apple HIG (Human Interface Guidelines)
- **视觉层级**：系统浅灰底（`bg-background`）、纯白 Inset Grouped 扁平卡片（`rounded-xl border shadow-sm`）。
- **零手写配色**：严禁 AI 在代码中手写任何十六进制色值，所有样式必须从语义化 Token 继承。
- **去说明书化**：彻底移除冗余副标题（`<DialogDescription>`），杜绝在页面到处贴小字；面包屑已自解释，不堆砌重复大黑标题。
- **纯文字操作行**：表格行内严禁使用孤独的小方块图标，一律采用自解释中文文字按钮（“编辑”、“删除”）。
- **视口防截断**：数据表格自带水平滚动保护（`min-w`），居中弹窗附带 `max-h-[88vh]` 滚动兜底，小屏与分屏永不崩盘。
- **居中平衡对齐**：除层级缩进列外，数值、状态胶囊、开关及操作列全量居中对齐。

### 2. 后端：强契约与企业级防御
- **三层严格分工**：`models/` (模型与 DTO)、`services/` (业务事务)、`api/v1/` (路由与契约外壳)。
- **统一响应契约**：所有接口统一包裹 `success_response(data=...)` 或 `error_response(...)`。
- **标准分页机制**：出参标准化包裹 `PaginatedData`，入参强制校验 `page` 与 `page_size`。
- **多租户与软删除物理防呆**：底座模型自带审计字段；数据库查询拦截器自动过滤 `is_deleted` 与当前 `tenant_id`，防止跨租户越权。
- **异常优雅处理**：统一拦截 `IntegrityError`（数据库唯一性冲突）与 `RequestValidationError`，输出清晰业务报错，不向前端吐裸露堆栈。

---

## 🚀 极速上手

### 选项 A：从母版一键衍生新项目（推荐，10秒）

```bash
# 赋予执行权限并克隆骨架到新目录
./create-saas-project.sh ~/projects/my-new-saas
```

### 选项 B：直接本地运行母版

#### 1. 启动后端 API (Port 8000)

```bash
cd backend

# 创建并激活虚拟环境（推荐使用 uv）
uv venv
source .venv/bin/activate

# 安装依赖并启动开发服务
uv pip install -e .
python run.py
```
- 📖 Swagger 交互式文档：[http://localhost:8000/docs](http://localhost:8000/docs)
- 💡 一键重置测试表与种子数据：`python run.py --reset-db`

#### 2. 启动前端 Dashboard (Port 5173)

```bash
cd frontend

# 安装依赖
pnpm install

# 启动开发服务器
pnpm dev
```
- 🖥️ 页面预览：[http://localhost:5173](http://localhost:5173)

---

## 🎯 产品经理极简提需求口径 (PM Direct Prompts)

当配合 Cursor / Claude Code / Antigravity 开发时，将 `AGENTS.md` 注入上下文，直接以 PM 业务语言下达指令：

- **全栈新增模块**：
  > “新增【服务商资质合规】模块，包含列表查询、准入审核状态机、资质补正说明，支持详情弹窗查看与软删除。”
  - *AI 将依据军规自动完成 Model、Service、API 路由构建，并生成遵循 Apple HIG 的 Inset Card 表格与 Dialog 弹窗。*
- **纯前端交互**：
  > “在前端新增【合规监控大盘】页面，读取后端接口并展示四色柔和指标卡。”
- **纯后端逻辑**：
  > “在后端增加批量导入服务商 Excel 并进行统一信用代码正则校验的接口。”

---

## 📜 开源协议与致谢

- 本项目基于 [MIT License](LICENSE) 开源。
- **致谢与上游声明**：
  - 前端交互组件基底参考并重构自 [satnaing/shadcn-admin](https://github.com/satnaing/shadcn-admin)（MIT License），在此基础上深度融入了 Apple HIG Inset Grouped 视觉体系、Toolbar 控件流与 Agentic 规范约束；
  - 后端架构由 FastAPI 与 SQLModel 强驱动。

---

## ⚠️ 免责与维护说明

本项目为作者个人在 **AI 协同编程（Agentic Coding）** 与 **B 端产品敏捷交付** 上的工程化沉淀，核心用于设计规范参考、个人架构验证与原型自用衍生。

**本项目不设专职客服与高频 Issue 运维通道**。代码开箱即用，欢迎开发者与产品经理自由 Fork、Star 或基于本框架衍生自己的商业与原型项目！
