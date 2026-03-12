# 하이웍스 UI 컴포넌트 라이브러리 문서

Mantine v7 기반의 하이웍스 디자인 시스템 React 컴포넌트 라이브러리.

## 플랫폼 접두사

| 접두사 | 플랫폼 |
|-------|--------|
| `O_` | Office (하이웍스 오피스) |
| `P_` | Platform (경영 플랫폼) |
| `A_` | Admin (관리자) |

## 시작하기

### 설치

```bash
yarn add hiworks-ui-components
```

### 기본 설정

모든 컴포넌트를 사용하려면 앱 최상위에 `HiworksMantineProvider`를 래핑해야 합니다.

```tsx
import { HiworksMantineProvider } from 'hiworks-ui-components'

function App() {
  return (
    <HiworksMantineProvider>
      {/* 앱 내용 */}
    </HiworksMantineProvider>
  )
}
```

---

## 컴포넌트 목록

### 버튼 (Buttons)

| 컴포넌트 | 지원 플랫폼 | 문서 |
|---------|-----------|------|
| Button | O / P / A | [Button.md](./components/Button.md) |
| IconButton | O / P / A | [IconButton.md](./components/IconButton.md) |

### 입력 (Inputs)

| 컴포넌트 | 지원 플랫폼 | 문서 |
|---------|-----------|------|
| TextInput | O / P / A | [TextInput.md](./components/TextInput.md) |
| NumberInput | O / P / A | [NumberInput.md](./components/NumberInput.md) |
| Textarea | O / P | [Textarea.md](./components/Textarea.md) |
| FileInput | O / P | [FileInput.md](./components/FileInput.md) |

### 선택 (Selection)

| 컴포넌트 | 지원 플랫폼 | 문서 |
|---------|-----------|------|
| Select | O / P / A | [Select.md](./components/Select.md) |
| MultiSelect | O / P / A | [MultiSelect.md](./components/MultiSelect.md) |
| Autocomplete | O / P | [Autocomplete.md](./components/Autocomplete.md) |
| Checkbox | O / P / A | [Checkbox.md](./components/Checkbox.md) |
| Radio | O / P / A | [Radio.md](./components/Radio.md) |
| BoxRadio | O / P / A | [BoxRadio.md](./components/BoxRadio.md) |
| Toggle | O / P / A | [Toggle.md](./components/Toggle.md) |

### 날짜/시간 (Date & Time)

| 컴포넌트 | 지원 플랫폼 | 문서 |
|---------|-----------|------|
| DatePicker | O / P / A | [DatePicker.md](./components/DatePicker.md) |
| DateRangePicker | O / P / A | [DateRangePicker.md](./components/DateRangePicker.md) |

### 레이아웃 (Layout)

| 컴포넌트 | 지원 플랫폼 | 문서 |
|---------|-----------|------|
| Lnb | O / P / A | [Lnb.md](./components/Lnb.md) |
| Tabs | O / P / A | [Tabs.md](./components/Tabs.md) |
| P_PageTab | P | [P_PageTab.md](./components/P_PageTab.md) |
| Pagination | O / P / A | [Pagination.md](./components/Pagination.md) |

### 데이터 표시 (Data Display)

| 컴포넌트 | 지원 플랫폼 | 문서 |
|---------|-----------|------|
| Table | O / P / A | [Table.md](./components/Table.md) |
| Tree | O / P / A | [Tree.md](./components/Tree.md) |
| Badge | O | [Badge.md](./components/Badge.md) |
| Tag | O / P / A | [Tag.md](./components/Tag.md) |
| Progress | P | [Progress.md](./components/Progress.md) |

### 오버레이 (Overlay)

| 컴포넌트 | 지원 플랫폼 | 문서 |
|---------|-----------|------|
| Modal | O / P / A | [Modal.md](./components/Modal.md) |
| Dropdown | O / P / A | [Dropdown.md](./components/Dropdown.md) |
| Popover | O / P / A | [Popover.md](./components/Popover.md) |
| Menu | O | [Menu.md](./components/Menu.md) |
| Tooltip | O / P / A | [Tooltip.md](./components/Tooltip.md) |
| Toast | O / P / A | [Toast.md](./components/Toast.md) |
| Banner | O / P / A | [Banner.md](./components/Banner.md) |

### 폼 (Form)

| 컴포넌트 | 지원 플랫폼 | 문서 |
|---------|-----------|------|
| SearchForm | O / P / A | [SearchForm.md](./components/SearchForm.md) |
| Stepper | P / A | [Stepper.md](./components/Stepper.md) |

### 피드백 (Feedback)

| 컴포넌트 | 지원 플랫폼 | 문서 |
|---------|-----------|------|
| Spinner | O / P / A | [Spinner.md](./components/Spinner.md) |

### 패턴 (Patterns)

| 컴포넌트 | 지원 플랫폼 | 문서 |
|---------|-----------|------|
| TableDatePicker | P / A | [TableDatePicker.md](./components/TableDatePicker.md) |
| TableInput | P / A | [TableInput.md](./components/TableInput.md) |

---

## 공통 패턴

### 크기 (Size)

대부분의 입력 컴포넌트는 `size` prop을 지원합니다:
- `'small'` - 소형
- `'large'` - 대형 (기본값)

### Variant

플랫폼에 따라 지원하는 variant가 다릅니다:
- `'default'` - 기본 스타일 (공통)
- `'table'` - 테이블 셀 내 사용 최적화 (O, P, A)
- `'essential'` - 필수 입력 강조 표시 (P만)

### 제어/비제어 컴포넌트

모든 입력 컴포넌트는 제어/비제어 패턴을 지원합니다:

```tsx
// 비제어 (defaultValue 사용)
<O_TextInput defaultValue="초기값" />

// 제어 (value + onChange 사용)
const [value, setValue] = useState('')
<O_TextInput value={value} onChange={(e) => setValue(e.target.value)} />
```

### 에러 처리

```tsx
<O_TextInput error="유효하지 않은 입력입니다" />
```

---

## 개발 환경 실행

```bash
# Storybook 실행 (http://localhost:6006)
yarn storybook

# 빌드
yarn build

# 테스트
yarn test:run
```
