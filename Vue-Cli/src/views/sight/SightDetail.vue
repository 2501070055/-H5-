<template>
    <div class="page-sight-list">
      <!-- 页面头部 -->
      <van-nav-bar
        left-text="返回"
        left-arrow
        @click-left="goBack"
        fixed
      />
      <!-- 大图 -->
      <div class="sight-banner">
        <van-image
          width="100%"
          height="100%"
          :src="sightDetail.img"
        />
        <div class="tips">
          <router-link class="pic-sts" :to="{ name: 'SightImage', params: { id: id } }">
            <van-icon name="photo-o" /><span>{{ sightDetail.image_count }}</span>
          </router-link>
          <div class="title">{{ sightDetail.name }}</div>
        </div>
      </div>
      <!-- 评分，景点介绍 -->
      <div class="sight-info">
        <div class="right" @click="goPage">
          <div class="info-title">
            <strong>{{ sightDetail.score }}分</strong>
            <small>很棒</small>
          </div>
          <div class="info-tips">{{ sightDetail.comment_count }} 评论</div>
          <van-icon name="arrow" />
        </div>
        <div class="left">
          <div class="info-title">
            <span>景点介绍</span>
          </div>
          <div class="info-tips">开放时间</div>
          <van-icon name="arrow" />
        </div>
      </div>
      <!-- 地址信息 -->
      <van-cell
        :title="fullArea"
        icon="location-o"
        is-link
        :title-style="{ 'text-align': 'left' }" >
        <!-- 使用 right-icon 插槽来自定义右侧图标 -->
        <template #right-icon>
          <van-icon name="arrow" />
        </template>
      </van-cell>
      <!-- 门票列表 -->
      <div class="sight-ticket">
        <van-cell title="门票" icon="bookmark-o" :title-style="{ 'text-align': 'left' }"/>
        <div class="ticcket-item" v-for="item in ticketList" :key="item.pk">
          <div class="left">
            <div class="title">{{ item.name }}</div>
            <div class="tips">
              <van-icon name="clock-o" />
              <span>{{ item.desc }}</span>
            </div>
            <div class="tags">
              <van-tag mark type="primary">标签1</van-tag>
            </div>
          </div>
          <div class="right">
            <div class="price">
              <span>$</span>
              <strong>{{ item.sell_price }}</strong>
            </div>
            <router-link :to="{ name: 'OrderSubmit', params: { id: item.pk } }">
              <van-button type="warning" size="samll" round>预订</van-button>
            </router-link>
          </div>
        </div>
      </div>
      <!-- 用户评价 -->
      <div class="sight-comment">
        <van-cell title="热门评论" icon="comment-o" :title-style="{ 'text-align': 'left' }"/>
        <CommentItem
          v-for="item in commentList"
          :key="item.pk"
          :item="item"
        />
        <router-link :to="{ name: 'SightComment', params: { id: id } }" class="link-more">查看更多</router-link>
      </div>
    </div>
</template>
<script>
// 评论列表
import CommentItem from '@/components/sight/CommentItem'
import { ajax } from '@/utils/ajax'
import { SightApi } from '@/utils/apis'
export default {
  data () {
    return {
      id: '',
      // 景点详细信息
      sightDetail: {},
      // 门票列表
      ticketList: [],
      // 评论列表
      commentList: []
    }
  },
  components: {
    CommentItem
  },
  computed: {
    /**
     * 地址全部信息
    */
    fullArea () {
      let area = this.sightDetail.province + this.sightDetail.city
      if (this.sightDetail.area) {
        area += this.sightDetail.area
      }
      if (this.sightDetail.town) {
        area += this.sightDetail.town
      }
      return area
    }
  },
  watch: {
    $route () {
      this.loadData()
    }
  },
  methods: {
    /**
     * 跳转评论列表
    */
    goPage () {
      this.$router.push({ name: 'SightComment', params: { id: this.id } })
    },
    loadData () {
      this.id = this.$route.params.id
      this.getSightDetail()
      this.getTicketList()
      this.getCommentList()
    },
    goBack () {
      this.$router.go(-1)
    },
    /**
     * 获取景点详细信息
    */
    getSightDetail () {
      const url = SightApi.sightDetailUrl.replace('#{id}', this.id)
      ajax.get(url).then(({ data }) => {
        this.sightDetail = data
      })
    },
    /**
     * 门票列表
    */
    getTicketList () {
      const url = SightApi.sightTicketUrl.replace('#{id}', this.id)
      ajax.get(url).then(({ data: { objects } }) => {
        this.ticketList = objects
      })
    },
    /**
     * 评论列表
    */
    getCommentList () {
      const url = SightApi.sightCommentUrl.replace('#{id}', this.id)
      ajax.get(url).then(({ data: { objects } }) => {
        this.commentList = objects
      })
    }
  },
  created () {
    this.loadData()
  }
}
</script>
<style lang="less">
.page-sight-list {
  .van-nav-bar {
    background-color: transparent;
  }
  // 景点大图
  .sight-banner {
    position: relative;
    .tips {
      position: absolute;
      left: 10px;
      bottom: 10px;
      font-size: 16px;
      color: #000;
      .pic-sts {
        position: relative;
        display: block;
        width: 32px;
        text-align: right;
        padding-right: 5px;
        color: #000;
        border-radius: 30px;
        font-size: 10px;
        background-color: rgba(0, 0, 0, 0.4);
        .van-icon {
          position: absolute;
          top: 1px;
          left: 7px;
        }
      }
    }
  }
  // 评分和景点介绍
  .sight-info {
    display: flex;
    background-color: #fff;
    border-bottom: 1px solid #f6f6f6;
    & > div {
      flex: 1;
      position: relative;
    }
    .right {
      border-left: 1px solid #f6f6f6;
    }
    .info-title {
      text-align: left;
      padding: 5px 10px;
      strong {
        color: #ff8300;
      }
    }
    .info-tips {
      color: #999;
      font-size: 12px;
      text-align: left;
      padding: 5px 10px;
    }
    .van-icon {
      position: absolute;
      right: 5px;
      top: 5px;
    }
  }
  // 地址信息
  .van-cell {
    background-color: #fff;
    position: relative;
    .van-icon-arrow {
      position: absolute;
      top: 15px;
      right: 5px;
    }
  }
  // 门票列表
  .sight-ticket {
    margin-top: 10px;
    background-color: #fff;
    .ticcket-item {
      display: flex;
      border-bottom: 1px solid #f6f6f6;
      padding-bottom: 10px;
      .left {
        flex: 1;
        text-align: left;
        padding: 5px 10px;
        .title {
          padding: 5px 0;
        }
        .tips {
          font-size: 12px;
          position: relative;
          width: 105px;
          height: 20px;
          .van-icon-clock-o {
            position: absolute;
            top: 2px;
          }
          span {
            position: absolute;
            left: 14px;
          }
        }
      }
      .right {
        padding-top: 10px;
        width: 100px;
        .price {
          color: #ff9800;
          strong {
            font-size: 20px;
          }
        }
        .van-button {
          padding: 0 5px;
        }
      }
    }
  }
  // 评论列表
  .sight-comment {
    margin-top: 10px;
    background-color: #fff;
  }
  // 查看更多
  .link-more {
    display: block;
    color: #666;
    padding: 10px;
  }
}
</style>
