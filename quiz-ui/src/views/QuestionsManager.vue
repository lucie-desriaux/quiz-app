<template>
  <h1>Questions manager</h1>
  <button type="button" class="btn btn-outline-danger" @click="launchScore">
    GO!
  </button>
</template>

<script>
export default {
  name: "HomePage",
  data() {
    return {};
  },
  methods: {
    launchScore() {
      this.$router.push("/score");
    }
  }
};
</script>

<style>
</style>
