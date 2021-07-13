# lvyou-H5-yingyong
基于Django和Vue-Cli的H5应用
## 小旅游小项目展示

- 本项目采用`vant-UI`作为项目的`UI`，快速成型界面，`Vant`的官方地址：
  - https://vant-contrib.gitee.io/vant/#/zh-CN/home
- 前端页面采用`Vue-cli`成型，后端依靠`Django`，使用`Api`通信快速完成

## 前端页面展示

### 主页面

![image-20210516174608315](https://gitee.com/zrri/img/raw/master/img/20210516174608.png)

### 搜索页面

![image-20210516174902457](https://gitee.com/zrri/img/raw/master/img/20210516174902.png)

### 我的页面

![image-20210516174932206](https://gitee.com/zrri/img/raw/master/img/20210516174932.png)

---

### 其他页面

| ![image-20210516183234870](https://gitee.com/zrri/img/raw/master/img/20210516183234.png) | ![image-20210516183306324](https://gitee.com/zrri/img/raw/master/img/20210516183306.png) | ![image-20210516183327768](https://gitee.com/zrri/img/raw/master/img/20210516183327.png) |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| ![image-20210516183348170](https://gitee.com/zrri/img/raw/master/img/20210516183348.png) | ![image-20210516183410062](https://gitee.com/zrri/img/raw/master/img/20210516183410.png) | ![image-20210516183430778](https://gitee.com/zrri/img/raw/master/img/20210516183430.png) |
| ![image-20210516183447738](https://gitee.com/zrri/img/raw/master/img/20210516183447.png) | ![image-20210516183510751](https://gitee.com/zrri/img/raw/master/img/20210516183510.png) | ![image-20210516183528690](https://gitee.com/zrri/img/raw/master/img/20210516183528.png) |
| ![image-20210516183608618](https://gitee.com/zrri/img/raw/master/img/20210516183608.png) | ![image-20210516183622793](https://gitee.com/zrri/img/raw/master/img/20210516183622.png) | ![image-20210516183723165](https://gitee.com/zrri/img/raw/master/img/20210516183723.png) |

---

## 后端页面展示

![image-20210516230222393](https://gitee.com/zrri/img/raw/master/img/20210516230222.png)

![屏幕截图 2021-05-12 223406](https://gitee.com/zrri/img/raw/master/img/20210516230409.png)

## `PDMan`ORM建模

- system模块
- sight模块
- accounts模块
- order模块

---

### 关系图

![image-20210516231057911](https://gitee.com/zrri/img/raw/master/img/20210516231058.png)

---

![image-20210516231302325](https://gitee.com/zrri/img/raw/master/img/20210516231302.png)

## `API`接口

### `accounts`模块接口

####用户登录`api`

- 请求URL（POST）

```
/account/user/api/login/
```

- 请求参数

|   参数值   | 类型 |  描述  |
| :--------: | :--: | :----: |
| `username` | 必填 | 用户名 |
| `password` | 必填 |  密码  |

- 返回实例

```json
{
    "user": {
        "nickname": "李四",
        "avatar": "http://localhost:8000/medias/avatar/202105/%E4%B8%BB%E4%BA%A7%E5%93%81.png",
        "username": "17083430700"
    },
    "profile": {
        "real_name": "ZRR",
        "sex": 1,
        "sex_display": "男"
    }
}
```

---

#### 用户登出`api`

- 请求URL（GET）

```
/account/user/api/logout/
```

- 返回状态码`status`=201

---

#### 用户注册`api`

- 请求URL（POST）

```
/account/user/api/register/
```

- 请求参数（需用到验证码接口）

|   参数值   | 类型 |  描述  |
| :--------: | :--: | :----: |
| `username` | 必填 | 手机号 |
| `password` | 必填 |  密码  |
| `nickname` | 必填 |  昵称  |
| `sms_code` | 必填 | 验证码 |

- 返回实例

```json
{
    "user": {
        "nickname": "张三",
        "avatar": "",
        "username": "17083430701"
    },
    "profile": {
        "real_name": "",
        "sex": 1,
        "sex_display": "男"
    }
}
```

---

#### 用户详细信息`api`

- 请求URL（GET）

```
/account/user/api/info/
```

- 返回实例

```json
{
    "user": {
        "nickname": "张三",
        "avatar": "",
        "username": "17083430701"
    },
    "profile": {
        "real_name": "",
        "sex": 1,
        "sex_display": "男"
    }
}
```

---

### `system`模块接口

#### 轮播图`api`

- 请求URL（GET）

```
/system/slider/list/
```

- 返回实例

```json
{    "meta": {},    "objects": [        {            "id": 1,            "img_url": "http://localhost:8000/medias/202105/slider/banner2.png",            "target_url": null,            "name": "窦大夫祠"        },        {            "id": 2,            "img_url": "http://localhost:8000/medias/202105/slider/banner1.png",            "target_url": null,            "name": "二龙山"        },        {            "id": 3,            "img_url": "http://localhost:8000/medias/202105/slider/banner3.png",            "target_url": null,            "name": "崛围山"        }    ]}
```

---

#### `smsCodeapi`

- 请求URL（POST）

```
/system/send/sms/
```

- 请求参数

|   参数值    | 类型 |  描述  |
| :---------: | :--: | :----: |
| `phone_num` | 必填 | 手机号 |

- 返回实例

```json
{    "phone_num": "17083430701",    "sms_code": 397702,    "timeout": 300}
```

---

### `sight`模块接口

#### 景点列表`api`

- 请求URL（GET）

```
/sight/sight/list/
```

- 请求参数

|  参数值  | 类型 |   描述   |
| :------: | :--: | :------: |
|  `page`  | 选填 |   页码   |
| `is_hot` | 选填 | 是否热门 |
| `is_top` | 选填 | 是否精选 |
|  `name`  | 选填 |   名称   |

- 返回实例

```json
{    "meta": {        "total_count": 6,        "page_count": 2,        "current_page": 2    },    "objects": [        {            "id": 27,            "name": "迎泽公园",            "main_img": "http://localhost:8000/medias/202105/sight/wKgE2l1bTouAHckxACFKt8kMMXs85.jpg",            "score": 5.0,            "city": "太原",            "min_price": 10.0,            "province": "山西",            "comment_count": 0        }    ]}
```

---

#### 景点缓存（`redis`）列表

- 请求URL（GET）

```
/sight/sight/list/cache/
```

- 同景点列表`api`一样

---

#### 景点详细信息`api`

- 请求URL（GET）

```
/sight/sight/detail/<int:pk>/
```

- 返回实例

```json
{    "id": 1,    "name": "二龙山",    "desc": "二龙山",    "img": "http://localhost:8000/medias/202105/sight/04f1842f6cea4753aebde62e9b680a97.jpg",    "score": 5.0,    "content": "<h1>位于太原市西北部，中北大学校内，山高百余米，景色秀丽，山上鲜花遍开，有益足道、爱心林、怡人台、龙山飞瀑、爱心台、长廊、大型草画等景点，为中北大学勤工助学学生修建而成。</h1>\r\n\r\n<hr />\r\n<p><span class=\"marker\">交通</span></p>\r\n\r\n<p>835路中北大学站</p>\r\n\r\n<p><span class=\"marker\">门票</span></p>\r\n\r\n<p>具体详情请咨询景区</p>\r\n\r\n<p><span class=\"marker\">开放时间</span></p>\r\n\r\n<p>全天 (1月1日-12月31日 周一-周日)</p>\r\n\r\n<hr />\r\n<h2>景点位置</h2>\r\n\r\n<p>山西省太原市尖草坪区上兰村（中北大学校园内）</p>",    "province": "山西",    "city": "太原",    "area": "尖草坪",    "town": "上兰村",    "min_price": 10.0,    "comment_count": 1,    "image_count": 1}
```

---

#### 景点评论列表`api`

- 请求URL（GET）

```
/comment/list/<int:pk>/
```

- 请求参数

| 参数值 | 类型 | 描述 |
| :----: | :--: | :--: |
| `page` | 选填 | 页码 |

- 返回实例

```json
{    "meta": {        "total_count": 1,        "page_count": 1,        "current_page": 1    },    "objects": [        {            "user": {                "pk": 2,                "nickname": "李四"            },            "pk": 2,            "content": "二龙山又名烈石山，西临汾河，地势险要，是太原的北大门。解放战争期间，阎锡山军队在烈石山上修建了大量军事设施，现保存有碉堡3座、地下暗道1处。二龙山，在太原市西北角中北大学校园内，是少有的和校园相依托的风景区。山势不太高，但是景色秀丽，山上鲜花遍布，景点众多，太原二龙山旅游风景区是太原为数不多的避暑胜地。",            "love_count": 65,            "score": 5.0,            "is_public": 1,            "images": [                {                    "img": "http://localhost:8000/medias/202105/file/c711f75cfc1f4f3d8c009bbb21919a2e.jpg",                    "summary": "二龙山评论"                },                {                    "img": "http://localhost:8000/medias/202105/file/2427bc6964aa48b08ec3b6fc56de6552.jpg",                    "summary": "二龙山评论"                },                {                    "img": "http://localhost:8000/medias/202105/file/019f654a568044a5ae091043923c378c.jpg",                    "summary": "二龙山评论"                }            ],            "created_at": "2021-04-15"        }    ]}
```

---

#### 景点下的门票列表`api`

- 请求URL（GET）

```
/ticket/list/<int:pk>/
```

- 请求参数

| 参数值 | 类型 | 描述 |
| :----: | :--: | :--: |
| `page` | 选填 | 页码 |

- 返回实例

```json
{    "meta": {        "total_count": 1,        "page_count": 1,        "current_page": 1    },    "objects": [        {            "pk": 1,            "name": "二龙山门票",            "desc": "23:52前可订明日",            "types": 11,            "price": 10.0,            "discount": 10.0,            "total_stock": 100000,            "remain_stock": 99976,            "sell_price": 10.0        }    ]}
```

---

####景点介绍`api`

- 请求URL（GET）

```
/sight/info/<int:pk>/
```

- 返回实例

```json
{    "pk": 1,    "entry_explain": "<h1>位于太原市西北部，中北大学校内，山高百余米，景色秀丽，山上鲜花遍开，有益足道、爱心林、怡人台、龙山飞瀑、爱心台、长廊、大型草画等景点，为中北大学勤工助学学生修建而成。</h1>\r\n\r\n<hr />\r\n<p>交通</p>\r\n\r\n<p>835路中北大学站</p>\r\n\r\n<p>门票</p>\r\n\r\n<p>具体详情请咨询景区</p>\r\n\r\n<p>开放时间</p>\r\n\r\n<p>全天 (1月1日-12月31日 周一-周日)</p>\r\n\r\n<hr />\r\n<h2>景点位置</h2>\r\n\r\n<p>山西省太原市尖草坪区上兰村（中北大学校园内）</p>",    "play_way": "<h3>二龙山又名烈石山，西临汾河，地势险要，是太原的北大门。解放战争期间，阎锡山军队在烈石山上修建了大量军事设施，现保存有碉堡3座、地下暗道1处。二龙山，在太原市西北角中北大学校园内，是少有的和校园相依托的风景区。山势不太高，但是景色秀丽，山上鲜花遍布，景点众多，太原二龙山旅游风景区是太原为数不多的避暑胜地。</h3>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/2340c93ebce0477b82788c24318edabb.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/719ec2d7ebce4ac88f286ea863e243d7.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/9a7d9bb6b64d427d871efb3619d8bfd9.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/0b7568fc46794e778ac4204cfff7c403.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/887b1678c5c84c11a0fd34439abdb8ba.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/fb1d4c4aa4f94fe48f6a5f59f35e4c8d.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/0f48ef1e3f94444d86a871eafa69f47e.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/019f654a568044a5ae091043923c378c.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/2427bc6964aa48b08ec3b6fc56de6552.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/2ffe0923eedc4765888ce1ff6cda71a4.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/20c36e99210f41e9a3706d05e4ea6cc8.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/ed7886c77b0b42e3b7d7c32fe60805ef.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/c711f75cfc1f4f3d8c009bbb21919a2e.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/04f1842f6cea4753aebde62e9b680a97.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/12e2e1a4def4490dae87237799a55ee8.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/10651892dc234bc7b63dab3263dccf85.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/7b0c11d676f749478e827ca7b35d54ac.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/2f47940515ed4d06bcf4ecc29bbcffc4.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/32920e45f036419fa09a7c9c51cfbbd3.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/bef9359ad2354ef88a49453c02ced182.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/e64328fb06cf40d1b9288924f4af3dc8.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/f2f1c116018d43e59c5ed55f6940be7a.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/232bf0fa1d0d475c9704e8c29dc41147.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>\r\n\r\n<p><img src=\"https://ss2.meipian.me/users/418550/6253aa30173e454bb78bb9f79756f191.jpg?imageView2/2/w/750/h/1400/q/80\" /></p>",    "tips": "<h4><strong>小贴士</strong></h4>\r\n\r\n<p>交通</p>\r\n\r\n<p>835路中北大学站</p>\r\n\r\n<p>门票</p>\r\n\r\n<p>具体详情请咨询景区</p>\r\n\r\n<p>开放时间</p>\r\n\r\n<p>全天 (1月1日-12月31日 周一-周日)</p>",    "traffic": "<h2>景点位置</h2>\r\n\r\n<p>山西省太原市尖草坪区上兰村（中北大学校园内）</p>"}
```

---

#### 景点详情图片列表`api`

- 请求URL（GET）

```
/sight/image/list/<int:pk>
```

- 请求参数

| 参数值 | 类型 | 描述 |
| :----: | :--: | :--: |
| `page` | 选填 | 页码 |

- 返回实例

```json
{    "meta": {        "total_count": 1,        "page_count": 1,        "current_page": 1    },    "objects": [        {            "image": "http://localhost:8000/medias/202105/file/2ffe0923eedc4765888ce1ff6cda71a4.jpg",            "summary": "二龙山基础"        }    ]}
```

---

#### 门票详情`api`

- 请求URL（GET）

```
/sight/ticket/detail/<int:pk>
```

- 返回实例

```json
{    "pk": 1,    "name": "二龙山门票",    "desc": "23:52前可订明日",    "types": 11,    "price": 10.0,    "sell_price": 10.0,    "discount": 10.0,    "expire_date": 7,    "return_policy": "联系管理员",    "has_invoice": true,    "entry_way": "短信换票入园",    "tips": "<div>位于太原市西北部，中北大学校内，山高百余米，景色秀丽，山上鲜花遍开，有益足道、爱心林、怡人台、龙山飞瀑、爱心台、长廊、大型草画等景点，为中北大学勤工助学学生修建而成。</div>\r\n\r\n<hr />\r\n<p>交通</p>\r\n\r\n<p>835路中北大学站</p>\r\n\r\n<p>门票</p>\r\n\r\n<p>具体详情请咨询景区</p>\r\n\r\n<p>开放时间</p>\r\n\r\n<p>全天 (1月1日-12月31日 周一-周日)</p>\r\n\r\n<hr />\r\n<h2>景点位置</h2>\r\n\r\n<p>山西省太原市尖草坪区上兰村（中北大学校园内）</p>",    "remark": "<p>这里没有小<span class=\"marker\">tips</span></p>"}
```

---

### `order`模块接口

#### 订单提交`api`

- 请求URL（POST）

```
/order/ticket/submit/
```

- 请求参数

|   参数值    | 类型 |    描述    |
| :---------: | :--: | :--------: |
| `ticket_id` | 必填 |   门票ID   |
| `play_date` | 必填 |  出行时间  |
|  `to_user`  | 必填 |  用户昵称  |
| `to_phone`  | 必填 | 用户手机号 |
| `buy_count` | 必填 |  购买总价  |

- 返回实例

```json
{    "sn": "202105171247379691779086"}
```

---

####订单详情`api`

- 请求URL（GET）

```
/order/order/detail/<int:sn>
```

- 返回实例

```json
{    "sn": "202105171247379691779086",    "buy_count": 20,    "buy_amount": 200.0,    "types": 10,    "status": 11,    "created_at": "2021-05-17",    "remark": null,    "to_user": "李四",    "to_area": "",    "to_address": "",    "to_phone": "17083430700",    "express_type": null,    "express_no": null,    "items": [        {            "pk": 21,            "flash_name": "二龙山门票",            "flash_price": 10.0,            "flash_img": "http://localhost:8000/medias/202105/sight/7b0c11d676f749478e827ca7b35d54ac.jpg",            "flash_origin_price": 10.0,            "flash_discount": 10.0,            "count": 20,            "amount": 200.0,            "remark": "出行时间2021-05-20",            "object_id": 1,            "app_label": "sight",            "model": "ticket"        }    ]}
```

---

#### 订单列表

- 请求URL（GET）

```
/order/order/list/
```

- 请求参数

| 参数值 | 类型 | 描述 |
| :----: | :--: | :--: |
| `page` | 选填 | 描述 |

- 返回实例

```json
{    "meta": {        "total_count": 1,        "page_count": 1,        "current_page": 1    },    "objects": [        {            "sn": "202105171247379691779086",            "buy_amount": 200.0,            "buy_count": 20,            "types": 10,            "status": 11,            "remark": null,            "created_at": "2021-05-17",            "item_first": {                "pk": 21,                "flash_name": "二龙山门票",                "flash_price": 10.0,                "flash_img": "http://localhost:8000/medias/202105/sight/7b0c11d676f749478e827ca7b35d54ac.jpg",                "flash_origin_price": 10.0,                "flash_discount": 10.0,                "count": 20,                "amount": 200.0,                "remark": "出行时间2021-05-20",                "object_id": 1,                "app_label": "sight",                "model": "ticket"            }        }    ]}
```

---

## 全局状态`Code`

| status |  Code   |            描述            |
| :----: | :-----: | :------------------------: |
|  404   | 4004000 | 您访问的内容不存在或被删除 |
|  400   | 4000000 |       参数格式不正确       |
|  405   | 4050000 |      表单请求方式错误      |
|  401   | 4010000 |           请登录           |
|  500   | 5000000 |   服务器正忙，请稍后重试   |

