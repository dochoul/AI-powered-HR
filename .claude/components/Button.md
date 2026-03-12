# Button

일반 버튼 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Button` | Office | `@components/Buttons` |
| `P_Button` | Platform | `@components/Buttons` |
| `A_Button` | Admin | `@components/Buttons` |

## Props

### O_Button

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `variant` | `'filled' \| 'outline' \| 'text' \| 'ghost' \| 'cancel' \| 'destructive' \| 'danger'` | `'filled'` | 버튼 스타일 |
| `size` | `'x-small' \| 'small' \| 'regular' \| 'large'` | `'regular'` | 버튼 크기 |
| `leftIcon` | `ReactNode` | - | 왼쪽 아이콘 |
| `rightIcon` | `ReactNode` | - | 오른쪽 아이콘 |
| `isHeader` | `boolean` | `false` | 헤더 스타일 적용 (`variant='text'`일 때만 유효) |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `onClick` | `MouseEventHandler<HTMLButtonElement>` | - | 클릭 이벤트 핸들러 |
| `type` | `'button' \| 'submit' \| 'reset'` | `'button'` | 버튼 타입 |
| `component` | `ElementType` | - | 다형성 컴포넌트 (예: `'a'`) |
| `children` | `ReactNode` | - | 버튼 내용 |

### P_Button / A_Button

O_Button과 동일한 Props를 지원하며, 각 플랫폼의 디자인 시스템이 적용됩니다.

## 사용 예시

### 기본 사용

```tsx
import { O_Button } from '@components/Buttons'

function Example() {
  return <O_Button onClick={() => console.log('clicked')}>버튼</O_Button>
}
```

### Variant

```tsx
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <div style={{ display: 'flex', gap: '16px', flexWrap: 'wrap' }}>
      <O_Button variant="filled">filled</O_Button>
      <O_Button variant="outline">outline</O_Button>
      <O_Button variant="ghost">ghost</O_Button>
      <O_Button variant="cancel">cancel</O_Button>
      <O_Button variant="destructive">destructive</O_Button>
      <O_Button variant="danger">danger</O_Button>
      <O_Button variant="text">text</O_Button>
    </div>
  )
}
```

### Size

```tsx
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <div style={{ display: 'flex', gap: '16px', alignItems: 'center' }}>
      <O_Button size="x-small">x-small</O_Button>
      <O_Button size="small">small</O_Button>
      <O_Button size="regular">regular</O_Button>
      <O_Button size="large">large</O_Button>
    </div>
  )
}
```

### 아이콘 포함

```tsx
import { O_Button } from '@components/Buttons'
import { PlusIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <div style={{ display: 'flex', gap: '16px' }}>
      <O_Button leftIcon={<PlusIcon />}>왼쪽 아이콘</O_Button>
      <O_Button rightIcon={<PlusIcon />}>오른쪽 아이콘</O_Button>
    </div>
  )
}
```

### Disabled

```tsx
import { O_Button } from '@components/Buttons'

function Example() {
  return <O_Button disabled>비활성화 버튼</O_Button>
}
```

### 다형성 컴포넌트 (링크로 사용)

```tsx
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <O_Button component="a" href="/some-path">
      링크 버튼
    </O_Button>
  )
}
```

### 헤더 스타일 (text variant)

```tsx
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <O_Button variant="text" isHeader>
      헤더 버튼
    </O_Button>
  )
}
```

### 플랫폼별 사용

```tsx
import { O_Button, P_Button, A_Button } from '@components/Buttons'

function Example() {
  return (
    <>
      {/* Office */}
      <O_Button variant="filled">Office 버튼</O_Button>

      {/* Platform */}
      <P_Button variant="filled">Platform 버튼</P_Button>

      {/* Admin */}
      <A_Button variant="filled">Admin 버튼</A_Button>
    </>
  )
}
```
