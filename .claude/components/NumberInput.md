# NumberInput

숫자 전용 입력 필드 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_NumberInput` | Office | `@components/Inputs/NumberInput` |
| `P_NumberInput` | Platform | `@components/Inputs/NumberInput` |
| `A_NumberInput` | Admin | `@components/Inputs/NumberInput` |

## Props

### 공통 Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `size` | `'small' \| 'large'` | `'large'` | 입력 크기 |
| `textAlign` | `'left' \| 'right'` | `'left'` | 텍스트 정렬 |
| `value` | `number \| string` | - | 제어 컴포넌트 값 |
| `defaultValue` | `number \| string` | - | 비제어 초기값 |
| `onChange` | `(value: number \| string) => void` | - | 값 변경 핸들러 |
| `min` | `number` | - | 최솟값 |
| `max` | `number` | - | 최댓값 |
| `step` | `number` | - | 증감 단위 |
| `allowDecimal` | `boolean` | `true` | 소수점 허용 여부 |
| `decimalScale` | `number` | - | 소수점 자릿수 |
| `thousandSeparator` | `string` | - | 천 단위 구분자 (예: `','`) |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `readOnly` | `boolean` | `false` | 읽기 전용 여부 |
| `error` | `ReactNode` | - | 에러 메시지 |
| `placeholder` | `string` | - | 플레이스홀더 |

### P_NumberInput (추가 Props)

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `variant` | `'default' \| 'essential' \| 'table'` | `'default'` | 입력 스타일 |

## 사용 예시

### 기본 사용

```tsx
import { O_NumberInput } from '@components/Inputs/NumberInput'

function Example() {
  return <O_NumberInput placeholder="숫자를 입력해주세요" />
}
```

### 제어 컴포넌트

```tsx
import { O_NumberInput } from '@components/Inputs/NumberInput'
import { useState } from 'react'

function Example() {
  const [value, setValue] = useState<number | string>(0)

  return (
    <O_NumberInput
      value={value}
      onChange={setValue}
      min={0}
      max={100}
    />
  )
}
```

### 천 단위 구분자 / 소수점

```tsx
import { O_NumberInput } from '@components/Inputs/NumberInput'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
      {/* 천 단위 구분자 */}
      <O_NumberInput
        thousandSeparator=","
        placeholder="1,000,000"
      />

      {/* 소수점 2자리 */}
      <O_NumberInput
        allowDecimal
        decimalScale={2}
        placeholder="0.00"
      />

      {/* 정수만 */}
      <O_NumberInput
        allowDecimal={false}
        placeholder="정수만 입력"
      />
    </div>
  )
}
```

### 오른쪽 정렬

```tsx
import { O_NumberInput } from '@components/Inputs/NumberInput'

function Example() {
  return (
    <O_NumberInput
      textAlign="right"
      thousandSeparator=","
      defaultValue={1000000}
    />
  )
}
```

### 크기

```tsx
import { O_NumberInput } from '@components/Inputs/NumberInput'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
      <O_NumberInput size="small" placeholder="small" />
      <O_NumberInput size="large" placeholder="large" />
    </div>
  )
}
```

### Platform - Essential / Table Variant

```tsx
import { P_NumberInput } from '@components/Inputs/NumberInput'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
      <P_NumberInput variant="essential" placeholder="필수 입력" />
      <P_NumberInput variant="table" placeholder="테이블 셀" />
    </div>
  )
}
```
