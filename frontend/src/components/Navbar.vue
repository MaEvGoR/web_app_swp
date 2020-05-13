<template>
    <nav>
        <v-app-bar app dense color="#160F30">
            <v-img
            class="mx-2"
            src="@/assets/inno.png"
            max-height="30"
            max-width="140"
            contain
            ></v-img>
            <v-spacer></v-spacer>
            <v-btn class="white--text" color="#160F30" v-if="visibility === true" @click="signOut">
                <span>Sign out</span>
            </v-btn>
        </v-app-bar>
    </nav>
</template>

<script>
export default {
    props: {
        visibility: false
    },
    methods: {
        signOut(){
            this.$router.push('/');
            this.$store.commit("changeAuthorised", false);
        }
    }
}
</script>