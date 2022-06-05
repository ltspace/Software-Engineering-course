<template>

  <AniShowCard>
  </AniShowCard>

</template>

<script>
import AniShowCard from '../components/AniShowCard';
export default {
  name: 'AnimalShow',
  components: {
    AniShowCard
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

