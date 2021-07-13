/**
 * 存放项目中所有的接口地址
 */

const apiHost = 'http://localhost:8080/api'
/**
 * 用户账户相关的接口
 */
const AccountsApis = {
  // 用户登录
  loginUrl: apiHost + '/account/user/api/login/',
  // 用户退出登录
  logoutUrl: apiHost + '/account/user/api/logout/',
  // 用户信息
  userInfoUrl: apiHost + '/account/user/api/info/',
  // 用户注册
  registerUrl: apiHost + '/account/user/api/register/'
}

/**
 * 系统模块的接口
*/
const SystemApis = {
  // 轮播图列表
  sliderListUrl: apiHost + '/system/slider/list/',
  // 发送验证码
  sendSmsCodeUrl: apiHost + '/system/send/sms/'
}

/**
 * 景点模块
*/
const SightApi = {
  // 景点列表
  sightListUrl: apiHost + '/sight/sight/list/',
  sightListCacheUrl: apiHost + '/sight/sight/list/cache/',
  // 景点详情
  sightDetailUrl: apiHost + '/sight/sight/detail/#{id}/',
  // 景点下门票列表
  sightTicketUrl: apiHost + '/sight/ticket/list/#{id}/',
  // 评论列表
  sightCommentUrl: apiHost + '/sight/comment/list/#{id}/',
  // 景点详情图片
  sightImageUrl: apiHost + '/sight/image/list/#{id}/',
  // 门票详情
  ticketDetailUrl: apiHost + '/sight/ticket/detail/#{id}/'
}

const OrderApis = {
  // 订单列表
  orderListUrl: apiHost + '/order/order/list/',
  // 订单详情，支付，删除，取消
  orderDetailUrl: apiHost + '/order/order/detail/#{sn}/',
  // 提交订单
  ticketSubmitUrl: apiHost + '/order/ticket/submit/'
}

export {
  AccountsApis,
  SystemApis,
  SightApi,
  OrderApis
}
