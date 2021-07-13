<template>
  <div class="page-order-info">
    <van-nav-bar title="我的订单"
      left-text="返回"
      :right-text="constants.ORDER_STATUS[itemInfo.status]"
      left-arrow
      @click-left="goBack"/>
    <!-- 订单流水号 -->
    <h4>订单信息</h4>
    <van-cell title="订单号" :value="itemInfo.sn" class="order-mum" />
    <van-cell title="下单时间" :value="itemInfo.created_at" class="order-mum" />
    <h4>订单明细</h4>
    <div class="order-item" v-for="item in itemInfo.items" :key="item.pk">
      <div class="order-body">
        <div class="left">
          <van-image width="100" height="100" :src="item.flash_img" />
        </div>
        <div class="right">
          <div class="title">{{ item.flash_name }}</div>
          <div class="remark">{{ item.remark }}</div>
        </div>
      </div>
      <h4>订单总计</h4>
      <div class="order-footer">
        <div>总共{{ itemInfo.buy_count }}件商品 合计 ￥{{ itemInfo.buy_amount }}</div>
        <van-button round size="small" type="warning"
          v-if="itemInfo.status == constants.ORDER_STATUS_PAY"
          @click="goPay()">待支付</van-button>
        <van-button round size="small" type="warning"
          v-if="itemInfo.status == constants.ORDER_STATUS_DONE || itemInfo.status == constants.ORDER_STATUS_CANCEL"
          @click="deleteOrder()">删除订单</van-button>
      </div>
    </div>
  </div>
</template>
<script>
import { OrderApis } from '@/utils/apis'
import { ajax } from '@/utils/ajax'
import * as constants from '@/utils/constants'
export default {
  data () {
    return {
      sn: 123333,
      // 订单列表
      itemInfo: {},
      constants
    }
  },
  methods: {
    deleteOrder () {
      // 弹框确认
      this.$dialog.confirm({
        title: '温馨提示',
        message: '确认删除订单？'
      }).then(() => {
        // TODO 调用接口
        const url = OrderApis.orderDetailUrl.replace('#{sn}', this.sn)
        // delete调用接口
        ajax.delete(url).then(res => {
          console.log(res)
          // 用户提示,删除成功
          if (res.status === 201) {
            this.$notify({
              type: 'success',
              message: '订单成功删除'
            })
            this.itemInfo.sn = ''
          } else if (res.status === 200) {
            this.$notify({
              type: 'warning',
              message: '订单已被删除'
            })
          }
        })
      })
    },
    goBack () {
      this.$router.go(-1)
    },
    /**
     * 加载页面的数据
     */
    loadData () {
      // 订单状态
      this.sn = this.$route.params.sn
      // console.log('===', this.status, this.$route.params.status)
      // 清空数据
      this.itemInfo = {}
      // 加载数据列表
      this.getItemInfo()
    },
    /**
     * 跳转支付页面
    */
    goPay () {
      this.$router.push({ name: 'OrderPay', params: { sn: this.sn } })
    },
    /**
     * 加载订单列表
     */
    getItemInfo () {
      const url = OrderApis.orderDetailUrl.replace('#{sn}', this.sn)
      ajax.get(url).then(({ data }) => {
        this.itemInfo = data
      })
    }
  },
  created () {
    this.loadData()
  }
}
</script>
<style lang="less">
.page-order-info {
  h4 {
    text-align: left;
    padding: 5px 10px;
    margin: 0;
  }
  .order-mum {
    .van-cell__value {
      flex: 3;
    }
    .van-cell__title {
      text-align: left;
    }
  }
  .order-item {
    .order-body {
      padding: 10px 10px;
      background: #fff;
      display: flex;
      .left {
        width: 100px;
        height: 100px;
      }
      .right {
        flex: 1;
        text-align: left;
        padding-left: 10px;
        .title {
          padding-bottom: 5px;
          font-size: 16px;
        }
        .remark {
          font-size: 12px;
          color: #999;
        }
      }
    }
    .order-footer {
      background: #fff;
      text-align: right;
      padding-right: 10px;
      padding: 10px 10px;
      div {
        padding-bottom: 10px;
      }
    }
  }
}
</style>
