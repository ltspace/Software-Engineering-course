<template>
  <UNavBar />
      <div class="azu1" style="float:center">
          
  <div style="position: absolute;">
    <img src="../assets/left.png" class="d-block w-100" style="border-radius: 10%" alt="...">
    <div class="carousel-caption d-none d-md-block" >


          <h2>This cat can be coquettish and cute</h2>
        </div>
    </div>
    
       <div class="azu2" >
  <img src="../assets/Background.png" style="border-radius: 10%" alt="...">

</div> 

<div class="azu3" style="float:right">
    <h2>Adopt me</h2>
  <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">ID&emsp;&emsp;&emsp;&emsp;</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="001">
    </div>
  </div>
  <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">Name&emsp;&emsp;&emsp;&emsp;</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="果冻">
    </div>
  </div>
    <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">Sex&emsp;&emsp;&emsp;&emsp;</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="母">
    </div>
  </div>
    <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">Catvatar&emsp;&emsp;&emsp;&emsp;</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="英国短毛猫">

    </div>
  </div>
      <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">Category&emsp;&emsp;&emsp;&emsp;</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="猫">
    </div>
  </div>
      <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">Vaccine stuation&emsp;&emsp;&emsp;&emsp;</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="已接种猫三联">
    </div>

  </div>
</div>
<div class="azu5" style="float:right">
     <button type="button" class="btn btn-dark">申请领养</button>
</div>


<div class="azu4" style="float:right">
   
  <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">Address&emsp;&emsp;&emsp;&emsp;</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="贝克街221B">
    </div>
  </div>
  <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">Age&emsp;&emsp;&emsp;&emsp;</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="5个月">
    </div>
  </div>
    <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">Fur color&emsp;&emsp;&emsp;&emsp;</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="黑白相间">
    </div>
  </div>
    <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">Character&emsp;&emsp;&emsp;&emsp;</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="性格温和">

    </div>
  </div>
      <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">Disease situation&emsp;&emsp;&emsp;&emsp;</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="无疾病史">
    </div>
  </div>
      <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">Sterilize&emsp;&emsp;&emsp;&emsp;</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="已绝育">
    </div>
   

  </div>
</div>
  </div>



</template>

<script>
import UNavBar from '../components/UNavBar';
export default {
  name: 'AdoptionInfo',
  components: {
     UNavBar
  }
}
</script>
<style scoped>
.azu1 {  
        position: absolute;
  padding-top: 0em;
  padding-bottom: 0em;
}

.azu2 {  
  padding-top: 1em;
  padding-bottom: 1em;
} 
.a.router-link-exact-active {
  color: black;
}

.carousel {
  font-family: YouYuan, Avenir, Helvetica, Arial, sans-serif;
  width: 100rem;
  text-align: center;
  border-radius: 20%;
  transform: scale(1, 1.1);
  transform-origin: 0 0;
  font-weight: bolder;
  letter-spacing: 3px;
}

.center-in-center {
  position: absolute;
  top: 55%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  -o-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
.azu3
{
	position:absolute;
	left:900px;
	top:150px;
}
.azu4
{
	position:absolute;
	left:1100px;
	top:200px;
}
.azu5
{
	position:absolute;
	left:1050px;
	top:580px;
}

</style>





