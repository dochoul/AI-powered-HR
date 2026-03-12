# DateRangePicker

날짜 범위 선택 컴포넌트. 시작일과 종료일을 하나의 컴포넌트에서 선택합니다. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_DateRangePicker` | Office | `@components/DateRangePicker` |
| `P_DateRangePicker` | Platform | `@components/DateRangePicker` |
| `A_DateRangePicker` | Admin | `@components/DateRangePicker` |

## Props

### 공통 Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `startDate` | `Date \| null` | - | 제어 컴포넌트 시작 날짜 |
| `endDate` | `Date \| null` | - | 제어 컴포넌트 종료 날짜 |
| `initStartDate` | `Date \| null` | - | 비제어 초기 시작 날짜 |
| `initEndDate` | `Date \| null` | - | 비제어 초기 종료 날짜 |
| `onChange` | `(dates: [Date \| null, Date \| null]) => void` | - | 날짜 범위 변경 핸들러 |
| `size` | `'small' \| 'large'` | `'large'` | 입력 크기 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `readOnly` | `boolean` | `false` | 읽기 전용 여부 |
| `error` | `ReactNode` | - | 에러 메시지 |
| `minDate` | `Date \| null` | - | 선택 가능 최소 날짜 |
| `maxDate` | `Date \| null` | - | 선택 가능 최대 날짜 |
| `excludeDates` | `Date[]` | - | 선택 불가 날짜 목록 |
| `dateFormat` | `string` | `'yyyy-MM-dd'` | 날짜 표시 형식 |
| `isKorean` | `boolean` | `false` | 한국어 표시 여부 |
| `closeOnScroll` | `boolean` | `false` | 스크롤 시 달력 닫기 여부 |

### P_DateRangePicker (추가 Props)

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `variant` | `'default' \| 'essential'` | `'default'` | 입력 스타일 |

## 사용 예시

### 기본 사용

```tsx
import { O_DateRangePicker } from '@components/DateRangePicker'

function Example() {
  return (
    <O_DateRangePicker
      onChange={([start, end]) => {
        console.log('시작:', start)
        console.log('종료:', end)
      }}
    />
  )
}
```

### 제어 컴포넌트

```tsx
import { O_DateRangePicker } from '@components/DateRangePicker'
import { useState } from 'react'

function Example() {
  const [startDate, setStartDate] = useState<Date | null>(null)
  const [endDate, setEndDate] = useState<Date | null>(null)

  return (
    <div>
      <O_DateRangePicker
        startDate={startDate}
        endDate={endDate}
        onChange={([start, end]) => {
          setStartDate(start)
          setEndDate(end)
        }}
      />
      {startDate && endDate && (
        <p>
          선택 기간: {startDate.toLocaleDateString()} ~ {endDate.toLocaleDateString()}
        </p>
      )}
    </div>
  )
}
```

### 초기값 설정

```tsx
import { O_DateRangePicker } from '@components/DateRangePicker'

function Example() {
  return (
    <O_DateRangePicker
      initStartDate={new Date('2024-01-01')}
      initEndDate={new Date('2024-12-31')}
      onChange={([start, end]) => console.log(start, end)}
    />
  )
}
```

### 날짜 범위 제한

```tsx
import { O_DateRangePicker } from '@components/DateRangePicker'

function Example() {
  return (
    <O_DateRangePicker
      minDate={new Date()}
      maxDate={new Date(Date.now() + 30 * 24 * 60 * 60 * 1000)} // 30일 후
      onChange={([start, end]) => console.log(start, end)}
    />
  )
}
```

### Platform - Essential Variant

```tsx
import { P_DateRangePicker } from '@components/DateRangePicker'

function Example() {
  return (
    <P_DateRangePicker
      variant="essential"
      onChange={([start, end]) => console.log(start, end)}
    />
  )
}
```
