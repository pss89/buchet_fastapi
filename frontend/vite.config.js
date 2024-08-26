import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  server:{
    // host: '0.0.0.0', // docker 환경에서만
    // port: 5173, // docker 환경에서만
    port: 3000, // node 로컬 환경 port 
    watch: {
      usePolling: true,
      interval: 1000,
    },
  },
  plugins: [svelte()],
})
