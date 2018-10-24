import unittest
import requests
from common.logger import Log
class Test_Kuaidi(unittest.TestCase):
    u'''测试快递查询接口'''
    log = Log()
    def setUp(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"

                  }

    def chaxun_kuaidi(self,danhao,kd,kd_name):
        #对url的单号参数
        self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" %(danhao,kd)
        self.log.info(u"测试url地址：%s"%self.url)
        #发请求
        r = requests.get(self.url,headers=self.headers,verify=False)
        result = r.json()
        self.log.info(u"获取请求结果：%s"%result)
        #获取结果
        self.log.info(u"获取公司名称：%s"%result['company'])
        #获取data里面内容
        data = result["data"]
        self.log.info(u"获取data内容：%s"%result["data"])
        # 获取已签收状态
        get_result = data[0]['context']
        self.log.info(u"获取已签收状态：%s"%get_result)
        # 断言：测试结果与期望结果对比
        self.assertEqual(kd_name, result['company'])
        self.assertIn(u"已签收", get_result)


    def test_shentong(self):
        u'''测试申通快递，单号：3381022448107'''
        self.log.info("----------start!-------")
        danhao = '3381022448107'
        kd = 'shentong'
        kd_name = u"申通快递"
        self.log.info(u"测试单号：%s 快递名称：%s"%(danhao,kd_name))
        # self.chaxun_kuaidi(danhao,kd,kd_name)

        self.chaxun_kuaidi(danhao='3381022448107',kd='shentong',kd_name=u"申通快递")
        self.log.info("----------pass!-------")

    def test_yuantong(self):
        u'''测试圆通快递，单号：802187905646723978'''
        self.log.info("----------start!-------")
        danhao = '802187905646723978'
        kd = 'yuantong'
        kd_name =u"圆通快递"
        self.log.info(u"测试单号：%s 快递名称：%s"%(danhao,kd_name))
        self.chaxun_kuaidi(danhao,kd,kd_name)
        self.log.info("----------pass!-------")
if __name__ == "__main__":
    unittest.main()