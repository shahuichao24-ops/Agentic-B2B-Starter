import {
  ChevronLeft,
  ChevronRight,
  ChevronsLeft,
  ChevronsRight,
} from 'lucide-react'
import { Button } from '@/components/ui/button'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'

export interface DataPaginationProps {
  currentPage: number
  pageSize: number
  totalItems: number
  onPageChange: (page: number) => void
  onPageSizeChange?: (pageSize: number) => void
  pageSizeOptions?: number[]
  className?: string
}

export function DataPagination({
  currentPage,
  pageSize,
  totalItems,
  onPageChange,
  onPageSizeChange,
  pageSizeOptions = [10, 20, 50],
  className = '',
}: DataPaginationProps) {
  const totalPages = Math.max(1, Math.ceil(totalItems / pageSize))

  // 生成页码序列（显示当前页附近页码）
  const getPageNumbers = () => {
    const pages: (number | string)[] = []
    if (totalPages <= 5) {
      for (let i = 1; i <= totalPages; i++) pages.push(i)
    } else {
      if (currentPage <= 3) {
        pages.push(1, 2, 3, 4, '...', totalPages)
      } else if (currentPage >= totalPages - 2) {
        pages.push(
          1,
          '...',
          totalPages - 3,
          totalPages - 2,
          totalPages - 1,
          totalPages
        )
      } else {
        pages.push(
          1,
          '...',
          currentPage - 1,
          currentPage,
          currentPage + 1,
          '...',
          totalPages
        )
      }
    }
    return pages
  }

  return (
    <div
      className={`flex flex-wrap items-center justify-between gap-3 border-t bg-card/50 px-4 py-3 text-xs text-muted-foreground ${className}`}
    >
      {/* 左侧：统计信息 */}
      <div className='flex items-center gap-2'>
        <span>
          共{' '}
          <strong className='font-semibold text-foreground'>
            {totalItems}
          </strong>{' '}
          条记录
        </span>
        <span className='text-muted-foreground/40'>|</span>
        <span>
          第{' '}
          <strong className='font-semibold text-foreground'>
            {currentPage}
          </strong>{' '}
          / {totalPages} 页
        </span>
      </div>

      {/* 右侧：每页条数与翻页按钮 */}
      <div className='flex items-center gap-4'>
        {onPageSizeChange && (
          <div className='flex items-center gap-1.5'>
            <span>每页</span>
            <Select
              value={String(pageSize)}
              onValueChange={(val) => {
                onPageSizeChange(Number(val))
                onPageChange(1)
              }}
            >
              <SelectTrigger className='h-7 w-20 text-xs'>
                <SelectValue placeholder={String(pageSize)} />
              </SelectTrigger>
              <SelectContent>
                {pageSizeOptions.map((opt) => (
                  <SelectItem key={opt} value={String(opt)} className='text-xs'>
                    {opt} 条
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
        )}

        {/* 翻页按钮组 */}
        <div className='flex items-center gap-1'>
          <Button
            variant='outline'
            size='sm'
            className='h-7 w-7 p-0'
            disabled={currentPage <= 1}
            onClick={() => onPageChange(1)}
            title='首页'
          >
            <ChevronsLeft className='h-3.5 w-3.5' />
          </Button>
          <Button
            variant='outline'
            size='sm'
            className='h-7 w-7 p-0'
            disabled={currentPage <= 1}
            onClick={() => onPageChange(currentPage - 1)}
            title='上一页'
          >
            <ChevronLeft className='h-3.5 w-3.5' />
          </Button>

          {/* 页码 */}
          <div className='flex items-center gap-1'>
            {getPageNumbers().map((page, idx) =>
              typeof page === 'number' ? (
                <Button
                  key={idx}
                  variant={currentPage === page ? 'default' : 'outline'}
                  size='sm'
                  className={`h-7 w-7 p-0 text-xs ${
                    currentPage === page ? 'pointer-events-none' : ''
                  }`}
                  onClick={() => onPageChange(page)}
                >
                  {page}
                </Button>
              ) : (
                <span
                  key={idx}
                  className='px-1 text-muted-foreground/60 select-none'
                >
                  ...
                </span>
              )
            )}
          </div>

          <Button
            variant='outline'
            size='sm'
            className='h-7 w-7 p-0'
            disabled={currentPage >= totalPages}
            onClick={() => onPageChange(currentPage + 1)}
            title='下一页'
          >
            <ChevronRight className='h-3.5 w-3.5' />
          </Button>
          <Button
            variant='outline'
            size='sm'
            className='h-7 w-7 p-0'
            disabled={currentPage >= totalPages}
            onClick={() => onPageChange(totalPages)}
            title='尾页'
          >
            <ChevronsRight className='h-3.5 w-3.5' />
          </Button>
        </div>
      </div>
    </div>
  )
}
