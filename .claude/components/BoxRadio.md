# BoxRadio

박스 형태의 라디오 버튼 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_BoxRadio` | Office | `@components/Radios/BoxRadio` |
| `P_BoxRadio` | Platform | `@components/Radios/BoxRadio` |
| `A_BoxRadio` | Admin | `@components/Radios/BoxRadio` |

## Props

### BoxRadio Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `value` | `string` | - | 라디오 값 (Group 내에서 사용) |
| `label` | `ReactNode` | - | 라벨 텍스트 |
| `checked` | `boolean` | - | 제어 컴포넌트 체크 상태 |
| `onChange` | `(e: ChangeEvent<HTMLInputElement>) => void` | - | 상태 변경 핸들러 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `size` | `'large' \| 'small'` | `'large'` | 박스 크기 |
| `width` | `string \| number` | - | 박스 너비 (CSS 값) |

### BoxRadio.Group Props

Radio.Group과 동일한 props를 사용합니다.

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `value` | `string` | - | 제어 컴포넌트 선택값 |
| `defaultValue` | `string` | - | 비제어 초기 선택값 |
| `onChange` | `(value: string) => void` | - | 값 변경 핸들러 |
| `alignment` | `'horizontal' \| 'vertical'` | `'horizontal'` | 정렬 방향 |

## 사용 예시

### 기본 사용

```tsx
import { O_BoxRadio } from '@components/Radios/BoxRadio'

function Example() {
  return (
    <O_BoxRadio.Group defaultValue="option1">
      <O_BoxRadio value="option1" label="옵션 1" />
      <O_BoxRadio value="option2" label="옵션 2" />
      <O_BoxRadio value="option3" label="옵션 3" />
    </O_BoxRadio.Group>
  )
}
```

### 제어 컴포넌트

```tsx
import { O_BoxRadio } from '@components/Radios/BoxRadio'
import { useState } from 'react'

function Example() {
  const [selected, setSelected] = useState('month')

  return (
    <O_BoxRadio.Group value={selected} onChange={setSelected}>
      <O_BoxRadio value="day" label="일별" />
      <O_BoxRadio value="week" label="주별" />
      <O_BoxRadio value="month" label="월별" />
      <O_BoxRadio value="year" label="연별" />
    </O_BoxRadio.Group>
  )
}
```

### 크기 / 너비 조절

```tsx
import { O_BoxRadio } from '@components/Radios/BoxRadio'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
      {/* large (기본) */}
      <O_BoxRadio.Group defaultValue="a">
        <O_BoxRadio value="a" label="Large A" size="large" />
        <O_BoxRadio value="b" label="Large B" size="large" />
      </O_BoxRadio.Group>

      {/* small */}
      <O_BoxRadio.Group defaultValue="a">
        <O_BoxRadio value="a" label="Small A" size="small" />
        <O_BoxRadio value="b" label="Small B" size="small" />
      </O_BoxRadio.Group>

      {/* 너비 고정 */}
      <O_BoxRadio.Group defaultValue="a">
        <O_BoxRadio value="a" label="너비 120px" width={120} />
        <O_BoxRadio value="b" label="너비 120px" width={120} />
      </O_BoxRadio.Group>
    </div>
  )
}
```

### 비활성화

```tsx
import { O_BoxRadio } from '@components/Radios/BoxRadio'

function Example() {
  return (
    <O_BoxRadio.Group defaultValue="a">
      <O_BoxRadio value="a" label="활성화" />
      <O_BoxRadio value="b" label="비활성화" disabled />
    </O_BoxRadio.Group>
  )
}
```
