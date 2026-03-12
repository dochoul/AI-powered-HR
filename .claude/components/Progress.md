# Progress

진행률 바 컴포넌트. Platform 플랫폼만 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `P_Progress` | Platform | `@components/Progress` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `value` | `number` | - | 진행률 (0~100) |
| `color` | `string` | - | 진행 바 색상 |
| `size` | `'xs' \| 'sm' \| 'md' \| 'lg' \| 'xl' \| number` | `'md'` | 진행 바 높이 |
| `radius` | `number \| string` | - | 모서리 둥글기 |
| `striped` | `boolean` | `false` | 줄무늬 패턴 여부 |
| `animated` | `boolean` | `false` | 줄무늬 애니메이션 여부 |
| `className` | `string` | - | 추가 CSS 클래스 |

## 사용 예시

### 기본 사용

```tsx
import { P_Progress } from '@components/Progress'

function Example() {
  return <P_Progress value={60} />
}
```

### 다양한 값

```tsx
import { P_Progress } from '@components/Progress'

function Example() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      <P_Progress value={25} />
      <P_Progress value={50} />
      <P_Progress value={75} />
      <P_Progress value={100} />
    </div>
  )
}
```

### 애니메이션 진행 바

```tsx
import { P_Progress } from '@components/Progress'
import { useState, useEffect } from 'react'

function Example() {
  const [progress, setProgress] = useState(0)

  useEffect(() => {
    const interval = setInterval(() => {
      setProgress(prev => {
        if (prev >= 100) {
          clearInterval(interval)
          return 100
        }
        return prev + 10
      })
    }, 500)

    return () => clearInterval(interval)
  }, [])

  return (
    <div>
      <P_Progress value={progress} />
      <p>{progress}% 완료</p>
    </div>
  )
}
```

### 파일 업로드 진행 표시

```tsx
import { P_Progress } from '@components/Progress'
import { useState } from 'react'
import { P_Button } from '@components/Buttons'

function Example() {
  const [uploading, setUploading] = useState(false)
  const [progress, setProgress] = useState(0)

  const handleUpload = () => {
    setUploading(true)
    setProgress(0)

    const interval = setInterval(() => {
      setProgress(prev => {
        if (prev >= 100) {
          clearInterval(interval)
          setUploading(false)
          return 100
        }
        return prev + 20
      })
    }, 400)
  }

  return (
    <div style={{ width: 300 }}>
      {uploading && (
        <div style={{ marginBottom: 8 }}>
          <P_Progress value={progress} />
          <small style={{ color: '#718096' }}>업로드 중... {progress}%</small>
        </div>
      )}
      <P_Button onClick={handleUpload} disabled={uploading}>
        파일 업로드
      </P_Button>
    </div>
  )
}
```
