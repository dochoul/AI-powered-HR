# Pagination

페이지네이션 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Pagination` | Office | `@components/Pagination` |
| `P_Pagination` | Platform | `@components/Pagination` |
| `A_Pagination` | Admin | `@components/Pagination` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `total` | `number` | - | 전체 페이지 수 (필수) |
| `onChange` | `(page: number) => void` | - | 페이지 변경 핸들러 (필수) |
| `page` | `number` | - | 제어 컴포넌트 현재 페이지 |
| `defaultValue` | `number` | `1` | 비제어 초기 페이지 |
| `pageCountPerSet` | `number` | `10` | 한 번에 표시할 페이지 버튼 수 |
| `withEdges` | `boolean` | `true` | 처음/마지막 페이지 버튼 표시 여부 |
| `withControls` | `boolean` | `true` | 이전/다음 페이지 버튼 표시 여부 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `isHideAtOneSet` | `boolean` | `false` | 한 세트(pageCountPerSet 이하)일 때 숨김 여부 |

## 사용 예시

### 기본 사용

```tsx
import { O_Pagination } from '@components/Pagination'
import { useState } from 'react'

function Example() {
  const [page, setPage] = useState(1)

  return (
    <O_Pagination
      total={20}
      page={page}
      onChange={setPage}
    />
  )
}
```

### 다양한 버튼 조합

```tsx
import { O_Pagination } from '@components/Pagination'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      {/* 모든 버튼 (기본) */}
      <O_Pagination defaultValue={3} total={20} onChange={() => {}} />

      {/* edges 버튼 없음 */}
      <O_Pagination defaultValue={3} total={20} withEdges={false} onChange={() => {}} />

      {/* controls 버튼 없음 */}
      <O_Pagination defaultValue={3} total={20} withControls={false} onChange={() => {}} />

      {/* 버튼 없음 (숫자만) */}
      <O_Pagination
        defaultValue={3}
        total={20}
        withEdges={false}
        withControls={false}
        onChange={() => {}}
      />
    </div>
  )
}
```

### 세트당 페이지 수 조절

```tsx
import { O_Pagination } from '@components/Pagination'

function Example() {
  return (
    // 한 번에 5개 페이지 버튼만 표시
    <O_Pagination
      total={50}
      pageCountPerSet={5}
      defaultValue={1}
      onChange={(page) => console.log('현재 페이지:', page)}
    />
  )
}
```

### 한 세트일 때 숨기기

```tsx
import { O_Pagination } from '@components/Pagination'

function Example({ items }: { items: any[] }) {
  const totalPages = Math.ceil(items.length / 10)

  return (
    <div>
      {/* 아이템 목록 */}
      <ul>
        {items.map((item, i) => <li key={i}>{item}</li>)}
      </ul>

      {/* 총 페이지가 pageCountPerSet 이하면 숨김 */}
      <O_Pagination
        total={totalPages}
        isHideAtOneSet
        onChange={(page) => console.log(page)}
      />
    </div>
  )
}
```

### 비활성화

```tsx
import { O_Pagination } from '@components/Pagination'

function Example() {
  return (
    <O_Pagination
      total={10}
      defaultValue={3}
      disabled
      onChange={() => {}}
    />
  )
}
```

### 테이블과 함께 사용

```tsx
import { O_Pagination } from '@components/Pagination'
import { O_Table } from '@components/Table'
import { useState } from 'react'

const PAGE_SIZE = 10

function Example({ data }: { data: any[] }) {
  const [page, setPage] = useState(1)
  const totalPages = Math.ceil(data.length / PAGE_SIZE)
  const pageData = data.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE)

  return (
    <div>
      <O_Table>
        <O_Table.Thead>
          <O_Table.Tr>
            <O_Table.Th>이름</O_Table.Th>
            <O_Table.Th>이메일</O_Table.Th>
          </O_Table.Tr>
        </O_Table.Thead>
        <O_Table.Tbody>
          {pageData.map((row, i) => (
            <O_Table.Tr key={i}>
              <O_Table.Td>{row.name}</O_Table.Td>
              <O_Table.Td>{row.email}</O_Table.Td>
            </O_Table.Tr>
          ))}
        </O_Table.Tbody>
      </O_Table>

      <O_Pagination
        total={totalPages}
        page={page}
        onChange={setPage}
      />
    </div>
  )
}
```
