# AI HR Chatbot

## 시작하기

### 1. 환경변수 파일 준비

`server/.env` 파일을 생성하고 아래 내용을 채운다:

```env
GEMINI_API_KEY=your_gemini_api_key

SLACK_BOT_TOKEN=xoxb-...
SLACK_SIGNING_SECRET=...
SLACK_APP_TOKEN=xapp-...
```

### 2. 서버 실행

```bash
docker compose up
```

DB(PostgreSQL)와 백엔드 서버가 함께 실행된다.

### 3. 샘플 데이터 삽입 (최초 1회)

```bash
docker compose exec server python -m server.seeds.sample_data
```

### 4. API 확인

- Swagger UI: http://localhost:8000/docs

---

## 테스트용 계정

| slack_user_id | 이름 | 역할 | 챗봇 접근 | 연봉 조회 |
|---|---|---|---|---|
| `U_CEO_001` | 이대표 | executive | O | O |
| `U_EXEC_002` | 박상무 | executive | O | O |
| `U_HR_024` | 강미래 | hr_admin | X | - |
| `U_MGR_005` | 한승우 | manager | X | - |
| `U_EMP_006` | 김민수 | employee | X | - |

### 요청 예시

```json
{
  "slack_user_id": "U_CEO_001",
  "message": "홍길동 정보 알려줘"
}
```
