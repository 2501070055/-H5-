<template>
  <div class="page-sight-image">
    <van-pull-refresh v-model="refreshing" @refresh="onRefresh">
      <van-list
        class="sight-comment"
        v-model="loading"
        :finished="finished"
        finished-text="没有更多了"
        :error.sync="error"
        error-text="请求失败，点击重新加载"
        @load="getImageList"
      >
        <van-image
          v-for="(item, index) in imageList"
          :key="index"
          :src="item.image"
        />
      </van-list>
    </van-pull-refresh>
  </div>
</template>
<script>
import { ajax } from '@/utils/ajax'
import { SightApi } from '@/utils/apis'
export default {
  data () {
    return {
      id: '',
      // 评论列表
      imageList: [],
      loading: false,
      finished: false,
      error: false,
      refreshing: false,
      // 当前页
      currentPage: 1
    }
  },
  methods: {
    goBack () {
      this.$router.go(-1)
    },
    /**
     * 下拉刷新
    */
    onRefresh () {
      // 清空数据
      this.imageList = []
      this.currentPage = 1

      this.finished = false
      this.error = false
      this.loading = true

      // 从新加载数据
      this.getImageList()
    },
    /**
     * 评论列表
    */
    getImageList () {
      const url = SightApi.sightImageUrl.replace('#{id}', this.id)
      ajax.get(url, {
        params: {
          page: this.currentPage
        }
      }).then(({ data: { meta, objects } }) => {
        this.imageList = this.imageList.concat(objects)
        // 加载状态结束
        this.loading = false
        this.currentPage = meta.current_page + 1
        // 数据全部加载完成
        if (this.currentPage > meta.page_count) {
          this.finished = true
        }
        this.refreshing = false
      }).catch(() => {
        this.loading = false
        this.error = true
        this.refreshing = false
      })
    }
  },
  mounted () {
    this.id = this.$route.params.id
    // this.getCommentList()
  }
}
</script>
<style lang="less">
.page-sight-image {
  margin: 10px 10px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  .van-image {
    width: 45%;
    margin-bottom: 15px;
    .van-image__img {
        width: 100%;
    }
  }
}
</style>
