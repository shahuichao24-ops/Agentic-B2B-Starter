import { Link } from '@tanstack/react-router'
import { User, Settings, LogOut } from 'lucide-react'
import useDialogState from '@/hooks/use-dialog-state'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
import { Button } from '@/components/ui/button'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import { SignOutDialog } from '@/components/sign-out-dialog'

export function ProfileDropdown() {
  const [open, setOpen] = useDialogState()

  return (
    <>
      <DropdownMenu modal={false}>
        <DropdownMenuTrigger asChild>
          <Button
            variant='ghost'
            className='flex h-9 items-center gap-2 rounded-full px-2 transition-colors hover:bg-muted/60'
          >
            <Avatar className='h-7 w-7 border border-border/60'>
              <AvatarImage src='/avatars/01.png' alt='系统管理员' />
              <AvatarFallback className='bg-primary/10 text-xs font-bold text-primary'>
                管
              </AvatarFallback>
            </Avatar>
            <div className='hidden flex-col text-left sm:flex'>
              <span className='text-xs leading-tight font-semibold text-foreground'>
                系统管理员
              </span>
              <span className='text-[10px] leading-none text-muted-foreground'>
                超级管理员
              </span>
            </div>
          </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent className='w-56' align='end' forceMount>
          <DropdownMenuLabel className='p-3 font-normal'>
            <div className='flex flex-col gap-1'>
              <div className='flex items-center gap-1.5'>
                <span className='text-sm font-bold text-foreground'>
                  系统管理员
                </span>
                <span className='py-0.2 inline-flex items-center rounded-sm bg-primary/10 px-1.5 text-[10px] font-medium text-primary'>
                  管理员
                </span>
              </div>
              <p className='font-mono text-xs text-muted-foreground'>
                admin@example.com
              </p>
            </div>
          </DropdownMenuLabel>
          <DropdownMenuSeparator />
          <DropdownMenuGroup>
            <DropdownMenuItem asChild>
              <Link
                to='/settings'
                className='flex cursor-pointer items-center gap-2'
              >
                <User className='size-4 text-muted-foreground' />
                <span>个人资料与偏好</span>
              </Link>
            </DropdownMenuItem>
            <DropdownMenuItem asChild>
              <Link
                to='/settings'
                className='flex cursor-pointer items-center gap-2'
              >
                <Settings className='size-4 text-muted-foreground' />
                <span>系统管理设置</span>
              </Link>
            </DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuItem
            variant='destructive'
            onClick={() => setOpen(true)}
            className='flex cursor-pointer items-center gap-2 text-red-600 focus:text-red-700'
          >
            <LogOut className='size-4 text-red-600' />
            <span>退出登录</span>
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>

      <SignOutDialog open={!!open} onOpenChange={setOpen} />
    </>
  )
}
