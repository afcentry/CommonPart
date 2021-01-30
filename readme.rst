### CommonPart

一. 模块描述  
  封装Python脚本通用功能(数据库操作、网络请求、时间操作等)，对其进行深层次的封装加固。
二. 环境支持  
  1. Python3.7.2  
  2. 开发操作系统为Windows10，目前未发现其它系统兼容问题   
三. 引入方式   
  from CommonPart.combuiltin.combuiltin import ComBuiltin
  from CommonPart.commonvar.commonvar import CommonVar   
四. 功能列表   
    1.time模块   
    
    (1) 获取当前格式化时间 
        CommonBuiltin.get_current_time()   
        
    (2) 获取当前日期   
        CommonBuiltin.get_current_date()   
        
    (3) 获取13位时间戳   
        CommonBuiltin.get_timestamp13()   
        
    (4) 发送http-get请求   
        CommonBuiltin.get(**kwarg)   
        
    (5) 发送http-post请求   
        CommonBuiltin.post(**kwarg)