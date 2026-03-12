import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import ChatBot from './ChatBot'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ChatBot />
  </StrictMode>,
)
