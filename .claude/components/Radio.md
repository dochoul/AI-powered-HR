# Radio

라디오 버튼 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Radio` | Office | `@components/Radios/Radio` |
| `P_Radio` | Platform | `@components/Radios/Radio` |
| `A_Radio` | Admin | `@components/Radios/Radio` |

## Props

### Radio Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `value` | `string` | - | 라디오 값 (Group 내에서 사용) |
| `label` | `ReactNode` | - | 라벨 텍스트 |
| `checked` | `boolean` | - | 제어 컴포넌트 체크 상태 |
| `onChange` | `(e: ChangeEvent<HTMLInputElement>) => void` | - | 상태 변경 핸들러 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `error` | `ReactNode` | - | 에러 메시지 |

### Radio.Group Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `value` | `string` | - | 제어 컴포넌트 선택값 |
| `defaultValue` | `string` | - | 비제어 초기 선택값 |
| `onChange` | `(value: string) => void` | - | 값 변경 핸들러 |
| `alignment` | `'horizontal' \| 'vertical'` | `'horizontal'` | 정렬 방향 |
| `gap` | `number` | - | 라디오 간격 (px) |
| `children` | `ReactNode` | - | Radio 컴포넌트들 |

## 사용 예시

### 기본 사용

```tsx
import { O_Radio } from '@components/Radios/Radio'

function Example() {
  return (
    <O_Radio.Group defaultValue="option1">
      <O_Radio value="option1" label="옵션 1" />
      <O_Radio value="option2" label="옵션 2" />
      <O_Radio value="option3" label="옵션 3" />
    </O_Radio.Group>
  )
}
```

### 제어 컴포넌트

```tsx
import { O_Radio } from '@components/Radios/Radio'
import { useState } from 'react'

function Example() {
  const [selected, setSelected] = useState('option1')

  return (
    <O_Radio.Group value={selected} onChange={setSelected}>
      <O_Radio value="option1" label="옵션 1" />
      <O_Radio value="option2" label="옵션 2" />
      <O_Radio value="option3" label="옵션 3" />
    </O_Radio.Group>
  )
}
```

### 수직 정렬

```tsx
import { O_Radio } from '@components/Radios/Radio'

function Example() {
  return (
    <O_Radio.Group defaultValue="a" alignment="vertical">
      <O_Radio value="a" label="항목 A" />
      <O_Radio value="b" label="항목 B" />
      <O_Radio value="c" label="항목 C" />
    </O_Radio.Group>
  )
}
```

### 비활성화

```tsx
import { O_Radio } from '@components/Radios/Radio'

function Example() {
  return (
    <O_Radio.Group defaultValue="a">
      <O_Radio value="a" label="활성화" />
      <O_Radio value="b" label="비활성화" disabled />
      <O_Radio value="c" label="비활성화 (선택됨)" disabled checked />
    </O_Radio.Group>
  )
}
```
