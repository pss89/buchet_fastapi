import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  server:{ // 임의로 변경 (docker port 사용을 위함)
    host: '0.0.0.0',
    // port: 8080, // 주석제거 (기존 port인 5173으로 사용하기)
    watch: {
      usePolling: true,
      // interval: 1000,
    },
  },
  plugins: [svelte()],
})
