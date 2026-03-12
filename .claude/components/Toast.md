# Toast

토스트 알림 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트 및 헬퍼

| 플랫폼 | 컴포넌트 | 헬퍼 함수 | import 경로 |
|--------|---------|----------|------------|
| Office | `Toast` | `o_toastHelper` | `@components/Toast` |
| Platform | `Toast` | `p_toastHelper` | `@components/Toast` |
| Admin | `Toast` | `a_toastHelper` | `@components/Toast` |

## 사용 방법

Toast는 두 단계로 사용합니다:
1. 앱 최상위에 `<Toast />` 컴포넌트 배치
2. 헬퍼 함수로 토스트 표시

## ToastHelper Options

| 옵션 | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `message` | `string` | - | 토스트 메시지 (필수) |
| `id` | `string` | - | 토스트 ID (중복 방지) |
| `type` | `'success' \| 'warning' \| 'error' \| 'info'` | - | 토스트 타입 |
| `isAutoClose` | `boolean` | `true` | 자동 닫기 여부 |
| `autoCloseTime` | `number` | `3000` | 자동 닫기 시간 (ms) |
| `icon` | `ReactElement<SVGProps<SVGSVGElement>>` | - | 커스텀 아이콘 |
| `withCloseButton` | `boolean` | `true` | 닫기 버튼 표시 여부 |
| `onOpen` | `() => void` | - | 열릴 때 콜백 |
| `onClose` | `() => void` | - | 닫힐 때 콜백 |

## 사용 예시

### 앱 최상위 설정

```tsx
// App.tsx 또는 Layout 컴포넌트
import { Toast } from '@components/Toast'

function App() {
  return (
    <div>
      <Toast />  {/* 반드시 포함해야 함 */}
      {/* 나머지 앱 내용 */}
    </div>
  )
}
```

### Office 토스트

```tsx
import { Toast, o_toastHelper } from '@components/Toast'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <>
      <Toast />

      <div style={{ display: 'flex', gap: 8 }}>
        <O_Button onClick={() => o_toastHelper.show({ message: '기본 토스트', type: 'info' })}>
          Info
        </O_Button>

        <O_Button onClick={() => o_toastHelper.show({ message: '성공했습니다', type: 'success' })}>
          Success
        </O_Button>

        <O_Button onClick={() => o_toastHelper.show({ message: '경고가 있습니다', type: 'warning' })}>
          Warning
        </O_Button>

        <O_Button onClick={() => o_toastHelper.show({ message: '오류가 발생했습니다', type: 'error' })}>
          Error
        </O_Button>
      </div>
    </>
  )
}
```

### Platform 토스트

```tsx
import { Toast, p_toastHelper } from '@components/Toast'
import { P_Button } from '@components/Buttons'

function Example() {
  return (
    <>
      <Toast />
      <P_Button onClick={() => p_toastHelper.show({ message: '저장되었습니다', type: 'success' })}>
        저장
      </P_Button>
    </>
  )
}
```

### Admin 토스트

```tsx
import { Toast, a_toastHelper } from '@components/Toast'
import { A_Button } from '@components/Buttons'

function Example() {
  return (
    <>
      <Toast />
      <A_Button onClick={() => a_toastHelper.show({ message: '처리되었습니다', type: 'info' })}>
        처리
      </A_Button>
    </>
  )
}
```

### 자동 닫기 설정

```tsx
import { Toast, o_toastHelper } from '@components/Toast'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <>
      <Toast />

      {/* 5초 후 자동 닫기 */}
      <O_Button onClick={() =>
        o_toastHelper.show({
          message: '5초 후 자동으로 닫힙니다',
          isAutoClose: true,
          autoCloseTime: 5000,
        })
      }>
        5초 토스트
      </O_Button>

      {/* 자동 닫기 비활성화 */}
      <O_Button onClick={() =>
        o_toastHelper.show({
          message: '직접 닫아야 합니다',
          isAutoClose: false,
          withCloseButton: true,
        })
      }>
        수동 닫기
      </O_Button>
    </>
  )
}
```

### 이벤트 콜백

```tsx
import { Toast, o_toastHelper } from '@components/Toast'
import { O_Button } from '@components/Buttons'

function Example() {
  return (
    <>
      <Toast />
      <O_Button onClick={() =>
        o_toastHelper.show({
          message: '알림 메시지',
          type: 'info',
          onOpen: () => console.log('토스트가 열렸습니다'),
          onClose: () => console.log('토스트가 닫혔습니다'),
        })
      }>
        이벤트 토스트
      </O_Button>
    </>
  )
}
```

### 커스텀 아이콘

```tsx
import { Toast, o_toastHelper } from '@components/Toast'
import { O_Button } from '@components/Buttons'
import { InfoCircleIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <>
      <Toast />
      <O_Button onClick={() =>
        o_toastHelper.show({
          message: '커스텀 아이콘 토스트',
          icon: <InfoCircleIcon />,
        })
      }>
        커스텀 아이콘
      </O_Button>
    </>
  )
}
```
