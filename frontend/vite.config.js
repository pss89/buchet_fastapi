import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  server:{ // 임의로 변경 (docker port 사용을 위함)
    host: '0.0.0.0',
    port: 8080,
  },
  plugins: [svelte()],
})
