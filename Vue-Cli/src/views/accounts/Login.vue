<template>
  <div class="page-account-login">
    <!-- 导航 -->
    <van-nav-bar
      title="用户登录"
      left-text="返回"
      left-arrow
      @click-left="goBack"
    />
    <!-- 表单输入 -->
    <van-form @submit="onSubmit">
      <van-field
        v-model="username"
        label="用户名"
        placeholder="用户名"
        type="tel"
        maxlength="11"
        clearable
        :rules="ruleName"
      />
      <van-field
        v-model="password"
        type="password"
        label="密码"
        placeholder="密码"
        :rules="[{ required: true, message: '请填写密码' }]"
      />
      <div style="margin: 16px;">
        <van-button round block type="info" native-type="submit">提交</van-button>
      </div>
    </van-form>
    <!-- 文字提示 -->
    <div class="tips">
      登录表示同意，<a href="#">用户使用协议</a>-<a href="#">隐私条款</a>
    </div>
    <div class="tips">
      没有账号？<router-link :to="{ name: 'AccountRegister' }">点击注册>></router-link>
    </div>
    <!-- 版权 -->
    <Copyright/>
  </div>
</template>
<script>
import { AccountsApis } from '@/utils/apis'
import { ajax } from '@/utils/ajax'
import * as types from '@/store/mutation-types'
import Copyright from '@/components/common/Copyright'
export default {
  components: {
    Copyright
  },
  data () {
    return {
      // 用户名验证规则
      ruleName: [{
        required: true,
        message: '请填写用户名'
      }, {
        pattern: /1\d{10}/,
        message: '请填写正确的手机号'
      }],
      username: '',
      password: ''
    }
  },
  methods: {
    // 提交表单
    onSubmit () {
      // 1. 调用接口
      ajax.post(AccountsApis.loginUrl, {
        username: this.username,
        password: this.password
      }).then(({ data }) => {
        // 2. 拿到用户信息，存储到到vuex
        this.$store.commit(types.UPDATE_USER_INFO, data)
        this.$toast('登录成功')
        this.$router.replace({ name: 'Mine' })
      }).catch(({ response: { data } }) => {
        // 3. 如果出现了异常，需要提示信息
        this.$toast(`${data.error_code},${data.error_msg}`)
      })
    },
    goBack () {
      this.$router.go(-1)
    }
  }
}
</script>
