# Tabs

탭 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Tabs` | Office | `@components/Tabs` |
| `P_Tabs` | Platform | `@components/Tabs` |
| `A_Tabs` | Admin | `@components/Tabs` |

## 서브 컴포넌트 구조

- `Tabs` - 최상위 컨테이너
- `Tabs.List` - 탭 목록 컨테이너
- `Tabs.Tab` - 개별 탭 버튼
- `Tabs.Panel` - 탭 패널 (내용 영역)

## Props

### Tabs Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `defaultValue` | `string` | - | 비제어 초기 선택 탭 |
| `value` | `string` | - | 제어 컴포넌트 선택 탭 |
| `onChange` | `(value: string \| null) => void` | - | 탭 변경 핸들러 |
| `variant` | `'page' \| 'contents'` | `'page'` | 탭 스타일 |
| `grow` | `boolean` | `false` | 탭이 전체 너비를 차지하는 여부 |
| `firstTabAlign` | `'start' \| 'center'` | `'start'` | 첫 번째 탭 정렬 |

### Tabs.List Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `grow` | `boolean` | `false` | 탭이 전체 너비를 차지하는 여부 |
| `justify` | `'flex-start' \| 'center' \| 'flex-end'` | `'flex-start'` | 탭 정렬 |

### Tabs.Tab Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `value` | `string` | - | 탭 값 (필수) |
| `disabled` | `boolean` | `false` | 비활성화 여부 |
| `leftSection` | `ReactNode` | - | 왼쪽 아이콘/내용 |
| `rightSection` | `ReactNode` | - | 오른쪽 아이콘/내용 |

### Tabs.Panel Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `value` | `string` | - | 연결될 탭 값 (필수) |
| `children` | `ReactNode` | - | 패널 내용 |

## 사용 예시

### 기본 사용

```tsx
import { O_Tabs } from '@components/Tabs'

function Example() {
  return (
    <O_Tabs defaultValue="tab1">
      <O_Tabs.List>
        <O_Tabs.Tab value="tab1">탭1</O_Tabs.Tab>
        <O_Tabs.Tab value="tab2">탭2</O_Tabs.Tab>
        <O_Tabs.Tab value="tab3" disabled>탭3 (비활성화)</O_Tabs.Tab>
      </O_Tabs.List>

      <O_Tabs.Panel value="tab1">탭1 내용</O_Tabs.Panel>
      <O_Tabs.Panel value="tab2">탭2 내용</O_Tabs.Panel>
      <O_Tabs.Panel value="tab3">탭3 내용</O_Tabs.Panel>
    </O_Tabs>
  )
}
```

### 제어 컴포넌트

```tsx
import { O_Tabs } from '@components/Tabs'
import { useState } from 'react'

function Example() {
  const [activeTab, setActiveTab] = useState<string | null>('tab1')

  return (
    <O_Tabs value={activeTab} onChange={setActiveTab}>
      <O_Tabs.List>
        <O_Tabs.Tab value="tab1">탭1</O_Tabs.Tab>
        <O_Tabs.Tab value="tab2">탭2</O_Tabs.Tab>
        <O_Tabs.Tab value="tab3">탭3</O_Tabs.Tab>
      </O_Tabs.List>

      <O_Tabs.Panel value="tab1">탭1 내용</O_Tabs.Panel>
      <O_Tabs.Panel value="tab2">탭2 내용</O_Tabs.Panel>
      <O_Tabs.Panel value="tab3">탭3 내용</O_Tabs.Panel>
    </O_Tabs>
  )
}
```

### Contents Variant

```tsx
import { O_Tabs } from '@components/Tabs'

function Example() {
  return (
    <O_Tabs defaultValue="tab1" variant="contents">
      <O_Tabs.List justify="center">
        <O_Tabs.Tab value="tab1">상세정보</O_Tabs.Tab>
        <O_Tabs.Tab value="tab2">첨부파일</O_Tabs.Tab>
        <O_Tabs.Tab value="tab3">댓글</O_Tabs.Tab>
      </O_Tabs.List>

      <O_Tabs.Panel value="tab1">상세 내용</O_Tabs.Panel>
      <O_Tabs.Panel value="tab2">첨부파일 목록</O_Tabs.Panel>
      <O_Tabs.Panel value="tab3">댓글 목록</O_Tabs.Panel>
    </O_Tabs>
  )
}
```

### 아이콘이 있는 탭

```tsx
import { O_Tabs } from '@components/Tabs'
import { HomeIcon, SettingsIcon } from 'hiworks-icons/react/solid/16'

function Example() {
  return (
    <O_Tabs defaultValue="home">
      <O_Tabs.List>
        <O_Tabs.Tab value="home" leftSection={<HomeIcon />}>홈</O_Tabs.Tab>
        <O_Tabs.Tab value="settings" leftSection={<SettingsIcon />}>설정</O_Tabs.Tab>
      </O_Tabs.List>

      <O_Tabs.Panel value="home">홈 내용</O_Tabs.Panel>
      <O_Tabs.Panel value="settings">설정 내용</O_Tabs.Panel>
    </O_Tabs>
  )
}
```

### 전체 너비 탭 (Grow)

```tsx
import { O_Tabs } from '@components/Tabs'

function Example() {
  return (
    <O_Tabs defaultValue="tab1">
      <O_Tabs.List grow>
        <O_Tabs.Tab value="tab1">탭1</O_Tabs.Tab>
        <O_Tabs.Tab value="tab2">탭2</O_Tabs.Tab>
        <O_Tabs.Tab value="tab3">탭3</O_Tabs.Tab>
      </O_Tabs.List>

      <O_Tabs.Panel value="tab1">탭1 내용</O_Tabs.Panel>
      <O_Tabs.Panel value="tab2">탭2 내용</O_Tabs.Panel>
      <O_Tabs.Panel value="tab3">탭3 내용</O_Tabs.Panel>
    </O_Tabs>
  )
}
```
