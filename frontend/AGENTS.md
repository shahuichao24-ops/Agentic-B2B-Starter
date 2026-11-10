# B2B SaaS Frontend Engineering & Design Standard (Agent Rules)

> **Core Philosophy**: 
> "Avoid unnecessary secondary labels and descriptions. Let the layout do the explaining."
> Strictly follow Apple Human Interface Guidelines (HIG): Deference (遵从内容), Clarity (清晰字阶), Depth (Inset Grouped 扁平卡片流与微投影).

---

## 1. 视觉 DNA 与绝对禁区 (Visual DNA & Hard Constraints)

1. **零自由发挥配色 (No Custom Colors)**:
   - 严禁在代码中手写任何十六进制颜色（如 `#3b82f6`）或非系统调色盘类名。
   - 所有前景色、背景色必须从设计 Token 继承：
     - 系统背景：`bg-background`（Apple System Gray 6 浅灰）
     - 内容卡片：`bg-card text-card-foreground`（纯白卡片）
     - 辅助说明文字：`text-muted-foreground`（次级灰）
     - 主操作按钮：`bg-primary text-primary-foreground`（克制深灰/黑）
     - 微弱边框：`border-border`（0.5px ~ 1px 微投影边框）
2. **卡片与间距层级 (Depth & Inset Grouped)**:
   - 所有独立内容块必须封装在 `<Card className="rounded-xl border shadow-sm">` 中。
   - 统一使用 8pt 步进网格：间距仅限 `p-4` (16px), `p-6` (24px), `gap-4`, `gap-6`。严禁随意写 `mt-[13px]` 之类的像素微调。
3. **文字与说明书式设计审查 (Clarity & Restraint)**:
   - 杜绝冗余的副标签和长篇使用说明小字。用结构排版、合理空白、清晰的标题自解释。
   - 内容区面包屑已自解释，严禁在页面顶部重复堆砌大黑标题与说明副标题。
   - 过滤与搜索严禁在表格上方堆砌独立高额大卡片，必须集成在列表 Card 顶部的紧凑 Toolbar（高度 `h-8` 控件流），搜索靠左，全局操作紧贴右上角。
   - **操作按钮纯文字化规范**：严禁在表格行内使用孤独的小方块图标按钮（Pencil、Trash2、Plus 等），一律使用语义清晰的中文**纯文字按钮**（如“添加岗位”、“编辑”、“删除”，危险操作使用红色文字）。全局操作按钮去图标化。
   - **弹窗去说明书化规范**：弹窗头部仅保留干练的 `<DialogTitle>`，彻底移除 `<DialogDescription>` 冗余副标题；所有下钻与详情交互统一使用居中 `<Dialog>`，挂载标准分页 `<DataPagination>`。
   - **表格表头与内容居中规范**：数据列表除表达树状层级缩进的首列外，其余所有数据列（状态、分类、数值、标签、防护措施、启用开关）及操作列，表头与单元格内容必须全量居中对齐（`text-center` 与 `justify-center`）。
   - **侧边栏二级菜单字阶规范**：二级菜单项字号与一级分类保持相同的 14px（`text-sm`），高度 `h-8`，挂载左侧微发丝树形导轨，确保充足的可读性与点击舒适度。

---

## 2. 组件引用白名单 (Component Whitelist)

所有 UI 元素必须直接从 `@/components/ui/` 导入，严禁造轮子或编写原生 html 无样式标签：
- 按钮：`import { Button } from '@/components/ui/button'`
- 卡片：`import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'`
- 表格：`import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'`
- 状态标签：`import { Badge } from '@/components/ui/badge'`
- 抽屉/弹窗：`import { Sheet, SheetContent } from '@/components/ui/sheet'` 或 `Dialog`
- 下拉/表单：`import { Select } from '@/components/ui/select'`, `import { Input } from '@/components/ui/input'`
- 图标库：唯一标准为 [Lucide Icons](https://lucide.dev/icons/)（`lucide-react` 线性细描边图标，严禁混入其他图标库或随意手写 SVG，速查清单与场景映射见 `docs/icon-library.md`）。

---

## 3. 标准 B 端 SaaS 页面骨架范式 (Standard Screen Anatomy)

每次生成新业务页面时，必须严格套用以下标准三段式结构（参考 `@/features/tasks`）：

```tsx
import { Header } from '@/components/layout/header'
import { Main } from '@/components/layout/main'
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
// ... 业务组件

export function BusinessFeature() {
  return (
    <>
      {/* 1. 顶部全局导航栏 */}
      <Header fixed>
        {/* 搜索与右上角头像/主题切换 */}
      </Header>

      {/* 2. 主内容区（自动居中、自适应边距） */}
      <Main className='flex flex-1 flex-col gap-4 sm:gap-6'>
        {/* 页面标题栏 + 主操作按钮 */}
        <div className='flex flex-wrap items-end justify-between gap-2'>
          <div>
            <h2 className='text-2xl font-bold tracking-tight'>模块名称</h2>
            <p className='text-muted-foreground text-sm'>
              一句话清晰定义本模块业务职责（严禁废话说明书）
            </p>
          </div>
          <div className='flex items-center gap-2'>
            <Button variant='outline'>导出</Button>
            <Button>新建记录</Button>
          </div>
        </div>

        {/* 主数据卡片：筛选栏 + 数据表格/看板 */}
        <Card className='rounded-xl border shadow-sm'>
          {/* 表格内容与分页 */}
        </Card>
      </Main>

      {/* 3. 详情滑出抽屉或编辑弹窗（不打断主视图浏览） */}
    </>
  )
}
```

---

## 4. 状态与业务表达 (Status & Micro-feedback)

- **状态胶囊 (Badges)**：
  - 待审核 / 草稿：`<Badge variant="outline" className="bg-zinc-100 text-zinc-700">待审核</Badge>`
  - 正常 / 合规 / 已通过：`<Badge variant="outline" className="bg-emerald-50 text-emerald-700 border-emerald-200">已通过</Badge>`
  - 警告 / 补正：`<Badge variant="outline" className="bg-amber-50 text-amber-700 border-amber-200">需补正</Badge>`
  - 驳回 / 异常：`<Badge variant="outline" className="bg-rose-50 text-rose-700 border-rose-200">已驳回</Badge>`
- **操作反馈**：统一调用 `sonner` 的 `toast.success()` / `toast.error()`。

---

## 5. 路由与样式特别防呆 (Router & Tailwind v4 Guardrails)

### ① Tailwind v4 特别警示（严禁旧版语法）
- 本工程使用最新的 Tailwind CSS v4（基于 `@theme inline`），**项目中不存在 `tailwind.config.js`**！
- 严禁尝试新建或修改 `tailwind.config.js`，所有样式微调直接调用语义 Token 类名或写在 `src/styles/theme.css`。

### ② TanStack Router 路由新建标准范式（严禁使用 react-router 旧语法）
- 严禁调用 `useHistory`、`useParams` 裸函数，必须套用以下官方模板：
- **普通页面**（例：`src/routes/_authenticated/suppliers/index.tsx`）：
  ```tsx
  import { createFileRoute } from '@tanstack/react-router'
  import { Suppliers } from '@/features/suppliers'

  export const Route = createFileRoute('/_authenticated/suppliers/')({
    component: Suppliers,
  })
  ```
- **带动态参数页面**（例：`src/routes/_authenticated/suppliers/$supplierId.tsx`）：
  ```tsx
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/_authenticated/suppliers/$supplierId')({
    component: SupplierDetail,
  })

  function SupplierDetail() {
    const { supplierId } = Route.useParams()
    return <div>Detail ID: {supplierId}</div>
  }
  ```
- **页面间跳转**：
  ```tsx
  import { useNavigate } from '@tanstack/react-router'
  const navigate = useNavigate()
  navigate({ to: '/suppliers' }) // 必须传对象 { to: '...' }
  ```
