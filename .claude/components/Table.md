# Table

테이블 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Table` | Office | `@components/Table` |
| `P_Table` | Platform | `@components/Table` |
| `A_Table` | Admin | `@components/Table` |

## 서브 컴포넌트 구조

- `Table` - 최상위 컨테이너
- `Table.Thead` - 헤더 영역
- `Table.Tbody` - 바디 영역
- `Table.Tr` - 행 (Table Row)
- `Table.Th` - 헤더 셀 (Table Header)
- `Table.Td` - 데이터 셀 (Table Data)

## Props

### Table Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `type` | `'vertical' \| 'horizontal'` | `'vertical'` | 테이블 레이아웃 방향 |
| `size` | `'small' \| 'large'` | `'large'` | 셀 크기 |
| `narrowMode` | `boolean` | `false` | 좁은 모드 (compact) |
| `tbodyScrollHeight` | `number \| string` | - | tbody 스크롤 높이 |
| `className` | `string` | - | 추가 CSS 클래스 |

### Table.Th Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `w` | `number \| string` | - | 열 너비 |
| `isMultiLine` | `boolean` | `false` | 여러 줄 표시 여부 |
| `align` | `'left' \| 'center' \| 'right'` | `'center'` | 텍스트 정렬 |
| `sortable` | `boolean` | `false` | 정렬 가능 여부 |
| `sortOrder` | `'asc' \| 'desc' \| null` | - | 현재 정렬 순서 |
| `onSort` | `() => void` | - | 정렬 클릭 핸들러 |

### Table.Td Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `w` | `number \| string` | - | 열 너비 |
| `align` | `'left' \| 'center' \| 'right'` | `'left'` | 텍스트 정렬 |

## useTableSortParams Hook

정렬 상태를 관리하는 유틸리티 훅.

```typescript
const { sortParams, handleSort } = useTableSortParams()
```

## 사용 예시

### 기본 테이블

```tsx
import { O_Table } from '@components/Table'

function Example() {
  return (
    <O_Table>
      <O_Table.Thead>
        <O_Table.Tr>
          <O_Table.Th w={100}>번호</O_Table.Th>
          <O_Table.Th w={200}>이름</O_Table.Th>
          <O_Table.Th>이메일</O_Table.Th>
          <O_Table.Th w={120}>상태</O_Table.Th>
        </O_Table.Tr>
      </O_Table.Thead>
      <O_Table.Tbody>
        {[
          { id: 1, name: '홍길동', email: 'hong@example.com', status: '활성' },
          { id: 2, name: '김철수', email: 'kim@example.com', status: '비활성' },
        ].map((row) => (
          <O_Table.Tr key={row.id}>
            <O_Table.Td w={100} align="center">{row.id}</O_Table.Td>
            <O_Table.Td w={200}>{row.name}</O_Table.Td>
            <O_Table.Td>{row.email}</O_Table.Td>
            <O_Table.Td w={120} align="center">{row.status}</O_Table.Td>
          </O_Table.Tr>
        ))}
      </O_Table.Tbody>
    </O_Table>
  )
}
```

### 다중 라인 헤더

```tsx
import { O_Table } from '@components/Table'

function Example() {
  return (
    <O_Table>
      <O_Table.Thead>
        <O_Table.Tr>
          <O_Table.Th w={100}>번호</O_Table.Th>
          <O_Table.Th w={300} isMultiLine>
            헤더가 두 줄일 경우<br />isMultiLine props을 추가해야 합니다
          </O_Table.Th>
          <O_Table.Th>내용</O_Table.Th>
        </O_Table.Tr>
      </O_Table.Thead>
      <O_Table.Tbody>
        <O_Table.Tr>
          <O_Table.Td w={100}>1</O_Table.Td>
          <O_Table.Td w={300}>데이터</O_Table.Td>
          <O_Table.Td>내용</O_Table.Td>
        </O_Table.Tr>
      </O_Table.Tbody>
    </O_Table>
  )
}
```

### 스크롤 테이블

```tsx
import { O_Table } from '@components/Table'

function Example() {
  return (
    <O_Table tbodyScrollHeight={300}>
      <O_Table.Thead>
        <O_Table.Tr>
          <O_Table.Th>이름</O_Table.Th>
          <O_Table.Th>이메일</O_Table.Th>
        </O_Table.Tr>
      </O_Table.Thead>
      <O_Table.Tbody>
        {Array.from({ length: 30 }, (_, i) => (
          <O_Table.Tr key={i}>
            <O_Table.Td>사용자 {i + 1}</O_Table.Td>
            <O_Table.Td>user{i + 1}@example.com</O_Table.Td>
          </O_Table.Tr>
        ))}
      </O_Table.Tbody>
    </O_Table>
  )
}
```

### 정렬 기능

```tsx
import { O_Table, useTableSortParams } from '@components/Table'

const data = [
  { name: '홍길동', age: 30 },
  { name: '김철수', age: 25 },
  { name: '이영희', age: 28 },
]

function Example() {
  const { sortParams, handleSort } = useTableSortParams()

  const sortedData = [...data].sort((a, b) => {
    if (!sortParams.field) return 0
    const aVal = a[sortParams.field as keyof typeof a]
    const bVal = b[sortParams.field as keyof typeof b]
    if (sortParams.order === 'asc') return aVal > bVal ? 1 : -1
    return aVal < bVal ? 1 : -1
  })

  return (
    <O_Table>
      <O_Table.Thead>
        <O_Table.Tr>
          <O_Table.Th
            sortable
            sortOrder={sortParams.field === 'name' ? sortParams.order : null}
            onSort={() => handleSort('name')}
          >
            이름
          </O_Table.Th>
          <O_Table.Th
            sortable
            sortOrder={sortParams.field === 'age' ? sortParams.order : null}
            onSort={() => handleSort('age')}
          >
            나이
          </O_Table.Th>
        </O_Table.Tr>
      </O_Table.Thead>
      <O_Table.Tbody>
        {sortedData.map((row, i) => (
          <O_Table.Tr key={i}>
            <O_Table.Td>{row.name}</O_Table.Td>
            <O_Table.Td>{row.age}</O_Table.Td>
          </O_Table.Tr>
        ))}
      </O_Table.Tbody>
    </O_Table>
  )
}
```

### 수평 테이블

```tsx
import { O_Table } from '@components/Table'

function Example() {
  return (
    <O_Table type="horizontal">
      <O_Table.Tbody>
        <O_Table.Tr>
          <O_Table.Th w={120}>이름</O_Table.Th>
          <O_Table.Td>홍길동</O_Table.Td>
          <O_Table.Th w={120}>이메일</O_Table.Th>
          <O_Table.Td>hong@example.com</O_Table.Td>
        </O_Table.Tr>
        <O_Table.Tr>
          <O_Table.Th w={120}>부서</O_Table.Th>
          <O_Table.Td>개발팀</O_Table.Td>
          <O_Table.Th w={120}>직책</O_Table.Th>
          <O_Table.Td>시니어 개발자</O_Table.Td>
        </O_Table.Tr>
      </O_Table.Tbody>
    </O_Table>
  )
}
```
