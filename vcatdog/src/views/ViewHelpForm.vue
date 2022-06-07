<template>
  <HelpForm/>
<div class="vzu1" >
   <div class="mb-3 row">
    <label class="" slogan>查看救助单</label>
    </div>
  <span class="badge text-bg-primary">动物ID:</span>
<span class="badge text-bg-info">002</span>

  <span class="badge text-bg-primary">领养情况</span>
<span class="badge text-bg-info">否</span>

  </div>
</template>

<script>
import HelpForm from '../components/HelpForm';
export default {
  name: 'ViewHelpForm',
  components: {
    HelpForm
  }
}
</script>

<style scoped>
.vzu1
{
	position:absolute;
	left:200px;
	top:60px;
}
</style>
