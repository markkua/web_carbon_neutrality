<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="left = !left" />

        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar>
          Carbon Neutrality -- Where are we
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="left" side="left" overlay elevated>
      <!-- drawer content -->
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>



<script>
import { defineComponent, ref } from 'vue'
// import EssentialLink from 'components/EssentialLink.vue'

export default defineComponent({
  name: 'MainLayout',

  components: {
    // EssentialLink
  },

  data () {
    return {
      left: false
    }
  },

  setup () {
    const leftDrawerOpen = ref(false)

    return {
      // essentialLinks: linksList,
      // leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
})
</script>
