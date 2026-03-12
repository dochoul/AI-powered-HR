# Textarea

여러 줄 텍스트 입력 컴포넌트. Office, Platform을 지원합니다 (Admin 미지원).

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Textarea` | Office | `@components/Inputs/Textarea` |
| `P_Textarea` | Platform | `@components/Inputs/Textarea` |

## Props

### 공통 Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `value` | `string` | - | 제어 컴포넌트 값 |
| `defaultValue` | `string` | - | 비제어 초기값 |
| `onChange` | `(e: ChangeEvent<HTMLTextAreaElement>) => void` | - | 값 변경 핸들러 |
| `placeholder` | `string` | - | 플레이스홀더 텍스트 |
| `autosize` | `boolean` | `false` | 내용에 따라 높이 자동 조절 |
| `minRows` | `number` | - | 최소 행 수 |
| `maxRows` | `number` | - | 최대 행 수 (`autosize`와 함께 사용) |
| `resize` | `'none' \| 'both' \| 'horizontal' \| 'vertical'` | `'none'` | 크기 조절 방향 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `readOnly` | `boolean` | `false` | 읽기 전용 여부 |
| `error` | `ReactNode` | - | 에러 메시지 |
| `label` | `ReactNode` | - | 라벨 |

### P_Textarea (추가 Props)

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `variant` | `'default' \| 'table' \| 'essential'` | `'default'` | 입력 스타일 |

## 사용 예시

### 기본 사용

```tsx
import { O_Textarea } from '@components/Inputs/Textarea'

function Example() {
  return (
    <O_Textarea placeholder="내용을 입력해주세요" />
  )
}
```

### 제어 컴포넌트

```tsx
import { O_Textarea } from '@components/Inputs/Textarea'
import { useState } from 'react'

function Example() {
  const [value, setValue] = useState('')

  return (
    <O_Textarea
      value={value}
      onChange={(e) => setValue(e.target.value)}
      placeholder="내용을 입력해주세요"
    />
  )
}
```

### 자동 높이 조절 (Autosize)

```tsx
import { O_Textarea } from '@components/Inputs/Textarea'

function Example() {
  return (
    <O_Textarea
      autosize
      minRows={3}
      maxRows={8}
      placeholder="내용이 길어지면 자동으로 높이가 늘어납니다"
    />
  )
}
```

### 크기 조절 가능

```tsx
import { O_Textarea } from '@components/Inputs/Textarea'

function Example() {
  return (
    <O_Textarea
      resize="vertical"
      minRows={3}
      placeholder="세로로 크기 조절 가능"
    />
  )
}
```

### 에러 상태

```tsx
import { O_Textarea } from '@components/Inputs/Textarea'

function Example() {
  return (
    <O_Textarea
      error="내용을 입력해주세요"
      placeholder="필수 입력 항목"
    />
  )
}
```

### Platform - Essential Variant

```tsx
import { P_Textarea } from '@components/Inputs/Textarea'

function Example() {
  return (
    <P_Textarea
      variant="essential"
      placeholder="필수 입력 항목"
      minRows={3}
    />
  )
}
```
