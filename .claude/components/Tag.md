# Tag

태그 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Tag` | Office | `@components/Tag` |
| `P_Tag` | Platform | `@components/Tag` |
| `A_Tag` | Admin | `@components/Tag` |

## Props

### 공통 Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `text` | `string` | - | 태그 텍스트 |
| `shape` | `'square' \| 'round'` | `'square'` | 태그 모양 |
| `borderless` | `boolean` | `false` | 테두리 없음 여부 |
| `size` | `'small' \| 'large'` | `'large'` | 태그 크기 |
| `readonly` | `boolean` | `false` | 읽기 전용 여부 |
| `className` | `string` | - | 추가 CSS 클래스 |
| `style` | `CSSProperties` | - | 인라인 스타일 |

### O_Tag (추가 Props)

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `color` | `'gray' \| 'blue' \| 'yellow' \| 'green' \| 'red' \| 'blueGray'` | `'gray'` | 태그 색상 |
| `withTextColor` | `boolean` | `false` | 텍스트 색상 적용 여부 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `withRemoveButton` | `boolean` | `false` | 제거 버튼 표시 여부 |
| `onRemove` | `() => void` | - | 제거 버튼 클릭 핸들러 |
| `leftSection` | `ReactNode` | - | 왼쪽 아이콘/내용 |

### P_Tag (추가 Props)

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `color` | `'gray' \| 'blue' \| 'orange' \| 'green' \| 'red' \| 'violet'` | `'gray'` | 태그 색상 |
| `variant` | `'filled' \| 'light'` | `'light'` | 태그 스타일 |
| `withRemoveButton` | `boolean` | `false` | 제거 버튼 표시 여부 |
| `onRemove` | `() => void` | - | 제거 버튼 클릭 핸들러 |

### A_Tag (추가 Props)

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `color` | `'gray' \| 'blue' \| 'orange' \| 'green' \| 'red'` | `'gray'` | 태그 색상 |
| `variant` | `'filled' \| 'light'` | `'light'` | 태그 스타일 |
| `withRemoveButton` | `boolean` | `false` | 제거 버튼 표시 여부 |
| `onRemove` | `() => void` | - | 제거 버튼 클릭 핸들러 |
| `leftSection` | `ReactNode` | - | 왼쪽 아이콘/내용 |

## 사용 예시

### 기본 사용 (Office)

```tsx
import { O_Tag } from '@components/Tag'

function Example() {
  return (
    <div style={{ display: 'flex', gap: 8 }}>
      <O_Tag text="기본" />
      <O_Tag text="파랑" color="blue" />
      <O_Tag text="노랑" color="yellow" />
      <O_Tag text="초록" color="green" />
      <O_Tag text="빨강" color="red" />
      <O_Tag text="블루그레이" color="blueGray" />
    </div>
  )
}
```

### 크기 및 모양

```tsx
import { O_Tag } from '@components/Tag'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      <div style={{ display: 'flex', gap: 8 }}>
        <O_Tag text="Large" size="large" />
        <O_Tag text="Small" size="small" />
      </div>
      <div style={{ display: 'flex', gap: 8 }}>
        <O_Tag text="Square" shape="square" />
        <O_Tag text="Round" shape="round" />
      </div>
    </div>
  )
}
```

### 제거 가능한 태그

```tsx
import { O_Tag } from '@components/Tag'
import { useState } from 'react'

function Example() {
  const [tags, setTags] = useState(['디자인', '개발', '기획'])

  return (
    <div style={{ display: 'flex', gap: 8 }}>
      {tags.map((tag) => (
        <O_Tag
          key={tag}
          text={tag}
          withRemoveButton
          onRemove={() => setTags(prev => prev.filter(t => t !== tag))}
        />
      ))}
    </div>
  )
}
```

### 왼쪽 아이콘

```tsx
import { O_Tag } from '@components/Tag'
import { StarIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <O_Tag
      text="즐겨찾기"
      leftSection={<StarIcon width={12} />}
    />
  )
}
```

### Platform - Variant

```tsx
import { P_Tag } from '@components/Tag'

function Example() {
  return (
    <div style={{ display: 'flex', gap: 8 }}>
      <P_Tag text="Light 파랑" color="blue" variant="light" />
      <P_Tag text="Filled 파랑" color="blue" variant="filled" />
      <P_Tag text="Light 주황" color="orange" variant="light" />
      <P_Tag text="Filled 초록" color="green" variant="filled" />
    </div>
  )
}
```
