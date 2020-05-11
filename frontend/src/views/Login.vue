<template>
  <v-container
      style="background: #eae7af;"
      fluid
      fill-height
    >
    <v-layout align-center justify-center row fill-height>
      <v-flex
        xs12
        sm8
        md4
        offset-xs1
      >
        <v-card class="mx-auto mt-5">
          <v-toolbar color = "#241663"
            dark
            flat>
            <v-toolbar-title>
              Login
            </v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field 
                label="Username"
                hint="Innopolis email"
                prepend-icon="mdi-account-circle" 
                v-model="email"/>
              <v-text-field
                :type="showPassword ? 'text' : 'password'"
                label="Password"
                prepend-icon="mdi-lock"
                :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                v-model="password"
                @click:append="showPassword = !showPassword"/>
            </v-form>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <!-- <v-btn color="success">Register</v-btn> -->
            <v-spacer></v-spacer>
            <v-btn dark color="#241663" @click="login">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>    
</template>

<script>
  export default {
    props: {
      source: String,
    },
    data() {
      return {
        email: '',
        password: '',
        showPassword: false,
        user: null
      };
    },
    methods: {
      async login() {
        const response = await fetch('/api/log_in', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password,
          }),
        });
        if(!response.ok) return;
        const json = await response.json();
        this.user = json;
        this.$store.commit("changeStatus", this.user.status);
        this.$store.commit("changeId", this.user._id);
        this.$router.push({path:`/${this.user.status}`});
        this.email = '';
        this.password = '';
      }
    } 
  }
</script>