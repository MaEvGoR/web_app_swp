<template>
	<v-app>
    <Navbar :visibility="this.$store.state.authorised"></Navbar>
    <v-content>
      <router-view />
    </v-content>
    <v-footer
      color="#160F30"
      app
    >
      <span class="white--text">&copy; 2019</span>
    </v-footer>
	</v-app>
</template>

<script>

import Navbar from '@/components/Navbar'

export default {
  name: 'App',
  components: { Navbar }
}

</script>