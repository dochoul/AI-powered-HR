# IconButton

아이콘만 표시하는 버튼 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_IconButton` | Office | `@components/Buttons` |
| `P_IconButton` | Platform | `@components/Buttons` |
| `A_IconButton` | Admin | `@components/Buttons` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `variant` | `'filled' \| 'outline' \| 'text' \| 'ghost' \| 'cancel' \| 'destructive' \| 'danger'` | `'filled'` | 버튼 스타일 |
| `size` | `'x-small' \| 'small' \| 'regular' \| 'large'` | `'regular'` | 버튼 크기 |
| `iconColor` | `string` | - | 아이콘 색상 (CSS color 값) |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `onClick` | `MouseEventHandler<HTMLButtonElement>` | - | 클릭 이벤트 핸들러 |
| `children` | `ReactNode` | - | 아이콘 엘리먼트 |

## 사용 예시

### 기본 사용

```tsx
import { O_IconButton } from '@components/Buttons'
import { PlusIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <O_IconButton onClick={() => console.log('clicked')}>
      <PlusIcon />
    </O_IconButton>
  )
}
```

### Variant

```tsx
import { O_IconButton } from '@components/Buttons'
import { PlusIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <div style={{ display: 'flex', gap: '8px' }}>
      <O_IconButton variant="filled"><PlusIcon /></O_IconButton>
      <O_IconButton variant="outline"><PlusIcon /></O_IconButton>
      <O_IconButton variant="ghost"><PlusIcon /></O_IconButton>
      <O_IconButton variant="text"><PlusIcon /></O_IconButton>
    </div>
  )
}
```

### 아이콘 색상 커스터마이징

```tsx
import { O_IconButton } from '@components/Buttons'
import { TrashIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <O_IconButton variant="ghost" iconColor="#e53e3e">
      <TrashIcon />
    </O_IconButton>
  )
}
```

### Disabled

```tsx
import { O_IconButton } from '@components/Buttons'
import { PlusIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <O_IconButton disabled>
      <PlusIcon />
    </O_IconButton>
  )
}
```
