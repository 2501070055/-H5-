<template>
  <div class="home-fine-box">
    <van-cell
      title="精选景点"
      con="location-o"
      is-link value="更多"
      title-style="text-align: left"
      :to="{ name: 'Search', query: { isTop: 1 } }"
    />
    <div class="box-main">
      <SightItem v-for="item in dataList" :key="item.id" :item="item" />
    </div>
  </div>
</template>
<script>
import SightItem from '@/components/common/ListSight'
import { ajax } from '@/utils/ajax'
import { SightApi } from '@/utils/apis'
export default {
  components: {
    SightItem
  },
  data () {
    return {
      dataList: []
    }
  },
  methods: {
    /**
     * 查询精选景点数据
    */
    getDataList () {
      ajax.get(SightApi.sightListCacheUrl, {
        params: {
          is_top: 1
        }
      }).then(({ data }) => {
        this.dataList = data.objects
      })
    }
  },
  created () {
    // 获取接口数据
    this.getDataList()
  }
}
</script>
<style lang="less">
  .home-fine-box {
    padding: 0 10px;
    .van-cell {
      padding: 10px 0;
    }
    .box-main {
      padding-bottom: 50px;
    }
  }
</style>
