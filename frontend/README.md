# Agentic B2B Starter (Frontend)

Modern Apple HIG B2B SaaS Dashboard crafted for PMs and Agentic AI coding (React 19, Vite, Tailwind CSS v4, shadcn/ui).

> **Attribution**: The core layout foundation is adapted and re-engineered from [satnaing/shadcn-admin](https://github.com/satnaing/shadcn-admin), with extensive Apple HIG Inset Grouped card tuning, compact Toolbar flows, and Agentic design governance.

## Key Features

- **Apple HIG Visual System**: `bg-background` canvas, Inset Grouped card depth, and zero redundant secondary labels.
- **Agent-Ready Governance**: Fully aligned with root `AGENTS.md` and `frontend/AGENTS.md`.
- **Pure Text Table Operations**: Inline actions use clean text buttons instead of isolated icon blocks.
- **Safe Viewports & Modals**: Built-in horizontal table overflow guards and `max-h-[88vh]` dialog boundaries.
- **Standard Pagination**: Pre-wired with `@/components/data-pagination`.

<details>
<summary>Customized Components (click to expand)</summary>

This project uses Shadcn UI components, but some have been slightly modified for better RTL (Right-to-Left) support and other improvements. These customized components differ from the original Shadcn UI versions.

If you want to update components using the Shadcn CLI (e.g., `npx shadcn@latest add <component>`), it's generally safe for non-customized components. For the listed customized ones, you may need to manually merge changes to preserve the project's modifications and avoid overwriting RTL support or other updates.

> If you don't require RTL support, you can safely update the 'RTL Updated Components' via the Shadcn CLI, as these changes are primarily for RTL compatibility. The 'Modified Components' may have other customizations to consider.

### Modified Components

- scroll-area
- sonner
- separator

### RTL Updated Components

- alert-dialog
- calendar
- command
- dialog
- dropdown-menu
- select
- table
- sheet
- sidebar
- switch

**Notes:**

- **Modified Components**: These have general updates, potentially including RTL adjustments.
- **RTL Updated Components**: These have specific changes for RTL language support (e.g., layout, positioning).
- For implementation details, check the source files in `src/components/ui/`.
- All other Shadcn UI components in the project are standard and can be safely updated via the CLI.

</details>

## Tech Stack

**UI:** [ShadcnUI](https://ui.shadcn.com) (TailwindCSS + RadixUI)

**Build Tool:** [Vite](https://vitejs.dev/)

**Routing:** [TanStack Router](https://tanstack.com/router/latest)

**Type Checking:** [TypeScript](https://www.typescriptlang.org/)

**Linting/Formatting:** [ESLint](https://eslint.org/) & [Prettier](https://prettier.io/)

**Icons:** [Lucide Icons](https://lucide.dev/icons/), [Tabler Icons](https://tabler.io/icons) (Brand icons only)

**Auth (partial):** [Clerk](https://go.clerk.com/GttUAaK)

## Run Locally

Clone the project

```bash
  git clone https://github.com/satnaing/shadcn-admin.git
```

```bash
cd frontend
pnpm install
pnpm run dev
```

## Credits & Upstream License

- Original dashboard architecture by [@satnaing](https://github.com/satnaing) ([shadcn-admin](https://github.com/satnaing/shadcn-admin)).
- Licensed under the [MIT License](LICENSE).
