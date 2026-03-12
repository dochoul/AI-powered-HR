# Lnb (Left Navigation Bar)

좌측 내비게이션 바 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Lnb` | Office | `@components/Lnb` |
| `P_Lnb` | Platform | `@components/Lnb` |
| `A_Lnb` | Admin | `@components/Lnb` |

## 서브 컴포넌트 구조

각 플랫폼별로 약간의 구조 차이가 있습니다:

### Office
- `O_Lnb` - LNB 최상위 컨테이너
- `O_LnbMenu` - 메뉴 항목 (재귀적으로 중첩 가능)

### Platform
- `P_Lnb` - LNB 최상위 컨테이너
- `P_LnbMenu` - 메뉴 항목

### Admin
- `A_Lnb` - LNB 최상위 컨테이너
- `A_LnbMenu` - 메뉴 항목

## Props

### LnbMenu 공통 Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `label` | `string` | - | 메뉴 텍스트 (필수) |
| `icon` | `ReactNode` | - | 메뉴 아이콘 |
| `children` | `ReactElement \| ReactElement[]` | - | 하위 메뉴 항목 |
| `expand` | `boolean` | - | 펼침 상태 (제어) |
| `onMenuClick` | `MouseEventHandler<HTMLButtonElement>` | - | 클릭 핸들러 |
| `childrenAs` | `ElementType` | - | 하위 메뉴 컨테이너 타입 |

## 사용 예시

### Office LNB

```tsx
import { O_Lnb } from '@components/Lnb'
import { MailIcon, CalendarIcon, ContactIcon } from 'hiworks-icons/react/solid/20'

function Example() {
  return (
    <O_Lnb>
      <O_Lnb.Menu
        label="받은 편지함"
        icon={<MailIcon />}
        onMenuClick={() => console.log('받은 편지함')}
      />
      <O_Lnb.Menu
        label="캘린더"
        icon={<CalendarIcon />}
        onMenuClick={() => console.log('캘린더')}
      />
      <O_Lnb.Menu
        label="주소록"
        icon={<ContactIcon />}
        onMenuClick={() => console.log('주소록')}
      >
        <O_Lnb.Menu label="내 주소록" onMenuClick={() => console.log('내 주소록')} />
        <O_Lnb.Menu label="공유 주소록" onMenuClick={() => console.log('공유 주소록')} />
      </O_Lnb.Menu>
    </O_Lnb>
  )
}
```

### Platform LNB

```tsx
import { P_Lnb } from '@components/Lnb'
import { HomeIcon, UsersIcon, SettingsIcon } from 'hiworks-icons/react/solid/20'

function Example() {
  return (
    <P_Lnb>
      <P_Lnb.Menu
        label="대시보드"
        icon={<HomeIcon />}
        onMenuClick={() => console.log('대시보드')}
      />
      <P_Lnb.Menu
        label="직원 관리"
        icon={<UsersIcon />}
        onMenuClick={() => console.log('직원 관리')}
      >
        <P_Lnb.Menu label="직원 목록" onMenuClick={() => console.log('직원 목록')} />
        <P_Lnb.Menu label="부서 관리" onMenuClick={() => console.log('부서 관리')} />
        <P_Lnb.Menu label="직급 관리" onMenuClick={() => console.log('직급 관리')} />
      </P_Lnb.Menu>
      <P_Lnb.Menu
        label="시스템 설정"
        icon={<SettingsIcon />}
        onMenuClick={() => console.log('시스템 설정')}
      />
    </P_Lnb>
  )
}
```

### Admin LNB

```tsx
import { A_Lnb } from '@components/Lnb'
import { DatabaseIcon, SecurityIcon, LogIcon } from 'hiworks-icons/react/solid/20'

function Example() {
  return (
    <A_Lnb>
      <A_Lnb.Menu
        label="데이터 관리"
        icon={<DatabaseIcon />}
        onMenuClick={() => console.log('데이터 관리')}
      />
      <A_Lnb.Menu
        label="보안 설정"
        icon={<SecurityIcon />}
        onMenuClick={() => console.log('보안')}
      >
        <A_Lnb.Menu label="IP 제한" onMenuClick={() => console.log('IP 제한')} />
        <A_Lnb.Menu label="2단계 인증" onMenuClick={() => console.log('2단계 인증')} />
      </A_Lnb.Menu>
      <A_Lnb.Menu
        label="접속 로그"
        icon={<LogIcon />}
        onMenuClick={() => console.log('로그')}
      />
    </A_Lnb>
  )
}
```

### 현재 활성 메뉴 표시

```tsx
import { O_Lnb } from '@components/Lnb'
import { useState } from 'react'

type MenuItem = { id: string; label: string }

const menuItems: MenuItem[] = [
  { id: 'inbox', label: '받은 편지함' },
  { id: 'sent', label: '보낸 편지함' },
  { id: 'drafts', label: '임시 보관함' },
]

function Example() {
  const [activeMenu, setActiveMenu] = useState('inbox')

  return (
    <div style={{ display: 'flex' }}>
      <div style={{ width: 200, borderRight: '1px solid #e2e8f0' }}>
        <O_Lnb>
          {menuItems.map(item => (
            <O_Lnb.Menu
              key={item.id}
              label={item.label}
              onMenuClick={() => setActiveMenu(item.id)}
            />
          ))}
        </O_Lnb>
      </div>
      <div style={{ padding: 24 }}>
        현재 메뉴: {menuItems.find(m => m.id === activeMenu)?.label}
      </div>
    </div>
  )
}
```
