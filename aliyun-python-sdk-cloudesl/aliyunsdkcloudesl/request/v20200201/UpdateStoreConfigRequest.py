# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkcloudesl.endpoint import endpoint_data

class UpdateStoreConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2020-02-01', 'UpdateStoreConfig','cloudesl')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_EnableNotification(self):
		return self.get_body_params().get('EnableNotification')

	def set_EnableNotification(self,EnableNotification):
		self.add_body_params('EnableNotification', EnableNotification)

	def get_NotificationWebHook(self):
		return self.get_body_params().get('NotificationWebHook')

	def set_NotificationWebHook(self,NotificationWebHook):
		self.add_body_params('NotificationWebHook', NotificationWebHook)

	def get_StoreId(self):
		return self.get_body_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_body_params('StoreId', StoreId)

	def get_NotificationSilentTimes(self):
		return self.get_body_params().get('NotificationSilentTimes')

	def set_NotificationSilentTimes(self,NotificationSilentTimes):
		self.add_body_params('NotificationSilentTimes', NotificationSilentTimes)