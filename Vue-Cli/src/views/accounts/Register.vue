<template>
  <div class="page-account-register">
    <!-- 导航 -->
    <van-nav-bar
      title="用户注册"
      left-text="返回"
      left-arrow
      @click-left="goBack"
    />
    <!-- 表单输入 -->
    <van-form @submit="onSubmit">
      <van-field
        v-model="form.username"
        label="手机号码"
        placeholder="手机号码"
        type="tel"
        maxlength="11"
        clearable
        @input="onPhoneChange"
        :rules="ruleName"
      />
      <van-field
        v-model="form.sms_code"
        center
        clearable
        label="短信验证码"
        placeholder="请输入短信验证码"
        :rules="[{ required: true, message: '请输入短信验证码' }]"
      >
        <template #button>
          <SendSmsCode ref="refSms" :phoneNum='form.username'/>
        </template>
      </van-field>
      <van-field
        v-model="form.nickname"
        label="用户昵称"
        placeholder="用户昵称"
        maxlength="32"
        clearable
        :rules="[{ required: true, message: '请输入用户昵称' }]"
      />
      <van-field
        v-model="form.password"
        type="password"
        label="密码"
        placeholder="密码"
        :rules="[{ required: true, message: '请填写密码' }]"
      />
      <van-field
        v-model="form.passwordRepeat"
        type="password"
        label="确认密码"
        placeholder="确认密码"
        :rules="rulePassword"
      />
      <div style="margin: 16px;">
        <van-button round block type="info" native-type="submit">提交</van-button>
      </div>
    </van-form>
    <!-- 文字提示 -->
    <div class="tips">
      注册表示同意，<a href="#">用户使用协议</a>-<a href="#">隐私条款</a>
    </div>
    <div class="tips">
      已有账号<router-link :to="{ name: 'AccountLogin' }">点击登录>></router-link>
    </div>
    <!-- 版权 -->
    <Copyright/>
  </div>
</template>
<script>
import { ajax } from '@/utils/ajax'
import { AccountsApis } from '@/utils/apis'
import * as types from '@/store/mutation-types'
import Copyright from '@/components/common/Copyright'
import SendSmsCode from '@/components/common/SendSmsCode'
export default {
  components: {
    Copyright,
    SendSmsCode
  },
  data () {
    return {
      id: '1',
      // 用户名验证规则
      ruleName: [{
        required: true,
        message: '请填写用户名'
      }, {
        pattern: /1\d{10}/,
        message: '请填写正确的手机号'
      }],
      // 重复密码验证
      rulePassword: [{
        required: true,
        message: '请确认密码'
      }, {
        validator: () => this.form.password === this.form.passwordRepeat,
        message: '两次密码不一致'
      }],
      form: {
        username: '',
        sms_code: '',
        password: '',
        nickname: '',
        passwordRepeat: ''
      }
    }
  },
  methods: {
    /**
     * 手机号变化时，重置验证码状态
    */
    onPhoneChange () {
      this.$refs.refSms.reset()
    },
    // 提交表单
    onSubmit () {
      // 调用接口
      ajax.post(AccountsApis.registerUrl, {
        username: this.form.username,
        password: this.form.passwordRepeat,
        sms_code: this.form.sms_code,
        nickname: this.form.nickname
      }).then(({ data }) => {
        // 成功返回结果，信息写入vuex
        this.$store.commit(types.UPDATE_USER_INFO, data)
        // 提示用户
        this.$notify({
          message: '注册成功',
          type: 'success'
        })
        // 跳转个人中心
        this.$router.replace({ name: 'Mine' })
      })
    },
    goBack () {
      this.$router.go(-1)
    }
  }
}
</script>
