# MultiSelect

다중 선택 드롭다운 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_MultiSelect` | Office | `@components/MultiSelect` |
| `P_MultiSelect` | Platform | `@components/MultiSelect` |
| `A_MultiSelect` | Admin | `@components/MultiSelect` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `data` | `MultiSelectData[]` | - | 선택 옵션 목록 |
| `value` | `MultiSelectData[]` | - | 제어 컴포넌트 선택값 |
| `defaultValue` | `MultiSelectData[]` | - | 비제어 초기 선택값 |
| `onChange` | `(value: MultiSelectData[]) => void` | - | 값 변경 핸들러 |
| `onRemove` | `(value: MultiSelectData) => void` | - | 항목 제거 핸들러 |
| `onMaxValues` | `() => void` | - | 최대 선택 개수 초과 시 콜백 |
| `placeholder` | `string` | - | 플레이스홀더 텍스트 |
| `size` | `'small' \| 'large'` | `'large'` | 입력 크기 |
| `maxValues` | `number` | - | 최대 선택 가능 개수 |
| `searchable` | `boolean` | `true` | 검색 가능 여부 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `error` | `ReactNode` | - | 에러 메시지 |
| `useVirtual` | `boolean` | `false` | 가상 스크롤 사용 여부 |
| `valueDisplayMode` | `'tag' \| 'text'` | `'tag'` | 선택값 표시 방식 |
| `withEllipsis` | `boolean` | `false` | 태그 말줄임 처리 여부 |
| `truncateValue` | `boolean` | `false` | 값 잘라내기 여부 |
| `scrollType` | `'auto' \| 'always' \| 'scroll' \| 'hover' \| 'never'` | `'auto'` | 스크롤바 표시 방식 |
| `renderTag` | `(props: { text: string; onRemove?: () => void }) => ReactNode` | - | 태그 커스텀 렌더링 |
| `withinPortal` | `boolean` | `true` | 드롭다운을 Portal로 렌더링 여부 |

### MultiSelectData 타입

```typescript
type MultiSelectData = {
  label: string
  value: string
  imgElement?: ReactNode  // 이미지/아이콘 표시
  disabled?: boolean
}
```

## 사용 예시

### 기본 사용

```tsx
import { O_MultiSelect } from '@components/MultiSelect'

const options = [
  { label: '디자인팀', value: '디자인팀' },
  { label: '개발팀', value: '개발팀' },
  { label: '마케팅팀', value: '마케팅팀' },
  { label: '기획팀', value: '기획팀' },
]

function Example() {
  return (
    <O_MultiSelect
      data={options}
      placeholder="팀을 선택해주세요"
    />
  )
}
```

### 제어 컴포넌트

```tsx
import { O_MultiSelect } from '@components/MultiSelect'
import { useState } from 'react'

const options = [
  { label: '디자인팀', value: '디자인팀' },
  { label: '개발팀', value: '개발팀' },
]

function Example() {
  const [selected, setSelected] = useState<typeof options>([])

  return (
    <div>
      <O_MultiSelect
        data={options}
        value={selected}
        onChange={setSelected}
        placeholder="팀을 선택해주세요"
      />
      <p>선택된 팀: {selected.map(s => s.label).join(', ')}</p>
    </div>
  )
}
```

### 최대 선택 개수 제한

```tsx
import { O_MultiSelect } from '@components/MultiSelect'

const options = [
  { label: '옵션1', value: '1' },
  { label: '옵션2', value: '2' },
  { label: '옵션3', value: '3' },
  { label: '옵션4', value: '4' },
]

function Example() {
  return (
    <O_MultiSelect
      data={options}
      maxValues={2}
      onMaxValues={() => alert('최대 2개까지 선택 가능합니다')}
      placeholder="최대 2개 선택 가능"
    />
  )
}
```

### 이미지/아이콘이 있는 옵션

```tsx
import { O_MultiSelect } from '@components/MultiSelect'

const options = [
  {
    label: '홍길동',
    value: 'user1',
    imgElement: <img src="/avatar1.png" width={20} height={20} style={{ borderRadius: '50%' }} />,
  },
  {
    label: '김철수',
    value: 'user2',
    imgElement: <img src="/avatar2.png" width={20} height={20} style={{ borderRadius: '50%' }} />,
  },
]

function Example() {
  return (
    <O_MultiSelect
      data={options}
      placeholder="사용자를 선택해주세요"
    />
  )
}
```

### 텍스트 표시 모드

```tsx
import { O_MultiSelect } from '@components/MultiSelect'

const options = [
  { label: '항목1', value: '1' },
  { label: '항목2', value: '2' },
  { label: '항목3', value: '3' },
]

function Example() {
  return (
    <O_MultiSelect
      data={options}
      valueDisplayMode="text"
      defaultValue={[options[0], options[1]]}
    />
  )
}
```

### 커스텀 태그 렌더링

```tsx
import { O_MultiSelect } from '@components/MultiSelect'

const options = [
  { label: '긴급', value: 'urgent' },
  { label: '중요', value: 'important' },
  { label: '일반', value: 'normal' },
]

function Example() {
  return (
    <O_MultiSelect
      data={options}
      placeholder="우선순위를 선택해주세요"
      renderTag={({ text, onRemove }) => (
        <span
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: 4,
            padding: '2px 8px',
            borderRadius: 12,
            backgroundColor: '#e2e8f0',
            fontSize: 12,
          }}
        >
          {text}
          {onRemove && (
            <button onClick={onRemove} style={{ border: 'none', background: 'none', cursor: 'pointer' }}>
              ×
            </button>
          )}
        </span>
      )}
    />
  )
}
```
