# Select

드롭다운 선택 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Select` | Office | `@components/Select` |
| `P_Select` | Platform | `@components/Select` |
| `A_Select` | Admin | `@components/Select` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `data` | `{ value: string; label: string; disabled?: boolean }[]` | - | 선택 옵션 목록 |
| `value` | `string \| null` | - | 제어 컴포넌트 선택값 |
| `defaultValue` | `string` | - | 비제어 초기 선택값 |
| `onChange` | `(value: string \| null) => void` | - | 값 변경 핸들러 |
| `placeholder` | `string` | - | 플레이스홀더 텍스트 |
| `size` | `'small' \| 'large'` | `'large'` | 입력 크기 |
| `searchable` | `boolean` | `true` | 검색 가능 여부 |
| `allowDeselect` | `boolean` | `false` | 선택 해제 허용 여부 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `readOnly` | `boolean` | `false` | 읽기 전용 여부 |
| `error` | `ReactNode` | - | 에러 메시지 |
| `maxDropdownHeight` | `number` | - | 드롭다운 최대 높이 |
| `useVirtual` | `boolean` | `false` | 가상 스크롤 사용 여부 (항목이 많을 때) |
| `itemHeight` | `number` | - | 가상 스크롤 아이템 높이 |
| `showClearButton` | `boolean` | `false` | 초기화 버튼 표시 여부 |
| `toggleIcon` | `ReactNode` | - | 드롭다운 토글 아이콘 커스터마이징 |
| `resetOnEmptySearch` | `boolean` | `false` | 검색어 비울 때 선택값 초기화 여부 |
| `onReset` | `() => void` | - | 초기화 시 콜백 |
| `renderOption` | `(item: ComboboxItem) => ReactNode` | - | 옵션 커스텀 렌더링 |
| `withinPortal` | `boolean` | `true` | 드롭다운을 Portal로 렌더링 여부 |

## 사용 예시

### 기본 사용

```tsx
import { O_Select } from '@components/Select'

const options = [
  { value: '디자인팀', label: '디자인팀' },
  { value: '개발팀', label: '개발팀' },
  { value: '마케팅팀', label: '마케팅팀' },
]

function Example() {
  return (
    <O_Select
      data={options}
      placeholder="팀을 선택해주세요"
    />
  )
}
```

### 제어 컴포넌트

```tsx
import { O_Select } from '@components/Select'
import { useState } from 'react'

const options = [
  { value: '디자인팀', label: '디자인팀' },
  { value: '개발팀', label: '개발팀' },
]

function Example() {
  const [selected, setSelected] = useState<string | null>(null)

  return (
    <O_Select
      data={options}
      value={selected}
      onChange={setSelected}
      placeholder="팀을 선택해주세요"
    />
  )
}
```

### 초기값 / allowDeselect

```tsx
import { O_Select } from '@components/Select'

const options = [
  { value: 'UI개발팀', label: 'UI개발팀' },
  { value: '하이웍스팀', label: '하이웍스팀', disabled: true },
]

function Example() {
  return (
    <O_Select
      data={options}
      defaultValue="UI개발팀"
      allowDeselect
      maxDropdownHeight={200}
      searchable={false}
    />
  )
}
```

### 그룹 데이터

```tsx
import { O_Select } from '@components/Select'

const groupedData = [
  {
    group: '개발',
    items: [
      { value: 'frontend', label: '프론트엔드' },
      { value: 'backend', label: '백엔드' },
    ]
  },
  {
    group: '디자인',
    items: [
      { value: 'ux', label: 'UX 디자인' },
      { value: 'ui', label: 'UI 디자인' },
    ]
  },
]

function Example() {
  return (
    <O_Select
      data={groupedData}
      placeholder="직군을 선택해주세요"
    />
  )
}
```

### 옵션 커스텀 렌더링

```tsx
import { O_Select } from '@components/Select'

const options = [
  { value: 'active', label: '활성화' },
  { value: 'inactive', label: '비활성화' },
]

function Example() {
  return (
    <O_Select
      data={options}
      placeholder="상태를 선택해주세요"
      renderOption={({ option }) => (
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <span
            style={{
              width: 8,
              height: 8,
              borderRadius: '50%',
              backgroundColor: option.value === 'active' ? '#48bb78' : '#fc8181',
            }}
          />
          {option.label}
        </div>
      )}
    />
  )
}
```

### 많은 항목 (가상 스크롤)

```tsx
import { O_Select } from '@components/Select'

const manyOptions = Array.from({ length: 1000 }, (_, i) => ({
  value: `item-${i}`,
  label: `항목 ${i + 1}`,
}))

function Example() {
  return (
    <O_Select
      data={manyOptions}
      placeholder="항목을 선택해주세요"
      useVirtual
      itemHeight={36}
    />
  )
}
```

### 초기화 버튼

```tsx
import { O_Select } from '@components/Select'
import { useState } from 'react'

function Example() {
  const [value, setValue] = useState<string | null>('디자인팀')

  return (
    <O_Select
      data={[
        { value: '디자인팀', label: '디자인팀' },
        { value: '개발팀', label: '개발팀' },
      ]}
      value={value}
      onChange={setValue}
      showClearButton
      onReset={() => setValue(null)}
    />
  )
}
```

### Platform - Essential Variant

```tsx
import { P_Select } from '@components/Select'

function Example() {
  return (
    <P_Select
      data={[{ value: 'a', label: '옵션 A' }]}
      variant="essential"
      placeholder="필수 선택 항목"
    />
  )
}
```
