# P_PageTab / P_PageTabs

브라우저 탭 스타일의 페이지 탭 컴포넌트. Platform 플랫폼만 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `P_PageTab` | Platform | `@components/P_PageTab` |
| `P_PageTabs` | Platform | `@components/P_PageTab` |

## Props

### P_PageTab Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `tab` | `P_PageTabType` | - | 탭 데이터 (필수) |
| `isActive` | `boolean` | `false` | 활성화 상태 |
| `isDefault` | `boolean` | `false` | 기본 탭 여부 (닫기 버튼 표시 안 함) |
| `onClickTab` | `(tab: P_PageTabType) => void` | - | 탭 클릭 핸들러 |
| `onCloseTab` | `(tab: P_PageTabType) => void` | - | 탭 닫기 핸들러 |
| `className` | `string` | - | 추가 CSS 클래스 |

### P_PageTabs Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `tabs` | `P_PageTabType[]` | - | 탭 배열 (필수) |
| `setTabs` | `Dispatch<SetStateAction<P_PageTabType[]>>` | - | 탭 상태 업데이터 (필수) |
| `currentTab` | `string` | - | 현재 활성 탭 이름 |
| `onClickTab` | `(tab: P_PageTabType) => void` | - | 탭 클릭 핸들러 |
| `onCloseTab` | `(tab: P_PageTabType) => void` | - | 탭 닫기 핸들러 |
| `clickPreviousTabOnCloseActiveTab` | `boolean` | `false` | 활성 탭 닫을 때 이전 탭 선택 여부 |
| `shouldCloseActiveTab` | `() => Promise<boolean>` | - | 활성 탭 닫기 전 확인 콜백 |

### P_PageTabType

```typescript
type P_PageTabType = {
  name: string       // 탭 고유 이름 (키로 사용)
  icon: ReactElement // 탭 아이콘 (필수)
  [key: string]: any // 추가 데이터
}
```

## 사용 예시

### P_PageTabs 기본 사용

```tsx
import { P_PageTabs } from '@components/P_PageTab'
import { MailIcon, CalendarIcon, ContactIcon } from 'hiworks-icons/react/solid/16'
import { useState } from 'react'

const initialTabs = [
  { name: '메일', icon: <MailIcon /> },
  { name: '캘린더', icon: <CalendarIcon /> },
]

function Example() {
  const [tabs, setTabs] = useState(initialTabs)
  const [currentTab, setCurrentTab] = useState('메일')

  return (
    <P_PageTabs
      tabs={tabs}
      setTabs={setTabs}
      currentTab={currentTab}
      onClickTab={(tab) => setCurrentTab(tab.name)}
    />
  )
}
```

### 탭 추가/제거

```tsx
import { P_PageTabs } from '@components/P_PageTab'
import { MailIcon, PlusIcon } from 'hiworks-icons/react/solid/16'
import { useState } from 'react'
import { O_Button } from '@components/Buttons'

function Example() {
  const [tabs, setTabs] = useState([
    { name: '메일', icon: <MailIcon /> },
  ])
  const [currentTab, setCurrentTab] = useState('메일')

  const addTab = () => {
    const newTab = {
      name: `탭 ${tabs.length + 1}`,
      icon: <MailIcon />,
    }
    setTabs(prev => [...prev, newTab])
    setCurrentTab(newTab.name)
  }

  const handleClose = (tab: typeof tabs[0]) => {
    setTabs(prev => prev.filter(t => t.name !== tab.name))
    if (currentTab === tab.name) {
      setCurrentTab(tabs[0]?.name ?? '')
    }
  }

  return (
    <div>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <P_PageTabs
          tabs={tabs}
          setTabs={setTabs}
          currentTab={currentTab}
          onClickTab={(tab) => setCurrentTab(tab.name)}
          onCloseTab={handleClose}
        />
        <O_Button
          variant="ghost"
          size="x-small"
          onClick={addTab}
        >
          <PlusIcon />
        </O_Button>
      </div>

      <div style={{ padding: 16 }}>
        현재 탭: {currentTab}
      </div>
    </div>
  )
}
```

### 닫기 전 확인

```tsx
import { P_PageTabs } from '@components/P_PageTab'
import { MailIcon } from 'hiworks-icons/react/solid/16'
import { useState } from 'react'

function Example() {
  const [tabs, setTabs] = useState([
    { name: '편집 중', icon: <MailIcon />, isDirty: true },
    { name: '일반', icon: <MailIcon />, isDirty: false },
  ])
  const [currentTab, setCurrentTab] = useState('편집 중')

  const shouldClose = async () => {
    const activeTab = tabs.find(t => t.name === currentTab)
    if (activeTab?.isDirty) {
      return confirm('저장되지 않은 변경사항이 있습니다. 닫으시겠습니까?')
    }
    return true
  }

  return (
    <P_PageTabs
      tabs={tabs}
      setTabs={setTabs}
      currentTab={currentTab}
      onClickTab={(tab) => setCurrentTab(tab.name)}
      clickPreviousTabOnCloseActiveTab
      shouldCloseActiveTab={shouldClose}
    />
  )
}
```

### P_PageTab 단독 사용

```tsx
import { P_PageTab } from '@components/P_PageTab'
import { MailIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  const tab = { name: '메일', icon: <MailIcon /> }

  return (
    <P_PageTab
      tab={tab}
      isActive={true}
      onClickTab={(t) => console.log('클릭:', t.name)}
      onCloseTab={(t) => console.log('닫기:', t.name)}
    />
  )
}
```
