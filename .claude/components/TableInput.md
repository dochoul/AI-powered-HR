# TableInput

테이블 셀 내에서 사용하는 텍스트 입력 패턴 컴포넌트. Platform, Admin을 지원합니다 (Office 미지원).

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `P_TableInput` | Platform | `@patterns/TableInput` |
| `A_TableInput` | Admin | `@patterns/TableInput` |

## Props

TextInput의 props와 동일하게 사용하며, 테이블 셀에 최적화된 스타일이 적용됩니다.

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `value` | `string` | - | 제어 컴포넌트 값 |
| `defaultValue` | `string` | - | 비제어 초기값 |
| `onChange` | `(e: ChangeEvent<HTMLInputElement>) => void` | - | 값 변경 핸들러 |
| `placeholder` | `string` | - | 플레이스홀더 텍스트 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `readOnly` | `boolean` | `false` | 읽기 전용 여부 |
| `error` | `ReactNode` | - | 에러 메시지 |

## 사용 예시

### 기본 사용

```tsx
import { P_TableInput } from '@patterns/TableInput'
import { P_Table } from '@components/Table'
import { useState } from 'react'

function Example() {
  const [value, setValue] = useState('')

  return (
    <P_Table>
      <P_Table.Thead>
        <P_Table.Tr>
          <P_Table.Th>이름</P_Table.Th>
          <P_Table.Th>메모</P_Table.Th>
        </P_Table.Tr>
      </P_Table.Thead>
      <P_Table.Tbody>
        <P_Table.Tr>
          <P_Table.Td>홍길동</P_Table.Td>
          <P_Table.Td>
            <P_TableInput
              value={value}
              onChange={(e) => setValue(e.target.value)}
              placeholder="메모를 입력해주세요"
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
import { P_TableInput } from '@patterns/TableInput'
import { P_Table } from '@components/Table'
import { useState } from 'react'

type Row = { id: number; name: string; email: string; phone: string }

function Example() {
  const [rows, setRows] = useState<Row[]>([
    { id: 1, name: '홍길동', email: 'hong@example.com', phone: '010-1234-5678' },
    { id: 2, name: '김철수', email: 'kim@example.com', phone: '010-9876-5432' },
  ])

  const updateRow = (id: number, field: keyof Row, value: string) => {
    setRows(prev => prev.map(row => row.id === id ? { ...row, [field]: value } : row))
  }

  return (
    <P_Table>
      <P_Table.Thead>
        <P_Table.Tr>
          <P_Table.Th w={150}>이름</P_Table.Th>
          <P_Table.Th w={200}>이메일</P_Table.Th>
          <P_Table.Th w={150}>연락처</P_Table.Th>
        </P_Table.Tr>
      </P_Table.Thead>
      <P_Table.Tbody>
        {rows.map(row => (
          <P_Table.Tr key={row.id}>
            <P_Table.Td w={150}>
              <P_TableInput
                value={row.name}
                onChange={(e) => updateRow(row.id, 'name', e.target.value)}
              />
            </P_Table.Td>
            <P_Table.Td w={200}>
              <P_TableInput
                value={row.email}
                onChange={(e) => updateRow(row.id, 'email', e.target.value)}
              />
            </P_Table.Td>
            <P_Table.Td w={150}>
              <P_TableInput
                value={row.phone}
                onChange={(e) => updateRow(row.id, 'phone', e.target.value)}
              />
            </P_Table.Td>
          </P_Table.Tr>
        ))}
      </P_Table.Tbody>
    </P_Table>
  )
}
```

### 읽기 전용 모드와 편집 전환

```tsx
import { P_TableInput } from '@patterns/TableInput'
import { P_Table } from '@components/Table'
import { P_Button } from '@components/Buttons'
import { useState } from 'react'

type Row = { id: number; name: string }

function Example() {
  const [rows, setRows] = useState<Row[]>([
    { id: 1, name: '홍길동' },
    { id: 2, name: '김철수' },
  ])
  const [editingId, setEditingId] = useState<number | null>(null)

  return (
    <P_Table>
      <P_Table.Thead>
        <P_Table.Tr>
          <P_Table.Th>이름</P_Table.Th>
          <P_Table.Th w={100}>작업</P_Table.Th>
        </P_Table.Tr>
      </P_Table.Thead>
      <P_Table.Tbody>
        {rows.map(row => (
          <P_Table.Tr key={row.id}>
            <P_Table.Td>
              {editingId === row.id ? (
                <P_TableInput
                  value={row.name}
                  onChange={(e) =>
                    setRows(prev =>
                      prev.map(r => r.id === row.id ? { ...r, name: e.target.value } : r)
                    )
                  }
                />
              ) : (
                row.name
              )}
            </P_Table.Td>
            <P_Table.Td w={100}>
              {editingId === row.id ? (
                <P_Button size="small" onClick={() => setEditingId(null)}>완료</P_Button>
              ) : (
                <P_Button size="small" variant="outline" onClick={() => setEditingId(row.id)}>
                  수정
                </P_Button>
              )}
            </P_Table.Td>
          </P_Table.Tr>
        ))}
      </P_Table.Tbody>
    </P_Table>
  )
}
```
