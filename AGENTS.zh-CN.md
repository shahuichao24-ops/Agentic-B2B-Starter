# B2B SaaS 全栈母版协作军规 (Full-Stack Agent Rules - 中文版)

> **核心哲学**：
> 1. 前端遵从 Apple HIG：Deference（遵从内容）、Clarity（清晰字阶）、Depth（Inset Grouped 扁平卡片与微投影）。少写说明书，多花心思在 UI 结构与自解释布局上。
> 2. 后端强契约严约束：FastAPI + SQLModel，严格执行三层架构、统一响应外壳、标准分页、软删除与多租户基类。
> 3. 以工程确定性压制模型玄学：严禁手写 Hex 色值，严禁造原生 UI 轮子，严禁后端返回裸字典。

---

## 一、前端标准 (`frontend/`)

- **技术栈**：React 19 + Vite + Tailwind CSS v4 + `shadcn/ui` + TanStack Router / Table + Lucide Icons。
- **视觉约束**：
  - 系统底色统一为 `bg-background`（Apple System Gray 6），内容统一封装在 `<Card className="rounded-xl border shadow-sm">` 中。
  - 所有 UI 元素必须直接从 `@/components/ui/` 导入（Button, Card, Table, Badge, Sheet, Dialog, Select, Input）。
  - 状态胶囊使用四色微淡底色：`pending`（锌灰）、`approved`（柔绿）、`revision`（柔橙）、`rejected`（柔红）。
  - **布局与身份收拢规范**：用户个人信息与退出登录统一收拢在顶部 Header 右上角 `<ProfileDropdown />` 且全部为中文；左上角租户管理仅显示名称严禁放副标题；侧边栏底部保持纯净无多余用户条；开发调试浮窗默认关闭。
  - **字体与树形表格规范**：侧边栏一级分类为 14px 加粗（`text-sm font-semibold`）且必须带有大类图标，默认按需收起（仅当前激活组展开）；二级功能项同样放大为 14px（`text-sm`，与一级字阶一致确保充足可读性），挂载左侧微发丝树形导轨，未激活通透干净，激活时采用 `bg-primary/10 text-primary font-semibold` 柔和底色胶囊，严禁带图标与生硬大灰块；树状层级表格不放“展开全部/收起全部”冗余按钮，默认自解释展开。
  - **页面极简布局与 Toolbar 规范**：严禁在内容区堆砌重复的大标题与说明书式副标题（面包屑已自解释）；严禁在表格上方堆砌独立高额的大筛选 Card；所有过滤搜索项与全局操作按钮必须集成在列表 Card 顶部的紧凑 Toolbar（高度 `h-8` 控件流），搜索靠左，全局操作按钮（新增/批量）紧贴列表右上角。
  - **列表分页与弹窗交互硬规范**：所有数据列表（主表及下钻列表）必须挂载标准分页 `<DataPagination />`；所有详情下钻、在册名单穿透与表单交互统一使用居中弹窗 `<Dialog>`，严禁使用右侧滑出抽屉 `<Sheet>` 打断视线。
  - **纯文字操作与弹窗去说明书化规范**：严禁在表格行内使用孤独的方块小图标按钮（如只有 Pencil、Trash2 图标的小方块），所有行内与全局操作统一使用自解释的**纯文字按钮**（如“添加岗位”、“编辑”、“删除”，危险操作使用红色文字）；严禁在弹窗内堆砌说明书式副标题（彻底移除 `<DialogDescription>`），弹窗标题自解释，表单布局自解释。
  - **列表表头与内容居中规范**：数据列表除多层级树形列与长文本描述列（为展现缩进动线与左侧阅读基线需左对齐）外，其余所有数据属性列（状态、分类、数值、标签、启用开关等）及操作列，表头（`<TableHead>`）与单元格内容（`<TableCell>`）必须全量**居中对齐**（`text-center` 与 `justify-center`），规避操作列孤悬右侧与内容偏左失衡。
  - **表格视口防护与弹窗高度兜底规范**：主表 Card 内必须使用 `<div className="overflow-x-auto">` 包裹带有 min-width 的 Table，确保 1280px 分屏或窄视口下操作列永不被截断切除；`DialogContent` 必须带 `max-h-[88vh] overflow-y-auto` 滚动保护，杜绝复杂表单底部按钮掉出屏幕。
  - **统一高危确认拦截规范**：严禁调用浏览器原生阻塞式 `window.confirm()`，全系统删除及敏感阻断操作统一使用居中微投影的 `<ConfirmDialog />` 组件进行安全确认。
  - **图标库唯一标准与检索机制**：全系统图标唯一来源为 **Lucide Icons**（`lucide-react`，官方检索入口：https://lucide.dev/icons/ ）。严禁混入第三方图标包或原生 SVG；后续新增业务模块优先从 `docs/icon-library.md` 业务速查表及 Lucide 官网搜索挑选，规格统一为 `h-4 w-4` 线性微质感。
  - **防幻觉硬规则**：Tailwind v4 无 config 文件；TanStack Router 必须使用 `createFileRoute`，严禁旧版 react-router-dom 语法。
- **详见前端专属规则**：`frontend/AGENTS.md`。

---

## 二、后端标准 (`backend/`)

- **技术栈**：Python 3.12 + FastAPI + SQLModel + Pydantic v2 + SQLite（本地）/ PostgreSQL（生产）。
- **架构约束**：
  - 严格三层分工：`models/`（表模型与 DTO）、`services/`（业务逻辑与事务）、`api/v1/`（路由与响应包装）。
  - 所有返回必须包裹 `success_response(data=...)` 或 `error_response(message=..., code=...)`。
  - 列表接口入参必须为 `page`、`page_size`，出参包裹 `PaginatedData`。
  - 所有业务模型必须继承 `app.models.base.BaseModel`（天然自带 id, created_at, updated_at, is_deleted, tenant_id）。
  - **物理防呆隔离机制**：数据库底层已挂载自动租户拦截器，SELECT 查询自动注入 `tenant_id` 与未软删除条件，业务代码即便漏写也绝不越权。
  - **角色权限切面 (RBAC)**：支持 `UserRole (admin | reviewer | operator)`，敏感接口通过 `dependencies=[Depends(require_roles([...]))]` 守门。
  - 严禁硬删除，一律 `is_deleted = True` 软删除。状态机必须使用 `str, Enum`。
  - **一键重置指令**：执行 `python run.py --reset-db` 秒级全量重建最新表结构与干净种子。
- **详见后端专属规则**：`backend/AGENTS.md`。

---

## 三、产品经理极简提需求口径 (PM Direct Prompts)

当产品经理/用户在对话中提出需求时，按以下规范直接落地，无需反问重复废话：
1. **加全栈功能**：“新增【客户跟进】模块，包含跟进记录列表、跟进状态、下次拜访提醒，支持新增和详情查看。”
   - AI 先在 `backend/` 创建 Model、Service 和 API；
   - 并在 `frontend/` 创建对应的 Inset Card 表格与详情弹窗。
2. **纯前端页面**：“在前端新增【资质准入大盘】页面，读取后端接口并展示指标卡片。”
3. **纯后端逻辑**：“在后端增加批量导入客户 Excel 并进行规则校验的接口。”
