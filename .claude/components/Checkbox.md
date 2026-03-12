# Checkbox

체크박스 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Checkbox` | Office | `@components/Checkbox` |
| `P_Checkbox` | Platform | `@components/Checkbox` |
| `A_Checkbox` | Admin | `@components/Checkbox` |

## Props

### Checkbox Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `checked` | `boolean` | - | 제어 컴포넌트 체크 상태 |
| `defaultChecked` | `boolean` | - | 비제어 초기 체크 상태 |
| `onChange` | `(e: ChangeEvent<HTMLInputElement>) => void` | - | 상태 변경 핸들러 |
| `label` | `ReactNode` | - | 라벨 텍스트 |
| `indeterminate` | `boolean` | `false` | 중간 상태 (일부 선택) |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `error` | `ReactNode` | - | 에러 메시지 |
| `labelColor` | `string` | - | 라벨 색상 |

### Checkbox.Group Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `value` | `string[]` | - | 제어 컴포넌트 선택값 목록 |
| `defaultValue` | `string[]` | - | 비제어 초기 선택값 목록 |
| `onChange` | `(value: string[]) => void` | - | 값 변경 핸들러 |
| `alignment` | `'horizontal' \| 'vertical'` | `'horizontal'` | 정렬 방향 |
| `gap` | `number` | - | 체크박스 간격 (px) |
| `children` | `ReactNode` | - | Checkbox 컴포넌트들 |

## 사용 예시

### 기본 사용

```tsx
import { O_Checkbox } from '@components/Checkbox'

function Example() {
  return <O_Checkbox label="동의합니다" />
}
```

### 제어 컴포넌트

```tsx
import { O_Checkbox } from '@components/Checkbox'
import { useState } from 'react'

function Example() {
  const [checked, setChecked] = useState(false)

  return (
    <O_Checkbox
      checked={checked}
      onChange={(e) => setChecked(e.currentTarget.checked)}
      label="Controlled Checkbox"
    />
  )
}
```

### Indeterminate (중간 상태)

```tsx
import { O_Checkbox } from '@components/Checkbox'
import { useState } from 'react'

function Example() {
  const [state, setState] = useState<Set<string>>(new Set(['value2', 'value3']))
  const allValues = ['value1', 'value2', 'value3', 'value4', 'value5']
  const isIndeterminate = state.size > 0 && state.size < allValues.length
  const isCheckedAll = state.size === allValues.length

  const handleCheckAll = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.currentTarget.checked) {
      setState(new Set(allValues))
    } else {
      setState(new Set())
    }
  }

  return (
    <div>
      <O_Checkbox
        checked={isCheckedAll}
        indeterminate={isIndeterminate}
        onChange={handleCheckAll}
        label={`전체 선택 (${state.size}/${allValues.length})`}
      />
      {allValues.map((value) => (
        <O_Checkbox
          key={value}
          checked={state.has(value)}
          onChange={(e) => {
            const next = new Set(state)
            if (e.currentTarget.checked) next.add(value)
            else next.delete(value)
            setState(next)
          }}
          label={value}
        />
      ))}
    </div>
  )
}
```

### 그룹 (수평/수직)

```tsx
import { O_Checkbox } from '@components/Checkbox'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
      {/* 수평 정렬 (기본) */}
      <O_Checkbox.Group alignment="horizontal">
        <O_Checkbox value="a" label="항목 A" />
        <O_Checkbox value="b" label="항목 B" />
        <O_Checkbox value="c" label="항목 C" />
      </O_Checkbox.Group>

      {/* 수직 정렬 */}
      <O_Checkbox.Group alignment="vertical">
        <O_Checkbox value="x" label="항목 X" />
        <O_Checkbox value="y" label="항목 Y" />
        <O_Checkbox value="z" label="항목 Z" />
      </O_Checkbox.Group>
    </div>
  )
}
```

### 그룹 제어 컴포넌트

```tsx
import { O_Checkbox } from '@components/Checkbox'
import { useState } from 'react'

function Example() {
  const [selected, setSelected] = useState<string[]>(['b'])

  return (
    <O_Checkbox.Group
      value={selected}
      onChange={setSelected}
      alignment="horizontal"
    >
      <O_Checkbox value="a" label="옵션 A" />
      <O_Checkbox value="b" label="옵션 B" />
      <O_Checkbox value="c" label="옵션 C" />
    </O_Checkbox.Group>
  )
}
```

### 비활성화 / 에러 상태

```tsx
import { O_Checkbox } from '@components/Checkbox'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      <O_Checkbox disabled label="비활성화" />
      <O_Checkbox checked disabled label="비활성화 (체크됨)" />
      <O_Checkbox error="필수 항목입니다" label="에러 상태" />
    </div>
  )
}
```
