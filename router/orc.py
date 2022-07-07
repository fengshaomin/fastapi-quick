# conding:utf-8
from fastapi import APIRouter, File

import utils.id_validator.validator
from client.OcrClient import OcrClient
from utils.cardbin import cardbin

ocr_app = APIRouter()


# ocr相关的controller
@ocr_app.post("/invoice")
def read_invoice(file: bytes = File(...), invoice_type: str = "normal"):
    """
    增值税发票识别，invoice_type normal:是正常的那种大票，
    额度：500次/天 超过会报错,如果是卷票，请设置invoice_type=“roll”
    :param file:
    :param invoice_type:
    :return:
    """
    _result = OcrClient.fapiao_file_byte(file, invoice_type)
    return _result


@ocr_app.post("/fapiao")
def read_fapiao(file: bytes = File(...)):
    """
    通用的机打发票的识别
    :param file:，
    :return:
    """
    _result = OcrClient.rec_fapiao(file)
    return _result


@ocr_app.post("/image")
def read_image(file: bytes = File(...)):
    """
    普通的文字识别，给个图片识别其中的文字
    :param file:
    :return:
    """
    _result = OcrClient.simple_ocr(file)
    return _result


@ocr_app.post("/idcard")
def read_IDCard(file: bytes = File(...), side: str = "front"):
    """
    识别身份证信息，图像数据，base64编码，要求base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    :param file: 上传文件，直接读成bytes，所以文件不能太大，会爆
    :param side: 正面-front 反面=back
    :return:
    """
    _result = OcrClient.rec_idcard(file, side=side)
    return _result


@ocr_app.post("/bankcard")
def read_BankCard(file: bytes = File(...)):
    """
    银行卡信息，图像数据，base64编码，要求base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式,我自己试了一下，浦发的卡太亮，识别可能存在误差，需要手工检查
    :param file: 上传文件，直接读成bytes，所以文件不能太大，会爆
    :param side: 正面-front 反面=back
    :return:bank_card_number	string	是	银行卡卡号
            bank_name	string	是	银行名，不能识别时为空
            bank_card_type	number	是	银行卡类型，0:不能识别; 1: 借记卡; 2: 信用卡
    """
    _result = OcrClient.rec_bankcard(file)
    return _result


@ocr_app.post("/taxi")
def read_fapiao(file: bytes = File(...)):
    """
    出租车发票识别
    :param file:，
    :return:
    """
    _result = OcrClient.rec_taxi_receipt(file)
    return _result


@ocr_app.post("/cardNo")
def verify_bankcard_no(card_no: str = None):
    """
    校验银行卡
    :param cardNo:
    :return:
    """
    print(card_no)
    a = cardbin.valid(card_no)
    print(a)
    return a


@ocr_app.post("/idcardInfo")
def verify_idcard_info(card_no: str = None):
    """
    校验身份证号信息，包括籍贯、生日、性别，如果身份证号不对，则直接返回false
    :param cardNo:
    :return:
    """
    print(card_no)
    a = utils.id_validator.validator.get_info(card_no)
    print(a)
    return a
