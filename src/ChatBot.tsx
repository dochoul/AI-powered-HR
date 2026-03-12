import { useState, useRef, useEffect } from 'react'

interface Message {
  role: 'user' | 'bot'
  text: string
  toolUsed?: string | null
  securityLevel?: string
}

const USERS = [
  { id: 'U_CEO_001', label: '이대표 (사장/경영진)', role: 'executive' },
  { id: 'U_EXEC_002', label: '박상무 (상무/경영진)', role: 'executive' },
  { id: 'U_MGR_005', label: '한승우 (개발팀장)', role: 'manager' },
  { id: 'U_EMP_006', label: '김민수 (개발팀 과장)', role: 'employee' },
  { id: 'U_HR_024', label: '강미래 (인사팀장/HR)', role: 'hr_admin' },
]

export default function ChatBot() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [userId, setUserId] = useState(USERS[0].id)
  const [loading, setLoading] = useState(false)
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const send = async () => {
    const text = input.trim()
    if (!text || loading) return

    setMessages(prev => [...prev, { role: 'user', text }])
    setInput('')
    setLoading(true)

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ slack_user_id: userId, message: text }),
      })
      const data = await res.json()
      setMessages(prev => [
        ...prev,
        {
          role: 'bot',
          text: data.response,
          toolUsed: data.tool_used,
          securityLevel: data.security_level,
        },
      ])
    } catch {
      setMessages(prev => [
        ...prev,
        { role: 'bot', text: '서버 연결에 실패했습니다. 서버가 실행 중인지 확인해 주세요.' },
      ])
    } finally {
      setLoading(false)
    }
  }

  const currentUser = USERS.find(u => u.id === userId)

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <h2 style={styles.title}>AI 인사정보 챗봇</h2>
        <span style={styles.badge}>MVP 테스트</span>
      </div>

      <div style={styles.userSelect}>
        <label style={styles.label}>접속 사용자:</label>
        <select
          value={userId}
          onChange={e => {
            setUserId(e.target.value)
            setMessages([])
          }}
          style={styles.select}
        >
          {USERS.map(u => (
            <option key={u.id} value={u.id}>
              {u.label}
            </option>
          ))}
        </select>
        <span style={{
          ...styles.roleBadge,
          backgroundColor: currentUser?.role === 'executive' ? '#2563eb' :
            currentUser?.role === 'hr_admin' ? '#7c3aed' : '#6b7280',
        }}>
          {currentUser?.role}
        </span>
      </div>

      <div style={styles.chatArea}>
        {messages.length === 0 && (
          <div style={styles.empty}>
            <p style={{ fontSize: 15, color: '#6b7280' }}>질문을 입력해 보세요.</p>
            <div style={styles.examples}>
              {['홍길동 정보 알려줘', '개발팀에 누가 있어?', '홍길동 연봉 얼마야?', '이번 달 입사한 사람 있어?'].map(q => (
                <button key={q} style={styles.exampleBtn} onClick={() => { setInput(q) }}>
                  {q}
                </button>
              ))}
            </div>
          </div>
        )}

        {messages.map((msg, i) => (
          <div key={i} style={{ display: 'flex', justifyContent: msg.role === 'user' ? 'flex-end' : 'flex-start', marginBottom: 12 }}>
            <div style={{
              ...styles.bubble,
              backgroundColor: msg.role === 'user' ? '#2563eb' : '#f3f4f6',
              color: msg.role === 'user' ? '#fff' : '#111827',
              borderRadius: msg.role === 'user' ? '16px 16px 4px 16px' : '16px 16px 16px 4px',
            }}>
              <pre style={styles.msgText}>{msg.text}</pre>
              {msg.role === 'bot' && msg.toolUsed && (
                <div style={styles.meta}>
                  <span style={styles.metaTag}>{msg.toolUsed}</span>
                  {msg.securityLevel === 'confidential' && (
                    <span style={{ ...styles.metaTag, backgroundColor: '#fef2f2', color: '#dc2626' }}>기밀</span>
                  )}
                </div>
              )}
            </div>
          </div>
        ))}

        {loading && (
          <div style={{ display: 'flex', justifyContent: 'flex-start', marginBottom: 12 }}>
            <div style={{ ...styles.bubble, backgroundColor: '#f3f4f6' }}>
              <span style={{ color: '#9ca3af' }}>답변 생성 중...</span>
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      <div style={styles.inputArea}>
        <input
          style={styles.input}
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && send()}
          placeholder="직원 이름, 부서, 직급 등에 대해 질문해 주세요"
          disabled={loading}
        />
        <button style={styles.sendBtn} onClick={send} disabled={loading || !input.trim()}>
          전송
        </button>
      </div>
    </div>
  )
}

const styles: Record<string, React.CSSProperties> = {
  container: {
    maxWidth: 640,
    margin: '0 auto',
    height: '100vh',
    display: 'flex',
    flexDirection: 'column',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
  },
  header: {
    padding: '16px 20px',
    borderBottom: '1px solid #e5e7eb',
    display: 'flex',
    alignItems: 'center',
    gap: 10,
  },
  title: { margin: 0, fontSize: 18, fontWeight: 700 },
  badge: {
    fontSize: 11,
    padding: '2px 8px',
    borderRadius: 10,
    backgroundColor: '#fef3c7',
    color: '#92400e',
    fontWeight: 600,
  },
  userSelect: {
    padding: '10px 20px',
    borderBottom: '1px solid #e5e7eb',
    display: 'flex',
    alignItems: 'center',
    gap: 8,
    backgroundColor: '#fafafa',
  },
  label: { fontSize: 13, color: '#6b7280', whiteSpace: 'nowrap' },
  select: {
    flex: 1,
    padding: '6px 10px',
    border: '1px solid #d1d5db',
    borderRadius: 6,
    fontSize: 13,
    backgroundColor: '#fff',
  },
  roleBadge: {
    fontSize: 11,
    padding: '2px 8px',
    borderRadius: 10,
    color: '#fff',
    fontWeight: 600,
    whiteSpace: 'nowrap',
  },
  chatArea: {
    flex: 1,
    overflowY: 'auto',
    padding: 20,
  },
  empty: { textAlign: 'center', paddingTop: 60 },
  examples: { display: 'flex', flexWrap: 'wrap', gap: 8, justifyContent: 'center', marginTop: 16 },
  exampleBtn: {
    padding: '8px 14px',
    border: '1px solid #d1d5db',
    borderRadius: 20,
    backgroundColor: '#fff',
    fontSize: 13,
    cursor: 'pointer',
    color: '#374151',
  },
  bubble: {
    maxWidth: '80%',
    padding: '10px 14px',
  },
  msgText: {
    margin: 0,
    whiteSpace: 'pre-wrap',
    wordBreak: 'break-word',
    fontSize: 14,
    lineHeight: 1.6,
    fontFamily: 'inherit',
  },
  meta: { display: 'flex', gap: 6, marginTop: 6 },
  metaTag: {
    fontSize: 10,
    padding: '1px 6px',
    borderRadius: 4,
    backgroundColor: '#eff6ff',
    color: '#2563eb',
  },
  inputArea: {
    padding: '12px 20px',
    borderTop: '1px solid #e5e7eb',
    display: 'flex',
    gap: 8,
  },
  input: {
    flex: 1,
    padding: '10px 14px',
    border: '1px solid #d1d5db',
    borderRadius: 8,
    fontSize: 14,
    outline: 'none',
  },
  sendBtn: {
    padding: '10px 20px',
    backgroundColor: '#2563eb',
    color: '#fff',
    border: 'none',
    borderRadius: 8,
    fontSize: 14,
    fontWeight: 600,
    cursor: 'pointer',
  },
}
