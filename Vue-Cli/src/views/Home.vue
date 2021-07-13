<template>
  <div class="page-home">
    <Banner/>
    <Hot/>
    <Fine/>
    <TripFooter/>
  </div>
</template>

<script>
// @ is an alias to /src
import Banner from '@/components/home/Banner'
import Hot from '@/components/home/Hot'
import Fine from '@/components/home/Fine'
import TripFooter from '@/components/common/Footer'

export default {
  name: 'Home',
  components: {
    Banner,
    Hot,
    Fine,
    TripFooter
  },
  created () {

  }
}
</script>
<style lang="less" scoped>

</style>
