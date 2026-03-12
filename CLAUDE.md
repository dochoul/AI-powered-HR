# 프로젝트 참고 자료

## 디자인 시스템
- Hiworks Design System: https://hiworks-design-system.hiworks.com/?path=/docs/%EC%95%88%EB%82%B4-%EB%AC%B8%EC%84%9C--docs
- 자체 서명 SSL 인증서를 사용하므로 `curl -k`로 접근해야 함

### 컴포넌트 목록 조회
```bash
curl -k -s "https://hiworks-design-system.hiworks.com/index.json" | python3 -c "
import json, sys
data = json.load(sys.stdin)
entries = data['entries']
titles = sorted(set(v['title'] for v in entries.values()))
for t in titles:
    print(t)
"
```

### 특정 컴포넌트 문서 조회
`index.json`의 `importPath` 값을 이용해 MDX 파일에 직접 접근:
```bash
# 예시: 오피스 플랫폼 Button 문서
curl -k -s "https://hiworks-design-system.hiworks.com/src/stories/demos/core/Button/office/Button.mdx"
```

### 플랫폼 구성
- **오피스 플랫폼** - office.hiworks.com 등 오피스 제품군
- **경영 플랫폼** - 경영 관련 제품군
- **하이웍스 관리** - 하이웍스 관리자 제품군

## 컴포넌트 예시
@.claude/components/O_Button.md
