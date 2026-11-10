# B2B SaaS 官方图标库规范与速查手册 (Lucide Icons)

> **核心原则**：
> 全系统所有图标**唯一合法来源**为 **[Lucide Icons](https://lucide.dev/icons)**。
> 严禁随意引入第三方图标包（如 FontAwesome、Ant Design Icons、Material Icons）或散乱手写 SVG。所有页面设计、导航菜单、状态徽标与行内说明，均优先从 Lucide 官方库挑选。

---

## 一、图标库核心档案

- **官方网站与检索器**：[https://lucide.dev/icons/](https://lucide.dev/icons/)
  - 支持中文/英文关键词模糊搜索（如输入 `user`, `chart`, `shield`, `building`, `tool` 等）；
  - 点击任意图标可直接复制 React 组件导入代码或 SVG。
- **NPM 依赖包**：`lucide-react`
- **设计规格 (DNA)**：
  - **网格基底**：标准 24×24 视口；
  - **默认描边**：2px（在 Tailwind 中通过 `size-4` (16px) 或 `size-3.5` (14px) 继承微缩缩放）；
  - **端点与转角**：`stroke-linecap="round"` 与 `stroke-linejoin="round"`，具备纯粹现代、克制内敛的 Apple HIG 线性质感。

---

## 二、B2B SaaS 核心业务场景图标速查推荐

为确保整个系统风格高度统一、语义精准，整理各业务场景推荐使用的 Lucide 图标如下：

### 1. 导航与大盘总览 (Navigation & Dashboard)
| 业务场景 | 推荐图标名称 | 导入示例 | 说明 |
| :--- | :--- | :--- | :--- |
| **工作台 / 数据大盘** | `LayoutDashboard` | `import { LayoutDashboard } from 'lucide-react'` | 概览、大屏、看板 |
| **基础数据 / 字典** | `Database` | `import { Database } from 'lucide-react'` | 核心基础数据底座 |
| **现场与工程现场** | `HardHat` | `import { HardHat } from 'lucide-react'` | 安全帽、矿井/工地/车间 |
| **健康体检 / 职业卫生** | `HeartPulse` | `import { HeartPulse } from 'lucide-react'` | 脉搏健康、医疗体检 |
| **报表 / 交付文书** | `FileSpreadsheet` | `import { FileSpreadsheet } from 'lucide-react'` | 统计台账、Excel 表格、文书 |
| **系统管理 / 设置** | `Settings` / `Sliders` | `import { Settings } from 'lucide-react'` | 后台配置、系统参数 |

### 2. 组织架构与人员 (Organization & Personnel)
| 业务场景 | 推荐图标名称 | 导入示例 | 说明 |
| :--- | :--- | :--- | :--- |
| **组织架构 / 部门层级** | `FolderTree` | `import { FolderTree } from 'lucide-react'` | 树形组织、多级部门 |
| **单位 / 区队 / 厂房** | `Building` / `Building2` | `import { Building } from 'lucide-react'` | 实体单位、区队部门 |
| **岗位 / 工种** | `Briefcase` | `import { Briefcase } from 'lucide-react'` | 职业职位、作业岗位 |
| **人员档案 / 名册** | `Users` / `UserCheck` | `import { Users } from 'lucide-react'` | 员工名单、在册人员 |
| **个人账号 / 身份** | `User` | `import { User } from 'lucide-react'` | 当前登录人、个人资料 |

### 3. 生产作业与空间单元 (Workfaces & Engineering)
| 业务场景 | 推荐图标名称 | 导入示例 | 说明 |
| :--- | :--- | :--- | :--- |
| **生产区域 / 作业面** | `Layers` / `Compass` | `import { Layers } from 'lucide-react'` | 分层区域、工作面作业单元 |
| **危害因素 / 风险源** | `ShieldAlert` / `AlertTriangle` | `import { ShieldAlert } from 'lucide-react'` | 职业病危害、风险预警 |
| **设备与巡检** | `Wrench` / `Cpu` | `import { Wrench } from 'lucide-react'` | 机电设备、传感器台账 |
| **现场检测** | `Activity` / `Gauge` | `import { Activity } from 'lucide-react'` | 浓度检测、风速仪表 |

### 4. 状态与交互指示 (Status & Actions)
| 业务场景 | 推荐图标名称 | 导入示例 | 说明 |
| :--- | :--- | :--- | :--- |
| **搜索** | `Search` | `import { Search } from 'lucide-react'` | 工具栏搜索框 |
| **折叠展开** | `ChevronRight` / `ChevronDown` | `import { ChevronRight } from 'lucide-react'` | 树状或折叠导轨 |
| **成功 / 正常 / 通过** | `Check` / `CheckCircle2` | `import { Check } from 'lucide-react'` | 审核通过、启用 |
| **警示 / 审核中** | `AlertCircle` / `Clock` | `import { AlertCircle } from 'lucide-react'` | 待办、预警 |
| **危险 / 拦截** | `XCircle` / `Ban` | `import { XCircle } from 'lucide-react'` | 停用、超标拦截 |

---

## 三、开发调用军规

1. **导入规范**：直接从 `'lucide-react'` 命名导入，如：
   ```tsx
   import { Database, FolderTree, ShieldAlert } from 'lucide-react'
   ```
2. **尺寸规范 (Size Hierarchy)**：
   - 侧边栏一级大类图标：统一使用 `h-4 w-4`（16px）；
   - 页面面包屑 / 标题前导图标：`h-4 w-4`（16px）；
   - 弹窗大标题前导图标：`h-4 w-4`（16px）；
   - 表格内部辅助指示图标（如部门/折叠）：`h-3.5 w-3.5`（14px）；
   - 严禁放大到 `h-6` 以上导致破坏 HIG 紧凑细腻感。
3. **按钮去图标化原则**：
   - 遵循母版准则，表格行内操作与顶栏全局操作统一使用**纯文字按钮**，禁止使用孤立的图标方块按钮。图标仅用于导航指引、结构层级辨识与关键状态表达。
