# Spinner

로딩 스피너 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Spinner` | Office | `@components/Spinner` |
| `P_Spinner` | Platform | `@components/Spinner` |
| `A_Spinner` | Admin | `@components/Spinner` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `size` | `'xs' \| 'sm' \| 'md' \| 'lg' \| 'xl' \| number` | `'md'` | 스피너 크기 |
| `color` | `string` | - | 스피너 색상 |
| `className` | `string` | - | 추가 CSS 클래스 |

## 사용 예시

### 기본 사용

```tsx
import { O_Spinner } from '@components/Spinner'

function Example() {
  return <O_Spinner />
}
```

### 크기 변경

```tsx
import { O_Spinner } from '@components/Spinner'

function Example() {
  return (
    <div style={{ display: 'flex', gap: 16, alignItems: 'center' }}>
      <O_Spinner size="xs" />
      <O_Spinner size="sm" />
      <O_Spinner size="md" />
      <O_Spinner size="lg" />
      <O_Spinner size="xl" />
    </div>
  )
}
```

### 로딩 상태와 함께 사용

```tsx
import { O_Spinner } from '@components/Spinner'
import { useState, useEffect } from 'react'

function Example() {
  const [loading, setLoading] = useState(true)
  const [data, setData] = useState<string | null>(null)

  useEffect(() => {
    setTimeout(() => {
      setData('데이터가 로드되었습니다')
      setLoading(false)
    }, 2000)
  }, [])

  return (
    <div>
      {loading ? (
        <div style={{ display: 'flex', justifyContent: 'center', padding: 32 }}>
          <O_Spinner />
        </div>
      ) : (
        <p>{data}</p>
      )}
    </div>
  )
}
```

### 버튼 내 스피너

```tsx
import { O_Spinner } from '@components/Spinner'
import { O_Button } from '@components/Buttons'
import { useState } from 'react'

function Example() {
  const [saving, setSaving] = useState(false)

  const handleSave = async () => {
    setSaving(true)
    await new Promise(resolve => setTimeout(resolve, 2000))
    setSaving(false)
  }

  return (
    <O_Button onClick={handleSave} disabled={saving}>
      {saving ? (
        <span style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <O_Spinner size="xs" />
          저장 중...
        </span>
      ) : '저장'}
    </O_Button>
  )
}
```

### 전체 화면 오버레이

```tsx
import { O_Spinner } from '@components/Spinner'

function LoadingOverlay({ visible }: { visible: boolean }) {
  if (!visible) return null

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'rgba(0, 0, 0, 0.3)',
        zIndex: 9999,
      }}
    >
      <O_Spinner size="xl" />
    </div>
  )
}
```
