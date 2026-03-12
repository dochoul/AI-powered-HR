# TableDatePicker

테이블 셀 내에서 사용하는 날짜 선택 패턴 컴포넌트. Platform, Admin을 지원합니다 (Office 미지원).

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `P_TableDatePicker` | Platform | `@patterns/TableDatePicker` |
| `A_TableDatePicker` | Admin | `@patterns/TableDatePicker` |

## Props

DatePicker의 props와 동일하게 사용하며, 테이블 셀에 최적화된 스타일이 적용됩니다.

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `date` | `Date \| null` | - | 제어 컴포넌트 선택 날짜 |
| `initDate` | `Date \| null` | - | 비제어 초기 날짜 |
| `onChange` | `(date: Date \| null) => void` | - | 날짜 변경 핸들러 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `readOnly` | `boolean` | `false` | 읽기 전용 여부 |
| `minDate` | `Date \| null` | - | 최소 날짜 |
| `maxDate` | `Date \| null` | - | 최대 날짜 |
| `dateFormat` | `string` | `'yyyy-MM-dd'` | 날짜 표시 형식 |
| `error` | `ReactNode` | - | 에러 메시지 |

## 사용 예시

### 기본 사용

```tsx
import { P_TableDatePicker } from '@patterns/TableDatePicker'
import { P_Table } from '@components/Table'
import { useState } from 'react'

function Example() {
  const [date, setDate] = useState<Date | null>(null)

  return (
    <P_Table>
      <P_Table.Thead>
        <P_Table.Tr>
          <P_Table.Th>이름</P_Table.Th>
          <P_Table.Th>시작일</P_Table.Th>
        </P_Table.Tr>
      </P_Table.Thead>
      <P_Table.Tbody>
        <P_Table.Tr>
          <P_Table.Td>홍길동</P_Table.Td>
          <P_Table.Td>
            <P_TableDatePicker
              date={date}
              onChange={setDate}
            />
          </P_Table.Td>
        </P_Table.Tr>
      </P_Table.Tbody>
    </P_Table>
  )
}
```

### 편집 가능한 테이블

```tsx
import { P_TableDatePicker } from '@patterns/TableDatePicker'
import { P_Table } from '@components/Table'
import { useState } from 'react'

type Row = { id: number; name: string; startDate: Date | null; endDate: Date | null }

function Example() {
  const [rows, setRows] = useState<Row[]>([
    { id: 1, name: '프로젝트 A', startDate: null, endDate: null },
    { id: 2, name: '프로젝트 B', startDate: new Date(), endDate: null },
  ])

  const updateDate = (id: number, field: 'startDate' | 'endDate', date: Date | null) => {
    setRows(prev => prev.map(row => row.id === id ? { ...row, [field]: date } : row))
  }

  return (
    <P_Table>
      <P_Table.Thead>
        <P_Table.Tr>
          <P_Table.Th>프로젝트명</P_Table.Th>
          <P_Table.Th>시작일</P_Table.Th>
          <P_Table.Th>종료일</P_Table.Th>
        </P_Table.Tr>
      </P_Table.Thead>
      <P_Table.Tbody>
        {rows.map(row => (
          <P_Table.Tr key={row.id}>
            <P_Table.Td>{row.name}</P_Table.Td>
            <P_Table.Td>
              <P_TableDatePicker
                date={row.startDate}
                onChange={(date) => updateDate(row.id, 'startDate', date)}
                maxDate={row.endDate}
              />
            </P_Table.Td>
            <P_Table.Td>
              <P_TableDatePicker
                date={row.endDate}
                onChange={(date) => updateDate(row.id, 'endDate', date)}
                minDate={row.startDate}
              />
            </P_Table.Td>
          </P_Table.Tr>
        ))}
      </P_Table.Tbody>
    </P_Table>
  )
}
```
