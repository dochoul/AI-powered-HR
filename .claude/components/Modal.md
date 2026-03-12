# Modal

모달 대화상자 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Modal` | Office | `@components/Modal` |
| `P_Modal` | Platform | `@components/Modal` |
| `A_Modal` | Admin | `@components/Modal` |

## 서브 컴포넌트 구조

Modal은 Compound Component 패턴으로 구성됩니다:

- `Modal` - 최상위 컨테이너
- `Modal.Title` - 모달 제목
- `Modal.Contents` - 모달 내용
- `Modal.ButtonArea` - 하단 버튼 영역

## Props

### Modal Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `opened` | `boolean` | - | 모달 열림 상태 |
| `onClose` | `() => void` | - | 모달 닫기 핸들러 |
| `variant` | `'default' \| 'alert' \| 'unstyled'` | `'default'` | 모달 스타일 |
| `title` | `ReactNode` | - | 모달 제목 (Modal.Title 대신 사용 가능) |
| `size` | `string \| number` | - | 모달 너비 |
| `withCloseButton` | `boolean` | `true` | 닫기 버튼 표시 여부 |
| `closeOnClickOutside` | `boolean` | `true` | 외부 클릭으로 닫기 여부 |
| `closeOnEscape` | `boolean` | `true` | ESC 키로 닫기 여부 |
| `centered` | `boolean` | `false` | 화면 중앙 배치 여부 |
| `fullScreen` | `boolean` | `false` | 전체화면 여부 |
| `zIndex` | `number` | - | z-index 값 |
| `children` | `ReactNode` | - | 모달 내용 |

## 사용 예시

### 기본 사용

```tsx
import { O_Modal } from '@components/Modal'
import { O_Button } from '@components/Buttons'
import { useState } from 'react'

function Example() {
  const [opened, setOpened] = useState(false)

  return (
    <>
      <O_Button onClick={() => setOpened(true)}>모달 열기</O_Button>

      <O_Modal opened={opened} onClose={() => setOpened(false)}>
        <O_Modal.Title>모달 제목</O_Modal.Title>
        <O_Modal.Contents>
          모달 내용이 여기에 표시됩니다.
        </O_Modal.Contents>
        <O_Modal.ButtonArea>
          <O_Button variant="cancel" onClick={() => setOpened(false)}>취소</O_Button>
          <O_Button onClick={() => setOpened(false)}>확인</O_Button>
        </O_Modal.ButtonArea>
      </O_Modal>
    </>
  )
}
```

### Alert 모달 (확인/취소)

```tsx
import { O_Modal } from '@components/Modal'
import { O_Button } from '@components/Buttons'
import { useState } from 'react'

function Example() {
  const [opened, setOpened] = useState(false)

  const handleConfirm = () => {
    // 확인 처리
    setOpened(false)
  }

  return (
    <>
      <O_Button variant="danger" onClick={() => setOpened(true)}>삭제</O_Button>

      <O_Modal
        opened={opened}
        onClose={() => setOpened(false)}
        variant="alert"
        centered
      >
        <O_Modal.Title>정말 삭제하시겠습니까?</O_Modal.Title>
        <O_Modal.Contents>
          삭제된 데이터는 복구할 수 없습니다.
        </O_Modal.Contents>
        <O_Modal.ButtonArea>
          <O_Button variant="cancel" onClick={() => setOpened(false)}>취소</O_Button>
          <O_Button variant="danger" onClick={handleConfirm}>삭제</O_Button>
        </O_Modal.ButtonArea>
      </O_Modal>
    </>
  )
}
```

### 크기 지정

```tsx
import { O_Modal } from '@components/Modal'
import { useState } from 'react'

function Example() {
  const [opened, setOpened] = useState(false)

  return (
    <>
      <button onClick={() => setOpened(true)}>모달 열기</button>

      <O_Modal
        opened={opened}
        onClose={() => setOpened(false)}
        size={600}
      >
        <O_Modal.Title>넓은 모달</O_Modal.Title>
        <O_Modal.Contents>
          너비 600px 모달입니다.
        </O_Modal.Contents>
      </O_Modal>
    </>
  )
}
```

### 닫기 버튼 숨기기

```tsx
import { O_Modal } from '@components/Modal'
import { O_Button } from '@components/Buttons'
import { useState } from 'react'

function Example() {
  const [opened, setOpened] = useState(false)

  return (
    <>
      <O_Button onClick={() => setOpened(true)}>모달 열기</O_Button>

      <O_Modal
        opened={opened}
        onClose={() => setOpened(false)}
        withCloseButton={false}
        closeOnClickOutside={false}
      >
        <O_Modal.Title>알림</O_Modal.Title>
        <O_Modal.Contents>
          버튼으로만 닫을 수 있습니다.
        </O_Modal.Contents>
        <O_Modal.ButtonArea>
          <O_Button onClick={() => setOpened(false)}>확인</O_Button>
        </O_Modal.ButtonArea>
      </O_Modal>
    </>
  )
}
```

### useModals Hook으로 프로그래매틱 제어

```tsx
import { useModals } from '@components/ModalProvider'
import { O_Button } from '@components/Buttons'

function Example() {
  const modals = useModals()

  const handleClick = () => {
    modals.openModal({
      title: '확인',
      children: <p>정말 진행하시겠습니까?</p>,
      onConfirm: () => {
        // 확인 처리
      },
    })
  }

  return <O_Button onClick={handleClick}>모달 열기</O_Button>
}
```
