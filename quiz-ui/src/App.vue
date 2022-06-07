<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <nav class="nav">
      <div>
        <img alt="Vue logo" class="logo" src="@/assets/images/logo2.png" width="" height="30" />
      </div>
      <div>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/admin">Admin</RouterLink>
      </div>
    </nav>
  </header>

  <RouterView />
</template>

<style>
@import "@/assets/base.css";
@import url("https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@200&display=swap");
</style>
