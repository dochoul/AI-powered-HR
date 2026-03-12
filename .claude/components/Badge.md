# Badge

뱃지/라벨 컴포넌트. Office 플랫폼만 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Badge` | Office | `@components/Badge` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `text` | `string` | - | 뱃지 텍스트 (`isNew`가 false일 때) |
| `isNew` | `boolean` | `false` | "New" 뱃지 표시 여부 (text와 함께 사용 불가) |
| `size` | `'small' \| 'large'` | `'large'` | 뱃지 크기 |
| `color` | `'blue'` | - | 뱃지 색상 |
| `readonly` | `boolean` | `false` | 읽기 전용 여부 |
| `onClick` | `() => void` | - | 클릭 이벤트 핸들러 |
| `className` | `string` | - | 추가 CSS 클래스 |
| `style` | `CSSProperties` | - | 인라인 스타일 |

> `isNew`와 `text`는 동시에 사용할 수 없습니다 (TypeScript 타입으로 강제).

## 사용 예시

### 텍스트 뱃지

```tsx
import { O_Badge } from '@components/Badge'

function Example() {
  return (
    <div style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
      <O_Badge text="Large" size="large" />
      <O_Badge text="Small" size="small" />
    </div>
  )
}
```

### New 뱃지

```tsx
import { O_Badge } from '@components/Badge'

function Example() {
  return (
    <div style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
      <O_Badge isNew size="large" />
      <O_Badge isNew size="small" />
    </div>
  )
}
```

### 클릭 가능한 뱃지

```tsx
import { O_Badge } from '@components/Badge'

function Example() {
  return (
    <O_Badge
      text="클릭 가능한 뱃지"
      onClick={() => alert('뱃지를 클릭했습니다')}
    />
  )
}
```

### 읽기 전용 뱃지

```tsx
import { O_Badge } from '@components/Badge'

function Example() {
  return (
    <O_Badge
      text="읽기 전용"
      readonly
    />
  )
}
```

### 메뉴 아이템과 함께 사용

```tsx
import { O_Badge } from '@components/Badge'

function MenuItem({ label, isNew }: { label: string; isNew?: boolean }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
      <span>{label}</span>
      {isNew && <O_Badge isNew size="small" />}
    </div>
  )
}

function Example() {
  return (
    <nav>
      <MenuItem label="대시보드" />
      <MenuItem label="새 기능" isNew />
      <MenuItem label="설정" />
    </nav>
  )
}
```
