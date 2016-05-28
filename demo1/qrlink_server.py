# -*- coding: utf-8 -*-

import time

import qrlink_pb2
from scene_id_machine import get_scene_id
from utilities import get_tmp_qrcode

class QrLink(qrlink_pb2.EarlyAdopterQrLinkServicer):
	"""docstring for QrLinkServicer"""
	def GetlimitQrLink(self,request,context):
		scene_id = get_scene_id(request.tmp_ac,request.h_name,request.c_name)
		return qrlink_pb2.QrLinkReply( status=True, qr_link="%s"% (get_tmp_qrcode(scene_id)) )

	def GetTempQrLink(self,request,context):
		scene_id = get_scene_id(request.tmp_ac,request.h_name,request.c_name)
		return qrlink_pb2.QrLinkReply( status=True, qr_link="%s"% (get_tmp_qrcode(scene_id)) )

def main():
	server = qrlink_pb2.early_adopter_create_QrLink_server(
			QrLink(),50054,None,None)
	server.start()
	try:
		while True:
			time.sleep(3600)
	except Exception, e:
		raise e

if __name__ == '__main__':
	main()