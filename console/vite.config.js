import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'https://team-server',
        rewrite: path => path.replace(/^\/api/, ''),
        secure: false
      },
      '/ws': {
        target: 'wss://team-server',
        ws: true,
        changeOrigin: true,
        secure: false //cert auto signé
      }
    }
  }
})
