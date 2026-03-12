# Menu

메뉴 컴포넌트. Office 플랫폼만 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Menu` | Office | `@components/Menu` |

## 서브 컴포넌트 구조

- `Menu` - 최상위 컨테이너
- `Menu.Target` - 메뉴 트리거 요소
- `Menu.Dropdown` - 메뉴 드롭다운
- `Menu.Item` - 개별 메뉴 항목
- `Menu.Label` - 메뉴 그룹 라벨
- `Menu.Divider` - 구분선

## Props

### Menu Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `opened` | `boolean` | - | 제어 컴포넌트 열림 상태 |
| `defaultOpened` | `boolean` | `false` | 비제어 초기 열림 상태 |
| `onChange` | `(opened: boolean) => void` | - | 열림 상태 변경 핸들러 |
| `selectedMenuId` | `string` | - | 현재 선택된 메뉴 ID |
| `maxHeight` | `number \| string` | - | 드롭다운 최대 높이 |
| `position` | `PopoverProps['position']` | `'bottom'` | 메뉴 위치 |
| `withinPortal` | `boolean` | `true` | Portal로 렌더링 여부 |
| `closeOnItemClick` | `boolean` | `true` | 항목 클릭 시 닫기 여부 |

### Menu.Item Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `menuId` | `string` | - | 항목 ID (선택 상태 관리용) |
| `onClick` | `MouseEventHandler<HTMLButtonElement>` | - | 클릭 핸들러 |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `leftSection` | `ReactNode` | - | 왼쪽 아이콘/내용 |
| `rightSection` | `ReactNode` | - | 오른쪽 아이콘/내용 |
| `color` | `string` | - | 텍스트 색상 |

## 사용 예시

### 기본 메뉴

```tsx
import { O_Menu } from '@components/Menu'
import { O_IconButton } from '@components/Buttons'
import { DotsVerticalIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <O_Menu>
      <O_Menu.Target>
        <O_IconButton variant="ghost">
          <DotsVerticalIcon />
        </O_IconButton>
      </O_Menu.Target>
      <O_Menu.Dropdown>
        <O_Menu.Item onClick={() => console.log('수정')}>수정</O_Menu.Item>
        <O_Menu.Item onClick={() => console.log('복사')}>복사</O_Menu.Item>
        <O_Menu.Divider />
        <O_Menu.Item onClick={() => console.log('삭제')} color="red">삭제</O_Menu.Item>
      </O_Menu.Dropdown>
    </O_Menu>
  )
}
```

### 아이콘이 있는 메뉴

```tsx
import { O_Menu } from '@components/Menu'
import { O_Button } from '@components/Buttons'
import { EditIcon, CopyIcon, TrashIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <O_Menu>
      <O_Menu.Target>
        <O_Button variant="outline">더보기</O_Button>
      </O_Menu.Target>
      <O_Menu.Dropdown>
        <O_Menu.Item
          leftSection={<EditIcon width={14} />}
          onClick={() => console.log('수정')}
        >
          수정
        </O_Menu.Item>
        <O_Menu.Item
          leftSection={<CopyIcon width={14} />}
          onClick={() => console.log('복사')}
        >
          복사
        </O_Menu.Item>
        <O_Menu.Divider />
        <O_Menu.Item
          leftSection={<TrashIcon width={14} />}
          color="red"
          onClick={() => console.log('삭제')}
        >
          삭제
        </O_Menu.Item>
      </O_Menu.Dropdown>
    </O_Menu>
  )
}
```

### 그룹 라벨이 있는 메뉴

```tsx
import { O_Menu } from '@components/Menu'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <O_Menu>
      <O_Menu.Target>
        <O_Button>메뉴</O_Button>
      </O_Menu.Target>
      <O_Menu.Dropdown>
        <O_Menu.Label>파일</O_Menu.Label>
        <O_Menu.Item onClick={() => console.log('새 파일')}>새 파일</O_Menu.Item>
        <O_Menu.Item onClick={() => console.log('열기')}>열기</O_Menu.Item>
        <O_Menu.Item onClick={() => console.log('저장')}>저장</O_Menu.Item>

        <O_Menu.Divider />

        <O_Menu.Label>편집</O_Menu.Label>
        <O_Menu.Item onClick={() => console.log('복사')}>복사</O_Menu.Item>
        <O_Menu.Item onClick={() => console.log('붙여넣기')}>붙여넣기</O_Menu.Item>
      </O_Menu.Dropdown>
    </O_Menu>
  )
}
```

### 선택 상태 관리

```tsx
import { O_Menu } from '@components/Menu'
import { O_Button } from '@components/Buttons'
import { useState } from 'react'

function Example() {
  const [selectedId, setSelectedId] = useState('view')

  return (
    <O_Menu selectedMenuId={selectedId}>
      <O_Menu.Target>
        <O_Button>뷰 옵션</O_Button>
      </O_Menu.Target>
      <O_Menu.Dropdown>
        <O_Menu.Item menuId="view" onClick={() => setSelectedId('view')}>
          목록 보기
        </O_Menu.Item>
        <O_Menu.Item menuId="grid" onClick={() => setSelectedId('grid')}>
          그리드 보기
        </O_Menu.Item>
        <O_Menu.Item menuId="card" onClick={() => setSelectedId('card')}>
          카드 보기
        </O_Menu.Item>
      </O_Menu.Dropdown>
    </O_Menu>
  )
}
```

### 스크롤 메뉴

```tsx
import { O_Menu } from '@components/Menu'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <O_Menu maxHeight={200}>
      <O_Menu.Target>
        <O_Button>항목 선택</O_Button>
      </O_Menu.Target>
      <O_Menu.Dropdown>
        {Array.from({ length: 20 }, (_, i) => (
          <O_Menu.Item key={i} onClick={() => console.log(`항목 ${i + 1}`)}>
            항목 {i + 1}
          </O_Menu.Item>
        ))}
      </O_Menu.Dropdown>
    </O_Menu>
  )
}
```
