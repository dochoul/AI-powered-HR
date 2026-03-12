# Stepper

숫자 증감 스테퍼 컴포넌트. Platform, Admin을 지원합니다 (Office 미지원).

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `P_Stepper` | Platform | `@components/Stepper` |
| `A_Stepper` | Admin | `@components/Stepper` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `value` | `number \| string` | - | 제어 컴포넌트 값 |
| `defaultValue` | `number \| string` | - | 비제어 초기값 |
| `onChange` | `(value: number \| string) => void` | - | 값 변경 핸들러 |
| `min` | `number` | - | 최솟값 |
| `max` | `number` | - | 최댓값 |
| `step` | `number` | `1` | 증감 단위 |
| `size` | `'small' \| 'large'` | `'large'` | 스테퍼 크기 |
| `textAlign` | `'center'` | - | 텍스트 정렬 |
| `width` | `number` | - | 입력 너비 (px) |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `allowDecimal` | `boolean` | `false` | 소수점 허용 여부 |

## 사용 예시

### 기본 사용

```tsx
import { P_Stepper } from '@components/Stepper'

function Example() {
  return <P_Stepper defaultValue={1} />
}
```

### 제어 컴포넌트

```tsx
import { P_Stepper } from '@components/Stepper'
import { useState } from 'react'

function Example() {
  const [count, setCount] = useState(1)

  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
      <P_Stepper
        value={count}
        onChange={(value) => setCount(Number(value))}
        min={1}
        max={10}
      />
      <span>선택 수량: {count}</span>
    </div>
  )
}
```

### 범위 및 단위 설정

```tsx
import { P_Stepper } from '@components/Stepper'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      {/* 1~100, 기본 step=1 */}
      <P_Stepper defaultValue={1} min={1} max={100} />

      {/* 0~1000, step=10 */}
      <P_Stepper defaultValue={100} min={0} max={1000} step={10} />
    </div>
  )
}
```

### 크기

```tsx
import { P_Stepper } from '@components/Stepper'

function Example() {
  return (
    <div style={{ display: 'flex', gap: 12 }}>
      <P_Stepper size="small" defaultValue={1} />
      <P_Stepper size="large" defaultValue={1} />
    </div>
  )
}
```

### 장바구니 수량 선택 예시

```tsx
import { P_Stepper } from '@components/Stepper'
import { useState } from 'react'

type CartItem = { id: number; name: string; qty: number }

function Example() {
  const [items, setItems] = useState<CartItem[]>([
    { id: 1, name: '상품 A', qty: 1 },
    { id: 2, name: '상품 B', qty: 2 },
  ])

  const updateQty = (id: number, qty: number) => {
    setItems(prev => prev.map(item => item.id === id ? { ...item, qty } : item))
  }

  return (
    <table>
      <thead>
        <tr>
          <th>상품명</th>
          <th>수량</th>
        </tr>
      </thead>
      <tbody>
        {items.map(item => (
          <tr key={item.id}>
            <td>{item.name}</td>
            <td>
              <P_Stepper
                value={item.qty}
                onChange={(val) => updateQty(item.id, Number(val))}
                min={1}
                max={99}
              />
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}
```
