import { AlertTriangle } from 'lucide-react'
import { Button } from '@/components/ui/button'
import {
  Dialog,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog'

export interface ConfirmDialogProps {
  open: boolean
  onOpenChange: (open: boolean) => void
  title?: string
  content: string
  confirmText?: string
  cancelText?: string
  variant?: 'destructive' | 'default'
  loading?: boolean
  onConfirm: () => void | Promise<void>
}

export function ConfirmDialog({
  open,
  onOpenChange,
  title = '确认执行操作',
  content,
  confirmText = '确认删除',
  cancelText = '取消',
  variant = 'destructive',
  loading = false,
  onConfirm,
}: ConfirmDialogProps) {
  const handleConfirm = async () => {
    await onConfirm()
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className='max-w-md rounded-xl p-6'>
        <DialogHeader className='flex flex-row items-start gap-3 text-left'>
          <div
            className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-full ${
              variant === 'destructive'
                ? 'bg-red-50 text-red-600 dark:bg-red-950/40 dark:text-red-400'
                : 'bg-amber-50 text-amber-600 dark:bg-amber-950/40 dark:text-amber-400'
            }`}
          >
            <AlertTriangle className='h-5 w-5' />
          </div>
          <div className='space-y-1 pt-0.5'>
            <DialogTitle className='text-base font-semibold text-foreground'>
              {title}
            </DialogTitle>
            <p className='text-sm leading-relaxed text-muted-foreground'>
              {content}
            </p>
          </div>
        </DialogHeader>

        <DialogFooter className='mt-3 gap-2 sm:gap-2'>
          <Button
            type='button'
            variant='outline'
            size='sm'
            onClick={() => onOpenChange(false)}
            disabled={loading}
          >
            {cancelText}
          </Button>
          <Button
            type='button'
            variant={variant === 'destructive' ? 'destructive' : 'default'}
            size='sm'
            onClick={handleConfirm}
            disabled={loading}
          >
            {loading ? '正在处理...' : confirmText}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
