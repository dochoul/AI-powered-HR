# Tooltip

툴팁 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Tooltip` | Office | `@components/Tooltip` |
| `P_Tooltip` | Platform | `@components/Tooltip` |
| `A_Tooltip` | Admin | `@components/Tooltip` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `label` | `ReactNode` | - | 툴팁 내용 (필수) |
| `children` | `ReactNode` | - | 툴팁 트리거 요소 |
| `position` | `'top' \| 'bottom' \| 'left' \| 'right' \| ...` | `'top'` | 툴팁 위치 |
| `offset` | `number` | - | 오프셋 (px) |
| `openDelay` | `number` | - | 열림 지연 시간 (ms) |
| `closeDelay` | `number` | - | 닫힘 지연 시간 (ms) |
| `opened` | `boolean` | - | 제어 컴포넌트 열림 상태 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `multiline` | `boolean` | `false` | 여러 줄 표시 여부 |
| `width` | `number` | - | 툴팁 너비 |
| `maxWidth` | `number` | - | 툴팁 최대 너비 |
| `inline` | `boolean` | `false` | 인라인 표시 여부 |
| `withinPortal` | `boolean` | `true` | Portal로 렌더링 여부 |
| `events` | `{ hover?: boolean; focus?: boolean; touch?: boolean }` | - | 이벤트 트리거 설정 |

## 사용 예시

### 기본 사용

```tsx
import { O_Tooltip } from '@components/Tooltip'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <O_Tooltip label="툴팁 메시지입니다">
      <O_Button>마우스를 올려보세요</O_Button>
    </O_Tooltip>
  )
}
```

### 다양한 위치

```tsx
import { O_Tooltip } from '@components/Tooltip'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <div style={{ display: 'flex', gap: 16 }}>
      <O_Tooltip label="위" position="top">
        <O_Button>위</O_Button>
      </O_Tooltip>

      <O_Tooltip label="아래" position="bottom">
        <O_Button>아래</O_Button>
      </O_Tooltip>

      <O_Tooltip label="왼쪽" position="left">
        <O_Button>왼쪽</O_Button>
      </O_Tooltip>

      <O_Tooltip label="오른쪽" position="right">
        <O_Button>오른쪽</O_Button>
      </O_Tooltip>
    </div>
  )
}
```

### 여러 줄 툴팁

```tsx
import { O_Tooltip } from '@components/Tooltip'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <O_Tooltip
      label="이것은 긴 설명 텍스트입니다. 여러 줄에 걸쳐 표시될 수 있습니다."
      multiline
      width={200}
    >
      <O_Button>긴 툴팁</O_Button>
    </O_Tooltip>
  )
}
```

### 지연 시간 설정

```tsx
import { O_Tooltip } from '@components/Tooltip'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <O_Tooltip
      label="0.5초 후 표시됩니다"
      openDelay={500}
      closeDelay={200}
    >
      <O_Button>지연 툴팁</O_Button>
    </O_Tooltip>
  )
}
```

### 제어 컴포넌트 (항상 표시)

```tsx
import { O_Tooltip } from '@components/Tooltip'
import { O_Button } from '@components/Buttons'
import { useState } from 'react'

function Example() {
  const [show, setShow] = useState(false)

  return (
    <div>
      <O_Button onClick={() => setShow(!show)}>
        툴팁 {show ? '숨기기' : '보이기'}
      </O_Button>

      <O_Tooltip label="제어되는 툴팁입니다" opened={show}>
        <span style={{ marginLeft: 12 }}>이 요소에 툴팁이 표시됩니다</span>
      </O_Tooltip>
    </div>
  )
}
```

### 아이콘에 툴팁

```tsx
import { O_Tooltip } from '@components/Tooltip'
import { O_IconButton } from '@components/Buttons'
import { InfoCircleIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
      <span>항목 이름</span>
      <O_Tooltip label="항목에 대한 도움말입니다">
        <O_IconButton variant="ghost" size="x-small">
          <InfoCircleIcon />
        </O_IconButton>
      </O_Tooltip>
    </div>
  )
}
```
