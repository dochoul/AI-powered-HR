# Tree

트리 구조 컴포넌트. Office, Platform, Admin 3개 플랫폼을 지원합니다.

## 플랫폼별 컴포넌트

| 컴포넌트 | 플랫폼 | import 경로 |
|---------|--------|------------|
| `O_Tree` | Office | `@components/Tree` |
| `P_Tree` | Platform | `@components/Tree` |
| `A_Tree` | Admin | `@components/Tree` |

## 유틸리티

| 유틸리티 | 설명 | import 경로 |
|---------|------|------------|
| `createNodes` | 평탄한 배열을 트리 구조로 변환 | `@components/Tree` |
| `searchNodes` | 트리에서 노드 검색 | `@components/Tree` |
| `useTree` | 트리 컨트롤러 훅 | `@components/Tree` |

## Props

| Prop | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `nodes` | `Node<T>[]` | - | 트리 노드 배열 (필수) |
| `type` | `'office' \| 'admin' \| 'platform'` | - | 플랫폼 타입 (내부 사용) |
| `checked` | `T[]` | - | 체크된 노드 ID 배열 |
| `onCheck` | `(checked: T[], infos: NodeInfo<T>[]) => void` | - | 체크 변경 핸들러 |
| `initialExpanded` | `T[]` | - | 초기 펼쳐진 노드 ID 배열 |
| `initialSelected` | `T` | - | 초기 선택된 노드 ID |
| `onSelect` | `(nodeId: T, info: NodeInfo<T>) => void` | - | 노드 선택 핸들러 |
| `onExpand` | `(nodeId: T, expandedIds: T[]) => void` | - | 노드 펼침 핸들러 |
| `checkModel` | `'leaf' \| 'all' \| 'self'` | `'leaf'` | 체크 모델 (리프만/전체/자신만) |
| `onlyLeafCheckboxes` | `boolean` | `false` | 리프 노드만 체크박스 표시 |
| `forceExpand` | `boolean \| number` | - | 강제 펼침 (true 또는 깊이 숫자) |
| `expandOnClick` | `boolean` | `false` | 클릭 시 펼침 여부 |
| `checkOnClick` | `boolean` | `false` | 클릭 시 체크 여부 |
| `showChildrenCount` | `boolean` | `false` | 자식 수 표시 여부 |
| `noCheckboxes` | `boolean` | `false` | 체크박스 없애기 |
| `selectable` | `boolean \| ((node: NodeInfo<T>) => boolean)` | `false` | 선택 가능 여부 |
| `boldLabelModel` | `'parent' \| 'all' \| number \| Function` | - | 굵은 라벨 표시 모델 |
| `hideEmptyRootNode` | `boolean` | `false` | 빈 루트 노드 숨김 여부 |
| `hideCheckboxEmptyNode` | `boolean` | `false` | 자식 없는 노드 체크박스 숨김 |
| `itemHeight` | `number` | - | 가상 스크롤 아이템 높이 |
| `useKeyboardNavigation` | `boolean` | `false` | 키보드 내비게이션 사용 여부 |
| `disableCheckboxesOfNoLeaf` | `boolean` | `false` | 리프가 아닌 노드 체크박스 비활성화 |
| `controller` | `TreeController` | - | useTree로 생성한 컨트롤러 |
| `customSelectStyle` | `CSSProperties` | - | 선택된 노드 커스텀 스타일 |
| `className` | `string` | - | 추가 CSS 클래스 |

### Node 타입

```typescript
type Node<T = NodeId> = {
  id: T
  label: string
  children?: Node<T>[]
  [key: string]: any  // 추가 데이터
}
```

## 사용 예시

### 기본 트리

```tsx
import { O_Tree } from '@components/Tree'

const nodes = [
  {
    id: 1,
    label: '1팀',
    children: [
      {
        id: 2,
        label: '1-1팀',
        children: [
          { id: 3, label: '홍길동' },
          { id: 4, label: '김철수' },
        ],
      },
      { id: 5, label: '1-2팀' },
    ],
  },
  {
    id: 6,
    label: '2팀',
    children: [
      { id: 7, label: '이영희' },
    ],
  },
]

function Example() {
  return (
    <div style={{ width: 300, height: 400, border: '1px solid #e2e8f0' }}>
      <O_Tree nodes={nodes} />
    </div>
  )
}
```

### 체크박스 트리

```tsx
import { O_Tree } from '@components/Tree'
import { useState } from 'react'

const nodes = [
  {
    id: 1,
    label: '부서 A',
    children: [
      { id: 2, label: '팀 A-1' },
      { id: 3, label: '팀 A-2' },
    ],
  },
  {
    id: 4,
    label: '부서 B',
    children: [
      { id: 5, label: '팀 B-1' },
    ],
  },
]

function Example() {
  const [checked, setChecked] = useState<number[]>([2])

  return (
    <O_Tree
      nodes={nodes}
      checked={checked}
      onCheck={(checkedIds) => setChecked(checkedIds)}
      initialExpanded={[1, 4]}
    />
  )
}
```

### 선택 가능한 트리

```tsx
import { O_Tree } from '@components/Tree'
import { useState } from 'react'

const nodes = [
  { id: 1, label: '루트', children: [
    { id: 2, label: '자식 1' },
    { id: 3, label: '자식 2' },
  ]},
]

function Example() {
  const [selectedId, setSelectedId] = useState<number | null>(null)

  return (
    <O_Tree
      nodes={nodes}
      selectable
      initialSelected={selectedId ?? undefined}
      onSelect={(nodeId) => setSelectedId(nodeId)}
      noCheckboxes
    />
  )
}
```

### createNodes로 평탄한 데이터 변환

```tsx
import { O_Tree, createNodes } from '@components/Tree'

// 평탄한 데이터 (parentId로 계층 구조 표현)
const flatData = [
  { id: 1, label: '루트', parentId: null },
  { id: 2, label: '1팀', parentId: 1 },
  { id: 3, label: '2팀', parentId: 1 },
  { id: 4, label: '홍길동', parentId: 2 },
  { id: 5, label: '김철수', parentId: 2 },
]

function Example() {
  const nodes = createNodes(flatData, { parentKey: 'parentId' })

  return (
    <O_Tree
      nodes={nodes}
      initialExpanded={[1]}
    />
  )
}
```

### 트리 검색

```tsx
import { O_Tree, searchNodes } from '@components/Tree'
import { O_TextInput } from '@components/Inputs/TextInput'
import { useState, useMemo } from 'react'

const allNodes = [
  { id: 1, label: '홍길동', children: [] },
  { id: 2, label: '김철수', children: [] },
  { id: 3, label: '이영희', children: [
    { id: 4, label: '박민수', children: [] },
  ]},
]

function Example() {
  const [query, setQuery] = useState('')

  const filteredNodes = useMemo(
    () => query ? searchNodes(allNodes, query) : allNodes,
    [query]
  )

  return (
    <div>
      <O_TextInput
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="검색..."
      />
      <O_Tree nodes={filteredNodes} />
    </div>
  )
}
```

### useTree 컨트롤러

```tsx
import { O_Tree, useTree } from '@components/Tree'
import { O_Button } from '@components/Buttons'

const nodes = [
  { id: 1, label: '루트', children: [
    { id: 2, label: '자식 1' },
    { id: 3, label: '자식 2' },
  ]},
]

function Example() {
  const controller = useTree()

  return (
    <div>
      <div style={{ display: 'flex', gap: 8, marginBottom: 8 }}>
        <O_Button size="small" onClick={() => controller.expandAll()}>전체 펼치기</O_Button>
        <O_Button size="small" onClick={() => controller.collapseAll()}>전체 접기</O_Button>
        <O_Button size="small" onClick={() => controller.checkAll()}>전체 선택</O_Button>
        <O_Button size="small" onClick={() => controller.uncheckAll()}>전체 해제</O_Button>
      </div>
      <O_Tree
        nodes={nodes}
        controller={controller}
      />
    </div>
  )
}
```

### 클릭으로 체크 / 펼치기

```tsx
import { O_Tree } from '@components/Tree'

const nodes = [
  { id: 1, label: '폴더', children: [
    { id: 2, label: '파일 1' },
    { id: 3, label: '파일 2' },
  ]},
]

function Example() {
  return (
    <O_Tree
      nodes={nodes}
      expandOnClick
      checkOnClick
      noCheckboxes
    />
  )
}
```
