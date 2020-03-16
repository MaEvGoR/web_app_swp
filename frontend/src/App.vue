<template>
	<v-app>
    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-toolbar-title>Software Project</v-toolbar-title>
    </v-app-bar>
    <v-content>
      <router-view />
    </v-content>
    <v-footer
      color="indigo"
      app
    >
      <span class="white--text">&copy; 2019</span>
    </v-footer>
	</v-app>
</template>

<script>
export default {
	name: 'App',
}

</script>