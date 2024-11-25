"""����������ȡ��"""
from utils import Logger


class Base(object):
    """����������"""
    def __init__(self, driver):
        """��ȡ webdriver ����"""
        self.logger = Logger().get_logger()
        self.logger.info(f'[base]: ���ڻ�ȡ��ʼ��driver����:{driver}')
        self.driver = driver

    # Ԫ�ز��ҷ���
    def find_element(self, ele_obj):
        """��ȡԪ�ض���"""
        self.logger.info(f'[base]: ���ڶ�λ {ele_obj} ����')
        return self.driver.find_element(*ele_obj)

    # Ԫ�����뷽��
    def input_element(self, ele_obj, value):
        """�Ի�ȡ��Ԫ�ض�������ֵ"""
        self.logger.info(f'[base]: ������� {ele_obj} ����')
        ele = self.find_element(ele_obj)
        ele.clear()
        # ������־ pass
        ele.send_keys(value)

    # Ԫ�ص������
    def click_element(self, ele_obj):
        """���Ԫ�ض���"""
        self.logger.info(f'[base]: ���ڵ�� {ele_obj} ����')
        ele = self.find_element(ele_obj)
        ele.click()