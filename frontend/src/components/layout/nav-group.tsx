import { type ReactNode } from 'react'
import { Link, useLocation } from '@tanstack/react-router'
import { ChevronRight } from 'lucide-react'
import { cn } from '@/lib/utils'
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from '@/components/ui/collapsible'
import {
  SidebarGroup,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
  useSidebar,
} from '@/components/ui/sidebar'
import { Badge } from '../ui/badge'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '../ui/dropdown-menu'
import {
  type NavCollapsible,
  type NavItem,
  type NavLink,
  type NavGroup as NavGroupProps,
} from './types'

export function NavGroup({ title, icon: Icon, items }: NavGroupProps) {
  const { state, isMobile } = useSidebar()
  const href = useLocation({ select: (location) => location.href })

  const isGroupActive = items.some((item) => {
    if (checkIsActive(href, item)) return true
    if (item.items) return item.items.some((sub) => checkIsActive(href, sub))
    return false
  })

  if (state === 'collapsed' && !isMobile) {
    return (
      <SidebarGroup className='py-1'>
        <SidebarMenu>
          <SidebarMenuItem>
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <SidebarMenuButton
                  tooltip={title}
                  isActive={isGroupActive}
                  className='justify-center'
                >
                  {Icon ? (
                    <Icon className='size-4' />
                  ) : (
                    <span>{title.slice(0, 2)}</span>
                  )}
                </SidebarMenuButton>
              </DropdownMenuTrigger>
              <DropdownMenuContent side='right' align='start' className='w-48'>
                <DropdownMenuLabel className='text-xs font-semibold text-muted-foreground'>
                  {title}
                </DropdownMenuLabel>
                <DropdownMenuSeparator />
                {items.map((item) => {
                  if (!item.items) {
                    return (
                      <DropdownMenuItem key={item.title} asChild>
                        <Link
                          to={item.url}
                          className={
                            checkIsActive(href, item)
                              ? 'bg-accent font-medium'
                              : ''
                          }
                        >
                          <span>{item.title}</span>
                        </Link>
                      </DropdownMenuItem>
                    )
                  }
                  return item.items.map((sub) => (
                    <DropdownMenuItem key={sub.title} asChild>
                      <Link
                        to={sub.url}
                        className={
                          checkIsActive(href, sub)
                            ? 'bg-accent font-medium'
                            : ''
                        }
                      >
                        <span>{sub.title}</span>
                      </Link>
                    </DropdownMenuItem>
                  ))
                })}
              </DropdownMenuContent>
            </DropdownMenu>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarGroup>
    )
  }

  return (
    <Collapsible defaultOpen={isGroupActive} className='group/nav-group'>
      <SidebarGroup className='py-1.5'>
        <SidebarGroupLabel asChild className='h-8.5 px-2'>
          <CollapsibleTrigger className='flex w-full cursor-pointer items-center justify-between text-sm font-semibold tracking-tight text-sidebar-foreground transition-colors select-none hover:text-foreground'>
            <div className='flex min-w-0 items-center gap-2'>
              {Icon && <Icon className='h-4 w-4 shrink-0 text-primary' />}
              <span className='truncate'>{title}</span>
            </div>
            <ChevronRight className='h-4 w-4 shrink-0 text-muted-foreground/70 transition-transform duration-200 group-data-[state=open]/nav-group:rotate-90' />
          </CollapsibleTrigger>
        </SidebarGroupLabel>
        <CollapsibleContent className='CollapsibleContent pt-1 pb-0.5'>
          <SidebarMenu className='ml-3.5 gap-0.5 border-l border-sidebar-border/60 pl-2.5'>
            {items.map((item) => {
              const key = `${item.title}-${item.url}`

              if (!item.items)
                return <SidebarMenuLink key={key} item={item} href={href} />

              return (
                <SidebarMenuCollapsible key={key} item={item} href={href} />
              )
            })}
          </SidebarMenu>
        </CollapsibleContent>
      </SidebarGroup>
    </Collapsible>
  )
}

function NavBadge({ children }: { children: ReactNode }) {
  return (
    <Badge className='rounded-full px-1.5 py-0 text-[11px] font-normal'>
      {children}
    </Badge>
  )
}

function SidebarMenuLink({ item, href }: { item: NavLink; href: string }) {
  const { setOpenMobile } = useSidebar()
  const active = checkIsActive(href, item)
  return (
    <SidebarMenuItem>
      <SidebarMenuButton
        asChild
        isActive={active}
        tooltip={item.title}
        className={cn(
          'h-8 rounded-md px-2.5 text-sm transition-all duration-150',
          active
            ? 'bg-primary/10 font-semibold text-primary shadow-xs hover:bg-primary/15 hover:text-primary'
            : 'font-normal text-muted-foreground hover:bg-muted/40 hover:text-foreground'
        )}
      >
        <Link to={item.url} onClick={() => setOpenMobile(false)}>
          <span className='truncate'>{item.title}</span>
          {item.badge && <NavBadge>{item.badge}</NavBadge>}
        </Link>
      </SidebarMenuButton>
    </SidebarMenuItem>
  )
}

function SidebarMenuCollapsible({
  item,
  href,
}: {
  item: NavCollapsible
  href: string
}) {
  const { setOpenMobile } = useSidebar()
  return (
    <Collapsible
      asChild
      defaultOpen={checkIsActive(href, item, true)}
      className='group/collapsible'
    >
      <SidebarMenuItem>
        <CollapsibleTrigger asChild>
          <SidebarMenuButton
            tooltip={item.title}
            className='h-8 pl-7 text-sm font-normal text-muted-foreground hover:text-foreground data-[active=true]:font-medium'
          >
            <span className='truncate'>{item.title}</span>
            {item.badge && <NavBadge>{item.badge}</NavBadge>}
            <ChevronRight className='ms-auto size-3.5 transition-transform duration-200 group-data-[state=open]/collapsible:rotate-90 rtl:rotate-180' />
          </SidebarMenuButton>
        </CollapsibleTrigger>
        <CollapsibleContent className='CollapsibleContent'>
          <SidebarMenuSub className='mx-2 my-0.5 border-l border-sidebar-border/60 pl-2'>
            {item.items.map((subItem) => (
              <SidebarMenuSubItem key={subItem.title}>
                <SidebarMenuSubButton
                  asChild
                  isActive={checkIsActive(href, subItem)}
                  className='h-7 pl-4 text-xs font-normal'
                >
                  <Link to={subItem.url} onClick={() => setOpenMobile(false)}>
                    <span className='truncate'>{subItem.title}</span>
                    {subItem.badge && <NavBadge>{subItem.badge}</NavBadge>}
                  </Link>
                </SidebarMenuSubButton>
              </SidebarMenuSubItem>
            ))}
          </SidebarMenuSub>
        </CollapsibleContent>
      </SidebarMenuItem>
    </Collapsible>
  )
}

function checkIsActive(href: string, item: NavItem, mainNav = false) {
  return (
    href === item.url || // /end-point
    href.split('?')[0] === item.url || // endpoint?search=param
    !!item?.items?.filter((i) => i.url === href).length || // if child nav is active
    (mainNav &&
      href.split('/')[1] !== '' &&
      href.split('/')[1] === item?.url?.split('/')[1])
  )
}
