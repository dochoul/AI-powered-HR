# Autocomplete

자동완성 드롭다운 입력 컴포넌트. Office, Platform을 지원합니다 (Admin 미지원).

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Autocomplete` | Office | `@components/Autocomplete` |
| `P_Autocomplete` | Platform | `@components/Autocomplete` |

## Props

제네릭 타입 `T`를 지원합니다. 기본값은 `string`.

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `data` | `CustomType<T>[]` | - | 자동완성 옵션 목록 |
| `size` | `'small' \| 'large'` | - | 입력 크기 |
| `variant` | `'default' \| 'table'` | `'default'` | 입력 스타일 |
| `placeholder` | `string` | - | 플레이스홀더 텍스트 |
| `onItemSubmit` | `(item: CustomType<T>) => void` | - | 항목 선택 시 콜백 |
| `ItemComponent` | `(item: CustomType<T>) => ReactNode` | - | 옵션 커스텀 렌더링 |
| `EmptyComponent` | `({ searchValue }) => ReactNode` | - | 검색 결과 없을 때 렌더링 |
| `limit` | `number` | - | 표시할 최대 옵션 수 |
| `withEmptyValueOnOptionSubmit` | `boolean` | `false` | 옵션 선택 후 입력값 초기화 여부 |
| `scrollType` | `'auto' \| 'always' \| 'scroll' \| 'hover' \| 'never'` | `'auto'` | 스크롤바 표시 방식 |
| `dropdownMaxHeight` | `number` | - | 드롭다운 최대 높이 |
| `leftSection` | `ReactNode` | - | 왼쪽 섹션 |
| `rightSection` | `ReactNode` | - | 오른쪽 섹션 |
| `withinPortal` | `boolean` | `true` | 드롭다운을 Portal로 렌더링 여부 |
| `position` | `PopoverBaseProps['position']` | - | 드롭다운 위치 |
| `offset` | `number` | - | 드롭다운 오프셋 |
| `classes` | `{ wrapper?: string; input?: string; dropdown?: string; options?: string; option?: string }` | - | CSS 클래스 커스터마이징 |

### CustomType 타입

```typescript
type CustomType<T = string> = {
  key: string      // 고유 식별자
  value: T         // 실제 값
  label: string    // 표시 텍스트
}
```

## 사용 예시

### 기본 사용

```tsx
import { O_Autocomplete } from '@components/Autocomplete'

const data = [
  { key: '1', value: '홍길동', label: '홍길동' },
  { key: '2', value: '김철수', label: '김철수' },
  { key: '3', value: '이영희', label: '이영희' },
]

function Example() {
  return (
    <O_Autocomplete
      data={data}
      size="large"
      placeholder="이름을 입력해주세요"
      onItemSubmit={(item) => console.log('선택된 항목:', item)}
    />
  )
}
```

### 제네릭 타입 사용

```tsx
import { O_Autocomplete } from '@components/Autocomplete'

type User = {
  id: number
  name: string
  email: string
}

const data = [
  { key: '1', value: { id: 1, name: '홍길동', email: 'hong@example.com' }, label: '홍길동' },
  { key: '2', value: { id: 2, name: '김철수', email: 'kim@example.com' }, label: '김철수' },
]

function Example() {
  return (
    <O_Autocomplete<User>
      data={data}
      size="large"
      placeholder="사용자를 검색해주세요"
      onItemSubmit={(item) => {
        console.log('이메일:', item.value.email)
      }}
    />
  )
}
```

### 커스텀 아이템 렌더링

```tsx
import { O_Autocomplete } from '@components/Autocomplete'

const data = [
  { key: '1', value: '홍길동', label: '홍길동' },
  { key: '2', value: '김철수', label: '김철수' },
]

function Example() {
  return (
    <O_Autocomplete
      data={data}
      size="large"
      placeholder="이름을 입력해주세요"
      onItemSubmit={(item) => console.log(item)}
      ItemComponent={(item) => (
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, padding: '4px 8px' }}>
          <div
            style={{
              width: 28,
              height: 28,
              borderRadius: '50%',
              backgroundColor: '#4299e1',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: 'white',
              fontSize: 12,
            }}
          >
            {item.label[0]}
          </div>
          {item.label}
        </div>
      )}
    />
  )
}
```

### 검색 결과 없을 때 커스텀 UI

```tsx
import { O_Autocomplete } from '@components/Autocomplete'

function Example() {
  return (
    <O_Autocomplete
      data={[]}
      size="large"
      placeholder="검색어를 입력해주세요"
      onItemSubmit={() => {}}
      EmptyComponent={({ searchValue }) => (
        <div style={{ padding: '12px 16px', color: '#718096', textAlign: 'center' }}>
          "{searchValue}"에 대한 검색 결과가 없습니다
        </div>
      )}
    />
  )
}
```

### 선택 후 입력값 초기화

```tsx
import { O_Autocomplete } from '@components/Autocomplete'
import { useState } from 'react'

const data = [
  { key: '1', value: '항목1', label: '항목1' },
  { key: '2', value: '항목2', label: '항목2' },
]

function Example() {
  const [selected, setSelected] = useState<string[]>([])

  return (
    <div>
      <O_Autocomplete
        data={data}
        size="large"
        placeholder="항목을 추가해주세요"
        withEmptyValueOnOptionSubmit
        onItemSubmit={(item) => setSelected(prev => [...prev, item.label])}
      />
      <ul>
        {selected.map((item, i) => <li key={i}>{item}</li>)}
      </ul>
    </div>
  )
}
```
