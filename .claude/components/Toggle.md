# Toggle

토글 스위치 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Toggle` | Office | `@components/Toggle` |
| `P_Toggle` | Platform | `@components/Toggle` |
| `A_Toggle` | Admin | `@components/Toggle` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `checked` | `boolean` | - | 제어 컴포넌트 체크 상태 |
| `defaultChecked` | `boolean` | - | 비제어 초기 체크 상태 |
| `onChange` | `(e: ChangeEvent<HTMLInputElement>) => void` | - | 상태 변경 핸들러 |
| `label` | `ReactNode` | - | 라벨 텍스트 |
| `size` | `'regular' \| 'small' \| 'x-small'` | `'regular'` | 토글 크기 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `className` | `string` | - | 추가 CSS 클래스 |

## 사용 예시

### 기본 사용

```tsx
import { O_Toggle } from '@components/Toggle'

function Example() {
  return <O_Toggle label="알림 허용" />
}
```

### 제어 컴포넌트

```tsx
import { O_Toggle } from '@components/Toggle'
import { useState } from 'react'

function Example() {
  const [enabled, setEnabled] = useState(false)

  return (
    <O_Toggle
      checked={enabled}
      onChange={(e) => setEnabled(e.currentTarget.checked)}
      label={enabled ? '활성화됨' : '비활성화됨'}
    />
  )
}
```

### 크기

```tsx
import { O_Toggle } from '@components/Toggle'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      <O_Toggle size="regular" label="Regular" />
      <O_Toggle size="small" label="Small" />
      <O_Toggle size="x-small" label="X-Small" />
    </div>
  )
}
```

### 비활성화

```tsx
import { O_Toggle } from '@components/Toggle'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      <O_Toggle disabled label="비활성화 (꺼짐)" />
      <O_Toggle checked disabled label="비활성화 (켜짐)" />
    </div>
  )
}
```

### 설정 목록에서 사용

```tsx
import { O_Toggle } from '@components/Toggle'
import { useState } from 'react'

type Settings = {
  notifications: boolean
  autoSave: boolean
  darkMode: boolean
}

function Example() {
  const [settings, setSettings] = useState<Settings>({
    notifications: true,
    autoSave: false,
    darkMode: false,
  })

  const toggle = (key: keyof Settings) => {
    setSettings(prev => ({ ...prev, [key]: !prev[key] }))
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <span>알림 허용</span>
        <O_Toggle
          checked={settings.notifications}
          onChange={() => toggle('notifications')}
        />
      </div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <span>자동 저장</span>
        <O_Toggle
          checked={settings.autoSave}
          onChange={() => toggle('autoSave')}
        />
      </div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <span>다크 모드</span>
        <O_Toggle
          checked={settings.darkMode}
          onChange={() => toggle('darkMode')}
        />
      </div>
    </div>
  )
}
```
