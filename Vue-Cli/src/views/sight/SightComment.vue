<template>
  <div class="page-sight-comment">
    <!-- 页面头部 -->
    <van-nav-bar
      left-text="返回"
      left-arrow
      @click-left="goBack"
      title="景点评论"
    />
    <van-pull-refresh v-model="refreshing" @refresh="onRefresh">
      <van-list
        class="sight-comment"
        v-model="loading"
        :finished="finished"
        finished-text="没有更多了"
        :error.sync="error"
        error-text="请求失败，点击重新加载"
        @load="getCommentList"
      >
        <CommentItem
          v-for="item in commentList"
          :key="item.pk"
          :item="item"
        />
      </van-list>
    </van-pull-refresh>
  </div>
</template>
<script>
// 评论列表
import CommentItem from '@/components/sight/CommentItem'
import { ajax } from '@/utils/ajax'
import { SightApi } from '@/utils/apis'
export default {
  components: {
    CommentItem
  },
  data () {
    return {
      id: '',
      // 评论列表
      commentList: [],
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
      this.commentList = []
      this.currentPage = 1

      this.finished = false
      this.error = false
      this.loading = true

      // 从新加载数据
      this.getCommentList()
    },
    /**
     * 评论列表
    */
    getCommentList () {
      const url = SightApi.sightCommentUrl.replace('#{id}', this.id)
      ajax.get(url, {
        params: {
          page: this.currentPage
        }
      }).then(({ data: { meta, objects } }) => {
        this.commentList = this.commentList.concat(objects)
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
.page-sight-comment {
  background-color: #fff;
}
</style>
