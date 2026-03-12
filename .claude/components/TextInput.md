# TextInput

텍스트 입력 필드 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_TextInput` | Office | `@components/Inputs/TextInput` |
| `P_TextInput` | Platform | `@components/Inputs/TextInput` |
| `A_TextInput` | Admin | `@components/Inputs/TextInput` |

## Props

### O_TextInput / A_TextInput

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `variant` | `'default' \| 'table'` | `'default'` | 입력 스타일 |
| `size` | `'small' \| 'large'` | `'large'` | 입력 크기 |
| `placeholder` | `string` | - | 플레이스홀더 텍스트 |
| `value` | `string` | - | 제어 컴포넌트 값 |
| `defaultValue` | `string` | - | 비제어 컴포넌트 초기값 |
| `onChange` | `(e: ChangeEvent<HTMLInputElement>) => void` | - | 값 변경 핸들러 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `readOnly` | `boolean` | `false` | 읽기 전용 여부 |
| `error` | `ReactNode` | - | 에러 메시지 |
| `label` | `ReactNode` | - | 라벨 |
| `leftSection` | `ReactNode` | - | 왼쪽 섹션 |
| `rightSection` | `ReactNode` | - | 오른쪽 섹션 |

### P_TextInput (추가 Props)

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `variant` | `'default' \| 'table' \| 'essential'` | `'default'` | 입력 스타일 (`'essential'`은 Platform만 지원) |
| `success` | `ReactNode` | - | 성공 메시지 |
| `showClearButton` | `boolean` | `false` | 초기화 버튼 표시 여부 |
| `clearButtonProps` | `Record<string, any>` | - | 초기화 버튼 props |

## 사용 예시

### 기본 사용

```tsx
import { O_TextInput } from '@components/Inputs/TextInput'

function Example() {
  return <O_TextInput placeholder="텍스트를 입력해주세요" />
}
```

### 제어 컴포넌트

```tsx
import { O_TextInput } from '@components/Inputs/TextInput'
import { useState } from 'react'

function Example() {
  const [value, setValue] = useState('hig9.com')

  return (
    <O_TextInput
      placeholder="오피스를 입력해주세요"
      value={value}
      onChange={(e) => setValue(e.target.value)}
    />
  )
}
```

### 크기 (Size)

```tsx
import { O_TextInput } from '@components/Inputs/TextInput'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
      <O_TextInput size="small" placeholder="small" />
      <O_TextInput size="large" placeholder="large" />
    </div>
  )
}
```

### 에러 상태

```tsx
import { O_TextInput } from '@components/Inputs/TextInput'

function Example() {
  return (
    <O_TextInput
      placeholder="이메일을 입력해주세요"
      error="유효한 이메일 주소를 입력해주세요"
    />
  )
}
```

### 읽기 전용 / 비활성화

```tsx
import { O_TextInput } from '@components/Inputs/TextInput'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
      <O_TextInput value="읽기 전용" readOnly />
      <O_TextInput value="비활성화" disabled />
    </div>
  )
}
```

### Platform - Essential Variant

```tsx
import { P_TextInput } from '@components/Inputs/TextInput'

function Example() {
  return (
    <P_TextInput
      variant="essential"
      placeholder="필수 입력 항목"
    />
  )
}
```

### Platform - 성공 메시지 / 초기화 버튼

```tsx
import { P_TextInput } from '@components/Inputs/TextInput'
import { useState } from 'react'

function Example() {
  const [value, setValue] = useState('초기값')

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
      <P_TextInput
        value={value}
        onChange={(e) => setValue(e.target.value)}
        success="올바른 형식입니다"
      />
      <P_TextInput
        value={value}
        onChange={(e) => setValue(e.target.value)}
        showClearButton
        clearButtonProps={{ onClick: () => setValue('') }}
      />
    </div>
  )
}
```

### 테이블 Variant

```tsx
import { O_TextInput } from '@components/Inputs/TextInput'

function Example() {
  return (
    <O_TextInput
      variant="table"
      placeholder="테이블 셀 내 입력"
    />
  )
}
```
