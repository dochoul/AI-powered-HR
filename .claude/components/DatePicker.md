# DatePicker

날짜 선택 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_DatePicker` | Office | `@components/DatePicker` |
| `P_DatePicker` | Platform | `@components/DatePicker` |
| `A_DatePicker` | Admin | `@components/DatePicker` |

## Props

### 공통 Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `date` | `Date \| null` | - | 제어 컴포넌트 선택 날짜 |
| `initDate` | `Date \| null` | - | 비제어 초기 날짜 |
| `onChange` | `(date: Date \| null) => void` | - | 날짜 변경 핸들러 |
| `size` | `'small' \| 'large'` | `'large'` | 입력 크기 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `readOnly` | `boolean` | `false` | 읽기 전용 여부 |
| `error` | `ReactNode` | - | 에러 메시지 |
| `placeholder` | `string` | - | 플레이스홀더 텍스트 |
| `placeholderText` | `string` | - | 플레이스홀더 텍스트 (별칭) |
| `minDate` | `Date \| null` | - | 선택 가능 최소 날짜 |
| `maxDate` | `Date \| null` | - | 선택 가능 최대 날짜 |
| `excludeDates` | `Date[]` | - | 선택 불가 날짜 목록 |
| `excludeDateIntervals` | `{ start: Date; end: Date }[]` | - | 선택 불가 날짜 구간 |
| `dateFormat` | `string` | `'yyyy-MM-dd'` | 날짜 표시 형식 |
| `level` | `'year' \| 'month' \| 'day'` | `'day'` | 선택 단위 |
| `showYearPicker` | `boolean` | `false` | 연도 선택만 표시 |
| `showMonthYearPicker` | `boolean` | `false` | 월/연도 선택 표시 |
| `showFourColumnMonthYearPicker` | `boolean` | `false` | 4열 월 선택 표시 |
| `isKorean` | `boolean` | `false` | 한국어 표시 여부 |
| `useRawInput` | `boolean` | `false` | 직접 입력 허용 여부 |
| `useDeselect` | `boolean` | `false` | 날짜 선택 해제 허용 여부 |
| `inline` | `boolean` | `false` | 인라인 달력 표시 여부 |
| `multiple` | `boolean` | `false` | 다중 날짜 선택 여부 |
| `dates` | `Date[]` | - | 다중 선택 날짜 배열 (제어) |
| `initDates` | `Date[]` | - | 다중 선택 초기 날짜 배열 (비제어) |
| `onChangeDates` | `(dates: Date[]) => void` | - | 다중 선택 변경 핸들러 |
| `closeOnScroll` | `boolean` | `false` | 스크롤 시 달력 닫기 여부 |
| `portalId` | `string` | - | 렌더링할 Portal 대상 ID |
| `width` | `string` | - | 입력 너비 |

### P_DatePicker (추가 Props)

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `variant` | `'default' \| 'essential'` | `'default'` | 입력 스타일 |

## 사용 예시

### 기본 사용

```tsx
import { O_DatePicker } from '@components/DatePicker'

function Example() {
  return <O_DatePicker onChange={(date) => console.log(date)} />
}
```

### 제어 컴포넌트

```tsx
import { O_DatePicker } from '@components/DatePicker'
import { useState } from 'react'

function Example() {
  const [date, setDate] = useState<Date | null>(new Date())

  return (
    <O_DatePicker
      date={date}
      onChange={setDate}
    />
  )
}
```

### 날짜 범위 설정 (시작일~종료일 연동)

```tsx
import { O_DatePicker } from '@components/DatePicker'
import { useState } from 'react'

function Example() {
  const [startDate, setStartDate] = useState<Date | null>(new Date('2024-01-01'))
  const [endDate, setEndDate] = useState<Date | null>(new Date('2024-12-31'))

  return (
    <div style={{ display: 'flex', gap: 4, alignItems: 'center' }}>
      <O_DatePicker
        initDate={startDate}
        onChange={(date) => setStartDate(date)}
        maxDate={endDate}
      />
      ~
      <O_DatePicker
        initDate={endDate}
        onChange={(date) => setEndDate(date)}
        minDate={startDate}
      />
    </div>
  )
}
```

### 연도/월 선택 모드

```tsx
import { O_DatePicker } from '@components/DatePicker'

function Example() {
  return (
    <div style={{ display: 'flex', gap: 12 }}>
      {/* 연도만 선택 */}
      <O_DatePicker
        showYearPicker
        dateFormat="yyyy"
        onChange={(date) => console.log(date)}
      />

      {/* 월+연도 선택 */}
      <O_DatePicker
        showMonthYearPicker
        dateFormat="yyyy-MM"
        onChange={(date) => console.log(date)}
      />
    </div>
  )
}
```

### 선택 불가 날짜

```tsx
import { O_DatePicker } from '@components/DatePicker'

function Example() {
  const excludeDates = [
    new Date('2024-12-25'),
    new Date('2024-01-01'),
  ]

  const excludeIntervals = [
    { start: new Date('2024-07-01'), end: new Date('2024-07-07') },
  ]

  return (
    <O_DatePicker
      excludeDates={excludeDates}
      excludeDateIntervals={excludeIntervals}
      onChange={(date) => console.log(date)}
    />
  )
}
```

### 다중 날짜 선택

```tsx
import { O_DatePicker } from '@components/DatePicker'
import { useState } from 'react'

function Example() {
  const [dates, setDates] = useState<Date[]>([])

  return (
    <div>
      <O_DatePicker
        multiple
        dates={dates}
        onChangeDates={setDates}
      />
      <p>선택된 날짜: {dates.length}개</p>
    </div>
  )
}
```

### 인라인 달력

```tsx
import { O_DatePicker } from '@components/DatePicker'

function Example() {
  return (
    <O_DatePicker
      inline
      onChange={(date) => console.log(date)}
    />
  )
}
```

### 한국어 / 직접 입력

```tsx
import { O_DatePicker } from '@components/DatePicker'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      <O_DatePicker isKorean onChange={(date) => console.log(date)} />
      <O_DatePicker useRawInput onChange={(date) => console.log(date)} />
    </div>
  )
}
```

### Platform - Essential Variant

```tsx
import { P_DatePicker } from '@components/DatePicker'

function Example() {
  return (
    <P_DatePicker
      variant="essential"
      onChange={(date) => console.log(date)}
    />
  )
}
```
