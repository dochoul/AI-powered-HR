# Banner

알림 배너 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Banner` | Office | `@components/Banner` |
| `P_Banner` | Platform | `@components/Banner` |
| `A_Banner` | Admin | `@components/Banner` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `message` | `string \| ReactNode` | - | 배너 메시지 |
| `icon` | `ReactNode` | - | 아이콘 |
| `withCloseButton` | `boolean` | `true` | 닫기 버튼 표시 여부 |
| `onClose` | `() => void` | - | 닫기 클릭 핸들러 |
| `align` | `'center' \| 'left'` | `'center'` | 메시지 정렬 |
| `variant` | `'gray' \| 'white'` | `'gray'` | 배너 배경 스타일 |
| `hideCheckboxId` | `string` | - | "오늘 하루 보지 않기" 체크박스 ID (localStorage 키로 사용) |
| `children` | `ReactNode` | - | 추가 내용 |

## 사용 예시

### 기본 사용

```tsx
import { O_Banner } from '@components/Banner'
import { InfoCircleIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <O_Banner
      icon={<InfoCircleIcon width={18} fill="#e38c46" />}
      message="공지사항 배너 메시지입니다."
      withCloseButton
    />
  )
}
```

### 다양한 정렬 / Variant

```tsx
import { O_Banner } from '@components/Banner'
import { InfoCircleIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 20 }}>
      {/* 중앙 정렬 (기본) */}
      <O_Banner
        icon={<InfoCircleIcon width={18} fill="#e38c46" />}
        message="중앙 정렬 배너입니다."
        withCloseButton
      />

      {/* 왼쪽 정렬 */}
      <O_Banner
        icon={<InfoCircleIcon width={18} fill="#e38c46" />}
        align="left"
        message="왼쪽 정렬 배너입니다."
        withCloseButton
      />

      {/* 흰색 배경 */}
      <O_Banner
        icon={<InfoCircleIcon width={18} fill="#e38c46" />}
        message="흰색 배경 배너입니다."
        variant="white"
        withCloseButton
      />

      {/* 닫기 버튼 없음 */}
      <O_Banner
        icon={<InfoCircleIcon width={18} fill="#e38c46" />}
        message="닫기 버튼이 없는 배너입니다."
        withCloseButton={false}
      />
    </div>
  )
}
```

### 닫기 이벤트 처리

```tsx
import { O_Banner } from '@components/Banner'
import { InfoCircleIcon } from 'hiworks-icons/react/solid/16'
import { useState } from 'react'

function Example() {
  const [visible, setVisible] = useState(true)

  if (!visible) return null

  return (
    <O_Banner
      icon={<InfoCircleIcon width={18} fill="#e38c46" />}
      message="공지사항: 시스템 점검이 예정되어 있습니다."
      withCloseButton
      onClose={() => setVisible(false)}
    />
  )
}
```

### "오늘 하루 보지 않기" 기능

```tsx
import { O_Banner } from '@components/Banner'
import { InfoCircleIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <O_Banner
      icon={<InfoCircleIcon width={18} fill="#e38c46" />}
      message="중요 공지사항입니다."
      withCloseButton
      hideCheckboxId="announcement-banner-2024"
      // localStorage에 'announcement-banner-2024' 키로 저장됩니다
    />
  )
}
```

### 커스텀 내용 포함

```tsx
import { O_Banner } from '@components/Banner'
import { InfoCircleIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <O_Banner
      icon={<InfoCircleIcon width={18} fill="#e38c46" />}
      message={
        <span>
          정기 점검이 예정되어 있습니다.{' '}
          <a href="/notice" style={{ color: '#3182ce' }}>
            자세히 보기
          </a>
        </span>
      }
      withCloseButton
    />
  )
}
```
