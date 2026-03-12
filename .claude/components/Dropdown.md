# Dropdown

드롭다운 컨테이너 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Dropdown` | Office | `@components/Dropdown` |
| `P_Dropdown` | Platform | `@components/Dropdown` |
| `A_Dropdown` | Admin | `@components/Dropdown` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `target` | `string \| ReactElement` | - | 드롭다운 트리거 요소 (필수) |
| `children` | `ReactNode` | - | 드롭다운 내용 |
| `opened` | `boolean` | - | 제어 컴포넌트 열림 상태 |
| `defaultOpened` | `boolean` | `false` | 비제어 초기 열림 상태 |
| `onChange` | `(opened: boolean) => void` | - | 열림 상태 변경 핸들러 |
| `height` | `number \| string` | - | 드롭다운 고정 높이 |
| `maxHeight` | `number \| string` | - | 드롭다운 최대 높이 |
| `scrollType` | `'auto' \| 'always' \| 'scroll' \| 'hover' \| 'never'` | `'auto'` | 스크롤바 표시 방식 |
| `position` | `PopoverProps['position']` | `'bottom'` | 드롭다운 위치 |
| `offset` | `number` | - | 드롭다운 오프셋 |
| `width` | `number \| 'target'` | - | 드롭다운 너비 |
| `withinPortal` | `boolean` | `true` | Portal로 렌더링 여부 |
| `classNames` | `DropdownClassNames` | - | CSS 클래스 커스터마이징 |

## 사용 예시

### 기본 사용

```tsx
import { O_Dropdown } from '@components/Dropdown'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <O_Dropdown target={<O_Button>드롭다운 열기</O_Button>}>
      <div style={{ padding: 12 }}>
        <p>드롭다운 내용입니다.</p>
      </div>
    </O_Dropdown>
  )
}
```

### 제어 컴포넌트

```tsx
import { O_Dropdown } from '@components/Dropdown'
import { O_Button } from '@components/Buttons'
import { useState } from 'react'

function Example() {
  const [opened, setOpened] = useState(false)

  return (
    <O_Dropdown
      target={
        <O_Button onClick={() => setOpened(!opened)}>
          {opened ? '닫기' : '열기'}
        </O_Button>
      }
      opened={opened}
      onChange={setOpened}
    >
      <div style={{ padding: 12 }}>
        <p>제어 드롭다운입니다.</p>
        <O_Button size="small" onClick={() => setOpened(false)}>닫기</O_Button>
      </div>
    </O_Dropdown>
  )
}
```

### 위치 지정

```tsx
import { O_Dropdown } from '@components/Dropdown'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <div style={{ display: 'flex', gap: 12 }}>
      <O_Dropdown target={<O_Button>아래</O_Button>} position="bottom">
        <div style={{ padding: 8 }}>아래 드롭다운</div>
      </O_Dropdown>

      <O_Dropdown target={<O_Button>위</O_Button>} position="top">
        <div style={{ padding: 8 }}>위 드롭다운</div>
      </O_Dropdown>

      <O_Dropdown target={<O_Button>오른쪽</O_Button>} position="right">
        <div style={{ padding: 8 }}>오른쪽 드롭다운</div>
      </O_Dropdown>
    </div>
  )
}
```

### 스크롤 가능한 드롭다운

```tsx
import { O_Dropdown } from '@components/Dropdown'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <O_Dropdown
      target={<O_Button>목록 보기</O_Button>}
      maxHeight={200}
      scrollType="hover"
    >
      <ul style={{ padding: '8px 0', margin: 0, listStyle: 'none' }}>
        {Array.from({ length: 20 }, (_, i) => (
          <li
            key={i}
            style={{ padding: '8px 16px', cursor: 'pointer' }}
            onClick={() => console.log(`항목 ${i + 1} 클릭`)}
          >
            항목 {i + 1}
          </li>
        ))}
      </ul>
    </O_Dropdown>
  )
}
```

### 문자열 target

```tsx
import { O_Dropdown } from '@components/Dropdown'

function Example() {
  return (
    <O_Dropdown target="클릭하세요">
      <div style={{ padding: 12 }}>드롭다운 내용</div>
    </O_Dropdown>
  )
}
```
