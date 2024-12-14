import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'

import GET from './get.jsx'
import App from "./App.jsx"
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <GET />
  </StrictMode>,
)
