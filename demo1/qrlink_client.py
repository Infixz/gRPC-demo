# -*- coding: utf-8 -*-

import qrlink_pb2


def run():
	with qrlink_pb2.early_adopter_create_QrLink_stub('localhost',50054) as stub:
		resp = stub.GetTempQrLink(qrlink_pb2.QrLinkRequest(tmp_ac="this is tmp_ac",h_name="little wang",c_name="little zhang"),5)
		print "msg has been received\nqr_link= " + resp.qr_link


if __name__ == '__main__':
	run()