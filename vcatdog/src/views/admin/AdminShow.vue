<template>

  <AdNavBar>
  </AdNavBar>
</template>

<script>
import AdNavBar from '../components/AdNavBar';
export default {
  name: 'AdminShow',
  components: {
    AdNavBar
  }
}
</script>
<style scoped>
.stretch {
  transform: scale(1, 1.1);
  transform-origin: 0 0;
  font-weight: bolder;
  letter-spacing: 3px;
  color: black;
}

.card {
  background-color: transparent;
  padding-top: 5em;
}
</style>
