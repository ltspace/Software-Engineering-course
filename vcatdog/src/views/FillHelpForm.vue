<template>
  <HelpForm/>
<div class="fzu1" >
   <div class="mb-3 row">
    <label class="" slogan>填写新救助单</label>
    </div>

  </div>
</template>

<script>
import HelpForm from '../components/HelpForm';
export default {
  name: 'FillHelpForm',
  components: {
    HelpForm
  }
}
</script>

<style scoped>
.fzu1
{
	position:absolute;
	left:200px;
	top:60px;
}
</style>
