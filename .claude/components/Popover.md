# Popover

팝오버 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Popover` | Office | `@components/Popover` |
| `P_Popover` | Platform | `@components/Popover` |
| `A_Popover` | Admin | `@components/Popover` |

## 서브 컴포넌트 구조

- `Popover` - 최상위 컨테이너
- `Popover.Target` - 팝오버 트리거 요소
- `Popover.Dropdown` - 팝오버 내용

## Props

### Popover Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `opened` | `boolean` | - | 제어 컴포넌트 열림 상태 |
| `defaultOpened` | `boolean` | `false` | 비제어 초기 열림 상태 |
| `onChange` | `(opened: boolean) => void` | - | 열림 상태 변경 핸들러 |
| `position` | `PopoverProps['position']` | `'bottom'` | 팝오버 위치 |
| `offset` | `number` | - | 팝오버 오프셋 |
| `width` | `number \| 'target'` | - | 팝오버 너비 |
| `withinPortal` | `boolean` | `true` | Portal로 렌더링 여부 |
| `closeOnClickOutside` | `boolean` | `true` | 외부 클릭으로 닫기 여부 |
| `dropdownWidth` | `number \| 'target'` | - | 드롭다운 너비 |
| `classNames` | `{ dropdown?: string }` | - | CSS 클래스 커스터마이징 |

## 사용 예시

### 기본 사용

```tsx
import { O_Popover } from '@components/Popover'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <O_Popover>
      <O_Popover.Target>
        <O_Button>팝오버 열기</O_Button>
      </O_Popover.Target>
      <O_Popover.Dropdown>
        <div style={{ padding: 12 }}>
          <p>팝오버 내용입니다.</p>
        </div>
      </O_Popover.Dropdown>
    </O_Popover>
  )
}
```

### 제어 컴포넌트

```tsx
import { O_Popover } from '@components/Popover'
import { O_Button } from '@components/Buttons'
import { useState } from 'react'

function Example() {
  const [opened, setOpened] = useState(false)

  return (
    <O_Popover opened={opened} onChange={setOpened}>
      <O_Popover.Target>
        <O_Button onClick={() => setOpened(!opened)}>
          {opened ? '닫기' : '팝오버 열기'}
        </O_Button>
      </O_Popover.Target>
      <O_Popover.Dropdown>
        <div style={{ padding: 16 }}>
          <p>제어 팝오버입니다.</p>
          <O_Button size="small" onClick={() => setOpened(false)}>닫기</O_Button>
        </div>
      </O_Popover.Dropdown>
    </O_Popover>
  )
}
```

### 다양한 위치

```tsx
import { O_Popover } from '@components/Popover'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <div style={{ display: 'flex', gap: 12 }}>
      <O_Popover position="top">
        <O_Popover.Target><O_Button>위</O_Button></O_Popover.Target>
        <O_Popover.Dropdown><div style={{ padding: 8 }}>위 팝오버</div></O_Popover.Dropdown>
      </O_Popover>

      <O_Popover position="bottom">
        <O_Popover.Target><O_Button>아래</O_Button></O_Popover.Target>
        <O_Popover.Dropdown><div style={{ padding: 8 }}>아래 팝오버</div></O_Popover.Dropdown>
      </O_Popover>

      <O_Popover position="left">
        <O_Popover.Target><O_Button>왼쪽</O_Button></O_Popover.Target>
        <O_Popover.Dropdown><div style={{ padding: 8 }}>왼쪽 팝오버</div></O_Popover.Dropdown>
      </O_Popover>

      <O_Popover position="right">
        <O_Popover.Target><O_Button>오른쪽</O_Button></O_Popover.Target>
        <O_Popover.Dropdown><div style={{ padding: 8 }}>오른쪽 팝오버</div></O_Popover.Dropdown>
      </O_Popover>
    </div>
  )
}
```

### 폼이 있는 팝오버

```tsx
import { O_Popover } from '@components/Popover'
import { O_Button } from '@components/Buttons'
import { O_TextInput } from '@components/Inputs/TextInput'
import { useState } from 'react'

function Example() {
  const [opened, setOpened] = useState(false)
  const [name, setName] = useState('')

  const handleSubmit = () => {
    console.log('이름:', name)
    setOpened(false)
  }

  return (
    <O_Popover opened={opened} onChange={setOpened}>
      <O_Popover.Target>
        <O_Button onClick={() => setOpened(true)}>이름 추가</O_Button>
      </O_Popover.Target>
      <O_Popover.Dropdown>
        <div style={{ padding: 16, width: 240 }}>
          <O_TextInput
            placeholder="이름을 입력해주세요"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <div style={{ display: 'flex', gap: 8, marginTop: 12, justifyContent: 'flex-end' }}>
            <O_Button size="small" variant="cancel" onClick={() => setOpened(false)}>취소</O_Button>
            <O_Button size="small" onClick={handleSubmit}>추가</O_Button>
          </div>
        </div>
      </O_Popover.Dropdown>
    </O_Popover>
  )
}
```
