<template>
  <HelpForm/>
<div class="fzu1" >
   <div class="mb-3 row">
    <label class="" slogan>填写新救助单</label>
    </div>


<div class="form-group">
    <label class="col-sm-2 control-label">附件:</label>
    <div class="col-sm-7">
        <input id="myfile" type="file" style="display: none" multiple>
        <!--显示上传的文件名字-->
        <input type="text" id="FileCover" class="form-control" readonly="true">
    </div>
    <div class="col-sm-1">
        <button class="btn btn-primary btn-sm " type="button" onclick="$('input[id=myfile]').click();">
            <i class="fa fa-folder-open" id="browse">&nbsp;&nbsp;浏览</i>
        </button>
    </div>
    <div class="col-sm-1">
        <button class="btn btn-primary btn-sm " type="button" onclick="MyUpload()">
            <i class="fa fa-send" id="upload_status">&nbsp;&nbsp;上传</i>
        </button>
    </div>
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
