# SearchForm

검색 폼 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_SearchForm` | Office | `@components/SearchForm` |
| `P_SearchForm` | Platform | `@components/SearchForm` |
| `A_SearchForm` | Admin | `@components/SearchForm` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `value` | `string` | - | 제어 컴포넌트 입력값 |
| `defaultValue` | `string` | - | 비제어 초기값 |
| `onChange` | `(value: string) => void` | - | 입력값 변경 핸들러 |
| `onSearch` | `(value: string) => void` | - | 검색 실행 핸들러 |
| `onReset` | `() => void` | - | 초기화 핸들러 |
| `placeholder` | `string` | - | 플레이스홀더 텍스트 |
| `size` | `'small' \| 'large'` | `'large'` | 입력 크기 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |

## 사용 예시

### 기본 사용

```tsx
import { O_SearchForm } from '@components/SearchForm'

function Example() {
  return (
    <O_SearchForm
      placeholder="검색어를 입력해주세요"
      onSearch={(value) => console.log('검색:', value)}
    />
  )
}
```

### 제어 컴포넌트

```tsx
import { O_SearchForm } from '@components/SearchForm'
import { useState } from 'react'

function Example() {
  const [query, setQuery] = useState('')

  const handleSearch = (value: string) => {
    console.log('검색 실행:', value)
    // API 호출 등
  }

  const handleReset = () => {
    setQuery('')
    // 검색 결과 초기화 등
  }

  return (
    <O_SearchForm
      value={query}
      onChange={setQuery}
      onSearch={handleSearch}
      onReset={handleReset}
      placeholder="이름, 이메일로 검색"
    />
  )
}
```

### 테이블과 함께 사용

```tsx
import { O_SearchForm } from '@components/SearchForm'
import { O_Table } from '@components/Table'
import { useState, useMemo } from 'react'

const allData = [
  { id: 1, name: '홍길동', email: 'hong@example.com' },
  { id: 2, name: '김철수', email: 'kim@example.com' },
  { id: 3, name: '이영희', email: 'lee@example.com' },
]

function Example() {
  const [query, setQuery] = useState('')

  const filteredData = useMemo(
    () => allData.filter(
      row =>
        row.name.includes(query) ||
        row.email.includes(query)
    ),
    [query]
  )

  return (
    <div>
      <div style={{ marginBottom: 12 }}>
        <O_SearchForm
          value={query}
          onChange={setQuery}
          onSearch={(v) => setQuery(v)}
          onReset={() => setQuery('')}
          placeholder="이름 또는 이메일 검색"
        />
      </div>

      <O_Table>
        <O_Table.Thead>
          <O_Table.Tr>
            <O_Table.Th w={60}>번호</O_Table.Th>
            <O_Table.Th w={150}>이름</O_Table.Th>
            <O_Table.Th>이메일</O_Table.Th>
          </O_Table.Tr>
        </O_Table.Thead>
        <O_Table.Tbody>
          {filteredData.length === 0 ? (
            <O_Table.Tr>
              <O_Table.Td colSpan={3} align="center">
                검색 결과가 없습니다
              </O_Table.Td>
            </O_Table.Tr>
          ) : (
            filteredData.map(row => (
              <O_Table.Tr key={row.id}>
                <O_Table.Td w={60} align="center">{row.id}</O_Table.Td>
                <O_Table.Td w={150}>{row.name}</O_Table.Td>
                <O_Table.Td>{row.email}</O_Table.Td>
              </O_Table.Tr>
            ))
          )}
        </O_Table.Tbody>
      </O_Table>
    </div>
  )
}
```

### 플랫폼별 사용

```tsx
import { O_SearchForm, P_SearchForm, A_SearchForm } from '@components/SearchForm'

function Example() {
  const handleSearch = (value: string) => console.log('검색:', value)

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      {/* Office */}
      <O_SearchForm onSearch={handleSearch} placeholder="Office 검색" />

      {/* Platform */}
      <P_SearchForm onSearch={handleSearch} placeholder="Platform 검색" />

      {/* Admin */}
      <A_SearchForm onSearch={handleSearch} placeholder="Admin 검색" />
    </div>
  )
}
```
