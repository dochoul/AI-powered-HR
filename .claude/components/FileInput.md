# FileInput

파일 선택 입력 컴포넌트. Office, Platform을 지원합니다 (Admin 미지원).

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_FileInput` | Office | `@components/Inputs/FileInput` |
| `P_FileInput` | Platform | `@components/Inputs/FileInput` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `children` | `ReactNode` | - | 커스텀 버튼/트리거 |
| `initialValue` | `string` | - | 초기 파일명 표시값 |
| `value` | `File \| null` | - | 제어 컴포넌트 값 |
| `onChange` | `(file: File \| null) => void` | - | 값 변경 핸들러 |
| `accept` | `string` | - | 허용 파일 형식 (예: `'.pdf,.docx'`) |
| `multiple` | `boolean` | `false` | 다중 파일 선택 여부 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `placeholder` | `string` | - | 플레이스홀더 텍스트 |
| `error` | `ReactNode` | - | 에러 메시지 |

## 사용 예시

### 기본 사용

```tsx
import { O_FileInput } from '@components/Inputs/FileInput'

function Example() {
  return <O_FileInput placeholder="파일을 선택해주세요" />
}
```

### 제어 컴포넌트

```tsx
import { O_FileInput } from '@components/Inputs/FileInput'
import { useState } from 'react'

function Example() {
  const [file, setFile] = useState<File | null>(null)

  return (
    <div>
      <O_FileInput
        value={file}
        onChange={setFile}
        placeholder="파일을 선택해주세요"
      />
      {file && <p>선택된 파일: {file.name}</p>}
    </div>
  )
}
```

### 파일 형식 제한

```tsx
import { O_FileInput } from '@components/Inputs/FileInput'

function Example() {
  return (
    <O_FileInput
      accept=".pdf,.docx,.xlsx"
      placeholder="PDF, Word, Excel 파일만 허용"
    />
  )
}
```

### 초기값 설정

```tsx
import { O_FileInput } from '@components/Inputs/FileInput'

function Example() {
  return (
    <O_FileInput
      initialValue="기존파일.pdf"
      placeholder="파일을 선택해주세요"
    />
  )
}
```

### 에러 상태

```tsx
import { O_FileInput } from '@components/Inputs/FileInput'

function Example() {
  return (
    <O_FileInput
      error="파일을 선택해주세요"
      placeholder="필수 항목"
    />
  )
}
```
