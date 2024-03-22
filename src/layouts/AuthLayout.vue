<template>
  <VaLayout v-if="breakpoint.lgUp" class="h-screen bg-[var(--va-background-secondary)]">
    <template #left>
      <div
        class="h-full flex items-center justify-center"
        style="width: 35vw; background-color: black"
        aria-label="logo"
      >
        <LogoLogin :height="28" start="#FFFF" />
      </div>
    </template>
    <template #content>
      <main class="h-full flex items-center justify-center mx-auto max-w-[420px]">
        <RouterView />
      </main>
    </template>
  </VaLayout>
</template>

<script lang="ts" setup>
import { useBreakpoint } from 'vuestic-ui'
import LogoLogin from '../components/Logo_login.vue'

const breakpoint = useBreakpoint()
</script>
